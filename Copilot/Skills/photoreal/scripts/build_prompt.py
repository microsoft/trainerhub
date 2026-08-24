#!/usr/bin/env python3
"""Build English prompts for photorealistic image generation.

The builder combines the five layers documented in SKILL.md. With --n, it
rotates scene, light, framing, gaze, image-quality, and asymmetry details to
produce multiple prompts suitable for parallel generation.

Examples:
    python3 build_prompt.py --subject "a Korean woman in her late twenties" --scene cafe --n 4
    python3 build_prompt.py --subject "a Japanese man in his thirties" --scene commute --level full
    python3 build_prompt.py --subject "an American woman in her twenties" --scene custom \
        --situation "looking up while folding laundry" --n 3 --emit-batch ./out
"""

import argparse
import shlex
import sys


# Moments and lights rotate across --n variants.
SCENES = {
    "cafe": {
        "place": "at a window seat in a cafe",
        "lights": [
            "lit only by late-afternoon light through the window",
            "soft diffused light from an overcast window, weak indoor lamps mixed in",
            "low evening light through the glass catching only one cheek",
        ],
        "moments": [
            "caught mid-motion setting a cup down, looking out the window",
            "hand paused mid page-turn",
            "listening to someone across the table, just before a smile forms",
            "about to sip, attention drifting somewhere off-frame",
        ],
    },
    "home": {
        "place": "in a small apartment",
        "lights": [
            "morning light through a gap in the curtains, nothing else",
            "a single desk lamp on, the rest of the room dim",
            "window light bouncing off the floor, faintly lifting the underside of the face",
        ],
        "moments": [
            "one hand still in their hair, mid-motion",
            "sitting on the bed, looking up from a phone",
            "turning around mid-drink in the kitchen",
            "one hand paused over half-folded laundry",
        ],
    },
    "street": {
        "place": "on a narrow street at dusk",
        "lights": [
            "mixed light from shop signs and street lamps, nothing else",
            "blue post-sunset sky mixing with warm shopfront light",
            "cold white light from a convenience store window catching the side of the face",
        ],
        "moments": [
            "stopping mid-stride to look back",
            "waiting at a crossing, attention elsewhere",
            "mid-shrug, adjusting a bag strap",
            "hair blowing across the face in a gust",
        ],
    },
    "commute": {
        "place": "inside a subway car",
        "lights": [
            "only the carriage fluorescents, darkness outside",
            "outside light flooding in as the train leaves a tunnel",
            "overhead light landing on the crown of the head, faint shadow under the eyes",
        ],
        "moments": [
            "staring out the window, focus gone soft",
            "mid-adjustment of an earbud",
            "just waking from a doze",
            "body swaying while holding a strap",
        ],
    },
    "park": {
        "place": "in a park",
        "lights": [
            "dappled sunlight through leaves falling unevenly across the face",
            "flat natural light on an overcast day",
            "low sun from behind, rimming only the edge of the hair",
        ],
        "moments": [
            "on a bench, chin just lifted",
            "hair blown across the face",
            "stopped mid-walk, looking down at their shoes",
            "waiting for someone, looking off to the side",
        ],
    },
    "restaurant": {
        "place": "at a restaurant table",
        "lights": [
            "one warm ceiling lamp dropping onto the table",
            "mixed light from the next table and the kitchen",
            "a window seat, cool daylight on one side of the face and warm interior light on the other",
        ],
        "moments": [
            "mid-sentence, just before laughing",
            "chopsticks half-raised, looking at the person opposite",
            "setting a glass down while turning their head",
            "looking up from a menu",
        ],
    },
    "office": {
        "place": "at an office desk",
        "lights": [
            "ceiling fluorescents mixed with monitor glow",
            "daylight through blinds striping the desk",
            "only monitor light on the face, the surroundings dim",
        ],
        "moments": [
            "eyes moving from the monitor to the side",
            "hand paused halfway to a mug",
            "leaning back, gaze drifting up",
            "turning toward someone calling their name",
        ],
    },
    "night": {
        "place": "by a window at night",
        "lights": [
            "one lamp in the room plus city light through the glass",
            "phone screen lighting the face weakly from below",
            "light spilling from the next room, catching only half the face",
        ],
        "moments": [
            "looking up from a phone",
            "forehead resting lightly against the window",
            "hand stopped on the way to the light switch",
            "just after a yawn, eyes still soft",
        ],
    },
}


