import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_test_cases(requirement):

    prompt = f"""
    You are a Senior QA Engineer.

    Generate software test cases for the requirement below.

    Requirement:
    {requirement}

    Generate exactly:

    - 5 Positive Test Cases
    - 5 Negative Test Cases
    - 5 Boundary Test Cases
    - 5 Validation Test Cases

    Total: 20 Test Cases

    Return ONLY valid JSON.

    Format:

    [
    {{
        "id":"TC001",
        "category":"Positive",
        "scenario":"User enters valid data",
        "expected_result":"Operation should be successful",
        "priority":"High"
    }}
    ]

    Rules:
    - Every test case must have a unique ID.
    - Category must be one of:
    Positive, Negative, Boundary, Validation
    - Return exactly 20 test cases.
    - Do not return markdown.
    - Do not return explanations.
    - Return JSON only.
    """
    

    response = model.generate_content(prompt)

    return response.text