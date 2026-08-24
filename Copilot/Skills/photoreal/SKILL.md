---
name: photoreal
description: "Prompt-design skill for creating photorealistic images, especially portraits, without an obvious AI-generated look. It counteracts the advertising and editorial perfection that image models tend to produce, making the result resemble a casual smartphone photo posted to social media. Provides prompt layers, assembly rules, generation variants, and a post-generation review checklist. Use for requests containing terms such as 'photorealistic,' 'looks like a photo,' 'realistic photo,' 'not AI-looking,' 'real person,' 'social media photo,' 'selfie,' 'snapshot,' 'portrait,' 'profile photo,' or 'candid photo,' and whenever a generated image containing people should look photographed rather than rendered. Image-generation skills such as codex-image perform the actual generation; this skill designs their prompts. Excludes illustration, anime, 3D render, logo, and diagram requests."
---

# Photorealistic Photo Prompts

## What This Skill Is Counteracting

Image models gravitate toward images that their training data treats as well photographed: advertisements, editorials, stock photography, and fully retouched profiles. Without further direction, a generated person therefore tends to have the following traits:

Flawless skin, three-point lighting, centered composition, perfect bilateral symmetry, a catalog smile, direct eye contact, and oversized glassy pupils.

Each trait can look polished on its own. When all seven appear in one image, however, viewers quickly recognize it as AI-generated because that combination rarely occurs in an ordinary photograph.

**Photorealism therefore comes not from adding more detail, but from counteracting this default pull.** The goal is not "make it better" but "make it less perfect." Every directive in this skill supports that correction.

The correction needs a target. Too little produces an advertisement; too much produces a failed photograph. Each layer below describes how to find the useful middle ground.

## Workflow

1. Define the subject and situation: who they are, where they are, and what they are doing.
2. Assemble only the necessary directives from the five layers below.
3. Use [build_prompt.py](./scripts/build_prompt.py) to create multiple variants. Photorealism is inconsistent, so generating three to five images in parallel is the default.
4. Generate the images with `codex-image` or another image-generation skill.
5. Apply the **Post-Generation Review** below. Strengthen only the directives related to failed checks, then regenerate.

## The Five Layers

The layers become more detailed as they progress. The first two already provide a substantial improvement. Lower layers become more important as the face occupies more of the frame.

### L1 - Source: Who Took It, and Why?

This is the highest-leverage layer. A single premise - that the image records daily life rather than advertises something - influences lighting, composition, expression, and image quality at the same time.

> A natural smartphone photo. Not an advertising shoot, but a frame that an ordinary person might capture during everyday life and post to social media. The texture of a phone-camera snapshot rather than a high-end camera.

If the prompt can contain only one sentence, use this layer.

### L2 - Light and Image Quality: Prevent Excessive Cleanliness

> Lit only by window light or the lighting already present in the location. No studio lighting. Retain slight handshake blur, phone-camera noise, and mildly rough resolution. Suppress CG-like surfaces, heavy retouching, and unnatural sheen.

Restricting light to what is already present makes shadows fall in a coherent direction and allows mixed color temperatures. Studio lighting removes shadows, and a face without shadows is a major source of the AI-generated look.

**Add one more sentence when using backlight.** Even when asked for backlighting, models often brighten the front of the face by habit. Specify that the shadows on the front of the face should remain unfilled. When this works, only the back of the head and the ends of flyaway hairs catch the light, greatly improving realism.

**Be careful when requesting blurred lights in night scenes.** Terms such as "out-of-focus signs" and "bokeh" pull the model toward a cinematic still. They can override L1 and produce background blur that a phone camera could not achieve. For distant night scenes, omit blurred lights or constrain them to "the shallow blur achievable by a phone camera."

### L3 - Composition and Moment: Make It Feel Human-Captured

> Leave slightly uneven framing, such as a small tilt or unbalanced negative space, instead of refining the composition perfectly. Capture an incidental moment during an ordinary activity rather than a pose created for the camera. Do not default to direct eye contact; use a gaze slightly away from the lens.

