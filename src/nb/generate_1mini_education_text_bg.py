#!/usr/bin/env python3
"""Generate Adora 1 Mini in education scene with dark upper background for text overlay."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use Adora 1 Mini as reference
REFERENCE_IMAGE = "adora-1-mini-white.png"

EDUCATION_SCENE_PROMPT = """
Generate a photorealistic image of Adora 1 Mini robot in an education setting with DAYTIME lighting and DARK UPPER BACKGROUND for text overlay.

SCENE DESCRIPTION:
- Setting: Bright educational environment (classroom, library, or learning space)
- UPPER BACKGROUND: Dark colored area at the top of the image (perfect for light text display)
- LOWER PORTION: Bright, well-lit educational scene with daytime lighting
- Environment: Educational elements visible (books, learning materials, desks, or educational displays)

ROBOT PLACEMENT:
- Adora 1 Mini robot positioned in the lower/middle portion of the frame
- Robot should be in bright, daytime lighting
- Educational assistant/teaching companion role
- Welcoming and helpful pose

BACKGROUND COLOR SCHEME:
- TOP 1/3 to 1/2 of image: Dark solid color (dark blue, dark gray, or black)
- BOTTOM portion: Bright, well-lit educational environment
- Clean transition between dark upper area and bright lower area
- The dark upper area should be suitable for displaying light-colored text/headlines

LIGHTING & ATMOSPHERE:
- Overall: Bright daytime lighting in the robot area
- Upper background: Dark colored area for text contrast
- Professional photography style
- Modern, high-tech educational environment
- Clean, bright illumination on the robot and educational elements

TECHNICAL REQUIREMENTS:
- Photorealistic rendering quality
- High detail and sharp focus on the robot
- Robot and scene should be bright and clearly visible
- Dark upper background should be clean and uniform (suitable for text overlay)
- 16:9 aspect ratio for presentations/web banners
- Professional composition with space for text at top

PURPOSE:
The image is designed for marketing materials where light-colored text/headlines will be overlaid on the dark upper background area, while the robot and educational scene remain bright and visible below.

The image should have a professional header/banner appearance with dark text area at top and bright, engaging educational scene below.
"""

# Generation config for education scene with text background
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
        aspect_ratio="16:9",
        image_size="2K",
    ),
)

def generate_education_text_bg():
    """Generate Adora 1 Mini in education scene with dark upper background for text."""
    print(f"\n{'='*60}")
    print("Generating: Adora 1 Mini - Education with Dark Text Background")
    print(f"Reference: {REFERENCE_IMAGE}")
    print("Scene: Daytime education with dark upper background for text overlay")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-1-mini-education-text-bg.png")

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Combine reference image with education scene prompt
    contents = [input_image, EDUCATION_SCENE_PROMPT]

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
        print(f"Error generating education text background scene: {e}")
        return None

    return None

if __name__ == "__main__":
    print("Starting Adora 1 Mini Education Scene with Text Background Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference")
    print("Generating:")
    print("  • Daytime lighting for robot and scene")
    print("  • Dark upper background for light text overlay")
    print("  • Bright, clear visibility of robot")
    print("  • 16:9 aspect ratio for banners/presentations")
    print("  • 2K resolution")

    result = generate_education_text_bg()

    print("\n" + "="*60)
    if result:
        print("Education Text Background Scene Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Adora 1 Mini in bright educational environment")
        print("  • Dark upper background for light text overlay")
        print("  • Daytime lighting on robot and scene")
        print("  • Clean, professional banner-style composition")
        print("  • 16:9 aspect ratio perfect for marketing materials")
        print("  • 2K resolution")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)