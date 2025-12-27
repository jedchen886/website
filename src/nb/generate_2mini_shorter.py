#!/usr/bin/env python3
"""Generate Adora 2 Mini appearing shorter in education scene."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use Adora 2 Mini as reference
REFERENCE_IMAGE = "adora-2-mini-white.png"

INDOOR_EDUCATION_PROMPT = """
Generate a photorealistic image featuring the Adora 2 Mini robot in an education setting with beautiful indoor lighting.

CRITICAL REQUIREMENTS:
- DO NOT CHANGE the Adora 2 Mini robot design, colors, or appearance
- DO NOT CHANGE the robot arms - keep arms EXACTLY as shown in reference image
- Use the EXACT robot as shown in the reference image
- ROBOT HANDS MUST BE COMPLETELY EMPTY - DO NOT PLACE ANY OBJECTS IN THE ROBOT'S HANDS
- NO books, NO pointer, NO tools, NO items whatsoever in robot hands
- Robot arms should remain in their natural position as in reference

HEIGHT SCALE - CRITICAL:
- Make the Adora 2 Mini robot appear SHORTER and more COMPACT
- The robot should appear small and cute compared to the educational environment
- Show robot as significantly shorter than standard furniture:
  * Robot should appear notably shorter than desk height
  * Robot should look small compared to chairs and other furniture
  * Emphasize the compact, small, cute appearance
- The robot should appear petite and compact in the scene
- Use furniture and environmental elements to emphasize the small, short stature

SCENE DESCRIPTION:
- Setting: Modern indoor educational space (classroom, library, learning center)
- Environment: Warm, inviting educational atmosphere with furniture that makes robot look small
- Include desks, chairs, bookshelves that emphasize the robot's compact size
- Indoor lighting: Soft, natural indoor lighting from windows or warm artificial lighting

POSITIONING:
- Position the robot clearly in the educational environment
- Show the robot alongside furniture to emphasize its small, short appearance
- Robot should be positioned lower in the frame
- Composition should emphasize how small and compact the robot is

LIGHTING & ATMOSPHERE:
- Beautiful indoor lighting with warm tones
- Soft natural light streaming through windows OR warm artificial lighting
- Gentle shadows creating depth and dimension
- Bright, cheerful, and inviting atmosphere
- Professional photography style with excellent lighting
- Lighting that emphasizes the robot's cute, compact appearance

EDUCATIONAL ELEMENTS:
- Desks, chairs, bookshelves that make robot appear small
- Educational displays or chalkboard/whiteboard
- Modern classroom or library setting
- Technology-enhanced learning environment
- Warm, welcoming educational space

TECHNICAL REQUIREMENTS:
- Photorealistic rendering quality
- High detail and sharp focus on the robot
- Realistic depth of field
- Professional product photography composition
- Warm, inviting color palette
- Clean, sophisticated aesthetic
- NO HUMANS in the image

MOST IMPORTANT: The robot must appear SHORTER and more COMPACT. Make it look small and cute relative to the furniture and environment. Robot positioned lower in frame. Arms unchanged from reference. Empty hands.

The image should showcase Adora 2 Mini as a short, compact, cute robot within a beautifully lit indoor learning environment.
"""

# Generation config for indoor education scene with shorter robot
config = types.GenerateContentConfig(
    temperature=0.4,
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
    """Generate Adora 2 Mini appearing shorter in indoor education scene."""
    print(f"\n{'='*60}")
    print("Generating: Adora 2 Mini - Indoor Education (SHORTER)")
    print(f"Reference: {REFERENCE_IMAGE}")
    print("Requirements:")
    print("  → Make robot appear SHORTER and more COMPACT")
    print("  → Emphasize small, cute appearance relative to furniture")
    print("  → Robot arms UNCHANGED - exactly as in reference")
    print("  → Robot hands MUST BE COMPLETELY EMPTY")
    print("  → Position robot lower in frame")
    print("Scene: Indoor educational setting with beautiful lighting")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-2-mini-education-shorter.png")

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
    print("CRITICAL REQUIREMENTS:")
    print("  → Make robot appear SHORTER and more COMPACT")
    print("  → Emphasize small, cute size with furniture reference")
    print("  → Robot arms UNCHANGED from reference")
    print("  → Robot hands MUST BE COMPLETELY EMPTY")
    print("  → Position robot lower in frame")
    print("Generating with beautiful indoor lighting")
    print("Aspect ratio: 16:9, Resolution: 2K")

    result = generate_indoor_education()

    print("\n" + "="*60)
    if result:
        print("Indoor Education Scene Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Adora 2 Mini appearing SHORTER and more COMPACT")
        print("  • Small, cute appearance emphasized")
        print("  • Robot arms UNCHANGED - exactly as in reference")
        print("  • Positioned lower in frame")
        print("  • EMPTY HANDS - NOT holding anything")
        print("  • Beautiful indoor lighting")
        print("  • 16:9 aspect ratio, 2K resolution")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)