import os
import tkinter as tk
from tkinter import ttk



# This calls the config.py file to get the OpenAI API key. config.py is not included in this repo
# because it contains the OpenAI API key. You can create your own config.py file and add the
# OpenAI API key to it.
from config import OPENAI_API_KEY

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
import openai

def generate_response(prompt):
    model_id = "davinci:ft-personal-2023-03-25-10-48-27"
    response = openai.Completion.create(
        engine=model_id,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop="\n\n",
        temperature=0.7,
    )

    return response.choices[0].text.strip()


def on_button_click():
    input_text = entry.get("1.0", "end-1c")
    output_text = generate_response(input_text)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, output_text)


def create_main_window():
    root = tk.Tk()
    root.title("RuPert v0.1")

    entry = tk.Text(root, wrap="word", width=50, height=5)
    entry.grid(row=0, column=0, padx=10, pady=10, sticky="N")

    button = ttk.Button(root, text="Submit", command=on_button_click)
    button.grid(row=1, column=0, padx=10, pady=10, sticky="N")

    result_text = tk.Text(root, wrap="word", width=50, height=10)
    result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="N")

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=result_text.yview)
    scrollbar.grid(row=2, column=1, sticky="NS")
    result_text["yscrollcommand"] = scrollbar.set

    return root, entry, result_text


if __name__ == "__main__":
    root, entry, result_text = create_main_window()
    root.mainloop()
