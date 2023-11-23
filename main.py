import cv2
import os
import tkinter as tk
from tkinter import filedialog

# Initialize variables
msg = ""
password = ""
message = ""

# Create dictionary mappings
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# GUI setup
root = tk.Tk()
root.title("Image Encryption/Decryption")

# Encryption Frame
frame_encrypt = tk.Frame(root)
frame_encrypt.pack(pady=10)

label_msg = tk.Label(frame_encrypt, text="Enter secret message:")
label_msg.grid(row=0, column=0)

entry_msg = tk.Entry(frame_encrypt)
entry_msg.grid(row=0, column=1)

label_pass = tk.Label(frame_encrypt, text="Enter a passcode:")
label_pass.grid(row=1, column=0)

entry_pass = tk.Entry(frame_encrypt, show="*")
entry_pass.grid(row=1, column=1)

# Encryption button
button_encrypt = tk.Button(frame_encrypt, text="Encrypt Image", command=lambda: encrypt_image())
button_encrypt.grid(row=2, columnspan=2)

# Decryption Frame
frame_decrypt = tk.Frame(root)
frame_decrypt.pack(pady=10)

label_pass_decrypt = tk.Label(frame_decrypt, text="Enter passcode for Decryption:")
label_pass_decrypt.grid(row=0, column=0)

entry_pass_decrypt = tk.Entry(frame_decrypt, show="*")
entry_pass_decrypt.grid(row=0, column=1)

# Decryption button
button_decrypt = tk.Button(frame_decrypt, text="Decrypt Message", command=lambda: decrypt_message())
button_decrypt.grid(row=1, columnspan=2)

# Result label
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Encryption function
def encrypt_image():
    global img, msg, password

    img_path = filedialog.askopenfilename(title="Select Image")
    img = cv2.imread(img_path)

    msg = entry_msg.get()
    password = entry_pass.get()

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")

# Decryption function
def decrypt_message():
    global img, msg, password, message

    pas = entry_pass_decrypt.get()

    if password == pas:
        message = ""
        n = 0
        m = 0
        z = 0

        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3

        label_result.config(text="Decrypted message: " + message)
    else:
        label_result.config(text="YOU ARE NOT AUTHORIZED")

root.mainloop()
