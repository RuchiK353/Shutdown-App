from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="#1F1F1F")  # Dark background for a modern look

# Create a stylish title label
title_label = Label(st, text="System Control Panel", font=("Helvetica", 24, "bold"), fg="#00FFFF", bg="#1F1F1F")
title_label.pack(pady=20)

# Button styling
button_style = {
    "font": ("Helvetica", 16, "bold"),
    "bg": "#333333",  # Dark gray background
    "fg": "#FFFFFF",  # White text
    "activebackground": "#555555",  # Lighter gray when clicked
    "activeforeground": "#00FFFF",  # Cyan text when clicked
    "relief": RAISED,
    "bd": 5,
    "cursor": "hand2"
}

# Creating styled buttons
r_button = Button(st, text="Restart", command=restart, **button_style)
r_button.place(x=150, y=100, height=50, width=200)

rt_button = Button(st, text="Restart Time", command=restart_time, **button_style)
rt_button.place(x=150, y=180, height=50, width=200)

lg_button = Button(st, text="Log-Out", command=logout, **button_style)
lg_button.place(x=150, y=260, height=50, width=200)

st_button = Button(st, text="Shutdown", command=shutdown, **button_style)
st_button.place(x=150, y=340, height=50, width=200)

# Footer
footer_label = Label(st, text="Designed with ❤️ in Python", font=("Helvetica", 10, "italic"), fg="#FFFFFF", bg="#1F1F1F")
footer_label.pack(side=BOTTOM, pady=10)

st.mainloop()