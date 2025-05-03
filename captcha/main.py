
from captcha.image import ImageCaptcha
# Talvez seja necessário baixa a biblioteca captcha

imagem = ImageCaptcha()

data = imagem.generate('Python')
imagem.write('Python', 'captcha.png')