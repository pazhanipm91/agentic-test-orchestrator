## LLM Failure Reasoning Agent:

from openai import OpenAI

client = OpenAI()

def analyze_failure(test_name, request, response, error):
    prompt = f"""
You are an expert API reliability engineer.

Test Name: {test_name}
Request: {request}
Response: {response}
Error: {error}

1. Identify root cause
2. Classify failure type
3. Suggest test improvement
4. Suggest API fix if needed
"""

    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return result.choices[0].message.content
