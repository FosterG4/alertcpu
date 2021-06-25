import smtplib, ssl, psutil

senderEmail = "mail@gmail.com" #put in your own email address
senderPass = "PASSWORDHERE" #Enter your password
receiverEmail = "Receiver@gmail.com" #change this to receiver's email
cc = ['anotherreceive@gmail.com','anotherreceive2@gmail.com']
toaddrs = [receiverEmail] + cc

cpu_use_threshold = 40 #percent after which we want to send the email
interval = 300 #interval in seconds

while True:
    cpu_per_usage = psutil.cpu_percent(interval=interval)


    port=465 #PORT SMTP SSL
    context = ssl.create_default_context()


    #Next, log in to the server
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(senderEmail, senderPass)
        server.ehlo()


        #Message to be sent
        content = "Your CPU usage is more than " + str(cpu_use_threshold) + "%"
        msg = 'Subject: {}\n\n{}'.format("WARNING CPU HIGH", content)

        if (cpu_per_usage > cpu_use_threshold):
            server.sendmail(senderEmail, toaddrs, msg)
