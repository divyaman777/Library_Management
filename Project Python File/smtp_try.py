import random
import smtplib, ssl
def otp_fire(mail):
    otp=""
    for i in range(4):
        a=random.randrange(0,10)
        otp=otp+str(a)
    port=587
    msg1="""hello
    your OTP is"""+otp
    cont=ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.ehlo()
        server.starttls(context=cont)
        server.ehlo()
        server.login("Email","password")
        server.sendmail("Email",mail,msg1)
    return(otp)
