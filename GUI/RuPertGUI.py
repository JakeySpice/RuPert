import tkinter as tk
from tkinter import ttk

import os
os.environ["OPENAI_API_KEY"] = "<your key>"

import openai

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

def on_button_click():
    input_text = entry.get("1.0", "end-1c")
    # Call your finetuned OpenAI model here with input_text as the input
    output_text = generate_response(input_text)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, output_text)

# Create the main window
root = tk.Tk()
root.title("RuPert v0.1")

# Create an input field (Text widget)
entry = tk.Text(root, wrap="word", width=50, height=5)
entry.grid(row=0, column=0, padx=10, pady=10, sticky="N")

# Create a button
button = ttk.Button(root, text="Submit", command=on_button_click)
button.grid(row=1, column=0, padx=10, pady=10, sticky="N")

# Create an output text field
result_text = tk.Text(root, wrap="word", width=50, height=10)
result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="N")

# Run the main loop
root.mainloop()
