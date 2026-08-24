# Regional Details and Scene Presets

## Why Regional Details Matter

Using only "Korean woman" tends to push a model toward one of three defaults: a K-beauty advertisement, an idol profile, or a generic East Asian face with no clear local context. None represents an ordinary person who simply lives there.

Regional context is not expressed by a face alone. **Clothing, hair, makeup intensity, buildings, signs, and handheld objects** must work together to create an everyday local photograph. Treat the details below as ingredients. Select only two or three rather than inserting an entire list.

## Korea

- **Makeup**: A light base, softly defined brows, and muted lips. Glossy advertising-style lips can increase the generated look.
- **Hair**: Black to dark brown, with bangs or a half-up style. Leave some flyaways untidied.
- **Clothing**: Oversized knitwear, cropped outerwear, slacks, or ankle socks. Large logos risk malformed text.
- **Backgrounds**: Low-rise shops on narrow streets, vertical signs, convenience-store lighting, apartment complexes, or subway platform doors.
- **Props**: A disposable iced Americano cup, wireless earbuds, or a crossbody bag.
- **Caution**: Do not request legible sign text. Korean characters are likely to deform. Use "a sign softly out of focus in the background."

## Japan

- **Makeup**: Very light, with little eyeliner and a faint cheek flush.
- **Hair**: Dark brown to ash tones, with a layered bob or half-up style.
- **Clothing**: Layered loose fits, cardigans, long skirts, or loafers in low-saturation colors.
- **Backgrounds**: Narrow residential streets, utility poles and overhead wires, vending machines, bicycles, convenience stores, or train platforms.
- **Props**: Canned coffee, a tote bag, or a folding umbrella.
- **Caution**: Results can drift toward anime. Put "photorealistic photograph" near the beginning of the prompt.

## United States

- **Makeup**: Minimal makeup or strongly defined brows. Specifying freckles can substantially increase realism.
- **Hair**: Natural waves, a messy bun, or shades from light brown to blonde.
- **Clothing**: Hoodies, denim, sneakers, tank tops, or knit beanies.
- **Backgrounds**: Wide roads and parking lots, brick buildings, lawns, diners, or college campuses.
- **Props**: A paper coffee cup, backpack, or tumbler.
- **Caution**: The population is diverse. If ethnicity is relevant to the request, specify it rather than allowing the model to choose an implicit default.

## Scene Presets

Use these with `build_prompt.py --scene <key>`.

| Key | Setting | Light | Natural Moment |
| --- | --- | --- | --- |
| `cafe` | Window seat in a cafe | Afternoon window light | Setting down a cup and looking outside |
| `home` | Beside the bed or in the kitchen of a small apartment | Light through curtains or a desk lamp | Brushing hair aside or just after a yawn |
| `street` | Narrow street at dusk | Mixed shop-sign and street-lamp light | Stopping mid-stride to look back |
| `commute` | Subway or bus interior | Vehicle fluorescents | Staring through the window as focus drifts |
| `park` | Park bench or grass | Sunlight filtered through leaves | Wind pushing hair across the face |
| `restaurant` | Restaurant or bar table | A warm ceiling lamp and light from nearby tables | Just before laughter breaks through |
| `office` | Office desk | Ceiling fluorescents and monitor light | Looking away from the monitor |
| `night` | Interior beside a window at night | One room lamp and city light outside | Looking up from a phone |

## Depicting a Selfie

A selfie is physically different from a photograph taken by someone else. Without these differences, the result becomes a face photograph that does not read as a selfie.

- Arm's-length distance, with the face close and high in the frame.
- Wide-angle distortion, making the nose slightly larger, the ears smaller, and the frame edges stretched.
- A camera angle looking slightly down from above or up from below.
- One arm extending outside the frame, with the shoulder leaning toward it.
- Eyes focused on the on-screen preview rather than the lens, creating a subtly offset gaze.

Together, these five details create the characteristic awkwardness of a selfie. The final item is especially effective.

## When the Frame Contains Text

Signs, cup logos, clothing prints, and book covers can destroy realism quickly. Use one of three approaches:

1. **Remove it**: The most reliable option. Use "a plain cup with no logo" or "the sign remains outside the frame."
2. **Defocus it**: Use "the sign in the background is out of focus and unreadable." Depth of field provides the most natural explanation.
3. **Obscure it**: Cover part of the text with a hand or body.

Korean and Japanese characters deform more often than Latin text. Prefer the first or second approach in East Asian settings.

## Scenes With Multiple People

`--group N` adds baseline guidance, but the prompt should still assign gaze according to the situation. The key is to name **what each person is looking at**. Shared attention is natural when the activity calls for it; avoid unexplained synchronized gaze.

| Situation | Example Gaze Assignment |
| --- | --- |
| Meeting or study session | The speaker, a laptop, the whiteboard, or down at notes |
| Shared meal | The person speaking, a plate, a nearby table, or a phone |
| Outdoor outing | Relevant parts of the scenery, a companion beside the camera, or the ground |

Vary clothing as well, or every person may wear the same tones. Change at least one of color, material, or formality. If three people wear hoodies, for example, put one person in a shirt.

**Do not apply Directive 14 globally.** It assumes one subject and can make an entire group look in the same direction.
