#!/usr/bin/env python3
"""Generate Adora 1 Nano views with enhanced camera enclosure design."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use the enhanced side reference with premium features
REFERENCE_IMAGE = "adora-1-nano-enhanced-side-ref.png"

CAMERA_ENCLOSURE_DESIGN = """
CAMERA ENCLOSURE REQUIREMENTS:
- Robot head camera enclosed in a SMALL ROUND-CORNER RECTANGLE BOX
- TWO CAMERA HOLES positioned as EYES within the enclosure
- Enclosure should be sleek, modern, and integrated with head design
- Round corners for smooth, consumer electronics appearance
- Professional camera housing design with premium finish

COLOR SCHEME (MAINTAIN):
- ENTIRE ROBOT BASE/BODY: BRIGHT YELLOW (premium finish)
- ALL ROBOT ARMS: MEDIUM GRAY (premium finish)
- CAMERA ENCLOSURE: Should complement the design (black, dark gray, or metallic)

MAINTAIN THESE ENHANCED FEATURES FROM REFERENCE:
- Premium ABS plastic finish: High-quality, seamless surface treatment
- Concealed wiring with sleek covers: All wires hidden within arm/body structure
- Consumer electronics quality: Apple-level fit and finish, polished surfaces
- Enhanced arm design: Streamlined with protective covers and clean joints

CAMERA ENCLOSURE DETAILS:
- Small, compact design integrated into robot head
- Round-corner rectangle shape (not square, not fully round)
- Two circular camera holes positioned like eyes
- Sleek housing with premium finish
- Should look like a professional robot camera system
- No visible screws or fasteners
- Seamless integration with robot head design
"""

VIEW_PROMPTS = [
    {
        "name": "front_view",
        "filename": "adora-1-nano-camera-front.png",
        "description": "FRONT VIEW - Enhanced Camera Enclosure",
        "prompt": f"""
{CAMERA_ENCLOSURE_DESIGN}

FRONT VIEW SPECIFICS:
- Generate a front view of the Adora 1 Nano robot with ENHANCED CAMERA ENCLOSURE
- Robot head features a SMALL ROUND-CORNER RECTANGLE BOX
- TWO CAMERA HOLES positioned as EYES within the enclosure
- YELLOW base/body and GRAY arms maintained
- Premium finishes with seamless color transitions
- Clean studio background (white/light gray)
- Professional product lighting highlighting the camera enclosure

CAMERA DESIGN IMPLEMENTATION:
- Compact round-corner rectangle enclosure on robot head
- Two circular camera lenses positioned like eyes
- Professional camera housing with premium finish
- Sleek, modern consumer electronics appearance
- Clean integration with robot head structure

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Premium product photography lighting

The front view must showcase the enhanced camera enclosure with two eye-like camera holes.
"""
    },
    {
        "name": "side_view",
        "filename": "adora-1-nano-camera-side.png",
        "description": "SIDE VIEW - Enhanced Camera Enclosure",
        "prompt": f"""
{CAMERA_ENCLOSURE_DESIGN}

SIDE VIEW SPECIFICS:
- Generate a side view of the Adora 1 Nano robot with ENHANCED CAMERA ENCLOSURE
- Camera enclosure visible from side profile showing depth and integration
- YELLOW base/body and GRAY arms visible from side
- Premium finishes with seamless color transitions
- Clean studio background (white/light gray)
- Professional side-view lighting with rim highlights

CAMERA DESIGN IMPLEMENTATION:
- Round-corner rectangle enclosure visible from side
- Shows the depth and profile of camera housing
- Two camera holes visible from side angle
- Sleek housing integration with robot head
- Premium finish on camera enclosure
- Professional robot camera system appearance

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting with rim accents

The side view should show the camera enclosure profile and integration.
"""
    },
    {
        "name": "top_view",
        "filename": "adora-1-nano-camera-top.png",
        "description": "TOP VIEW - Enhanced Camera Enclosure",
        "prompt": f"""
{CAMERA_ENCLOSURE_DESIGN}

TOP VIEW SPECIFICS:
- Generate a top view of the Adora 1 Nano robot with ENHANCED CAMERA ENCLOSURE
- Camera enclosure visible from above showing layout and positioning
- YELLOW base/body and GRAY arms visible from above
- Premium finishes with seamless color transitions
- Clean studio background (white/light gray)
- Professional overhead lighting showcasing the camera design

CAMERA DESIGN IMPLEMENTATION:
- Round-corner rectangle enclosure visible from above
- Two camera holes positioned like eyes from top view
- Shows the spatial arrangement of camera system
- Sleek housing with premium finish visible from above
- Professional camera housing layout
- Clean integration with robot head structure

TECHNICAL SPECIFICATIONS:
- Clean studio background
- 2K resolution
- 4:3 aspect ratio
- Professional overhead studio lighting

The top view should display the camera enclosure layout and eye positioning.
"""
    }
]

# Generation config for precise camera enclosure implementation
config = types.GenerateContentConfig(
    temperature=0.2,  # Very low temperature for precise camera design
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

def generate_camera_enclosure_view(view_config):
    """Generate Adora 1 Nano views with enhanced camera enclosure."""
    print(f"\n{'='*60}")
    print(f"Generating: {view_config['description']}")
    print(f"Output: {view_config['filename']}")
    print(f"Reference: {REFERENCE_IMAGE}")
    print(f"New Feature: Round-corner rectangle camera enclosure with two eye holes")
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

    # Combine reference image with camera enclosure prompt
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
    print("Starting Enhanced Camera Enclosure Adora 1 Nano Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference for enhanced features")
    print("Adding: Round-corner rectangle camera enclosure with two eye holes")
    print("Color scheme: YELLOW BASE + GRAY ARMS")
    print("Maintaining all premium enhanced features")
    print(f"Generating {len(VIEW_PROMPTS)} views with new camera design")

    generated_files = []

    for i, view in enumerate(VIEW_PROMPTS, 1):
        print(f"\n[{i}/{len(VIEW_PROMPTS)}] Processing {view['name']}...")
        result = generate_camera_enclosure_view(view)
        if result:
            generated_files.append(result)

    print("\n" + "="*60)
    print("Enhanced Camera Enclosure Adora 1 Nano Generation Complete!")
    print(f"Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"  ✓ {file}")
    print(f"\nReference used: {REFERENCE_IMAGE}")
    print("\nAll views feature:")
    print("  • NEW: Round-corner rectangle camera enclosure")
    print("  • NEW: Two camera holes positioned as eyes")
    print("  • YELLOW robot base/body (premium ABS plastic)")
    print("  • GRAY robot arms (premium ABS plastic)")
    print("  • Premium ABS plastic finish (from reference)")
    print("  • Concealed wiring with sleek covers (from reference)")
    print("  • Consumer electronics quality (from reference)")
    print("  • Enhanced arm design with protective covers")
    print("  • Clean studio backgrounds")
    print("  • 2K resolution for professional use")
    print("="*60)