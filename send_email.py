import smtplib, ssl


def gmailer(message):
    host = "smtp.gmail.com"
    port = 465
    username = "hipython88@gmail.com"
    password = "veepxzrqwwornetv"
    receiver = "hipython88@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)