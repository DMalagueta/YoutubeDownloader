from sys import argv
from pytube import YouTube


# Store youtube link
link = input("Youtube link: ")

# Change download path, default is same folder as python file
download_path = "" #"/Users/mrmal/Desktop/"

yt = YouTube(link)

print(f"Title: {yt.title}")

yd = yt.streams.get_highest_resolution()


# Download Bar
download_size = yd.filesize
block_size = 1024  
downloaded = 0

while downloaded < download_size:
    progress = min(int(downloaded / download_size * 100), 100)
    bar = "[" + "#" * (progress // 10) + " " * ((100 - progress) // 10) + "]"
    print(f"\rDownloading: {bar} {progress}%", end="")
    downloaded += block_size

yd.download(download_path)



print("\nDownload complete!")



