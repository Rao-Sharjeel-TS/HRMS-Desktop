import customtkinter
from apps_and_urls_tracker import focus_tracker
from threading import Thread
import time
import requests
from start_files import start_both
from getOpenTabs import *

LOGIN_ENDPOINT = 'https://stagehrms.transemr.com/api/login'
login_status = ""

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("light")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

global app


app = customtkinter.CTk()
app.geometry("400x300")
app.title("Login")


def check_user(user, pas):
    r = requests.post(LOGIN_ENDPOINT, json={'username': user, 'password': pas})
    if r.status_code == 200:
        try:
            return r.json()['token'], r.json()
        except:
            return None, r.json()
    return None, None


def login_button_callback():
    print("Login Button click")
    username = str(username_entry.get())
    password = str(password_entry.get())

    token, json = check_user(username, password)
    if token:
        login_status = "Login Successful"
        status_label.configure(text=login_status)
        # time.sleep(1)
        app.destroy()

        start_both(json['data']['name'], json['data']['username'])

    else:
        login_status = "Login Unsuccessful"
        status_label.configure(text=login_status)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

heading = customtkinter.CTkLabel(
    master=frame_1, text="HRMS", justify=customtkinter.LEFT, font=('Helvetica bold', 20))
heading.pack(pady=10, padx=10)

username_entry = customtkinter.CTkEntry(
    master=frame_1, placeholder_text="Username")
username_entry.pack(pady=10, padx=10)

password_entry = customtkinter.CTkEntry(
    master=frame_1, placeholder_text="Password", show="*")
password_entry.pack(pady=10, padx=10)

login_button = customtkinter.CTkButton(
    master=frame_1, command=login_button_callback, text="Login", fg_color='#800080', hover_color='#900090')
login_button.pack(pady=10, padx=10)

status_label = customtkinter.CTkLabel(
    master=frame_1, text=login_status, justify=customtkinter.CENTER, font=('Helvetica bold', 18))
status_label.pack(pady=10, padx=10)

app.mainloop()
