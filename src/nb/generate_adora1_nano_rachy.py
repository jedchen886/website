#!/usr/bin/env python3
"""Generate artistic product renderings of Adora 1 Nano using rachy mini reference."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Enhanced design prompt
DESIGN_ENHANCEMENTS = """
CRITICAL DESIGN REQUIREMENTS:
- Based on Adora 1 Nano structure - maintain the basic robot form and proportions
- Use rachy mini as reference for styling and aesthetic inspiration
- Robot arms: Polished finish with consumer-grade molding quality using ABS plastic
- Wire management: All wires completely buried within the arm internals
- Arm covers: Sleek protective covers with consumer electronics appearance
- Robot head: Maintain robot/aesthetic design elements - NO HUMAN HEAD
- Use camera integrated into robot head design (not human face)
- Surface finish: Smooth, high-quality ABS plastic texture
- No exposed wiring or mechanical components
- Consumer electronics level fit and finish

QUALITY STANDARDS:
- Premium robotics product design aesthetics
- Smooth, seamless surfaces
- Precise molding lines
- Professional product photography quality
- Maintain Adora 1 Nano's distinctive robot characteristics
"""

VIEW_PROMPTS = [
    {
        "name": "front_view",
        "filename": "adora-1-nano-front-view-2k.png",
        "description": "FRONT VIEW - Technical Product Rendering",
        "prompt": f"""
{DESIGN_ENHANCEMENTS}

VIEW REQUIREMENTS:
- Front elevation view of Adora 1 Nano robot
- Show the complete front face with robot-style head design
- Camera system integrated into robot head (not human features)
- Both arms visible with polished finish and consumer-grade covers
- Standing position on neutral surface
- Professional studio lighting

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Product photography lighting setup
- Soft shadows for depth
- Clean, minimalist studio environment
- Sharp focus on design details
- High-resolution surface texture visibility

The robot should maintain its Adora 1 Nano identity while showing enhanced consumer electronics quality.
"""
    },
    {
        "name": "side_view",
        "filename": "adora-1-nano-side-view-2k.png",
        "description": "SIDE VIEW - Technical Product Rendering",
        "prompt": f"""
{DESIGN_ENHANCEMENTS}

VIEW REQUIREMENTS:
- Side elevation view of Adora 1 Nano robot
- Profile view showing the sleek contours and design lines
- Robot head profile with integrated camera system
- Arm design with consumer electronics aesthetic clearly visible
- Show the slim profile and polished surfaces

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Professional product photography lighting
- Rim lighting to highlight contours
- Studio environment with reflective surface
- Emphasis on silhouette and form factor
- Premium robotics product presentation

The side view should emphasize the sleek robot profile and premium manufacturing quality while maintaining Adora 1 Nano characteristics.
"""
    },
    {
        "name": "top_view",
        "filename": "adora-1-nano-top-view-2k.png",
        "description": "TOP VIEW - Technical Product Rendering",
        "prompt": f"""
{DESIGN_ENHANCEMENTS}

VIEW REQUIREMENTS:
- Top-down view of Adora 1 Nano robot
- Bird's eye perspective showing the overall design layout
- Robot head design from above with camera placement
- Arm placement and shoulder joint design
- Overall footprint and proportions

TECHNICAL SPECIFICATIONS:
- Transparent background (PNG)
- 2K resolution
- 4:3 aspect ratio
- Professional studio lighting from above
- Subtle shadows for dimension
- Clean, minimalist product presentation
- Technical drawing aesthetic
- Emphasis on design symmetry and layout

The top view should showcase the thoughtful robot design layout and premium construction quality while preserving Adora 1 Nano's form.
"""
    }
]

# Generation config for 2K quality
config = types.GenerateContentConfig(
    temperature=0.7,
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
        image_size="2K",  # 2K resolution
    ),
)

def generate_view(view_config):
    """Generate a single product view rendering."""
    print(f"\n{'='*60}")
    print(f"Generating: {view_config['description']}")
    print(f"Output: {view_config['filename']}")
    print(f"{'='*60}")

    # Load rachy mini reference image
    input_path = os.path.join(base_dir, "rachy minin.jpeg")

    if not os.path.exists(input_path):
        print(f"Error: rachy mini reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, view_config["filename"])

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/jpeg")

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
    print("Starting Adora 1 Nano Artistic Product Rendering (Using Rachy Mini Reference)...")
    print(f"Generating {len(VIEW_PROMPTS)} views at 2K resolution, 4:3 aspect ratio")
    print("All images will have transparent backgrounds for web/print use")
    print("Maintaining Adora 1 Nano robot characteristics with enhanced consumer electronics quality")

    generated_files = []

    for i, view in enumerate(VIEW_PROMPTS, 1):
        print(f"\n[{i}/{len(VIEW_PROMPTS)}] Processing {view['name']}...")
        result = generate_view(view)
        if result:
            generated_files.append(result)

    print("\n" + "="*60)
    print("Product Rendering Generation Complete!")
    print(f"Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"  ✓ {file}")
    print("\nAll images feature:")
    print("  • Adora 1 Nano robot structure maintained")
    print("  • Premium ABS plastic construction")
    print("  • Polished robot arm design with concealed wiring")
    print("  • Consumer electronics aesthetic (rachy mini inspired)")
    print("  • Robot head with integrated camera (NO HUMAN FEATURES)")
    print("  • Transparent backgrounds for flexibility")
    print("  • 2K resolution for web/print use")
    print("="*60)