
from captcha.image import ImageCaptcha
# Talvez seja necessário baixa a biblioteca captcha

imagem = ImageCaptcha() # Nessa função você pode personalizar a imagem

texto = input("\nDigite o texto para a imagem: ")

imagem.write(texto, 'captcha.png')