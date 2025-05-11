import csv
import os
import re
from datetime import datetime

# Define the input and output directories
# track = 'ai-infra'
# track = 'ai-models'
# track = 'embodied-ai'
track = 'ai-apps'
csv_file = track+'.csv'
output_dir = './speakers'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def get_slug(name):
    """Convert speaker name to a valid slug"""
    # Replace spaces with hyphens and remove special characters
    clean_name = re.sub(r'[^\w\s-]', '', name).strip().lower()
    return re.sub(r'[\s]+', '-', clean_name)

# Get current date for publishDate field
current_date = datetime.now().strftime("%Y-%m-%d %H:%M")

# Read the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    # Skip header rows
    for _ in range(2):
        next(csv_reader, None)

    # Process each row
    for row in csv_reader:
        # Skip empty rows or rows without enough data
        if not row or len(row) < 10 or not row[5]:
            continue

        # Extract data
        file_name = row[5].strip()
        if not file_name:
            continue

        # Get the data from the relevant columns
        organization = row[1].strip() if row[1].strip() else ""
        speaker_name = row[4].strip() if row[1].strip() else "To Be Announced"
        title = row[6].strip() if row[6].strip() else "Speaker"
        topic = row[9].strip() if row[9].strip() else ""

        # Generate filename
        slug = get_slug(file_name)
        filename = slug + '.md'

        # Create markdown content
        content = f"""---
draft: true
name: "{file_name}"
title: "{title}"
avatar: {{
    src: "/images/speakers/{slug}.png",
    alt: "{file_name}"
}}
topic: "{topic}"
org: "{organization}"
track: "{track}"
publishDate: "{current_date}"
---
"""

        # Write to file
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w', encoding='utf-8') as md_file:
            md_file.write(content)

        print(f"Created file: {output_path}")

print("Processing complete.")
