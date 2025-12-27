#!/usr/bin/env python3
"""Generate Adora 1 Nano views with yellow base and gray arms while maintaining enhanced features."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use the enhanced side reference with premium features
REFERENCE_IMAGE = "adora-1-nano-enhanced-side-ref.png"

COLOR_SCHEME = """
COLOR REQUIREMENTS:
- ENTIRE ROBOT BASE/BODY: BRIGHT YELLOW (premium finish)
- ALL ROBOT ARMS: MEDIUM GRAY (premium finish)
- Premium ABS plastic finish maintained for both colors
- Concealed wiring with sleek covers (same color as respective parts)
- Consumer electronics quality with seamless color transitions

MAINTAIN THESE ENHANCED FEATURES FROM REFERENCE:
- Premium ABS plastic finish: High-quality, seamless surface treatment
- Concealed wiring with sleek covers: All wires hidden within arm/body structure
- Consumer electronics quality: Apple-level fit and finish, polished surfaces
- Enhanced arm design: Streamlined with protective covers and clean joints
- Robot head with integrated camera system: Maintaining robot aesthetic
- Clean, professional appearance: No visible mechanical components

COLOR DETAILS:
- Base/Body: Vibrant, premium yellow with glossy ABS plastic finish
- Arms: Professional medium gray with matching glossy ABS plastic finish
- Head: Coordinate with base (yellow) or neutral (white/silver)
- Joints/Covers: Match respective part colors (yellow for base joints, gray for arm joints)
- Clean color separation with premium masking and finish
"""

VIEW_PROMPTS = [
    {
        "name": "front_view",
        "filename": "adora-1-nano-yellow-front.png",
        "description": "FRONT VIEW - Yellow Base & Gray Arms",
        "prompt": f"""
{COLOR_SCHEME}

FRONT VIEW SPECIFICS:
- Generate a front view of the Adora 1 Nano robot with YELLOW BASE and GRAY ARMS
- ENTIRE robot base/body in premium bright yellow ABS plastic
- ALL robot arms in professional medium gray ABS plastic
- Premium finishes with seamless color transitions
- Concealed wiring with color-matched sleek covers
- Clean studio background (white/light gray)
- Professional product lighting highlighting the premium color finishes

COLOR IMPLEMENTATION:
- Base/Body: Vibrant yellow with glossy premium finish
- Arms: Professional gray with matching glossy finish
- Clean color separation at arm-body connection points
- Enhanced consumer electronics quality maintained

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Premium product photography lighting

The front view must have yellow base and gray arms with premium enhanced features.
"""
    },
    {
        "name": "side_view",
        "filename": "adora-1-nano-yellow-side.png",
        "description": "SIDE VIEW - Yellow Base & Gray Arms",
        "prompt": f"""
{COLOR_SCHEME}

SIDE VIEW SPECIFICS:
- Generate a side view of the Adora 1 Nano robot with YELLOW BASE and GRAY ARMS
- ENTIRE robot base/body visible in premium bright yellow ABS plastic
- ALL robot arms visible in professional medium gray ABS plastic
- Premium finishes with seamless color transitions
- Concealed wiring with color-matched sleek covers visible in profile
- Clean studio background (white/light gray)
- Professional side-view lighting with rim highlights

COLOR IMPLEMENTATION:
- Base/Body: Vibrant yellow with glossy premium finish from side view
- Arms: Professional gray with matching glossy finish
- Clean color separation maintained from all angles
- Enhanced consumer electronics quality preserved

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting with rim accents

The side view must showcase yellow base and gray arms with premium enhanced features.
"""
    },
    {
        "name": "top_view",
        "filename": "adora-1-nano-yellow-top.png",
        "description": "TOP VIEW - Yellow Base & Gray Arms",
        "prompt": f"""
{COLOR_SCHEME}

TOP VIEW SPECIFICS:
- Generate a top view of the Adora 1 Nano robot with YELLOW BASE and GRAY ARMS
- ENTIRE robot base/body visible in premium bright yellow ABS plastic from above
- ALL robot arms visible in professional medium gray ABS plastic from above
- Premium finishes with seamless color transitions
- Concealed wiring with color-matched sleek covers
- Clean studio background (white/light gray)
- Professional overhead lighting showcasing premium color finishes

COLOR IMPLEMENTATION:
- Base/Body: Vibrant yellow with glossy premium finish visible from above
- Arms: Professional gray with matching glossy finish from above
- Clean color separation at arm attachment points
- Enhanced consumer electronics quality maintained

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Professional overhead studio lighting

The top view must display yellow base and gray arms with premium enhanced features.
"""
    }
]

# Generation config for precise color implementation
config = types.GenerateContentConfig(
    temperature=0.3,  # Very low temperature for precise color reproduction
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

def generate_colored_view(view_config):
    """Generate colored Adora 1 Nano views with yellow base and gray arms."""
    print(f"\n{'='*60}")
    print(f"Generating: {view_config['description']}")
    print(f"Output: {view_config['filename']}")
    print(f"Reference: {REFERENCE_IMAGE}")
    print(f"Color Scheme: YELLOW BASE + GRAY ARMS")
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

    # Combine reference image with color specification prompt
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
    print("Starting Yellow Base & Gray Arms Adora 1 Nano Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference for enhanced features")
    print("Applying color scheme: YELLOW BASE + GRAY ARMS")
    print("Maintaining all premium enhanced features")
    print(f"Generating {len(VIEW_PROMPTS)} views with new color scheme")

    generated_files = []

    for i, view in enumerate(VIEW_PROMPTS, 1):
        print(f"\n[{i}/{len(VIEW_PROMPTS)}] Processing {view['name']}...")
        result = generate_colored_view(view)
        if result:
            generated_files.append(result)

    print("\n" + "="*60)
    print("Yellow Base & Gray Arms Adora 1 Nano Generation Complete!")
    print(f"Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"  ✓ {file}")
    print(f"\nReference used: {REFERENCE_IMAGE}")
    print("\nAll views feature:")
    print("  • YELLOW robot base/body (premium ABS plastic)")
    print("  • GRAY robot arms (premium ABS plastic)")
    print("  • Premium ABS plastic finish (from reference)")
    print("  • Concealed wiring with sleek covers (from reference)")
    print("  • Consumer electronics quality (from reference)")
    print("  • Enhanced arm design with protective covers")
    print("  • Robot head with integrated camera")
    print("  • Clean studio backgrounds")
    print("  • 2K resolution for professional use")
    print("="*60)