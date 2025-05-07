
import pywhatkit
# Precisa baixar a biblioteca pywhatkit

numero = '+5514999999999' # Número de telefone da pessoa
mensagem = 'Teste' # Mensagem

# E precisa estar com o Whatsapp Web conectado!
pywhatkit.sendwhatmsg_instantly(numero, mensagem)

print("Mensagem enviada!")

# Você pode também enviar com um horário definido:
# horas = 00
# minutos = 00
# pywhatkit.sendwhatmsg(numero, mensagem, horas, minutos)