import re

from google import generativeai as gi 
gi.configure(api_key = 'AIzaSyAioEOAN72RG0nXT6V7s0_FTUv8Frx0-8k')


# for model in gi.list_models():
#     if 'generateContent' in model.supported_generation_methods:
#         print(model.name)


# Text-to-Text 
LLM_t2t = gi.GenerativeModel(model_name = 'gemini-1.5-pro-latest')

# answer = LLM_t2t.generate_content("Who is president of INDIA?")
# print(answer.text)

def genContent(user_q):
   return format_text(LLM_t2t.generate_content(user_q).text)

def format_text(text):
    # Replace `*` with a newline
    text = re.sub(r'\*', '\n', text)
    
    # Make text between `**-----**` bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
   #  print(text)
    return text

