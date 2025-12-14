#!/usr/bin/env python3
"""Regenerate Adora 1 Pro farming scene with taller trees and smaller robot."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))

# Base directory
base_dir = "/Users/yuechen/home/website/src/nb"

prompt = """
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

CRITICAL SIZE REQUIREMENTS:
- The apple trees must be TALL - at least twice the height of the robot
- The robot should appear SMALL compared to the trees - only about HALF the height of the apple trees
- Show the full height of the trees to emphasize their scale

Scene Description:
- Setting: A real working orchard / apple farm
- Environment: More natural and rough agricultural setting, not overly pristine
- Trees: TALL, mature apple trees with thick trunks and full canopy, loaded with ripe red apples
- Ground: Natural grass, some dirt patches, fallen leaves - realistic farm ground, not manicured
- Background: Rows of tall apple trees extending into the distance, natural blue sky

Robot Placement:
- Position the robot on the left side of the frame
- The robot should be SMALL in the frame - emphasize the scale difference with the tall trees
- Robot is reaching UP toward apples on the lower branches of the tall tree
- Show the robot from a slight distance to emphasize its compact size relative to environment

Atmosphere:
- Golden hour warm sunlight filtering through tree canopy
- Natural outdoor agricultural environment
- Slightly rough, authentic farm feeling - not too polished
- Realistic working orchard aesthetic

Style Requirements:
- Clean product photography style but with natural environment
- NO HUMANS in the image - only the robot
- Sharp focus on the robot
- Natural depth of field
- Warm color palette
- The robot should be clearly visible but appear appropriately sized for agricultural work
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
        aspect_ratio="4:3",
        image_size="2K",
    ),
)

print("Generating Adora 1 Pro farming scene v2...")
print("- Taller apple trees")
print("- Smaller robot (half tree height)")
print("- More rough/natural environment")

# Load input image
input_path = os.path.join(base_dir, "adora-1-pro-black.png")
output_path = os.path.join(base_dir, "adora-1-pro-farming-clean.png")

with open(input_path, "rb") as f:
    image_data = f.read()

input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

# Generate
contents = [input_image, prompt]

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

print("Generation complete!")
