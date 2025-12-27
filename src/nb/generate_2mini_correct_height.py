#!/usr/bin/env python3
"""Generate Adora 2 Mini with correct 1.2 meter height scale in education scene."""

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
- Adora 2 Mini robot is 1.2 METERS HIGH (approximately 4 feet / 47 inches tall)
- Show the robot at CORRECT SCALE relative to the educational environment
- The robot should appear COMPACT and SMALL compared to standard furniture:
  * Standard desk height is ~75cm, so robot should be visibly taller than desk but smaller than adult
  * Standard door is ~2 meters, robot should reach only about 60% of door height
  * Standard classroom chair seat is ~45cm, robot should be visibly taller than chair
- The robot's compact 1.2m height should be clearly evident in the scene
- Use furniture and environmental elements to establish the correct scale

SCENE DESCRIPTION:
- Setting: Modern indoor educational space (classroom, library, learning center)
- Environment: Warm, inviting educational atmosphere with properly scaled furniture
- Include desks, chairs, bookshelves, or other educational furniture for scale reference
- Indoor lighting: Soft, natural indoor lighting from windows or warm artificial lighting

POSITIONING:
- Position the robot clearly in the educational environment
- Show the robot alongside furniture to demonstrate the 1.2m height scale
- Robot should be positioned lower in the frame
- Create balanced composition showing robot and environment

LIGHTING & ATMOSPHERE:
- Beautiful indoor lighting with warm tones
- Soft natural light streaming through windows OR warm artificial lighting
- Gentle shadows creating depth and dimension
- Bright, cheerful, and inviting atmosphere
- Professional photography style with excellent lighting

EDUCATIONAL ELEMENTS:
- Properly scaled desks, chairs, bookshelves for reference
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

MOST IMPORTANT: The robot must appear at the correct scale of 1.2 meters high. Use furniture and environmental elements to clearly show this compact height. Robot positioned lower in frame. Arms unchanged from reference. Empty hands.

The image should showcase Adora 2 Mini at its correct 1.2 meter height scale within a beautifully lit indoor learning environment.
"""

# Generation config for indoor education scene with correct scale
config = types.GenerateContentConfig(
    temperature=0.3,  # Very low temperature for accurate scale
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
    """Generate Adora 2 Mini at correct 1.2m height scale in indoor education scene."""
    print(f"\n{'='*60}")
    print("Generating: Adora 2 Mini - Indoor Education (CORRECT 1.2m SCALE)")
    print(f"Reference: {REFERENCE_IMAGE}")
    print("Requirements:")
    print("  → Robot height: 1.2 METERS (4 feet / 47 inches)")
    print("  → Show CORRECT SCALE relative to furniture/environment")
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

    output_path = os.path.join(base_dir, "adora-2-mini-education-correct-height.png")

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
    print("  → Robot height: 1.2 METERS (compact size)")
    print("  → Show CORRECT SCALE with furniture reference")
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
        print("  • Adora 2 Mini at CORRECT 1.2 meter height")
        print("  • Proper scale shown with furniture reference")
        print("  • Robot arms UNCHANGED - exactly as in reference")
        print("  • Positioned lower in frame")
        print("  • EMPTY HANDS - NOT holding anything")
        print("  • Beautiful indoor lighting")
        print("  • 16:9 aspect ratio, 2K resolution")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)