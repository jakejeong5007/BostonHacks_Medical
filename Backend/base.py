from openai import OpenAI
import json



info = input("User information\n")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a medical assistant \
      that gives food recommendation depending on the medcial information of the user.\
      Please give an answer by listing three food recommendation and a sentence explanation for each of them"},
    {"role": "user", "content": info}
  ]
)


response = completion.choices[0].message.content.split("\n")

for row in response:
  if len(row) > 1:
    print(row)
    

def recommend_food(u_info):
  client = OpenAI(api_key = "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")
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a medical assistant \
        that gives food recommendation depending on the medcial information of the user.\
        Please give an answer by listing three food recommendation and a sentence explanation for each of them"},
      {"role": "user", "content": u_info}
    ]
  )
  response = completion.choices[0].message.content.split("\n")
  
  for row in response:
    if len(row) > 1:
      answer = "\n" + row
      
  return answer

  