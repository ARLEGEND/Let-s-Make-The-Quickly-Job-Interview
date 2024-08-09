import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyB7PLPdBxIGs5nwWkXF_qf7I7x7ItFMg8Q")

model = genai.GenerativeModel('gemini-1.5-flash')

tools= input("Kullandığınız teknolojileri girin aralarda virgül bırakarak giriniz")

response = model.generate_content("Ben bir developerım ve kullandığım teknolojiler "  + tools + ".  Bana bunlara uygun mülakat soruları üret")
print(response.text)