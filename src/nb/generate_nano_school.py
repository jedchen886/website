#!/usr/bin/env python3
"""Generate Adora 1 Nano middle school lab scene."""

import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

prompt = """
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

CRITICAL: NO TEXT, NO WORDS, NO LETTERS anywhere in the image. NO HUMANS.

Scene Description:
- Setting: A modern middle school robotics lab / STEM classroom
- Environment: Bright, colorful educational space with clean modern design
- Features: Lab benches/tables, robotics equipment, electronic components, educational tools
- Floor: Clean flooring (light wood or white tiles)
- Background: Interactive whiteboards, shelving with robotics kits, colorful educational elements

Robot Placement:
- Position the small robot in the center-left of the frame on a lab table/workbench
- The robot should appear as a learning tool / educational robot
- Robot is the cute, small centerpiece - like a student project or teaching aid

Atmosphere:
- Bright, cheerful educational environment
- Warm natural lighting from windows
- Modern STEM lab aesthetic
- Inspiring and engaging for young learners

Style Requirements:
- Clean, minimalist product showcase aesthetic
- NO HUMANS in the image - only the robot
- NO TEXT, NO SIGNS, NO WORDS anywhere
- Bright, well-lit educational environment
- Professional product photography style
- Sharp focus on the robot as the hero subject
- Warm color palette with soft yellows, blues, whites
- Premium educational/STEM aesthetic
"""

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

print("Generating Adora 1 Nano middle school lab scene...")

input_path = os.path.join(base_dir, "adora-1-nano-feature1.png")
output_path = os.path.join(base_dir, "adora-1-nano-school-clean.png")

with open(input_path, "rb") as f:
    image_data = f.read()

input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")
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
