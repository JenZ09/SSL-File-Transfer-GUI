# SSL receiver
import socket, ssl, tkinter as tk
from tkinter import filedialog
import threading

def handle_control_channel(output_text):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH) #creating ssl context
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem") #loading certificate and key
    control_sock = socket.socket()
    control_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    control_sock.bind(('', 4442)) #the recceiver control socket
    control_sock.listen(1)
    client, addr = control_sock.accept()
    with context.wrap_socket(client, server_side=True) as ssock: #wrapping socket with ssl
        output_text.insert(tk.END, f"Control channel connected from {addr}\n")
        while True:
            data = ssock.recv(1024)  
            if not data:
                break
            output_text.insert(tk.END, f"[Control] {data.decode()}\n")

def receive_file_ssl(save_path, output_text):
    try:
        threading.Thread(target=handle_control_channel, args=(output_text,), daemon=True).start()
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile="cert.pem", keyfile="key.pem") #loading the certificate and key
        data_sock = socket.socket()
        data_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        data_sock.bind(('', 4443)) #data channel
        data_sock.listen(1)

        client_socket, fromaddr = data_sock.accept()  
        output_text.insert(tk.END, f"Data connection from {fromaddr}\n")
        with context.wrap_socket(client_socket, server_side=True) as ssock:
            with open(save_path, "wb") as f:
                while True:
                    data = ssock.recv(4096)  #receiving data
                    if not data:
                        break
                    f.write(data) #writes data after receiving

        output_text.insert(tk.END, f"File saved as {save_path}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")

def start_receiver_ssl():
    filename = filedialog.asksaveasfilename(title="Save File As")
    if filename:
        threading.Thread(target=receive_file_ssl, args=(filename, output_text)).start()
 
root = tk.Tk() #tkinter section
root.title("SSL File Receiver")
tk.Button(root, text="Start SSL Receiving", command=start_receiver_ssl, bg="#4CAF50", fg="white").pack(pady=10)
output_text = tk.Text(root, height=15, width=60)
output_text.pack()
root.mainloop()