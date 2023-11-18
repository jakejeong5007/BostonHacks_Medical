from openai import OpenAI
import json
import config


def recommend_food(u_info):
  client = OpenAI(api_key = config.OPENAI_API_KEY)
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

  