"Caught in the middle of a moment" changes the hands and body as well as the pose. Removing the deliberate pose leaves arms in imperfect positions and creates natural folds in clothing. That is what reality looks like.

Foreground obstructions also belong to this layer: another person's shoulder, the back of a seat, or a window frame. One obstruction can make the photographer feel physically present in the scene.

### L4 - Anatomy: Face, Skin, Hands, and Hair

When a face occupies at least one quarter of the frame, this layer is usually necessary.

- **Structure**: Keep the contour, bone structure, eyes, brows, nose, and lips in realistic and coherent proportion.
- **Eyes**: Avoid oversized pupils. Retain a natural amount of sclera, slight left-right variation, and real eyelid thickness.
- **Expression**: Keep smiles restrained, using only small movements at the corners of the mouth and eyes.
- **Asymmetry**: Leave minute differences between the brows, eyes, and corners of the mouth. Avoid perfect bilateral symmetry.
- **Skin**: Retain a moderate amount of pores, fine facial hair, faint redness, and uneven natural shading rather than smoothing everything uniformly.
- **Hair**: Leave flyaways, loose strands, and irregularities in tied hair rather than arranging every strand evenly.
- **Hands**: Keep finger count, joints, lengths, and overlaps plausible. Make the grip on any object physically realistic.

**Direct hands twice.** Anatomy and action logic are separate problems. "Natural finger count and joints" can produce anatomically correct fingers held flat in front of a knife blade, which would be dangerous in real life. Whenever a hand performs an action, describe the hand shape required by that action as well: "the hand holding the garlic keeps its fingers curled back" or "the index finger hooks through the cup handle."

### L5 - Attractiveness Ceiling: How Polished Should the Subject Be?

Without this layer, the previous directives can be interpreted as "make the subject unattractive," causing the image to lose all appeal. State that realism and attractiveness are compatible.

> Preserve an appealing appearance, but do not perfect the face or skin. Keep the subject clean, well-kept, and approachable while prioritizing plausible, real-world attractiveness. Presence, signs of everyday life, and natural imperfection matter more than perfection.

Placed at the end, this sentence balances the corrective instructions that precede it. It is one of the most effective closing lines in practice.

**This layer can fail in either direction.** Omitting it can make the subject look neglected, while emphasizing it can pull the model back toward an actor or fashion model. Strong terms such as "beautiful," "attractive," or "cute" may cause the model to ignore L4. If a request for visible pores still produces smooth skin, suspect this layer. Use one of three strengths:

| Strength | Wording | Use Case |
| --- | --- | --- |
| Light | Preserve a likeable impression, but... | Default for most everyday scenes |
| Medium | Attractive, but not perfectly refined... | Scenes in which the person is the main subject |
| None | Omit attractiveness language; retain only presence | Older adults, documentary scenes, and close-ups of hands or objects |

## Specifying Age

**L4 skin and wrinkle directives can make the subject look older.** In repeated observations, prompts for a person in their mid-twenties can produce someone in their early thirties, while prompts for someone in their late thirties can produce someone in their forties.

When age matters, add:

> The subject must read as the specified age; the skin-texture directives must not make them appear older.

Alternatively, select age-appropriate imperfections. For a person in their twenties, use **shine, pores, acne marks, and fine facial hair instead of wrinkles**. For people in their forties and older, **wrinkles and pigmentation** can be appropriate. Requesting crow's feet for someone in their twenties inherently raises the perceived age.

## Scenes With Multiple People

Do not reuse single-person directives unchanged. Applying one "off-camera gaze" to several people can make everyone look in the same direction, producing a staged scene. Handle four concerns separately:

- **Assign gaze by role**: One person watches the whiteboard, one looks at a laptop, one watches the speaker, and one glances down. State that nobody looks at the camera.
- **Specify people farther back**: Ask for clear faces and hands on people in the background. Without this, background figures often deform.
- **Vary clothing**: Otherwise everyone may wear the same colors. Vary at least one of color, material, or formality.
- **Vary posture**: One person might cross their arms, another rest their chin on a hand, and another lean back in a chair.

