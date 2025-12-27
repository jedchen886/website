#!/usr/bin/env python3
"""Generate Adora 2 Mini positioned further down in indoor lighting education scene."""

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
- Robot hands should be visible and empty

POSITIONING:
- Adora 2 Mini should be positioned FURTHER DOWN in the frame
- Place the robot in the LOWER portion of the image
- Show more of the upper part of the educational environment (ceiling, upper walls, lights)
- Robot should be clearly visible but positioned lower in the composition
- This creates space above the robot for potential text overlay or to show the room's height

SCENE DESCRIPTION:
- Setting: Modern indoor educational space (classroom, library, learning center)
- Environment: Warm, inviting educational atmosphere with books, desks, learning materials
- Show more of the upper environment - ceiling, upper walls, light fixtures
- Indoor lighting: Soft, natural indoor lighting from windows or warm artificial lighting

LIGHTING & ATMOSPHERE:
- Beautiful indoor lighting with warm tones
- Soft natural light streaming through windows OR warm artificial lighting
- Gentle shadows creating depth and dimension
- Bright, cheerful, and inviting atmosphere
- Professional photography style with excellent lighting

EDUCATIONAL ELEMENTS:
- Books, desks, or learning materials visible
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

MOST IMPORTANT: Position the robot FURTHER DOWN in the frame - lower portion of image. Keep everything else unchanged. Robot arms EXACTLY as in reference. Robot hands must be completely EMPTY.

The image should showcase the Adora 2 Mini robot positioned lower in the frame within a beautifully lit indoor learning environment, with more visible space above.
"""

# Generation config for indoor education scene
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
    """Generate Adora 2 Mini positioned lower in indoor education scene."""
    print(f"\n{'='*60}")
    print("Generating: Adora 2 Mini - Indoor Education (POSITIONED LOWER)")
    print(f"Reference: {REFERENCE_IMAGE}")
    print("Requirements:")
    print("  → Position robot FURTHER DOWN in the frame (lower portion)")
    print("  → Keep everything else UNCHANGED")
    print("  → Robot arms UNCHANGED - exactly as in reference")
    print("  → Robot hands MUST BE COMPLETELY EMPTY")
    print("Scene: Indoor educational setting with beautiful lighting")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-2-mini-education-lower.png")

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
    print("  → Position robot FURTHER DOWN in the frame")
    print("  → Keep everything else UNCHANGED")
    print("  → Robot arms UNCHANGED from reference")
    print("  → Robot hands MUST BE COMPLETELY EMPTY")
    print("Generating with beautiful indoor lighting")
    print("Aspect ratio: 16:9, Resolution: 2K")

    result = generate_indoor_education()

    print("\n" + "="*60)
    if result:
        print("Indoor Education Scene Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Adora 2 Mini as in reference (unchanged)")
        print("  • Robot positioned FURTHER DOWN in frame")
        print("  • Robot arms UNCHANGED - exactly as in reference")
        print("  • More upper space visible in environment")
        print("  • EMPTY HANDS - NOT holding anything")
        print("  • Beautiful indoor lighting")
        print("  • 16:9 aspect ratio, 2K resolution")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)