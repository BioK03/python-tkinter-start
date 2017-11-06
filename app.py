import tkinter as tk


window = tk.Tk()

window.title("My app")

window.geometry("400x400")

# LABEL
title = tk.Label(text="Hello world!", font=("Times New Roman", 20))
title.grid(column=0, row=0)

# BUTTON
button1 = tk.Button(text="Click me!", bg="red")
button1.grid(column=0, row=1)

# ENTRY FIELD
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

# TEXT FIELD
text_field1 = tk.Text(master=window, height=10, width=30)
text_field1.grid()

window.mainloop()