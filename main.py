import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from datetime import datetime
import os

# Email configuration
sender_email = os.environ.get('my_email')  # Your Gmail address
sender_password = os.environ.get('password')  # Your Gmail password
receiver_email = os.environ.get('receiver')  # We add variable that will get hold of the receiver email
email_subject = "Daily Tasks Reminder"

# Some daily tasks that you can use for example
daily_tasks = [
    "Task 1: Go to school",
    "Task 3: Read a chapter of a book",
]


# Function that will send the email to the receiver_email you choose
def send_email():
    try:
        # Set up your email server. I am using gmail as example here.
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email 
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = email_subject

        # Construct the email message body from the list of tasks called daily_tasks
        email_message = "\n".join(daily_tasks)
        msg.attach(MIMEText(email_message, "plain"))

        # Send the email to the receiver_email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the email server
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        # This will be printed if there is error
        print("Error sending email:", str(e))


# Set the desired time to send the email
desired_time = "set the time you want to receive your email with tasks in this format - 00:00"

while True:
    # Get the current time using datetime.now() and then style it in 00:00 format
    current_time = datetime.now().strftime("%H:%M")

    # Check if the current time matches the desired time
    if current_time == desired_time:
        send_email()  # Send the email to receiver email
        break  # Exit the loop after sending the email

    # Sleep for 60 seconds before checking the time again 
    time.sleep(60)
