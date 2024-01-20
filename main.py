from pytube import YouTube
link = input("Enter url of video : ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
if stream.download():
    print("The video has been downloaded")
else:
    print("The video hasn't been downloaded")