#!/usr/bin/env python3
"""Regenerate Adora 2 Max hospital scene without text."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))

base_dir = "/Users/yuechen/home/website/src/nb"

prompt = """
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

CRITICAL: NO TEXT, NO WORDS, NO LETTERS, NO SIGNS WITH WRITING in the image. The scene must be completely free of any text or written characters.

Scene Description:
- Setting: A futuristic hospital lobby of tomorrow
- Environment: Ultra-clean, minimalist medical facility with smooth white surfaces
- Features: Curved architectural elements, soft blue ambient lighting accents, NO TEXT SIGNS - only abstract light patterns and shapes
- Floor: Pristine white polished floor with subtle reflections
- Background: Blurred futuristic corridor with soft lighting, NO WAYFINDING SIGNS OR TEXT

Robot Placement:
- Position the robot at the left-center of the frame (rule of thirds)
- The robot should have one arm in a gentle guiding gesture
- Robot appears ready to assist, welcoming pose

Atmosphere:
- Bright, airy, and immaculately clean
- Soft diffused lighting from above
- Futuristic but warm and inviting
- Premium healthcare environment aesthetic

Style Requirements:
- Clean, minimalist product showcase aesthetic
- NO HUMANS in the image - only the robot
- NO TEXT, NO SIGNS, NO WORDS anywhere in the image
- Futuristic, high-tech environment
- Warm, soft lighting with gentle highlights
- Professional product photography style
- Sharp focus on the robot as the hero subject
- Subtle depth of field, clean background
- Premium, polished look suitable for marketing materials
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

print("Generating Adora 2 Max hospital scene (NO TEXT)...")

input_path = os.path.join(base_dir, "adora-2-max-white.png")
output_path = os.path.join(base_dir, "adora-2-max-hospital-clean.png")

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
