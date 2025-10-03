# app.py  (no IntVar, no get/set)
import tkinter as tk

count = 0  # plain Python integer

def increment():
    global count
    count += 1
    lbl.config(text=str(count))  # manually refresh the label

root = tk.Tk()
root.title("Step 1 - no Tk variables")

lbl = tk.Label(root, text=str(count), font=("Segoe UI", 20))
lbl.pack(padx=20, pady=10)

btn = tk.Button(root, text="Add 1", command=increment)
btn.pack(pady=8)

root.mainloop()
