import json
import re
from openai import OpenAI

from agent_config import ARCHITECT_ROLE
from schemas import ArchitectureDesign


client = OpenAI()


def extract_json(content: str) -> dict:
    """
    Safely extract JSON from LLM output.
    Handles:
    - ```json ... ```
    - ``` ... ```
    - Plain JSON
    """
    content = content.strip()

    # Remove markdown code fences if present
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?", "", content)
        content = re.sub(r"```$", "", content)
        content = content.strip()

    return json.loads(content)


def architectural_agent(requirements: str) -> ArchitectureDesign:
    """
    Generates an architecture design from system requirements
    using an LLM and returns a validated ArchitectureDesign object.
    """

    prompt = f"""
{ARCHITECT_ROLE}

System Requirements:
{requirements}

IMPORTANT RULES:
- Return ONLY valid JSON
- Do NOT include markdown, code fences, or explanations
- The output MUST match this schema exactly

Schema:
{ArchitectureDesign.model_json_schema()}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    raw_content = response.choices[0].message.content

    # Extract and parse JSON safely
    parsed_json = extract_json(raw_content)

    # Validate and return strongly-typed architecture design
    return ArchitectureDesign.model_validate(parsed_json)
