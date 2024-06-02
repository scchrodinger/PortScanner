import socket
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry(f"{500}x{300}")
app.title("Port Scanner")

set_appearance_mode("Dark")
set_default_color_theme("dark-blue")

img = Image.open("images/portscanner.png")

def portscanner():
    sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = ip_input.get()
    edp = 0
    ebp = int(port_number_input.get())

    for port in range(edp,ebp+1):
        try:
            sc.connect((ip.port))
            output.configure(text=f"{port}th port is open")
            exit(0)
        except:
            pass
    output.configure(text="All ports are closed")

def clean():
    ip_input.delete(0, "end")
    port_number_input.delete(0, "end")
    output.configure(text="You haven't scanned.")

frame = CTkFrame(master=app)
frame.pack(pady=20, padx=60, expand=True, fill="both")

image = CTkImage(light_image=Image.open("images/portscanner.png"), dark_image=Image.open("images/portscanner.png"), size=(100,100))
logo = CTkLabel(master=frame, image=image, text="")
logo.place(relx=0.15, rely=0.015)

ip_input = CTkEntry(master=frame, corner_radius=32, placeholder_text="IP")
ip_input.place(relx=0.1, rely=0.4)

port_number_input = CTkEntry(master=frame, corner_radius=32, placeholder_text="Highest Port Value")
port_number_input.place(relx=0.1, rely=0.6)

start_button = CTkButton(master=frame, corner_radius=32, command=portscanner, text="Scan", fg_color="#6a588a", hover_color="#907db3")
start_button.place(relx=0.55, rely=0.4)

clear_button = CTkButton(master=frame, corner_radius=32, command=clean, text="Clean", fg_color="#6a588a", hover_color="#907db3")
clear_button.place(relx=0.55, rely=0.6)

output = CTkLabel(master=frame, text="You haven't scanned.", font=("Roboto", 16))
output.place(relx=0.55, rely=0.2)

app.mainloop()
