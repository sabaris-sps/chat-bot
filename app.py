import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

# Define your chatbot response function


def get_response(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Define your Flask routes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    prompt = request.args.get("prompt")
    bot_response = get_response(prompt)
    return bot_response


if __name__ == "__main__":
    app.run(debug=True)
