#!/usr/bin/env python3
"""Generate Adora 1 Nano views based on enhanced side reference with premium features."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use the enhanced side reference with premium features
REFERENCE_IMAGE = "adora-1-nano-enhanced-side-ref.png"

ENHANCED_FEATURES = """
MAINTAIN THESE EXACT ENHANCED FEATURES FROM REFERENCE:
- Premium ABS plastic finish: High-quality, seamless surface treatment
- Concealed wiring with sleek covers: All wires hidden within arm/body structure
- Consumer electronics quality: Apple-level fit and finish, polished surfaces
- Enhanced arm design: Streamlined with protective covers and clean joints
- Robot head with integrated camera system: Maintaining robot aesthetic
- Clean, professional appearance: No visible mechanical components

CRITICAL REQUIREMENTS:
- Reproduce the exact same level of enhancement as shown in reference
- Maintain the same premium surface quality and finish
- Keep the same sleek, consumer electronics aesthetic
- Consistent styling and proportions with reference image
- Professional product photography quality
"""

VIEW_PROMPTS = [
    {
        "name": "front_view",
        "filename": "adora-1-nano-premium-front.png",
        "description": "FRONT VIEW - Premium Enhanced Features",
        "prompt": f"""
{ENHANCED_FEATURES}

FRONT VIEW SPECIFICS:
- Generate a front view of the Adora 1 Nano robot with the EXACT same enhanced features as the reference
- Premium ABS plastic finish with seamless, high-quality surfaces
- Concealed wiring with sleek protective covers on arms and joints
- Consumer electronics quality finish throughout
- Robot head with integrated camera maintaining robot aesthetic
- Clean studio background (white/light gray)
- Professional product lighting highlighting the premium finishes

MAINTAIN CONSISTENCY:
- Same level of enhancement as the reference image
- Identical surface quality and material appearance
- Consistent premium consumer electronics aesthetic
- Professional product photography standards

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Premium product photography lighting

The front view must have the exact same premium enhanced features as the reference.
"""
    },
    {
        "name": "side_view",
        "filename": "adora-1-nano-premium-side.png",
        "description": "SIDE VIEW - Premium Enhanced Features",
        "prompt": f"""
{ENHANCED_FEATURES}

SIDE VIEW SPECIFICS:
- Generate a side view of the Adora 1 Nano robot with the EXACT same enhanced features as the reference
- Premium ABS plastic finish with smooth, seamless surfaces
- Concealed wiring with sleek covers visible in profile
- Consumer electronics quality with polished appearance
- Enhanced arm design with streamlined joints and covers
- Clean studio background (white/light gray)
- Professional side-view lighting with rim highlights

MAINTAIN CONSISTENCY:
- Match the exact enhancement level from reference
- Identical material quality and surface finish
- Same premium consumer electronics aesthetic
- Professional photography standards

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting with rim accents

The side view must match the premium enhanced features of the reference exactly.
"""
    },
    {
        "name": "top_view",
        "filename": "adora-1-nano-premium-top.png",
        "description": "TOP VIEW - Premium Enhanced Features",
        "prompt": f"""
{ENHANCED_FEATURES}

TOP VIEW SPECIFICS:
- Generate a top view of the Adora 1 Nano robot with the EXACT same enhanced features as the reference
- Premium ABS plastic finish visible from above
- Concealed wiring with sleek protective covers on arm joints
- Consumer electronics quality surface treatment
- Enhanced arm construction with premium finish
- Clean studio background (white/light gray)
- Professional overhead lighting showcasing premium quality

MAINTAIN CONSISTENCY:
- Same enhancement level as reference image
- Identical surface quality and premium finish
- Consistent consumer electronics aesthetic
- Professional product photography

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Professional overhead studio lighting

The top view must demonstrate the same premium enhanced features as the reference.
"""
    }
]

# Generation config for premium quality
config = types.GenerateContentConfig(
    temperature=0.4,  # Very low temperature for precise feature reproduction
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

def generate_premium_view(view_config):
    """Generate premium enhanced Adora 1 Nano views."""
    print(f"\n{'='*60}")
    print(f"Generating: {view_config['description']}")
    print(f"Output: {view_config['filename']}")
    print(f"Reference: {REFERENCE_IMAGE}")
    print(f"{'='*60}")

    # Load the enhanced side reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, view_config["filename"])

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Combine reference image with premium enhancement prompt
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
    print("Starting Premium Enhanced Adora 1 Nano Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference for exact enhanced features")
    print("Maintaining premium consumer electronics quality")
    print(f"Generating {len(VIEW_PROMPTS)} views with enhanced features")

    generated_files = []

    for i, view in enumerate(VIEW_PROMPTS, 1):
        print(f"\n[{i}/{len(VIEW_PROMPTS)}] Processing {view['name']}...")
        result = generate_premium_view(view)
        if result:
            generated_files.append(result)

    print("\n" + "="*60)
    print("Premium Enhanced Adora 1 Nano Generation Complete!")
    print(f"Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"  ✓ {file}")
    print(f"\nReference used: {REFERENCE_IMAGE}")
    print("\nAll views maintain EXACT enhanced features:")
    print("  • Premium ABS plastic finish (from reference)")
    print("  • Concealed wiring with sleek covers (from reference)")
    print("  • Consumer electronics quality (from reference)")
    print("  • Enhanced arm design with protective covers")
    print("  • Robot head with integrated camera")
    print("  • Clean studio backgrounds")
    print("  • 2K resolution for professional use")
    print("="*60)