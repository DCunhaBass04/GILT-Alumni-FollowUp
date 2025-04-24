import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('conf.cfg')
path = config['START']['excel_file_path']

dados = pd.read_excel(path, 'Respostas')
print(dados)