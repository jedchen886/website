#!/usr/bin/env python3
"""Generate Adora 1 Mini house cleaning scene."""

import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

prompt = """
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

CRITICAL: NO TEXT, NO WORDS, NO LETTERS anywhere in the image. NO HUMANS.

Scene Description:
- Setting: A futuristic smart home living space of tomorrow
- Environment: Ultra-modern, minimalist interior with curved architectural elements
- Features: Sleek futuristic furniture, smooth white surfaces, soft ambient lighting accents
- Floor: Pristine white or light gray polished flooring with subtle reflections
- Background: Futuristic open-plan living area with soft blue/warm ambient light strips

Robot Placement:
- Position the robot in the center-left of the frame
- The robot appears to be helping with household tasks
- One arm in a helpful, welcoming gesture
- Robot looks like an advanced home assistant

Atmosphere:
- Bright, airy, and immaculately clean
- Soft diffused lighting with warm accents
- Futuristic but warm and inviting
- Premium smart home environment aesthetic

Style Requirements:
- Clean, minimalist product showcase aesthetic
- NO HUMANS in the image - only the robot
- NO TEXT, NO SIGNS, NO WORDS anywhere
- Futuristic, high-tech home environment
- Warm, soft lighting with gentle highlights
- Professional product photography style
- Sharp focus on the robot as the hero subject
- Subtle depth of field, clean background
- Premium, polished look suitable for marketing materials
- Consistent with futuristic aesthetic (like hospital/lab scenes)
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

print("Generating Adora 1 Mini house cleaning scene...")

input_path = os.path.join(base_dir, "adora-1-mini-white.png")
output_path = os.path.join(base_dir, "adora-1-mini-home-clean.png")

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
