import smtplib
import csv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# y='Email.csv'
# import csv
# with open(y, 'w', newline='') as file:
#     z = csv.writer(file)
#     z.writerow(['paEfafysav@gmail.com'])
#     z.writerow(['SNjqsnxjx@gmail.com'])
#     z.writerow(['ax_aa2000@gmail.com'])
#     z.writerow(['mxaaxx2000@gmail.com'])

from_add="abc@gmail.com"
to_add=[]
with open('Email.csv','rt') as file:
    csv_rows=csv.reader(file)
    for row in csv_rows:
        for i in row:
            to_add.append(i)
print(to_add)
msg=MIMEMultipart()
msg['From']=from_add
msg['To']=" ,".join(to_add)
msg['subject']="sended a file"

body="hello im sending a file"
msg.attach(MIMEText(body,'plain'))
img_data=open('image.png','rb').read()
msg.attach(MIMEImage(img_data,name=os.path.basename('image.png')))

email='your_email_address'
password='your_email_password'

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_add,to_add,text)
mail.quit()
