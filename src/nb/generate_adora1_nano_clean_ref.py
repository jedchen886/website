#!/usr/bin/env python3
"""Generate Adora 1 Nano views based on adora-1-nano-club-clean reference with enhanced features."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use the club-clean reference that has correct wheels
REFERENCE_IMAGE = "adora-1-nano-club-clean.png"

ENHANCEMENT_PROMPT = """
ENHANCEMENT REQUIREMENTS:
- Start with the exact Adora 1 Nano robot structure from the reference image
- Maintain the CORRECT wheel design as shown in the reference
- Enhance with premium consumer electronics quality:
  * Polished ABS plastic finish on all surfaces
  * Conceal all visible wires within the arm and body structure
  * Add sleek protective covers over mechanical joints
  * Premium consumer electronics surface quality
- Robot head: Maintain the robot aesthetic, integrate camera system
- Clean background: Studio white or light gray background
- Professional product photography quality

CRITICAL: Keep the wheel design exactly as shown in the reference image - do not modify or distort the wheels.
"""

VIEW_PROMPTS = [
    {
        "name": "front_view",
        "filename": "adora-1-nano-clean-front.png",
        "description": "FRONT VIEW - Enhanced with Correct Wheels",
        "prompt": f"""
{ENHANCEMENT_PROMPT}

FRONT VIEW SPECIFICS:
- Generate a front view of the Adora 1 Nano robot
- Use the exact wheel design from the reference image
- Show both front wheels correctly positioned and proportioned
- Enhanced robot arms with polished ABS plastic finish
- Clean studio background (white/light gray)
- Professional product lighting highlighting enhanced finishes

TECHNICAL SPECIFICATIONS:
- Clean studio background (not transparent)
- 2K resolution
- 4:3 aspect ratio
- Product photography lighting
- Emphasize enhanced material quality while maintaining correct wheel design

The front view must have the exact same wheel design as the reference image.
"""
    },
    {
        "name": "side_view",
        "filename": "adora-1-nano-clean-side.png",
        "description": "SIDE VIEW - Enhanced with Correct Wheels",
        "prompt": f"""
{ENHANCEMENT_PROMPT}

SIDE VIEW SPECIFICS:
- Generate a side view of the Adora 1 Nano robot
- Show the correct wheel design from the side as in reference
- Enhanced robot arms with polished ABS plastic and concealed wiring
- Maintain original arm structure and joint placement
- Clean studio background (white/light gray)
- Professional side-view product photography

TECHNICAL SPECIFICATIONS:
- Clean studio background (not transparent)
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting with rim highlights
- Showcase the sleek profile with enhanced materials

The side view must maintain the correct wheel design from the reference.
"""
    },
    {
        "name": "top_view",
        "filename": "adora-1-nano-clean-top.png",
        "description": "TOP VIEW - Enhanced with Correct Wheels",
        "prompt": f"""
{ENHANCEMENT_PROMPT}

TOP VIEW SPECIFICS:
- Generate a top view of the Adora 1 Nano robot
- Show the wheel base and layout as in the reference
- Enhanced arm construction with consumer electronics quality
- Maintain original arm placement and robot head structure
- Clean studio background (white/light gray)
- Professional overhead product photography

TECHNICAL SPECIFICATIONS:
- Clean studio background (not transparent)
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting from above
- Emphasize enhanced material quality and construction

The top view should show the correct wheel layout from the reference.
"""
    }
]

# Generation config for 2K quality
config = types.GenerateContentConfig(
    temperature=0.5,  # Lower temperature for accurate wheel reproduction
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

def generate_clean_view(view_config):
    """Generate enhanced Adora 1 Nano with correct wheels."""
    print(f"\n{'='*60}")
    print(f"Generating: {view_config['description']}")
    print(f"Output: {view_config['filename']}")
    print(f"Reference: {REFERENCE_IMAGE}")
    print(f"{'='*60}")

    # Load the club-clean reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, view_config["filename"])

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Combine reference image with enhancement prompt
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
    print("Starting Enhanced Adora 1 Nano Generation with Correct Wheels...")
    print(f"Using {REFERENCE_IMAGE} as reference for accurate wheel design")
    print("Enhancing with consumer electronics quality")
    print(f"Generating {len(VIEW_PROMPTS)} views with clean studio backgrounds")

    generated_files = []

    for i, view in enumerate(VIEW_PROMPTS, 1):
        print(f"\n[{i}/{len(VIEW_PROMPTS)}] Processing {view['name']}...")
        result = generate_clean_view(view)
        if result:
            generated_files.append(result)

    print("\n" + "="*60)
    print("Enhanced Adora 1 Nano Generation Complete!")
    print(f"Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"  ✓ {file}")
    print(f"\nReference used: {REFERENCE_IMAGE}")
    print("\nAll views feature:")
    print("  • Correct wheel design from reference")
    print("  • Premium ABS plastic finish")
    print("  • Concealed wiring with sleek covers")
    print("  • Consumer electronics quality")
    print("  • Clean studio backgrounds")
    print("  • 2K resolution for professional use")
    print("="*60)