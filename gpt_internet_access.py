'''
Instructions:
1. pip install pip install google-search-results langchain
2. Create an account on https://serper.dev/
3. Replace the OpenAI and Serper API keys with the real ones
'''

import os
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent

os.environ["SERPER_API_KEY"] = PASTE_YOUR_SERPER_API_KEY_HERE
OPENAI_KEY = PASTE_YOUR_OPENAI_API_KEY_HERE

llm = OpenAI(openai_api_key=OPENAI_KEY, temperature=0.7, model_name='gpt-3.5-turbo')
tools = load_tools(["google-serper"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

print("*** Let's get answers to anything across the internet and beyond Sep 2023 ***")
while True:
    question = input("--> Enter a question: ")
    print('Fetching the answer...')
    print('The answer is: {}\n\n'.format(agent.run(question)))
