from exa_py import Exa
import google.generativeai as genai
import os
from datetime import datetime, timedelta

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
exa = Exa(api_key=os.environ["EXA_API_KEY"])


# getting search query from gemini , futher this query will be provided to exa
SYSTEM_MESSAGE1 = "You are a helpful assistant that generates search queries based on user questions. Only generate one search query."
print("Enter the Question: ")
USER_QUESTION = input()

model1=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_MESSAGE1)

search_response = model1.generate_content(contents=USER_QUESTION)
search_query = search_response.text
print("Search query:",search_query)

# Providing the search query to exa with time constrains
one_week_ago = (datetime.now() - timedelta(days=7))
date_cutoff = one_week_ago.strftime("%Y-%m-%d")


search_response = exa.search_and_contents(
    search_query,
    use_autoprompt=True,
    start_published_date=date_cutoff,
    num_results=4,
    highlights=True,exclude_domains=["https://www.youtube.com/"]
)

Highlights = [result.highlights for result in search_response.results]
print("Highlights:")
for highlight in Highlights:
    print(highlight)

# dynamic_dict = {}
# i=0
# for result in search_response.results:
#    dynamic_dict[] = result.highlights 
#    i+=1
# print(dynamic_dict)

URLs = [result.url for result in search_response.results]
# print("URLs:")
# for url in URLs:
#     print(url)



# summarizing the inputs from highlights 
SYSTEM_MESSAGE2 = "You are a helpful assistant that briefly summarizes the highlights of news. Summarize the users input and dont include 'the article discusses' or something similar directly give the summary."
model2 = genai.GenerativeModel(model_name='gemini-1.5-flash',system_instruction=SYSTEM_MESSAGE2)

response =""
for url,highlight in zip(URLs,Highlights):
    search_response=model2.generate_content(highlight)
    print("Source:")
    print(url)
    print("Summary:")
    print(search_response.text)
    response += search_response.text


# Getting 3 related questions
SYSTEM_MESSAGE3 = "You are an assistant. Respond in 3 short questions that user might search on the internet and start with How,Why,When,What,Where.DO NOT PROVIDE ANY OTHER TEXT THAN Questions."


model3=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_MESSAGE3)

search_response = model3.generate_content(contents= response)
print(f"Related Questions: {search_response.text}")

