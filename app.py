from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Secret key API OpenAI
openai.api_key = "OPENAI_API_KEY"

# Load ChatGPT model
model_engine = "text-davinci-003"
model_prompt = "Ask a question and I will try to answer it."
chat_gpt = openai.Completion.create(engine=model_engine, prompt=model_prompt)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

# Handling user requests and ChatGPT responses
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    model_input = model_prompt + "\nUser: " + user_message.strip() + "\nChatGPT:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=model_input,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.4,
    )
    model_output = response.choices[0].text.strip()
    return {'bot_message': model_output}

if __name__ == '__main__':
    app.run(debug=True)