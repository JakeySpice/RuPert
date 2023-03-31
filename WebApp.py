import os

from flask import Flask, render_template, request
import openai

from config import OPENAI_API_KEY

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

app = Flask(__name__)


def generate_response(prompt):
    model_id = "davinci:ft-personal-2023-03-25-10-48-27"
    response = openai.Completion.create(
        engine=model_id,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        output_text = generate_response(input_text)
        return render_template("index.html", output_text=output_text)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
