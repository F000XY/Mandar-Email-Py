from email.message import EmailMessage 
import ssl
import smtplib #SMTP permite enviar emails pela net, fazendo a conexão com o servidor SMTP
# do gmail usando o ssl

meu_mail = "" #seu email
senha_gerada = "" #sua senha aqui
destinatario = "" #email do destinatario
assunto = "teste"
body = "opa tudo bom"

em = EmailMessage()
em['From'] = meu_mail
em['To'] = destinatario
em['Subject'] = assunto
em.set_content(body)

context = ssl.create_default_context() #contexto ssl seguro

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_mail, senha_gerada) 
    smtp.sendmail(meu_mail, destinatario, em.as_string())
    
 