FRAMING = [
    "framing tilted a degree or two, the subject sitting left of center",
    "a little too much headroom, the subject settled toward the lower right",
    "the subject slightly out of frame, one shoulder cropped",
    "horizon tipped to the right, very little room at the bottom",
]

GAZE = [
    "eyes slightly off the lens, not locked on camera",
    "looking at someone standing beside the camera",
    "gaze dropped, eyelids covering part of the iris",
    "focus soft, looking at something far away",
]

DEFECT = [
    "a little handshake blur and the usual phone-camera noise",
    "focus landing just barely on the eyes, the ears going soft",
    "noise in the shadows, resolution mildly mushy",
    "the bright side slightly blown, shadow detail muddied",
]

ASYMMETRY = [
    "left brow a touch higher than the right, left corner of the mouth lifting more",
    "right eye opening slightly less than the left, right corner of the mouth lifting more",
    "a faint crease at one eye only, the lip line a little different side to side",
]

L1 = (
    "a natural smartphone photo, not an ad shoot but a snapshot an ordinary person took "
    "during an ordinary day and would post to their feed, with the texture of a phone camera "
    "rather than a high-end one"
)

L2_TAIL = "no CG-like surface, no heavy retouching, no unnatural sheen"

L4 = [
    "realistic, coherent proportions across the jawline, brow, eyes, nose, and lips",
    "human-sized pupils, natural sclera, eyelids with real thickness",
    "expression barely there, with only a small movement at the mouth and eyes",
    "visible pores and fine hair, faint redness beside the nose, a little shine on the forehead",
    "a few loose strands across the forehead, side hair not tidied",
]

HANDS = (
    "if hands are visible, use the correct finger count, plausible joints, and a realistic grip"
)

# L5 fails in both directions: omitting it can look neglected, while strong
# attractiveness wording can pull the result back toward an actor or model.
L5 = {
    "plain": (
        "keep the subject likeable but do not perfect the face or skin; prioritize presence, "
        "lived-in texture, and natural imperfection over perfection"
    ),
    "attractive": (
        "keep the subject genuinely attractive but do not perfect the face or skin; stay clean "
        "and approachable, and prioritize presence, lived-in texture, and natural imperfection "
        "over perfection"
    ),
    "none": "prioritize presence, lived-in texture, and natural imperfection over perfection",
}

# L4 texture directives can increase perceived age, so full prompts lock age by default.
AGE_LOCK = (
    "read as the stated age; the skin-texture notes must not push the subject older than specified"
)

HANDS_ACTION = (
    "if the hands are doing something, the grip must be one that actually performs it"
)

SELFIE = (
    "a selfie held at arm's length, with the face close and high in the frame, wide-angle "
    "distortion enlarging the nose and stretching the edges, one shoulder tilted toward the "
    "extended arm, and the eyes on the screen rather than the lens so the gaze is slightly off"
)


def group_guidance(group_size):
    return (
        f"the scene contains exactly {group_size} people; assign gaze and posture according to "
        "each person's role, with nobody looking at the camera unless the situation requires it; "
        "render the faces and hands of people farther back clearly; vary clothing colors, "
        "materials, and postures from person to person"
    )


def positive_int(value):
    try:
        parsed_value = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer") from error
    if parsed_value < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed_value


def valid_group_size(value):
    try:
        parsed_value = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer") from error
    if parsed_value < 2:
        raise argparse.ArgumentTypeError("must be at least 2")
    return parsed_value


