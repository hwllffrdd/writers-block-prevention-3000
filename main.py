from tkinter import *
from tkinter import messagebox, filedialog

inactivity_time = 5000

def reset_timer(event=None):
    global timer
    if timer:
        window.after_cancel(timer)
    timer = window.after(inactivity_time, clear_text)

def clear_text():
    input_text.delete(1.0, END)
    messagebox.showinfo("Yoink!", "5 seconds are over")

def set_inactivity_time():
    global inactivity_time
    try:
        inactivity_time = int(time_entry.get()) * 1000
        reset_timer()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number of seconds")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(input_text.get(1.0, END))
    messagebox.showinfo("Notification", "Text copied to clipboard")

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(input_text.get(1.0, END))
        messagebox.showinfo("Notification", "Text saved to file")


window = Tk()
window.config(padx=50, pady=15, bg="#F5F7F8")
window.resizable(False, False)
window.title("Writer's Block Prevention 3000")

timer = window.after(inactivity_time, clear_text)


app_label = Label(window, text="Writer's Block Prevention 3000", fg="#379777", bg="#F5F7F8", font=("Verdana", 22, "bold"))
app_label.grid(column=0, row=0, pady=20)

canvas = Canvas(width=400, height=260, bg="#F5F7F8", highlightthickness=0)
img = PhotoImage(file="image.png")
canvas.create_image(200, 130, image=img)
canvas.grid(column=0, row=1)

text_frame = Frame(window)
text_frame.grid(column=0, row=2, padx=10, pady=10)
input_text = Text(text_frame, wrap='word', width=38, height=10, font=("Verdana", 12))
input_text.grid(column=0, row=2)
scrollbar = Scrollbar(text_frame, command=input_text.yview)
scrollbar.grid(column=1, row=2, sticky='ns')
input_text.config(yscrollcommand=scrollbar.set)

input_text.bind("<Key>", reset_timer)
input_text.bind("<Button-1>", reset_timer)

button_style = {
    'bg': '#45474B',
    'fg': '#F5F7F8',
    'font': ('Verdana', 12, 'bold'),
    'activebackground': '#379777',
    'activeforeground': '#F4CE14',
    'bd': 0,
    'padx': 5,
    'pady': 0
}

lower_frame = Frame(window, bg="#F5F7F8")
lower_frame.grid(column=0, row=3, pady=10)

time_label = Label(lower_frame, text="Inactivity Time (seconds):", fg="#379777", bg="#F5F7F8", font=("Verdana", 12, "bold"))
time_label.grid(column=0, row=0, padx=5)

time_entry = Entry(lower_frame, width=5, font=("Verdana", 12))
time_entry.grid(column=1, row=0, padx=5)
time_entry.insert(0, "5")

set_time_button = Button(lower_frame, text="Set", command=set_inactivity_time, **button_style)
set_time_button.grid(column=2, row=0, padx=5)

lowest_frame = Frame(window, bg="#F5F7F8")
lowest_frame.grid(column=0, row=4, pady=10)

copy_button = Button(lowest_frame, text="Copy to Clipboard", command=copy_to_clipboard, **button_style)
copy_button.grid(column=0, row=0, padx=5)

save_button = Button(lowest_frame, text="Save to File", command=save_to_file, **button_style)
save_button.grid(column=1, row=0, padx=5)

window.mainloop()