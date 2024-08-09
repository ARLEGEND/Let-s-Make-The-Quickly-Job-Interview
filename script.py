from flask import Flask, request, render_template_string
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyB7PLPdBxIGs5nwWkXF_qf7I7x7ItFMg8Q")

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/generate', methods=['POST'])
def generate():
    tools = request.form.get('tools')
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Ben bir developerım ve kullandığım teknolojiler " + tools + ". Bana bunlara uygun mülakat soruları üret")
    return render_template_string(open('index.html').read() + "<div id='output'>" + response.text + "</div>")

if __name__ == '__main__':
    app.run(debug=True)