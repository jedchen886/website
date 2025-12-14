#!/usr/bin/env python3
"""Generate clean, futuristic robot scene images - product showcase style."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))

# Base directory
base_dir = "/Users/yuechen/home/website/src/nb"

# Common style guidelines for clean product showcase
STYLE_GUIDELINES = """
Style Requirements:
- Clean, minimalist product showcase aesthetic
- NO HUMANS in the image - only the robot
- Futuristic, high-tech environment
- Warm, soft lighting with gentle highlights
- Professional product photography style
- Sharp focus on the robot as the hero subject
- Subtle depth of field, clean background
- Cohesive warm color palette (soft whites, warm grays, subtle accent colors)
- Premium, polished look suitable for marketing materials
- The robot should be prominently displayed and clearly visible
- Environment should feel spacious and uncluttered
"""

# Scene configurations - clean futuristic environments
scenes = [
    {
        "input": "adora-2-max-white.png",
        "output": "adora-2-max-hospital-clean.png",
        "prompt": f"""
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

Scene Description:
- Setting: A futuristic hospital lobby of tomorrow
- Environment: Ultra-clean, minimalist medical facility with smooth white surfaces
- Features: Curved architectural elements, soft blue ambient lighting accents, holographic wayfinding displays
- Floor: Pristine white polished floor with subtle reflections
- Background: Blurred futuristic corridor with soft lighting

Robot Placement:
- Position the robot at the left-center of the frame (rule of thirds)
- The robot should have one arm in a gentle guiding gesture
- Robot appears ready to assist, welcoming pose

Atmosphere:
- Bright, airy, and immaculately clean
- Soft diffused lighting from above
- Futuristic but warm and inviting
- Premium healthcare environment aesthetic

{STYLE_GUIDELINES}
"""
    },
    {
        "input": "adora-2-pro-white.png",
        "output": "adora-2-pro-lab-clean.png",
        "prompt": f"""
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

Scene Description:
- Setting: A next-generation research laboratory
- Environment: Sleek, minimalist lab with clean lines and modern equipment
- Features: Futuristic monitors with blue glow, clean lab benches, subtle tech elements
- Floor: Smooth white or light gray flooring
- Background: Blurred high-tech equipment with soft blue accent lighting

Robot Placement:
- Position the robot in the center-left of the frame
- The robot should appear poised and ready for precision work
- Arms in a neutral, professional position

Atmosphere:
- Clean, scientific, and sophisticated
- Cool blue accent lighting mixed with warm ambient light
- High-tech but approachable
- Premium research facility aesthetic

{STYLE_GUIDELINES}
"""
    },
    {
        "input": "adora-2-mini-white.png",
        "output": "adora-2-mini-school-clean.png",
        "prompt": f"""
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

Scene Description:
- Setting: A futuristic smart classroom or learning space
- Environment: Bright, modern educational space with clean minimalist design
- Features: Interactive digital displays, sleek furniture, soft colorful accents (gentle yellows, soft blues)
- Floor: Clean light wood or white flooring
- Background: Blurred modern classroom elements with warm lighting

Robot Placement:
- Position the robot on the left side of the frame
- The robot should appear friendly and engaging
- Arms in a welcoming, expressive gesture

Atmosphere:
- Bright, cheerful, and inspiring
- Warm natural lighting with soft shadows
- Modern educational environment
- Friendly and approachable aesthetic

{STYLE_GUIDELINES}
"""
    },
    {
        "input": "adora-1-pro-black.png",
        "output": "adora-1-pro-farming-clean.png",
        "prompt": f"""
Generate a clean, futuristic product showcase image based on the robot in the provided reference image.

Scene Description:
- Setting: A futuristic smart farm or vertical farming facility
- Environment: Clean, modern agricultural setting with organized rows of plants/trees
- Features: Lush green apple trees or fruit plants, modern irrigation systems, clean pathways
- Ground: Well-maintained grass or clean agricultural flooring
- Background: Beautiful orchard with soft bokeh, blue sky visible

Robot Placement:
- Position the robot on the left side of the frame among the trees
- The robot should have arm extended toward fruit on tree
- Appears to be carefully reaching for or picking fruit

Atmosphere:
- Golden hour sunlight, warm and inviting
- Clean, organized agricultural setting
- Nature meets technology aesthetic
- Fresh, outdoor feel but pristine and well-maintained

{STYLE_GUIDELINES}
"""
    },
]

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


def generate_scene(scene_config):
    """Generate a single scene."""
    input_path = os.path.join(base_dir, scene_config["input"])
    output_path = os.path.join(base_dir, scene_config["output"])

    print(f"\n{'='*60}")
    print(f"Generating: {scene_config['output']}")
    print(f"Input: {scene_config['input']}")
    print(f"{'='*60}")

    # Load input image
    with open(input_path, "rb") as f:
        image_data = f.read()

    input_image = types.Part.from_bytes(data=image_data, mime_type="image/png")

    # Generate
    contents = [input_image, scene_config["prompt"]]

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


if __name__ == "__main__":
    print("Starting clean product showcase image generation...")
    print(f"Generating {len(scenes)} images at 2K resolution, 4:3 aspect ratio")
    print("Style: Clean, futuristic, NO HUMANS, product showcase")

    for i, scene in enumerate(scenes, 1):
        print(f"\n[{i}/{len(scenes)}] Processing {scene['output']}...")
        try:
            generate_scene(scene)
        except Exception as e:
            print(f"Error generating {scene['output']}: {e}")

    print("\n" + "="*60)
    print("All generations complete!")
    print("="*60)
