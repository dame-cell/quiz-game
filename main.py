import tkinter as tk
from tkinter import messagebox

# Function to handle submit button click
def submit_name():
    name = entry_name_var.get() # Retrieve name from entry widget variable
    print("Player's name:", name) # Print the name for demonstration
    
    # Update welcome label with player's name
    label_welcome.config(text="Welcome to my quiz game, {}!".format(name))
    
    # Add label with exit message
    label_exit.config(text="Please exit this window to play the quiz game.")

# Create the tkinter window
root = tk.Tk()
root.title("enter your name")
root.geometry("500x500")

# Create label for name input prompt
label_prompt = tk.Label(root, text="Please enter your name:")
label_prompt.pack(pady=10)

# Create entry widget for name input
entry_name_var = tk.StringVar() # Create a StringVar to store the entry value
entry_name = tk.Entry(root, textvariable=entry_name_var) # Associate entry widget with StringVar
entry_name.pack(pady=10)

# Create submit button
button_submit = tk.Button(root, text="Submit", command=submit_name)
button_submit.pack()

# Create label for welcome message
label_welcome = tk.Label(root, text="")
label_welcome.pack()

# Create label for exit message
label_exit = tk.Label(root, text="")
label_exit.pack()

# Start the tkinter event loop
root.mainloop()


def submit_name():
    name = entry_name.get() # Retrieve name from entry widget
    print("Player's name:", name) # Print the name for demonstration
    
    # Close the current window
    root.destroy()


root.mainloop()

questions = [   
    {"question": "What is the currency of Japan?", "answer": "Yen"},
    {"question": "What is the derivative of cos(x)?", "answer": "-sin(x)"},
    {"question": "What is the determinant of a 2x2 matrix [[a, b], [c, d]]?", "answer": "ad - bc"},
    {"question": "What is the SI unit of electric current?", "answer": "ampere"},
    {"question": "What is the integral of '3x^2'?", "answer": "x^3 + C (where C is the constant of integration)"},
    {"question": "What is the dot product of two vectors 'a' and 'b'?", "answer": "scalar"},
    {"question": "What is the acceleration due to gravity on Earth?", "answer": "9.8 m/s^2"},


]




current_question = 0

def check_answer():
    global current_question
    answer = entry_answer.get()
    if answer.strip().lower() == questions[current_question]["answer"].lower():
        messagebox.showinfo("Correct", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect", "Your answer is incorrect. Try again.")
    current_question += 1
    if current_question < len(questions):
        label_question.config(text=questions[current_question]["question"])
        entry_answer.delete(0, tk.END)
    else:
        messagebox.showinfo("Quiz Completed", "You have completed the quiz!")

root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x500")
# Set the background color to orange
root.configure(bg='orange')



label_question = tk.Label(root, text=questions[current_question]["question"], wraplength=300)
label_question.pack(pady=10)

entry_answer = tk.Entry(root)
entry_answer.pack(pady=10)

button_submit = tk.Button(root, text="Submit", command=check_answer)
button_submit.pack()

root.mainloop()




root.mainloop()


