from dotenv import find_dotenv, load_dotenv
from langchain.adapters import openai as lc_openai

# Load OpenAI API token 
load_dotenv(find_dotenv())

messages = [
    {
        "role": "user", 
        "content": '''
            Below is the list of websites URLS. Analyze each of the websites in it and answer the question: "What is the full name of Gus?"\n
            - https://en.wikipedia.org/wiki/Kamikaze
            - https://en.wikipedia.org/wiki/Copper
            - https://en.wikipedia.org/wiki/Breaking_Bad
            - https://en.wikipedia.org/wiki/Nagant_M1895
        '''
    }
]

lc_result = lc_openai.chat.completions.create(
    messages=messages, model="gpt-4", temperature=0.7
)

print(lc_result.choices[0].message['content'])
