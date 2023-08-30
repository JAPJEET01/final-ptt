import socket
import tkinter as tk

server_ip = '192.168.29.183'  # Raspberry Pi's IP address
server_port = 12346

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def key_pressed(event):
    if event.keysym == 'Control_L':
        client_socket.sendto(b'high', (server_ip, server_port))

def key_released(event):
    if event.keysym == 'Control_L':
        client_socket.sendto(b'low', (server_ip, server_port))

root = tk.Tk()
root.bind('<KeyPress>', key_pressed)
root.bind('<KeyRelease>', key_released)
root.mainloop()
