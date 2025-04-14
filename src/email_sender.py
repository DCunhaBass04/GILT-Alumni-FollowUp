import win32com.client as win32
import configparser

def send_email(subject, destination, content):
    # WARNING: This code does not work on a Virtual Environment.
    # We need to get authorization to create a SMTP app with a Microsoft email account.

    olApp = win32.Dispatch('Outlook.Application')

    mail_item = olApp.CreateItem(0)

    config = configparser.ConfigParser()
    config.read('credentials.cfg')

    mail_item.Subject = subject
    mail_item.BodyFormat = 1
    mail_item.Body = content
    mail_item.Sender = config['CREDENTIALS']['email']
    mail_item.To = destination

    mail_item.Save()
    mail_item.Send()
