#!/usr/bin/env python3
"""Generate Adora 1 Pro warehouse and Adora 1 Nano robot club scenes."""

import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
base_dir = "/Users/yuechen/home/website/src/nb"

scenes = [
    {
        "input": "adora-1-pro-black.png",
        "output": "adora-1-pro-warehouse-clean.png",
        "prompt": """
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

CRITICAL: NO TEXT, NO WORDS, NO LETTERS anywhere in the image.

Scene Description:
- Setting: A bright, modern Costco-style warehouse
- Environment: Large open warehouse space with high ceilings, bright LED lighting
- Features: Tall industrial shelving racks with organized products/boxes, wide clean aisles
- Floor: Polished concrete warehouse floor
- Lighting: Bright, even warehouse lighting from above - well-lit and clean

Robot Placement:
- Position the robot in the center-left of the frame
- The robot arm should be reaching toward or picking items from shelving
- Robot appears to be working efficiently in the warehouse

Atmosphere:
- Bright, clean, industrial but modern
- Professional warehouse/logistics environment
- High ceilings with visible steel structure
- Organized and efficient aesthetic

Style Requirements:
- Clean, minimalist product showcase aesthetic
- NO HUMANS in the image - only the robot
- NO TEXT, NO SIGNS, NO WORDS anywhere
- Bright, well-lit environment
- Professional product photography style
- Sharp focus on the robot
- Premium logistics/warehouse aesthetic
"""
    },
    {
        "input": "adora-1-nano-feature1.png",
        "output": "adora-1-nano-club-clean.png",
        "prompt": """
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

CRITICAL: NO TEXT, NO WORDS, NO LETTERS anywhere in the image.

Scene Description:
- Setting: A clean, modern robot club/lounge space
- Environment: Sleek, minimalist social space designed for robots and tech enthusiasts
- Features: Modern furniture, ambient lighting, clean geometric design elements
- Floor: Polished floor with subtle reflections
- Lighting: Soft ambient lighting with subtle colored accents (purple, blue, pink gradients)

Robot Placement:
- Position the small robot in the center-left of the frame
- The robot should appear friendly and social
- Robot is the cute, small centerpiece of the scene

Atmosphere:
- Modern, trendy, tech-forward social space
- Clean and minimalist but with personality
- Soft ambient glow, futuristic lounge vibe
- Welcoming and approachable

Style Requirements:
- Clean, minimalist product showcase aesthetic
- NO HUMANS in the image - only the robot
- NO TEXT, NO SIGNS, NO WORDS anywhere
- Futuristic club/lounge environment
- Warm, soft lighting with gentle highlights
- Professional product photography style
- Sharp focus on the robot as the hero subject
- Premium, polished look suitable for marketing
"""
    },
]

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

for i, scene in enumerate(scenes, 1):
    print(f"\n[{i}/{len(scenes)}] Generating {scene['output']}...")

    input_path = os.path.join(base_dir, scene["input"])
    output_path = os.path.join(base_dir, scene["output"])

    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")
    contents = [input_image, scene["prompt"]]

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

print("\nAll generations complete!")
