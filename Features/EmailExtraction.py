import datetime
import imaplib
import email
import os
import yaml
from email.header import decode_header
from Body.Speak import Speak
from Body.Listen import MicExecution

with open("E:\\PersonalAI(Assistant)\\Data\\gmailApi.yml") as f:
    content = f.read()

my_credential = yaml.load(content, Loader=yaml.FullLoader)

user, password = my_credential["user"], my_credential["password"]

# connection with gmail using ssl
imap_url = "imap.gmail.com"

my_mail = imaplib.IMAP4_SSL(imap_url)

# login using your credential
my_mail.login(user,password)

# select inbox to fetch message
# res, data = my_mail.select('"[Gmail]/Sent Mail"')  for recent sent message by me

status, messages = my_mail.select("INBOX")
N = 5
messages = int(messages[0])


def EmailExtract():
    Speak("Fetching recent emails sir!")
    for i in range(messages, messages - N, -1):
        # fetch the email message by ID
        res, msg = my_mail.fetch(str(i), "(RFC822)")
        FileLog = open("E:\\PersonalAI(Assistant)\\Database\\Mails.txt", "r")
        chat_log_template = FileLog.read()
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                date = decode_header(msg["Date"])[0][0]
                sender = decode_header(msg["from"])[0][0]
                subject = decode_header(msg["subject"])[0][0]
                print(date,sender,subject)
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime(" %y-%m-%d %H:%M:%S")
                chat_log_template_update = chat_log_template + f"\n Date : {now} \n FROM : {sender} \n SUBJECT : {subject} \n"
                FileLog = open("E:\\PersonalAI(Assistant)\\Database\\Mails.txt", "w")
                FileLog.write(chat_log_template_update)
                FileLog.close()


    Speak("You have some Emails, Do you want to see!")
    query = MicExecution()
    if "display" in query or "yes" in query or "haa" in query:
        os.startfile("E:\\PersonalAI(Assistant)\\Database\\Mails.txt")
    else:
        Speak("No Problem sir!")

# for num in mail_id_list:
#     typ,data= my_mail.fetch(num,'(RFC822)')
#     msgs.append(data)
#
# for msgs in msgs[::-1]:
#     for response_part in msgs:
#         if type(response_part) is tuple:
#             my_msg = email.message_from_bytes((response_part[1]))
#             print("-------------------------------------------")
#             print("subject : ", my_msg['subject'])
#             print("from : ",my_msg['from'])
#             print("body : ")
#             for part in my_msg.walk():
#                 print(part.get_content_type())
#                 if part.get_content_type() == 'text/plain':
#                     print(part.get_payload())

# EmailExtract()
