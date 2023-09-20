import customtkinter
from threading import Thread
import time
import requests
# from start_files import terminate_processes

def dashboard(name = "name", username = "username"):
    print("THIS IS DASHBOARD FILE")
    print("THIS IS DASHBOARD FILE")
    print("THIS IS DASHBOARD FILE")
    print("THIS IS DASHBOARD FILE")
    print("THIS IS DASHBOARD FILE")
    customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    t = time.time()
    app = customtkinter.CTk()
    app.geometry("500x500")
    app.title("HRMS Dashboard")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=10, fill="both", expand=True)

    heading = customtkinter.CTkLabel(master=frame_1, text="HRMS Desktop", justify=customtkinter.LEFT, font=('Helvetica bold',40))
    heading.pack(pady=10, padx=10)

    name_title = customtkinter.CTkLabel(master=frame_1, text="Name", justify=customtkinter.LEFT, font=('Helvetica bold',20))
    name_title.pack(pady=0, padx=10)

    name_text = customtkinter.CTkLabel(master=frame_1, text=name, justify=customtkinter.LEFT, font=('Helvetica bold',40))
    name_text.pack(pady=10, padx=10)

    username_title = customtkinter.CTkLabel(master=frame_1, text="Username", justify=customtkinter.LEFT, font=('Helvetica bold',20))
    username_title.pack(pady=0, padx=10)

    username_text = customtkinter.CTkLabel(master=frame_1, text=username, justify=customtkinter.LEFT, font=('Helvetica bold',30))
    username_text.pack(pady=10, padx=10)

    time_title = customtkinter.CTkLabel(master=frame_1, text="Status", justify=customtkinter.LEFT, font=('Helvetica bold',20))
    time_title.pack(pady=0, padx=10)

    time_text = customtkinter.CTkLabel(master=frame_1, text="working", justify=customtkinter.LEFT, font=('Helvetica bold',30))
    time_text.pack(pady=10, padx=10)

    end_button = customtkinter.CTkButton(master=frame_1, text="End Work", fg_color='#800080', hover_color='#900090')
    end_button.pack(pady=10, padx=10)

    # time_text.configure(text=(time.time() - t))
    app.mainloop()

# dashboard("Rao", "rao.sharjeel")

