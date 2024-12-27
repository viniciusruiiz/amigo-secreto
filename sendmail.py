import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import sorteio

load_dotenv()

#config server
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))
email_user = os.getenv("SMTP_MAIL")
email_password = os.getenv("SMTP_PASSWORD")

subject = "AMIGO SECRETO CRISTINHOS TESTE 2"

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_user, email_password)
    
    sorteios = sorteio.sortear()
    for escolha in sorteios:
      with open("email_template.html", "r", encoding="utf-8") as file:
        html_template = file.read()

      html_body = html_template.replace("{{NOME}}", escolha.pessoa).replace("{{ESCOLHIDO}}", escolha.escolhido)

      message = MIMEMultipart("alternative")
      message["From"] = email_user
      message["To"] = escolha.email
      message["Subject"] = subject
      message.attach(MIMEText(html_body, "html"))

      server.sendmail(email_user, escolha.email, message.as_string())

    print("E-mails enviados com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o e-mail: {e}")
finally:
    server.quit()