from pytube import YouTube

link=input("inserte el enlace del video: ")
yt=YouTube(link)
print(yt.title)
stream=yt.streams.first().download()