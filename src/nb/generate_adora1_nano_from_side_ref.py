#!/usr/bin/env python3
"""Generate Adora 1 Nano views based on the enhanced side reference image."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Base reference image
REFERENCE_IMAGE = "adora-1-nano-enhanced-side-ref.png"

VIEW_PROMPTS = [
    {
        "name": "front_view",
        "filename": "adora-1-nano-from-ref-front.png",
        "description": "FRONT VIEW - Based on Enhanced Side Reference",
        "prompt": """
Generate a front view of the Adora 1 Nano robot based on the enhanced side reference image.

REQUIREMENTS:
- Create the front view of the exact same robot model shown in the reference image
- Maintain all the enhanced features: premium ABS plastic finish, concealed wiring, consumer electronics quality
- Show the robot's front face with enhanced head design
- Both arms should be visible with the same polished finish and enhanced quality
- Keep the same proportions, style, and enhancement level as the reference

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting
- Consistent with the reference image quality and style

The front view should look like it's the exact same robot model as the reference, viewed from the front.
"""
    },
    {
        "name": "top_view",
        "filename": "adora-1-nano-from-ref-top.png",
        "description": "TOP VIEW - Based on Enhanced Side Reference",
        "prompt": """
Generate a top view of the Adora 1 Nano robot based on the enhanced side reference image.

REQUIREMENTS:
- Create a top-down view of the exact same robot model shown in the reference image
- Maintain all the enhanced features: premium ABS plastic finish, concealed wiring, consumer electronics quality
- Show the robot's head from above with enhanced design
- Both arms should be visible in their positions from above
- Keep the same proportions, style, and enhancement level as the reference

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting from above
- Consistent with the reference image quality and style

The top view should look like it's the exact same robot model as the reference, viewed from above.
"""
    }
]

# Generation config
config = types.GenerateContentConfig(
    temperature=0.6,
    top_p=0.95,
    max_output_tokens=32768,
    response_modalities=["TEXT", "IMAGE"],
    safety_settings=[
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="OFF"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="OFF"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="OFF"),
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="OFF"),
    ],
    image_config=types.ImageConfig(
        aspect_ratio="4:3",
        image_size="2K",
    ),
)

def generate_view_from_reference(view_config):
    """Generate a view based on the enhanced side reference."""
    print(f"\n{'='*60}")
    print(f"Generating: {view_config['description']}")
    print(f"Output: {view_config['filename']}")
    print(f"Reference: {REFERENCE_IMAGE}")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, view_config["filename"])

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Combine reference image with view prompt
    contents = [input_image, view_config["prompt"]]

    try:
        for chunk in client.models.generate_content_stream(
            model="gemini-3-pro-image-preview",
            contents=contents,
            config=config,
        ):
            if chunk.candidates and chunk.candidates[0].content and chunk.candidates[0].content.parts:
                for part in chunk.candidates[0].content.parts:
                    if part.text:
                        print(f"Model: {part.text}")
                    elif part.inline_data:
                        with open(output_path, "wb") as f:
                            f.write(part.inline_data.data)
                        print(f"✓ Saved: {output_path}")
                        return output_path
    except Exception as e:
        print(f"Error generating {view_config['filename']}: {e}")
        return None

    return None

if __name__ == "__main__":
    print("Starting Adora 1 Nano View Generation from Enhanced Side Reference...")
    print(f"Using {REFERENCE_IMAGE} as the base reference")
    print(f"Generating {len(VIEW_PROMPTS)} additional views at 2K resolution")
    print("Maintaining consistency with reference image quality and enhancements")

    generated_files = []

    for i, view in enumerate(VIEW_PROMPTS, 1):
        print(f"\n[{i}/{len(VIEW_PROMPTS)}] Processing {view['name']}...")
        result = generate_view_from_reference(view)
        if result:
            generated_files.append(result)

    print("\n" + "="*60)
    print("View Generation Complete!")
    print(f"Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"  ✓ {file}")
    print(f"\nReference used: {REFERENCE_IMAGE}")
    print("\nAll views maintain:")
    print("  • Same robot model as reference")
    print("  • Premium ABS plastic finish")
    print("  • Concealed wiring with sleek covers")
    print("  • Consumer electronics quality")
    print("  • Consistent proportions and style")
    print("  • Transparent backgrounds")
    print("  • 2K resolution")
    print("="*60)