def build(subject, scene_key, situation, index, level, shot,
          group=0, charm="plain", age_lock=False):
    scene = SCENES.get(scene_key)
    parts = []

    if scene:
        moment = scene["moments"][index % len(scene["moments"])]
        light = scene["lights"][index % len(scene["lights"])]
        parts.append(f"{subject}, {scene['place']}, {moment}")
    else:
        parts.append(f"{subject}, {situation}")
        light = "lit only by whatever light is already there, with no studio lighting"

    parts.append(L1)

    if group >= 2:
        parts.append(group_guidance(group))

    if shot == "selfie":
        parts.append(SELFIE)

    parts.append(light)
    parts.append(DEFECT[index % len(DEFECT)])
    parts.append(L2_TAIL)

    if level in ("standard", "full"):
        if shot != "selfie":
            parts.append(FRAMING[index % len(FRAMING)])
        if group < 2 and shot != "selfie":
            parts.append(GAZE[index % len(GAZE)])

    if level == "full":
        parts.extend(L4)
        parts.append(ASYMMETRY[index % len(ASYMMETRY)])
        parts.append(HANDS)
        parts.append(HANDS_ACTION)

    if age_lock:
        parts.append(AGE_LOCK)

    # Keep L5 last so it balances the preceding corrective directives.
    parts.append(L5[charm])

    return ", ".join(parts) + "."


def main():
    parser = argparse.ArgumentParser(description="Build photorealistic image prompts")
    parser.add_argument(
        "--subject",
        required=True,
        help='For example: "a Korean woman in her late twenties"',
    )
    parser.add_argument("--scene", default="cafe", choices=sorted(SCENES) + ["custom"])
    parser.add_argument(
        "--situation",
        action="append",
        default=[],
        help="Describe a custom situation. Repeat to rotate situations across variants.",
    )
    parser.add_argument("--n", type=positive_int, default=1, help="Number of prompt variants")
    parser.add_argument("--level", default="standard", choices=["light", "standard", "full"])
    parser.add_argument("--shot", default="other", choices=["other", "selfie"])
    parser.add_argument(
        "--group",
        type=valid_group_size,
        default=0,
        metavar="N",
        help="Create a scene with exactly N people and add multi-person guidance.",
    )
    parser.add_argument(
        "--charm",
        default="plain",
        choices=["plain", "attractive", "none"],
        help="L5 strength; strong attractiveness wording can restore an editorial look.",
    )
    age_lock_group = parser.add_mutually_exclusive_group()
    age_lock_group.add_argument(
        "--age-lock",
        dest="age_lock",
        action="store_true",
        help="Add age-lock wording. Enabled by default with --level full.",
    )
    age_lock_group.add_argument(
        "--no-age-lock",
        dest="age_lock",
        action="store_false",
        help="Omit age-lock wording, including with --level full.",
    )
    parser.set_defaults(age_lock=None)
    parser.add_argument(
        "--emit-batch",
        metavar="DIR",
        help="Also print a codex-image batch command for the output directory.",
    )
    parser.add_argument(
        "--prefix",
        default="photoreal",
        help="Output filename prefix used with --emit-batch.",
    )
    arguments = parser.parse_args()

    if arguments.scene == "custom" and not arguments.situation:
        parser.error("--scene custom requires at least one --situation")
    if arguments.shot == "selfie" and arguments.group >= 2:
        parser.error("--shot selfie cannot be combined with --group")

    age_lock = (
        arguments.age_lock
        if arguments.age_lock is not None
        else arguments.level == "full"
    )

    def situation_for(index):
        if not arguments.situation:
            return ""
        return arguments.situation[index % len(arguments.situation)]

    scene_key = arguments.scene if arguments.scene != "custom" else None
    prompts = [
        build(
            arguments.subject,
            scene_key,
            situation_for(index),
            index,
            arguments.level,
            arguments.shot,
            group=arguments.group,
            charm=arguments.charm,
            age_lock=age_lock,
        )
        for index in range(arguments.n)
    ]

    if arguments.scene == "custom" and arguments.n > 1 and len(arguments.situation) == 1:
        print(
            "# Note: only one --situation was provided, so variants differ only in lighting "
            "and composition.",
            file=sys.stderr,
        )
        print("#       Repeat --situation to vary the action itself.", file=sys.stderr)

    for index, prompt in enumerate(prompts, 1):
        print(f"--- {index} ---")
        print(prompt)
        print()

    if arguments.emit_batch:
        batch_arguments = " \\\n+  ".join(
            shlex.quote(f"{prompt}::{arguments.prefix}-{index}.png")
            for index, prompt in enumerate(prompts, 1)
        )
        print("--- codex-image batch command ---")
        print(
            "~/.claude/skills/codex-image/scripts/codex_imagegen_batch.sh "
            f"{shlex.quote(arguments.emit_batch)} \\\n+  {batch_arguments}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())