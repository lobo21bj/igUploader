#import PySimpleGUI
import os
import customtkinter as ctk
import uploader
import browser

def post(entry1, entry2, filepath, button_txt):
    username = entry1.get()
    password = entry2.get()
    filepath = os.environ['FILE_IMG']
    filepath = filepath.replace("/","\\")
    text = button_txt.get()
    print("Usuario Ingresado: " + username + " Contraseña: " + password)
    browser.post_to_instagram(uploader.current_path, username, password, filepath, text)
    exit

def selectfile():
        file = ctk.filedialog.askopenfilename()
        os.environ['FILE_IMG'] = file

def saveCredentials():
    print("Saving credentials")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue") #dark-blue, blue or green

    root = ctk.CTk()
    root.geometry("500x350")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Login System")
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)
    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    filepath=""
    button_file = ctk.CTkButton(master=frame, text="Photo", command=lambda: selectfile())
    button_file.pack(pady=12, padx=10)

    text=""
    button_txt = ctk.CTkEntry(master=frame, placeholder_text="Post text")
    button_txt.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text="Post", command=lambda: post(entry1, entry2, button_file, button_txt))                     
    button.pack(pady=12, padx=10)

    root.mainloop()
