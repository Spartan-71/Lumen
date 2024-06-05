from exa_py import Exa
import google.generativeai as genai
import os
from datetime import datetime, timedelta

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
exa = Exa(api_key=os.environ["EXA_API_KEY"])

SYSTEM_MESSAGE1 = "You are an assistant. Respond to the user query by giving 3 general questions dont go to deep. If the user query is related to some technology or product make sure to respond specifying pros and cons. Remember the questions must short and start with How,Why,When,What,Where."
USER_QUESTION = "What's the recent news from Pune,maharashtra?"

model=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_MESSAGE1)

context = "Intel introduced its Lunar Lake series of chips, which will power thin and light laptops in time for the 2024 holiday season. The new system-on-a-chip (SoC) features improved power efficiency, a 4x increase in NPU processing power, and a 50% faster Intel Arc GPU based on its next-gen Arc Battlemage architecture"
search_response = model.generate_content(contents=context)
print(f"Related Questions: {search_response.text}")