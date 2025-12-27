#!/usr/bin/env python3
"""Generate enhanced artistic renderings of Adora 1 Nano robot with consumer electronics improvements."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Enhanced design prompt - now using actual Adora 1 Nano as base
DESIGN_ENHANCEMENTS = """
ENHANCEMENT REQUIREMENTS (DO NOT CHANGE BASIC STRUCTURE):
- Start with the exact Adora 1 Nano robot structure and arms from the reference image
- Keep the original robot arm design and placement
- Enhance with premium consumer electronics quality:
  * Polished ABS plastic finish on all surfaces
  * Conceal all visible wires within the arm structure
  * Add sleek protective covers over arm joints
  * Enhance surface quality to consumer electronics standards
- Robot head: Maintain the robot aesthetic, integrate camera system into existing head design
- Improve molding quality: Seamless surfaces, precision fit and finish
- NO structural changes to arms or body - only surface and material quality improvements

QUALITY STANDARDS:
- Apple-level consumer electronics finish
- Smooth, premium ABS plastic texture
- Concealed wiring with seamless covers
- Professional product photography quality
- Maintain all Adora 1 Nano's distinctive features and proportions
"""

VIEW_PROMPTS = [
    {
        "name": "front_view",
        "filename": "adora-1-nano-enhanced-front.png",
        "description": "FRONT VIEW - Enhanced Adora 1 Nano",
        "prompt": f"""
{DESIGN_ENHANCEMENTS}

FRONT VIEW SPECIFICS:
- Front elevation of the exact Adora 1 Nano robot from reference image
- Enhance the existing robot arms with polished ABS plastic finish
- Conceal wires within the arm structure while maintaining arm design
- Add consumer electronics quality to the robot head with integrated camera
- Professional studio lighting highlighting the enhanced finish

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Product photography lighting
- Emphasize the enhanced material quality and finish
- Maintain all original Adora 1 Nano proportions and structure

Show the original Adora 1 Nano with premium consumer electronics enhancements.
"""
    },
    {
        "name": "side_view",
        "filename": "adora-1-nano-enhanced-side.png",
        "description": "SIDE VIEW - Enhanced Adora 1 Nano",
        "prompt": f"""
{DESIGN_ENHANCEMENTS}

SIDE VIEW SPECIFICS:
- Side profile of the exact Adora 1 Nano robot from reference image
- Show enhanced robot arms with polished ABS plastic and concealed wiring
- Maintain original arm structure and joint placement
- Consumer electronics quality finish on all visible surfaces
- Robot head with integrated camera enhancement

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting with rim highlights
- Showcase the sleek profile with enhanced materials
- Maintain authentic Adora 1 Nano silhouette

Display the original Adora 1 Nano side profile with premium enhancements.
"""
    },
    {
        "name": "top_view",
        "filename": "adora-1-nano-enhanced-top.png",
        "description": "TOP VIEW - Enhanced Adora 1 Nano",
        "prompt": f"""
{DESIGN_ENHANCEMENTS}

TOP VIEW SPECIFICS:
- Top-down view of the exact Adora 1 Nano robot from reference image
- Show enhanced arm construction with consumer electronics quality
- Maintain original arm placement and robot head structure
- Polished ABS plastic finish with concealed internal wiring
- Integrated camera system in robot head

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting from above
- Emphasize enhanced material quality and construction
- Maintain authentic Adora 1 Nano footprint and layout

Present the original Adora 1 Nano from above with premium enhancements.
"""
    }
]

# Generation config for 2K quality
config = types.GenerateContentConfig(
    temperature=0.6,  # Lower temperature for faithful enhancement
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

def generate_enhanced_view(view_config):
    """Generate enhanced Adora 1 Nano rendering."""
    print(f"\n{'='*60}")
    print(f"Generating: {view_config['description']}")
    print(f"Output: {view_config['filename']}")
    print(f"{'='*60}")

    # Use the actual Adora 1 nano image as base
    input_path = os.path.join(base_dir, "adora-1-nano-feature1.png")

    if not os.path.exists(input_path):
        print(f"Error: Adora 1 Nano reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, view_config["filename"])

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Combine Adora 1 Nano image with enhancement prompt
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
    print("Starting Enhanced Adora 1 Nano Rendering...")
    print("Using actual Adora 1 Nano as base reference")
    print("Enhancing with consumer electronics quality while maintaining original structure")
    print(f"Generating {len(VIEW_PROMPTS)} enhanced views at 2K resolution")

    generated_files = []

    for i, view in enumerate(VIEW_PROMPTS, 1):
        print(f"\n[{i}/{len(VIEW_PROMPTS)}] Processing {view['name']}...")
        result = generate_enhanced_view(view)
        if result:
            generated_files.append(result)

    print("\n" + "="*60)
    print("Enhanced Adora 1 Nano Rendering Complete!")
    print(f"Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"  ✓ {file}")
    print("\nEnhancements applied:")
    print("  • Original Adora 1 Nano structure and arms maintained")
    print("  • Premium ABS plastic finish on all surfaces")
    print("  • Concealed wiring within existing arm structure")
    print("  • Consumer electronics quality covers and finishes")
    print("  • Enhanced robot head with integrated camera")
    print("  • Transparent backgrounds for flexibility")
    print("  • 2K resolution for professional use")
    print("="*60)