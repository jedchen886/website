#!/usr/bin/env python3
"""Generate series of robot scene images with consistent styling."""

import os
from google import genai
from google.genai import types

# Initialize client
client = genai.Client(api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"))

# Base directory
base_dir = "/Users/yuechen/home/website/src/nb"

# Common style guidelines
STYLE_GUIDELINES = """
Technical Requirements:
- Photorealistic rendering quality
- High detail and sharp focus on the robot
- Realistic depth of field with slight background blur
- Professional photography style
- Warm, natural lighting
- The robot should be clearly visible and be a main subject
- Include realistic human characters where specified
"""

# Scene configurations
scenes = [
    {
        "input": "adora-2-max-white.png",
        "output": "adora-2-max-hospital.png",
        "prompt": f"""
Generate a photorealistic image based on the robot in the provided reference image.

Scene Description:
- Setting: A modern hospital lobby/corridor
- Environment: Clean, bright hospital interior with white walls and soft blue accents
- Features: Information desk area, directional signs, waiting area visible in background
- Floor: Polished hospital flooring

Robot Role & Pose:
- The robot is serving as a patient guide/assistant
- Position the robot at the left-center of the frame
- The robot should have one arm extended in a guiding gesture, pointing direction
- The robot appears helpful and approachable

Human Characters:
- An elderly Chinese patient (60-70 years old) standing near the robot
- The patient looks at the robot with a grateful expression
- Patient wearing casual comfortable clothing

Lighting and Atmosphere:
- Bright, clean hospital lighting
- Soft natural light from large windows
- Professional, reassuring atmosphere
- The mood should feel helpful and caring

{STYLE_GUIDELINES}
"""
    },
    {
        "input": "adora-2-pro-white.png",
        "output": "adora-2-pro-university-lab.png",
        "prompt": f"""
Generate a photorealistic image based on the robot in the provided reference image.

Scene Description:
- Setting: A modern university research laboratory / medical teaching facility
- Environment: High-tech lab with medical equipment, monitors, and research stations
- Features: Lab benches, computer screens, medical imaging displays, scientific equipment
- Floor: Clean laboratory flooring

Robot Role & Pose:
- The robot is serving as a lab assistant helper
- Position the robot in the center-left of the frame
- The robot should appear engaged in assisting with lab work
- Arms in a helpful, working position

Human Characters:
- A Chinese doctor/professor in white lab coat (male, 40-50 years old)
- A Chinese patient or research subject sitting nearby
- Both appear to be interacting with or observing the robot's assistance
- Professional, academic atmosphere

Lighting and Atmosphere:
- Bright laboratory lighting with some blue accent lights from equipment
- Clean, scientific environment
- Modern and high-tech feel
- The mood should feel innovative and professional

{STYLE_GUIDELINES}
"""
    },
    {
        "input": "adora-2-mini-white.png",
        "output": "adora-2-mini-school.png",
        "prompt": f"""
Generate a photorealistic image based on the robot in the provided reference image.

Scene Description:
- Setting: A modern Chinese middle school classroom or robotics lab
- Environment: Bright, colorful educational space with desks, educational posters, and technology
- Features: Student desks, interactive whiteboard, educational materials, robotics kits
- Floor: Clean classroom flooring

Robot Role & Pose:
- The robot is serving as an educational assistant for robotics learning
- Position the robot on the left side of the frame
- The robot should appear friendly and engaging with students
- Arms in an expressive, teaching gesture

Human Characters:
- 2-3 Chinese middle school students (ages 12-14) gathered around the robot
- Students wearing school uniforms (white shirts, dark pants/skirts)
- Students appear curious, engaged, and excited about learning
- Mix of boys and girls

Lighting and Atmosphere:
- Bright, warm classroom lighting
- Natural daylight from windows
- Cheerful, educational atmosphere
- The mood should feel fun, engaging, and inspiring

{STYLE_GUIDELINES}
"""
    },
    {
        "input": "adora-1-pro-black.png",
        "output": "adora-1-pro-farming.png",
        "prompt": f"""
Generate a photorealistic image based on the robot in the provided reference image.

Scene Description:
- Setting: An orchard or fruit farm during harvest season
- Environment: Lush green orchard with fruit trees (apple or orange trees)
- Features: Rows of fruit trees, ripe fruits on trees, harvesting baskets/crates nearby
- Ground: Natural orchard ground with grass and soil

Robot Role & Pose:
- The robot is assisting with fruit picking/harvesting
- Position the robot on the left side of the frame among the trees
- The robot should have arms extended upward toward fruits on the tree
- The robot appears to be carefully picking or reaching for fruits

Environment Details:
- Beautiful sunny day with blue sky visible through tree canopy
- Ripe, colorful fruits (red apples or oranges) on the trees
- Some harvested fruits in baskets nearby
- Natural, pastoral agricultural setting

Lighting and Atmosphere:
- Warm, golden sunlight filtering through the trees
- Natural outdoor lighting with soft shadows
- Fresh, outdoor agricultural atmosphere
- The mood should feel productive and harmonious with nature

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
        aspect_ratio="4:3",
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
    print("Starting batch image generation...")
    print(f"Generating {len(scenes)} images at 2K resolution, 4:3 aspect ratio")

    for i, scene in enumerate(scenes, 1):
        print(f"\n[{i}/{len(scenes)}] Processing {scene['output']}...")
        try:
            generate_scene(scene)
        except Exception as e:
            print(f"Error generating {scene['output']}: {e}")

    print("\n" + "="*60)
    print("All generations complete!")
    print("="*60)
