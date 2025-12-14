#!/usr/bin/env python3
"""Generate Adora 2 Mini house cleaning scene."""

import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

prompt = """
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

CRITICAL: NO TEXT, NO WORDS, NO LETTERS anywhere in the image. NO HUMANS.

Scene Description:
- Setting: A modern, bright, clean home living room / open living space
- Environment: Minimalist Scandinavian-style home interior, spacious and airy
- Features: Modern furniture (sofa, coffee table), clean floors, large windows with natural light
- Floor: Light hardwood or clean white flooring
- Background: Modern kitchen visible, indoor plants, minimalist decor

Robot Placement:
- Position the robot in the center-left of the frame
- The robot appears to be helping with household tasks / cleaning
- One arm could be gesturing or in a helpful pose
- Robot looks like a friendly home assistant

Atmosphere:
- Bright, clean, welcoming home environment
- Warm natural sunlight streaming through windows
- Fresh, airy, and immaculate
- Modern smart home aesthetic

Style Requirements:
- Clean, minimalist product showcase aesthetic
- NO HUMANS in the image - only the robot
- NO TEXT, NO SIGNS, NO WORDS anywhere
- Bright, well-lit home environment
- Professional interior photography style
- Sharp focus on the robot as the hero subject
- Warm, cozy color palette (whites, light woods, soft grays)
- Premium home/lifestyle aesthetic suitable for marketing
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

print("Generating Adora 2 Mini house cleaning scene...")

input_path = os.path.join(base_dir, "adora-2-mini-white.png")
output_path = os.path.join(base_dir, "adora-2-mini-home-clean.png")

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
