#sender
import socket, ssl, tkinter as tk
from tkinter import filedialog, messagebox
import threading

#defines the function to send file over ssl
def send_file_ssl(file_path, receiver_ip, output_text):
    try:
        output_text.insert(tk.END, f"📡 Connecting to {receiver_ip}...\n")

        #create ssl context without certificate verification
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        #1. control channel setup
        with socket.create_connection((receiver_ip, 4442)) as sock_ctrl:
            with context.wrap_socket(sock_ctrl, server_hostname=receiver_ip) as ssock_ctrl:
                ssock_ctrl.sendall(b"Starting file transfer...")

                #2. data channel setup
                with socket.create_connection((receiver_ip, 4443)) as sock_data:
                    with context.wrap_socket(sock_data, server_hostname=receiver_ip) as ssock_data:
                        output_text.insert(tk.END, "SSL connection established.\n")
                        with open(file_path, "rb") as f:
                            while chunk := f.read(4096):
                                ssock_data.sendall(chunk)

                ssock_ctrl.sendall(b"Transfer complete.")

        output_text.insert(tk.END, f"File sent: {file_path}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")

#starts the sender function in a new thread
def start_sender_ssl():
    file_path = filedialog.askopenfilename(title="Select File to Send")
    if not file_path:
        return
    receiver_ip = receiver_ip_entry.get()
    if not receiver_ip:
        messagebox.showerror("Error", "Enter receiver IP address.")
        return
    threading.Thread(target=send_file_ssl, args=(file_path, receiver_ip, output_text)).start()

#gui setup
root = tk.Tk()
root.title("SSL File Sender")
tk.Label(root, text="Receiver IP:").pack()
receiver_ip_entry = tk.Entry(root, width=30)
receiver_ip_entry.pack()
tk.Button(root, text="Send File Securely", command=start_sender_ssl, bg="#2196F3", fg="white").pack(pady=10)
output_text = tk.Text(root, height=15, width=60)
output_text.pack()
root.mainloop()
