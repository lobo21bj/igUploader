import os
import customtkinter as ctk
import emoji
import browser
import misc

filename = os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0]
current_path = os.path.dirname(os.path.abspath(__file__))

def post(entry1, entry2, filepath, button_txt, filename, logger, root):
    username = entry1.get()
    #username = 'seib.diego@gmail.com'
    password = entry2.get()
    #password = 'Mentor1234'
    filepath = os.environ['FILE_IMG']
    filepath = filepath.replace("/","\\")
    text = button_txt.get()
    logger.info("With the data entered hitting Instagram.com")
    browser.post_to_instagram(browser.current_path, username, password, filepath, text, filename, logger, root)
    exit

def selectfile():
        file = ctk.filedialog.askopenfilename()
        os.environ['FILE_IMG'] = file

def saveCredentials():
    print("Saving credentials")

if __name__ == "__main__":
    logger = misc.setupLogfile(filename, current_path)
    logger.info("##### Initiliazing " + filename + " #####")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue") #dark-blue, blue or green

    root = ctk.CTk()
    root.title("Instagram Uploader")
    icon_title_img=current_path+"\\asset\\icon.ico"
    root.iconbitmap(icon_title_img)
    root.geometry("600x400")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Instagram Uploader")
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)
    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button_txt = ctk.CTkEntry(master=frame, placeholder_text="Post text", width=250, height=30, justify='center')
    button_txt.pack(pady=12, padx=10)

    button_file = ctk.CTkButton(master=frame, text="Photo", command=lambda: selectfile())
    button_file.pack(pady=12, padx=10)
    logger.info("Media retreived")

    button = ctk.CTkButton(master=frame, text="Post", command=lambda: post(entry1, entry2, button_file, button_txt, filename, logger, root))                     
    button.pack(pady=12, padx=10)

    root.mainloop()
