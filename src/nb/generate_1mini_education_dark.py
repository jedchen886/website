#!/usr/bin/env python3
"""Generate Adora 1 Mini in education scene with dark background."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use Adora 1 Mini as reference
REFERENCE_IMAGE = "adora-1-mini-white.png"

EDUCATION_SCENE_PROMPT = """
Generate a photorealistic image of Adora 1 Mini robot in an education setting with DARK background.

SCENE DESCRIPTION:
- Setting: Educational environment (classroom, library, or learning space)
- Background: DARK atmospheric background with dramatic lighting
- Environment: Educational elements visible (books, learning materials, desks, or educational displays)
- Mood: Sophisticated, modern, and high-tech educational atmosphere

ROBOT PLACEMENT & ROLE:
- Adora 1 Mini robot as an educational assistant/teaching companion
- Robot positioned prominently in the scene
- Welcoming and helpful pose suitable for educational context
- Professional yet approachable appearance

LIGHTING & ATMOSPHERE:
- Dark, moody background with dramatic lighting effects
- Spotlight or focused lighting on the robot
- Contrast between dark background and illuminated robot
- Professional photography style with cinematic lighting
- Modern, high-tech educational environment
- Warm accent lighting to create depth

TECHNICAL REQUIREMENTS:
- Photorealistic rendering quality
- High detail and sharp focus on the robot
- Realistic depth of field
- Professional photography composition
- Dark background enhances the premium robot appearance
- NO HUMANS required (can be empty scene or with students if it fits naturally)
- Clean, sophisticated aesthetic

EDUCATIONAL ELEMENTS (optional):
- Books or educational materials visible
- Modern classroom or learning space elements
- Technology-enhanced learning environment
- Subtle educational displays or screens

The image should showcase Adora 1 Mini as a premium educational robot in a sophisticated, high-tech learning environment with dramatic dark background lighting.
"""

# Generation config for education scene
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

def generate_education_scene():
    """Generate Adora 1 Mini in education scene with dark background."""
    print(f"\n{'='*60}")
    print("Generating: Adora 1 Mini - Education Scene with Dark Background")
    print(f"Reference: {REFERENCE_IMAGE}")
    print("Scene: Educational setting with dramatic dark lighting")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-1-mini-education-dark.png")

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
        print(f"Error generating education scene: {e}")
        return None

    return None

if __name__ == "__main__":
    print("Starting Adora 1 Mini Education Scene Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference")
    print("Generating educational setting with dark, dramatic background")
    print("Aspect ratio: 16:9 (cinematic)")
    print("Resolution: 2K")

    result = generate_education_scene()

    print("\n" + "="*60)
    if result:
        print("Education Scene Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Adora 1 Mini in educational environment")
        print("  • Dark, dramatic background with spotlight lighting")
        print("  • Sophisticated, high-tech learning atmosphere")
        print("  • Professional cinematic photography style")
        print("  • 16:9 aspect ratio for presentations/web")
        print("  • 2K resolution")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)