'''

Here is the code for my CS2 Project titled "ReadMe" 

GitHub link for continued progress: https://github.com/mikey2fye/comp_sci_2_project

'''
import tkinter as tk
import sqlite3

# Create the main window
root = tk.Tk()
root.title("Sign In")

# Create labels and entry boxes for the user to enter their username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a function to check if the user's credentials are correct
def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    if username == "example_user" and password == "example_password":
        tk.messagebox.showinfo("Success", "You have successfully signed in!")
    else:
        tk.messagebox.showerror("Error", "Incorrect username or password. Please try again.")

# Create a button to submit the user's credentials
submit_button = tk.Button(root, text="Submit", command=check_credentials)
submit_button.pack()

# Run the main loop
root.mainloop()

# Connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('user_info.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# Create a table to store user information
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL,
              email TEXT NOT NULL)''')

# Add some sample data to the table
c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ('john', 'password123', 'john@example.com'))
c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ('jane', 'password456', 'jane@example.com'))

# Save the changes to the database
conn.commit()

# Connect to the database
conn = sqlite3.connect('user_info.db')

# Create a cursor object
c = conn.cursor()

# Insert a new user into the database
c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", ('new_user', 'new_password', 'new_user@example.com'))

# Save the changes to the database
conn.commit()
# Connect to the database
conn = sqlite3.connect('user_info.db')

# Create a cursor object
c = conn.cursor()

# Retrieve user information from the database
c.execute("SELECT * FROM users WHERE username=?", ('john',))
user = c.fetchone()
print(user)

# Close the connection to the database
conn.close()
