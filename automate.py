import os
import openai
# Token and ca-bundle.crt are in the same folder.
os.environ['REQUESTS_CA_BUNDLE'] = "./ca-bundle.crt"
with open("token", "r") as f:
    key = f.read().strip()
    
headers = {
    "Authorization": f"Bearer {key}",
}
openai.api_key = key
openai.api_base = "https://aml-llm-models.icp.infineon.com/v1"

text = "Hello, how are you?"
response = openai.Completion.create(
  engine="davinci",
  prompt=f"Translate from English to Spanish: {text}",
  max_tokens=50
)

translation = response.choices[0].text.strip()
print(translation)
