#!/usr/bin/env python3
"""Generate Adora 2 Mini in indoor lighting education scene with EMPTY HANDS."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use Adora 2 Mini as reference
REFERENCE_IMAGE = "adora-2-mini-white.png"

INDOOR_EDUCATION_PROMPT = """
Generate a photorealistic image featuring the EXACT Adora 2 Mini robot from the reference image in an education setting with beautiful indoor lighting.

CRITICAL REQUIREMENTS:
- DO NOT CHANGE the Adora 2 Mini robot design, colors, or appearance
- Use the EXACT robot as shown in the reference image
- ROBOT HANDS MUST BE COMPLETELY EMPTY - DO NOT PLACE ANY OBJECTS IN THE ROBOT'S HANDS
- NO books, NO pointer, NO tools, NO items whatsoever in robot hands
- Robot hands should be visible and empty, open or natural position
- Maintain the robot's original proportions and features
- Do NOT modify the robot's body, head, arms, or any part

SCENE DESCRIPTION:
- Setting: Modern indoor educational space (classroom, library, learning center)
- Environment: Warm, inviting educational atmosphere with books, desks, learning materials in background ONLY
- Indoor lighting: Soft, natural indoor lighting from windows or warm artificial lighting

ROBOT PLACEMENT:
- Adora 2 Mini robot positioned naturally in the educational space
- Robot hands MUST BE EMPTY - not holding any objects
- Natural standing or welcoming pose with empty, open hands
- Professional appearance

LIGHTING & ATMOSPHERE:
- Beautiful indoor lighting with warm tones
- Soft natural light streaming through windows OR warm artificial lighting
- Gentle shadows creating depth and dimension
- Bright, cheerful, and inviting atmosphere
- Professional photography style with excellent lighting

EDUCATIONAL ELEMENTS (BACKGROUND ONLY):
- Books, desks, or learning materials visible in background
- Educational displays or chalkboard/whiteboard in background
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
- NO HUMANS in the image

MOST IMPORTANT: The robot's hands must be completely EMPTY - NOT holding anything at all. Any educational items should be in the background, NOT in the robot's hands.

The image should showcase the EXACT Adora 2 Mini robot (unchanged) with EMPTY HANDS in a warm, beautifully lit indoor learning environment.
"""

# Generation config for indoor education scene
config = types.GenerateContentConfig(
    temperature=0.4,  # Lower temperature to maintain robot appearance
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
    """Generate Adora 2 Mini in indoor education scene with empty hands."""
    print(f"\n{'='*60}")
    print("Generating: Adora 2 Mini - Indoor Education (EMPTY HANDS)")
    print(f"Reference: {REFERENCE_IMAGE}")
    print("CRITICAL: Robot hands MUST BE EMPTY - NOT HOLDING ANYTHING")
    print("Scene: Indoor educational setting with beautiful lighting")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-2-mini-education-empty-hands.png")

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
    print("CRITICAL REQUIREMENT:")
    print("  → Robot hands MUST BE COMPLETELY EMPTY")
    print("  → NOT holding ANY objects (no books, no tools, nothing)")
    print("  → Educational items in BACKGROUND only")
    print("Generating with beautiful indoor lighting")
    print("Aspect ratio: 16:9, Resolution: 2K")

    result = generate_indoor_education()

    print("\n" + "="*60)
    if result:
        print("Indoor Education Scene Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Adora 2 Mini EXACT as in reference (unchanged)")
        print("  • EMPTY HANDS - NOT holding anything")
        print("  • Educational items in background only")
        print("  • Beautiful indoor lighting")
        print("  • Warm, inviting atmosphere")
        print("  • 16:9 aspect ratio, 2K resolution")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)