Use L5 carefully here. Strong attractiveness wording can make a mixed group awkward. Use the Light strength from the table above.

## Rewrite Negative Instructions as Positive Ones

This is one of the most practical rules in the skill. Image models often drop negation. With "do not make the skin smooth," the concept of smoothness may remain while the negation disappears, producing even smoother skin.

**Name what should remain instead of only naming what is forbidden.**

| Weak Negative Instruction | Strong Positive Instruction |
| --- | --- |
| Do not smooth the skin | Skin with visible pores, fine facial hair, and faint redness |
| Do not make the face symmetrical | The left brow sits slightly higher than the right |
| Do not pose | Caught while setting a cup down and turning to the side |
| Do not look straight at the camera | Looking toward the window, slightly away from the lens |
| Do not use a perfect composition | The horizon tilts one or two degrees and the subject sits left of frame |
| Do not retouch | An unfiltered original left as it appeared in the phone gallery |

Negative instructions do not need to disappear completely. Pair every important one with a positive description of the desired result.

## Assembly Template

```text
[subject] [situation and action] [place and time]
[L1 source] [L2 light and image quality] [L3 composition and moment]
[L4 anatomy - only what is needed] [L5 attractiveness ceiling]
```

**Example - Complete Prompt**

> A Korean woman in her late twenties sits at a low table beside the window in her apartment, caught while setting down an iced coffee and looking outside. Late afternoon, lit only by natural light through the window. Not an advertising shoot, but a casual phone snapshot that a friend might take and post to social media. The horizon is slightly tilted and the subject sits left of frame. Her gaze falls away from the camera toward the window, with only a slight lift at the corner of her mouth. Visible pores and fine facial hair, faint redness beside the nose, a few loose strands falling across the forehead, and the left brow slightly higher than the right. Her index finger hooks naturally through the cup handle. Retain phone-camera noise and slight handshake blur, without heavy retouching or unnatural sheen. Preserve a likeable impression without making her perfect, and ensure that she reads as being in her late twenties.

This is an appropriate length. Longer prompts make the model increasingly likely to ignore earlier instructions.

## Prompt Builder

Typing every directive manually causes omissions and makes parallel variants tedious. From the skill directory, run:

```bash
python3 ./scripts/build_prompt.py \
  --subject "a Korean woman in her late twenties" \
  --scene cafe \
  --n 4
```

- `--scene`: `cafe`, `home`, `street`, `commute`, `park`, `restaurant`, `office`, `night`, or `custom`
- `--n`: Number of variants. See **What Changes Between Variants** below.
- `--level`: `light` (L1+L2+L5), `standard` (default, L1-L3+L5), or `full` (all layers)
- `--shot`: `other` (default, photographed by someone else) or `selfie`
- `--group N`: A scene containing N people. Adds gaze assignment, background-person, clothing, and posture guidance.
- `--charm`: `plain` (default), `attractive`, or `none` for L5 strength
- `--age-lock` / `--no-age-lock`: Add or omit the age-lock sentence. Enabled by default with `--level full`.
- `--emit-batch <dir>`: Also print a `codex-image` batch command.

With `--scene custom`, pass the situation through `--situation "..."`. Repeat `--situation` to rotate through different actions across variants.

## What Changes Between Variants

Generate three to five images so that you can select the strongest result. Merely changing the lighting, however, produces nearly identical images. If the situation remains fixed, subject placement and posture also remain similar.

Vary the following four axes, in descending order of impact:

1. **Situation and action**: What the subject is doing. This creates the largest difference.
2. **Camera position**: From the adjacent seat, standing above, or from the doorway.
3. **Distance**: Facial close-up, upper body, or full body.
4. **Lighting**: Usually produces the smallest difference.

Preset scenes such as `cafe` rotate situations automatically. With `custom`, pass multiple `--situation` values or edit the prompts so that the situations differ.

## Post-Generation Review

