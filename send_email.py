import smtplib, ssl, json


def send_email(message):

    with open("config.json") as f:
        config = json.load(f)

    host = "smtp.gmail.com"
    port = 465

    username = config["email"] # Add your email to a config.json file: "email": email@email.com
    password = config["email_password"] # Add your gmail app password to a config.json file: "email_password": *Password*

    receiver = config["email"]
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    send_email("Hello, how are you?")
