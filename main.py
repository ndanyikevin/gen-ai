import os
from dotenv import load_dotenv
from groq import Groq, APIError

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing.")

client = Groq(api_key=api_key)

prompt = """
Act as an experienced startup incubator director in India. Generate 4 innovative product or business ideas specifically targeting millennial software engineers living in Bangalore (Bengaluru).

Constraints:
- Low Capital: Ideas must require minimal upfront investment, relying primarily on digital assets, platform subscriptions, local service coordination, or lean MVP software.
- Target Audience: Millennial tech workers (long working hours, tech-savvy, high disposable income, dealing with urban commuting, lifestyle burnouts).
- Format: For each idea, include the Concept Name, The Core Problem, The Solution, and Why It's Low-Capital.
"""

print("Generating business ideas using Groq...\n")

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",  # free, fast, capable
        messages=[
            {
                "role": "system",
                "content": "You are an experienced startup incubator director in India.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
    )
except APIError as e:
    raise SystemExit(f"Groq API error: {e}")

output_text = response.choices[0].message.content
print(output_text)

with open("assignment_ideas_output.md", "w", encoding="utf-8") as f:
    f.write(output_text)

print("\n[+] Success! Saved to 'assignment_ideas_output.md'.")