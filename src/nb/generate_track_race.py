#!/usr/bin/env python3
"""Generate 3 Adora 1 Pro robots racing on a track field."""

import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

prompt = """
Generate a photorealistic image featuring exactly 3 robots racing on a track.

REFERENCE IMAGE:
- Use the provided robot image as reference for all 3 robots

ROBOT REQUIREMENTS:
- Create exactly 3 identical robots based on the reference image
- Keep the robots clean - only show the small logo on the body/chassis as in reference
- NO additional logos or text on the head/arm part of the robot

SCENE REQUIREMENTS:
- Setting: Outdoor athletic track field / running track stadium
- Track: Classic RED/terracotta colored running track with white lane markings
- One robot is LEADING (positioned ahead of the other two)
- Two robots following behind in adjacent lanes
- All robots appear to be racing/moving forward

TECHNICAL REQUIREMENTS:
- NO BLUR anywhere - everything sharp and in focus
- Photorealistic rendering quality
- NO HUMANS in the scene
- Bright daylight, blue sky
- Green grass infield visible
- Stadium or grandstands in background
- Professional sports photography style

The image should look like a real photo of robots competing in a race on a professional athletic track.
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
        aspect_ratio="4:3",
        image_size="2K",
    ),
)

print("Generating 3 Adora 1 Pro robots racing on track...")

# Load robot reference image
robot_path = os.path.join(base_dir, "adora-1-pro-black.png")
with open(robot_path, "rb") as f:
    robot_data = f.read()
robot_image = types.Part.from_bytes(data=robot_data, mime_type="image/png")

# Combine: robot image + prompt (no logo)
contents = [robot_image, prompt]

output_path = os.path.join(base_dir, "adora-1-pro-track-race.png")

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
