import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))

# Load the robot image
robot_image = types.Part.from_bytes(
    data=open("/Users/yuechen/home/website/src/nb/adora-2-max-white.png", "rb").read(),
    mime_type="image/png",
)

# Detailed prompt for the scene
prompt = """
Generate a photorealistic image based on the robot in the provided reference image.

Scene Description:
- Setting: A modern, spacious IKEA-style apartment living room
- Floor: Polished granite flooring with subtle natural veining
- Furniture:
  - Contemporary minimalist couches (light gray or beige fabric)
  - A sleek wooden coffee table with clean lines
  - A large flat-screen TV mounted on the wall
- Decor: Simple, Scandinavian-inspired decor with clean aesthetics

Robot Placement and Pose:
- Position the robot at the 3/4 left side of the frame (rule of thirds)
- The robot should be making a welcoming gesture with both arms raised upward and forward
- The robot should appear friendly and inviting

Lighting and Atmosphere:
- Warm, cozy ambient lighting
- Soft natural light coming from large windows (off-frame)
- Golden hour warmth with gentle shadows
- The overall mood should feel welcoming and comfortable

Technical Requirements:
- Photorealistic rendering quality
- High detail and sharp focus on the robot
- Realistic depth of field with slight background blur
- Professional interior photography style

The robot should be the main subject while the living room provides context for a smart home environment.
"""

# Configure generation settings
config = types.GenerateContentConfig(
    temperature=1,
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

# Generate the image
print("Generating image... This may take a moment.")

contents = [robot_image, prompt]

for chunk in client.models.generate_content_stream(
    model="gemini-3-pro-image-preview",
    contents=contents,
    config=config,
):
    if chunk.candidates and chunk.candidates[0].content and chunk.candidates[0].content.parts:
        for part in chunk.candidates[0].content.parts:
            if part.text:
                print(f"Model response: {part.text}")
            elif part.inline_data:
                # Save the generated image
                output_path = "/Users/yuechen/home/website/src/nb/adora-2-max-living-room.png"
                with open(output_path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"Image saved to: {output_path}")

print("Generation complete!")
