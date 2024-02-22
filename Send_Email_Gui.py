import smtplib, ssl
import tkinter as tk
from tkinter import messagebox
from email.message import EmailMessage
import configparser

# Creo EmailSender class
class EmailSender:
    @staticmethod
    def send_email():
        # Config file
        config = configparser.ConfigParser()
        config.read('config.ini')
        email_sender = config['Email']['email_sender']
        email_password = config['Email']['email_password']
        email_receiver = receiver_entry.get()
        email_subject = subject_entry.get()
        email_body = body_entry.get('1.0', 'end-1c')
        
        # Creo email message
        msg = EmailMessage()
        msg['Subject'] = email_subject
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg.set_content(email_body)
        
        # Invio email
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login(email_sender, email_password)
                server.sendmail(email_sender, email_receiver, msg.as_string())
            messagebox.showinfo('Success', 'Email sent successfully!')
        except Exception as e:
            messagebox.showerror('Error', f'Error sending email: {e}')

# Creo main window
root = tk.Tk()
root.title('Email Sender')

# Creo labels e entry fields per email details
#tk.Label(root, text='Email Sender:').grid(row=0, column=0)
#sender_entry = tk.Entry(root, width=30)
#sender_entry.grid(row=0, column=1)
#tk.Label(root, text='Password:').grid(row=1, column=0)
#password_entry = tk.Entry(root, width=30, show='*')
#password_entry.grid(row=1, column=1)
tk.Label(root, text='Email Receiver:').grid(row=2, column=0)
receiver_entry = tk.Entry(root, width=30)
receiver_entry.grid(row=2, column=1)
tk.Label(root, text='Subject:').grid(row=3, column=0)
subject_entry = tk.Entry(root, width=30)
subject_entry.grid(row=3, column=1)
tk.Label(root, text='Body:').grid(row=4, column=0)
body_entry = tk.Text(root, width=30, height=10)
body_entry.grid(row=4, column=1)

# Creo button to send the email
send_button = tk.Button(root, text='Send Email', command=EmailSender.send_email)
send_button.grid(row=5, column=1)

# Run the main loop
root.mainloop()