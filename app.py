import openai
from secret import apiPass

openai.api_key = apiPass

story = input("\nHi, Im Simon. I can help you finish your story. What do you have so far?\n")

response = openai.Completion.create(
    model = "text-davinci-002",
    prompt = f"you are a friendly AI bot named Simon. You are speaking with a human who is desperately trying to get an ending for a story they created. Their story: {story}", 
    temperature = .28,
    max_tokens = 70,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0,
)

ending = response["choices"][0]["text"]

print(ending)