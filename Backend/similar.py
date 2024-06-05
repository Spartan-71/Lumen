import google.generativeai as genai
from exa_py import Exa
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
exa = Exa(api_key=os.environ["EXA_API_KEY"])


model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
response = model.generate_content('Explain me Quantum Computing like I’m a 5-year-old ')
print(response.text)

search_response = exa.find_similar(url="https://medium.com/predict/you-need-to-learn-ai-in-2024-and-here-is-your-roadmap-c28e6cb5c045",num_results=10,exclude_source_domain=True)
print(search_response)