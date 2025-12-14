#!/usr/bin/env python3
"""Generate Pixar-style robot family lineup image."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))

# Base directory
base_dir = "/Users/yuechen/home/website/src/nb"

# Load all 6 robot images
robot_files = [
    "adora-2-mini-white.png",
    "adora-2-pro-white.png",
    "adora-2-max-white.png",
    "adora-1-mini-white.png",
    "adora-1-nano-feature1.png",
    "adora-1-pro-black.png",
]

print("Loading robot images...")
robot_images = []
for filename in robot_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "rb") as f:
        image_data = f.read()
    robot_images.append(types.Part.from_bytes(data=image_data, mime_type="image/png"))
    print(f"  ✓ Loaded: {filename}")

prompt = """
Generate a Pixar/Disney animation film style promotional image featuring ALL 6 robots.

REFERENCE IMAGE MAPPING (CRITICAL - USE EXACT DESIGNS):
- 1st reference image provided → Adora 2 Mini (position 1, leftmost)
- 2nd reference image provided → Adora 2 Pro (position 2)
- 3rd reference image provided → Adora 2 Max (position 3, center-left)
- 4th reference image provided → Adora 1 Mini (position 4, center-right)
- 5th reference image provided → Adora 1 Nano (position 5)
- 6th reference image provided → Adora 1 Pro (position 6, rightmost)

Each robot MUST match the EXACT design, shape, and appearance from its corresponding reference image. Do not change the robot designs - only render them in Pixar animation style.

SCENE SETUP:
- Style: Pixar/Disney 3D animation film aesthetic - warm, charming, appealing
- Background: Beautiful gradient from green (left) to light blue (center) to bright green (right)
- Setting: A theatrical stage or showcase platform
- Lighting: Individual spotlights illuminating each robot from above, creating warm glows

SIZE SPECIFICATIONS (LEFT TO RIGHT):
1. Adora 2 Mini (from 1st ref image) - small humanoid robot (reference height: 1x)
2. Adora 2 Pro (from 2nd ref image) - medium humanoid robot (height: 1.2x)
3. Adora 2 Max (from 3rd ref image) - tallest robot with large screen display (height: 1.5x, the tallest)
4. Adora 1 Mini (from 4th ref image) - small humanoid robot (height: 1x)
5. Adora 1 Nano (from 5th ref image) - TINY robot, HALF the height of Adora 2 Mini (height: 0.5x, the smallest)
6. Adora 1 Pro (from 6th ref image) - black/dark colored industrial arm robot (height: 1x)

CRITICAL SIZE REQUIREMENTS:
- Adora 1 Nano (5th robot) must be exactly HALF the height of Adora 2 Mini
- Adora 1 Nano is the SMALLEST robot - like a tiny baby robot
- Adora 2 Max is the TALLEST robot in the lineup
- Size order from smallest to tallest: Nano < Mini/Pro < Max

ROBOT POSES:
- All robots should have a SHY, endearing gesture
- Slightly hunched shoulders, arms close to body
- Heads tilted slightly down or to the side
- Cute, bashful, timid expressions
- Like characters being introduced on stage for the first time

ATMOSPHERE:
- Warm, inviting Pixar movie poster feel
- Soft shadows and ambient occlusion
- Subsurface scattering on robot surfaces
- Dreamy, magical quality
- Each robot has their own spotlight creating a soft glow around them

TECHNICAL:
- All 6 robots must be clearly visible and recognizable
- Each robot must faithfully represent its reference image design
- Arranged in a single horizontal row
- Evenly spaced across the frame
- Clean composition suitable for promotional material
- High quality 3D animated film rendering style
"""

# Generation config
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

print("\nGenerating Pixar-style robot family image...")
print("- 6 robots in a row")
print("- Green to light blue gradient background")
print("- Spotlights on each robot")
print("- Shy, endearing poses")
print("- 16:9 aspect ratio, 2K resolution")

# Combine all images with the prompt
contents = robot_images + [prompt]

output_path = os.path.join(base_dir, "robot-family-pixar.png")

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

print("\nGeneration complete!")
