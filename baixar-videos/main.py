
from pytubefix import YouTube
# Caso não tenha, é preciso baixar a biblioteca pytubefix

yt = YouTube(input("Cole aqui a url: "))

print(yt.title)
print(yt.thumbnail_url)

stream = yt.streams.get_highest_resolution()

stream.download()