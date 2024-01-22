import openai

openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="What dinosaurs lived in the cretaceous period?",
  max_tokens=60
)

print(response.choices[0].text.strip())