**Photorealistic prompts rarely pass on the first attempt.** Generate three to five variants and choose among them. Review each result in the following order; the earlier items fail more often.

1. **Hand anatomy**: Finger count, joint direction, and length. This is the most common failure.
2. **Hand-action logic**: Could a real hand perform the depicted action? Correct finger count does not guarantee a plausible action.
3. **Catchlights**: Pixel-identical reflections in both eyes look synthetic. Their position or shape should differ slightly.
4. **Text**: Signs, cup logos, and clothing prints. Garbled text immediately reveals generation. Removing text-bearing props from the prompt is often the fastest solution.
5. **Age**: Does the subject appear to be the specified age? If the result looks older, consult **Specifying Age**.
6. **Skin uniformity**: Identical texture across the forehead, cheeks, and chin is a failure. The nose and cheeks should show some color variation.
7. **Hair boundaries**: Inspect behind the ears, where hair rests on the shoulders, and at the ends of flyaways. Painted-looking clumps are a failure.
8. **Background people**: Check whether faces, hands, or legs have melted or merged.
9. **Shadow direction**: Shadows on the face, body, and props should be explainable by the same lights.
10. **Phone-camera character**: Background blur should remain achievable by a phone camera rather than resembling a cinematic still.
11. **Teeth**: For smiling subjects, check count and spacing.

When an item fails, **strengthen only that item with a positive instruction** and regenerate. Do not rewrite the entire prompt. Replacing the whole prompt can destroy elements that already worked.

## Common Mistakes

- **Including all 20 directives**: Too many imperfection instructions produce a noisy, blurry failed photograph. Use only the required layers. A distant full-body scene does not need every L4 facial directive.
- **Omitting or overemphasizing L5**: Omitting it can make the subject look neglected; emphasizing it can produce an actor. Use the strength table above.
- **Overdoing image-quality defects**: "Heavy noise" and "strong motion blur" create a failed image rather than realism. Always use modifiers such as "slight" and "mild."
- **Listing camera specifications**: "85 mm, f/1.4, ISO 100, Sony A7" pulls the result toward editorial photography. Do not list specifications for a phone snapshot. Nighttime "bokeh" creates the same problem.
- **Judging from one image**: The same prompt can vary substantially between generations. Generate several images before changing the prompt.
- **Varying only the light**: The resulting images remain too similar. See **What Changes Between Variants**.
- **Using only negative instructions**: Pair important negatives with positive descriptions of the desired state.

## Situations That Work Well

These situations are especially effective at producing realism. When the user has not specified a situation, select one of these to reduce the failure rate.

- **Backlit close-up**: Leaving the face shadows unfilled immediately increases realism.
- **Light from below**: A phone screen or table lamp creates lighting that image models rarely choose by default.
- **Sweat, flushed skin, or puffy eyes**: These strongly counteract flawless generated skin.
- **A laugh breaking through**: Partly closed eyes and facial asymmetry prevent a catalog smile.
- **Through glass**: Raindrops, outdoor scenery, and indoor reflections at different focal distances create plausible optics.
- **Foreground obstruction**: Another person's shoulder or the back of a seat makes the photographer feel present.
- **Just awake**: Pillow marks and flattened hair work well with Light L5 wording.

## Additional Resources

- [directives.md](./references/directives.md): The 20 source directives, grouped by layer, with effects, positive alternatives, and English phrasing. Consult this when a particular instruction is ineffective.
- [scenes.md](./references/scenes.md): Regional details for Korea, Japan, and the United States, plus scene presets. Use it to keep clothing, hair, backgrounds, and props from becoming generic.
- [build_prompt.py](./scripts/build_prompt.py): Prompt assembly script.

## Depicting People Responsibly

Do not use this skill to reproduce the face of a real person. It is intended to make fictional people look plausible, not to imitate a specific individual. Do not present generated results as photographs of real people, including for impersonation or deceptive profiles. Because the output can be difficult to distinguish from a photograph, ask about intended use when the user has not provided it.
