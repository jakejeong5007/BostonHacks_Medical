from openai import OpenAI

client = OpenAI(
  api_key = "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",
)

info = input("User information")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a medical assistant that gives food recommendation depending on the medcial information of the user."},
    {"role": "user", "content": info}
  ]
)

print(completion.choices[0].message)