
import pandas as pd
# Talvez seja necessário instalar a biblioteca pandas

xlsx = pd.read_excel('clientes.xlsx')

# Emails dos clientes com menos de 40 anos
filtro = xlsx['Idade'] < 40
filtrado = xlsx[filtro]

emails = filtrado['Email']

with open('emails.txt', 'w') as f:
    for email in emails:
        f.write(f'{email}\n')

print("Emails extraídos com sucesso!")