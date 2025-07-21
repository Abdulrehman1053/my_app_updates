import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CustomTkinter Test App")
app.attributes('-fullscreen', True)

def toggle_fullscreen(event=None):
    is_fullscreen = app.attributes("-fullscreen")
    app.attributes("-fullscreen", not is_fullscreen)
    if is_fullscreen:
        app.geometry("400x200")

app.bind("<Escape>", toggle_fullscreen)

label = ctk.CTkLabel(app, text="Hello, this is a test app!\n(Press ESC to toggle fullscreen)", font=("Arial", 18))
label.pack(pady=20)

button = ctk.CTkButton(app, text="Click Me", command=lambda: label.configure(text="Button Clicked!"))
button.pack(pady=10)

app.mainloop()
