#!/usr/bin/env python3
"""Generate Adora 1 Nano with fully opened arms showing welcome gesture."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use the nano 01 image as reference
REFERENCE_IMAGE = "adora 1  nano 01.jpg"

WELCOME_GESTURE_PROMPT = """
RENDERING REQUIREMENTS:
- Based on the Adora 1 Nano robot from the reference image
- FULLY OPENED ARMS showing a WELCOME GESTURE
- Arms should be wide open, welcoming, and inviting
- Maintain the same robot design and features from reference
- Professional, friendly, and approachable appearance
- Clean studio background for product showcase

WELCOME GESTURE SPECIFICS:
- Both arms extended wide open to the sides
- Palms facing forward or slightly upward (welcoming position)
- Open, inviting posture that conveys friendliness
- Arms should be fully extended but natural looking
- Should look like the robot is greeting someone warmly
- Professional yet friendly demeanor

MAINTAIN THESE FEATURES FROM REFERENCE:
- Same robot body structure and proportions
- Same color scheme and appearance
- Premium finish and quality
- Professional robot design aesthetic
- All enhanced features (ABS plastic, concealed wiring, etc.)

TECHNICAL SPECIFICATIONS:
- Clean studio background (white/light gray)
- 2K resolution
- 4:3 aspect ratio
- Professional product photography lighting
- Sharp focus on the robot and welcome gesture
- High-quality rendering suitable for marketing materials

The robot should appear friendly and welcoming while maintaining its professional appearance.
"""

# Generation config for welcome gesture
config = types.GenerateContentConfig(
    temperature=0.5,
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

def generate_welcome_gesture():
    """Generate Adora 1 Nano with welcome gesture."""
    print(f"\n{'='*60}")
    print("Generating: Adora 1 Nano - Welcome Gesture")
    print("Reference: adora 1 nano 01.jpg")
    print("Gesture: Fully opened arms in welcoming position")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-1-nano-welcome-gesture.png")

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/jpeg")

    # Combine reference image with welcome gesture prompt
    contents = [input_image, WELCOME_GESTURE_PROMPT]

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
        print(f"Error generating welcome gesture: {e}")
        return None

    return None

if __name__ == "__main__":
    print("Starting Adora 1 Nano Welcome Gesture Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference")
    print("Generating robot with fully opened arms showing welcome gesture")
    print("Maintaining all design features and premium quality")

    result = generate_welcome_gesture()

    print("\n" + "="*60)
    if result:
        print("Welcome Gesture Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Fully opened arms in welcome gesture")
        print("  • Friendly and inviting appearance")
        print("  • Based on adora 1 nano 01.jpg reference")
        print("  • Premium robot design maintained")
        print("  • Clean studio background")
        print("  • 2K resolution for professional use")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)