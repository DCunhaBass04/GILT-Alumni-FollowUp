import pandas as pd
import configparser
from email_sender import send_email

config = configparser.ConfigParser()
config.read('conf.cfg')
pathToFile = config['START']['excel_output_path'] + '/' + config['START']['excel_file_name']

xls = pd.ExcelFile(pathToFile)
lista_autorizados = (pd.read_excel(xls, 'Emails_Autorizados').dropna())['Email'].tolist()
#print(lista_autorizados['Email'].tolist())
respostas = pd.read_excel(xls, 'Respostas')
#print(respostas)

for aut in lista_autorizados:
    send_email("Teste", aut, "Isto é um teste")
