from openai import AzureOpenAI
from pathlib import Path
import yaml
import os

# ==========================
# 1️⃣ Azure Configuration
# ==========================

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  # safer method
    api_version="2024-05-01-preview",
    azure_endpoint="https://kneeraja.openai.azure.com/"
)

DEPLOYMENT_NAME = "gpt-4o"

# ==========================
# 2️⃣ Load YAML
# ==========================

YAML_FILE = Path("tests_data/claims_data.yaml")

with open(YAML_FILE) as f:
    claims_data = yaml.safe_load(f)

prompt = f"""
Generate a complete Python pytest script for claims processing using:

{claims_data}

Requirements:
- Use pytest.mark.parametrize
- Validate expected_status
- Include positive and negative scenarios
- Return only valid Python code
"""

# ==========================
# 3️⃣ Call Azure OpenAI
# ==========================

response = client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=[
        {"role": "system", "content": "You are a pytest automation expert."},
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

generated_code = response.choices[0].message.content
print(generated_code)

# ==========================
# 4️⃣ Save Generated File
# ==========================

TESTS_FOLDER = Path("aitests")
TESTS_FOLDER.mkdir(exist_ok=True)

output_file = TESTS_FOLDER / "test_generated.py"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(generated_code)

print(f"\n✅ Pytest script generated at {output_file}")