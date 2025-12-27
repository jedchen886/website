#!/usr/bin/env python3
"""Generate Adora 2 Mini in indoor lighting education scene."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use Adora 2 Mini as reference
REFERENCE_IMAGE = "adora-2-mini-white.png"

INDOOR_EDUCATION_PROMPT = """
Generate a photorealistic image of Adora 2 Mini robot in an education setting with beautiful indoor lighting.

SCENE DESCRIPTION:
- Setting: Modern indoor educational space (classroom, library, learning center, or school hallway)
- Environment: Warm, inviting educational atmosphere with books, desks, learning materials, or educational displays
- Indoor lighting: Soft, natural indoor lighting from windows or warm artificial lighting

ROBOT PLACEMENT & ROLE:
- Adora 2 Mini robot as an educational assistant/teaching companion
- Robot positioned naturally in the educational space
- Welcoming, helpful pose suitable for interacting with students
- Professional yet approachable appearance

LIGHTING & ATMOSPHERE:
- Beautiful indoor lighting with warm tones
- Soft natural light streaming through windows OR warm artificial lighting
- Gentle shadows creating depth and dimension
- Bright, cheerful, and inviting atmosphere
- Professional photography style with excellent lighting
- Clean, modern educational environment

EDUCATIONAL ELEMENTS:
- Books, desks, or learning materials visible
- Educational displays or chalkboard/whiteboard
- Modern classroom or library setting
- Technology-enhanced learning environment
- Warm, welcoming educational space

TECHNICAL REQUIREMENTS:
- Photorealistic rendering quality
- High detail and sharp focus on the robot
- Realistic depth of field with subtle background blur
- Professional product photography composition
- Warm, inviting color palette
- Clean, sophisticated aesthetic
- NO HUMANS required (can be empty scene or with students if it fits naturally)

The image should showcase Adora 2 Mini as a premium educational robot in a warm, beautifully lit indoor learning environment.
"""

# Generation config for indoor education scene
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

def generate_indoor_education():
    """Generate Adora 2 Mini in indoor education scene."""
    print(f"\n{'='*60}")
    print("Generating: Adora 2 Mini - Indoor Education Scene")
    print(f"Reference: {REFERENCE_IMAGE}")
    print("Scene: Indoor educational setting with beautiful lighting")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-2-mini-education-indoor.png")

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Combine reference image with indoor education prompt
    contents = [input_image, INDOOR_EDUCATION_PROMPT]

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
        print(f"Error generating indoor education scene: {e}")
        return None

    return None

if __name__ == "__main__":
    print("Starting Adora 2 Mini Indoor Education Scene Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference")
    print("Generating beautiful indoor lighting educational setting")
    print("Aspect ratio: 16:9")
    print("Resolution: 2K")

    result = generate_indoor_education()

    print("\n" + "="*60)
    if result:
        print("Indoor Education Scene Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Adora 2 Mini in indoor educational environment")
        print("  • Beautiful indoor lighting (natural or warm artificial)")
        print("  • Warm, inviting atmosphere")
        print("  • Modern classroom or library setting")
        print("  • Professional photography quality")
        print("  • 16:9 aspect ratio")
        print("  • 2K resolution")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)