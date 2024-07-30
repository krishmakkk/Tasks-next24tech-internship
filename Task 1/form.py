import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to handle form submission
def submit_form():
    first_name = entry_first_name.get().strip()
    last_name = entry_last_name.get().strip()
    email = entry_email.get().strip()
    age = entry_age.get().strip()
    work = entry_work.get().strip()
    birth_date = entry_birth_date.get().strip()
    
    # Validate the inputs
    if not first_name or not last_name or not email or not age or not work or not birth_date:
        messagebox.showerror("Error", "All fields are required.")
        return
    
    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return
    
    # Show the submitted information
    messagebox.showinfo("Form Submitted", f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nAge: {age}\nWork: {work}\nBirth Date: {birth_date}")
    
    # Display "Form Submitted" message
    label_submit_message.config(text="Form Submitted")
    
    # Clear the form fields
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_work.delete(0, tk.END)
    entry_birth_date.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Form")

# Configure style
style = ttk.Style()
style.configure("TLabel", padding=6)
style.configure("TEntry", padding=6)
style.configure("TButton", padding=6)

# Create and place the labels and entry fields
label_first_name = ttk.Label(root, text="First Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_first_name = ttk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

label_last_name = ttk.Label(root, text="Last Name:")
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_last_name = ttk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

label_email = ttk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_email = ttk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_age = ttk.Label(root, text="Age:")
label_age.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_age = ttk.Entry(root)
entry_age.grid(row=3, column=1, padx=10, pady=5)

label_work = ttk.Label(root, text="Work:")
label_work.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
entry_work = ttk.Entry(root)
entry_work.grid(row=4, column=1, padx=10, pady=5)

label_birth_date = ttk.Label(root, text="Birth Date:")
label_birth_date.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
entry_birth_date = ttk.Entry(root)
entry_birth_date.grid(row=5, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Label to show the submission message
label_submit_message = ttk.Label(root, text="", foreground="green")
label_submit_message.grid(row=7, column=0, columnspan=2, pady=5)

# Add padding to the main window
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=5)

# Start the main event loop
root.mainloop()
