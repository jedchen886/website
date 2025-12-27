#!/usr/bin/env python3
"""Generate Adora 1 Nano with welcome gesture using camera-enhanced reference."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

# Use the camera-enhanced front view as reference
REFERENCE_IMAGE = "adora-1-nano-camera-front.png"

WELCOME_CAMERA_GESTURE_PROMPT = """
RENDERING REQUIREMENTS:
- Based on the Adora 1 Nano robot from the reference image (with enhanced camera enclosure)
- FULLY OPENED ARMS showing a WELCOME GESTURE
- Maintain ALL enhanced features from the reference:
  * Round-corner rectangle camera enclosure
  * Two camera holes positioned as eyes
  * YELLOW robot base/body
  * GRAY robot arms
  * Premium ABS plastic finish
  * Concealed wiring with sleek covers
  * Consumer electronics quality

WELCOME GESTURE SPECIFICS:
- Both arms extended wide open to the sides
- Palms facing forward or slightly upward (welcoming position)
- Open, inviting posture that conveys friendliness
- Arms should be fully extended but natural looking
- Should look like the robot is greeting someone warmly
- Professional yet friendly demeanor

ENHANCED FEATURES TO MAINTAIN:
- Camera enclosure with two eye holes clearly visible
- Yellow base/body with premium finish
- Gray arms with premium finish
- All consumer electronics quality enhancements
- Clean, professional appearance
- No visible mechanical components

TECHNICAL SPECIFICATIONS:
- Clean studio background (white/light gray)
- 2K resolution
- 4:3 aspect ratio
- Professional product photography lighting
- Sharp focus on the robot, camera enclosure, and welcome gesture
- High-quality rendering suitable for marketing materials

The robot should appear friendly and welcoming while maintaining all premium features and camera enclosure from reference.
"""

# Generation config for welcome gesture with camera features
config = types.GenerateContentConfig(
    temperature=0.3,  # Low temperature to maintain camera features accurately
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

def generate_welcome_camera_gesture():
    """Generate Adora 1 Nano with welcome gesture and camera enclosure."""
    print(f"\n{'='*60}")
    print("Generating: Adora 1 Nano - Welcome Gesture with Camera")
    print("Reference: adora-1-nano-camera-front.png")
    print("Gesture: Fully opened arms in welcoming position")
    print("Features: Enhanced camera enclosure + premium color scheme")
    print(f"{'='*60}")

    # Load the reference image
    input_path = os.path.join(base_dir, REFERENCE_IMAGE)

    if not os.path.exists(input_path):
        print(f"Error: Reference image not found at {input_path}")
        return None

    output_path = os.path.join(base_dir, "adora-1-nano-camera-welcome.png")

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Combine reference image with welcome camera gesture prompt
    contents = [input_image, WELCOME_CAMERA_GESTURE_PROMPT]

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
        print(f"Error generating welcome camera gesture: {e}")
        return None

    return None

if __name__ == "__main__":
    print("Starting Adora 1 Nano Welcome Gesture with Camera Generation...")
    print(f"Using {REFERENCE_IMAGE} as reference")
    print("Generating robot with:")
    print("  • Fully opened arms in welcome gesture")
    print("  • Enhanced camera enclosure with two eye holes")
    print("  • Yellow base and gray arms color scheme")
    print("  • All premium features maintained")

    result = generate_welcome_camera_gesture()

    print("\n" + "="*60)
    if result:
        print("Welcome Gesture with Camera Generation Complete!")
        print(f"Generated: {result}")
        print("\nFeatures:")
        print("  • Fully opened arms in welcome gesture")
        print("  • Round-corner rectangle camera enclosure")
        print("  • Two camera holes positioned as eyes")
        print("  • YELLOW robot base/body (premium ABS plastic)")
        print("  • GRAY robot arms (premium ABS plastic)")
        print("  • Premium ABS plastic finish")
        print("  • Concealed wiring with sleek covers")
        print("  • Consumer electronics quality")
        print("  • Clean studio background")
        print("  • 2K resolution for professional use")
    else:
        print("Generation failed - please check reference image and try again")
    print("="*60)