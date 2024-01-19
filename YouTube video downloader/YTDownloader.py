from pytube import YouTube
from tkinter import *
from PIL import ImageTk, Image
import urllib.request
import io
from random import *

def downloading():  # accepting the video download
    global yt, resolution
    i = randint(1,1000000)  # adding a random number from 1 - 1000000 to avoid overriding other mp4 files with the same name
    nazwa = yt.title+str(i)+".mp4"  # you can change ".mp4" to ".mp3" if you want  

    if (resolution == "max"):
       video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.filter(res=resolution).first() 

    video.download("downloaded videos", filename=nazwa)
    root2.withdraw()
    DownloadingProgress.set("Downloaded successfully")
    progressLabel.place(x=100,y=300)
    resolution = "360p"
    res2Btn.config(bg="white")
    res1Btn.config(bg="white")

def display_thumbnail(url):
    global raw_data,photo, imglabel
    u = urllib.request.urlopen(url)
    raw_data = u.read()
    u.close()
    image = Image.open(io.BytesIO(raw_data))
    image = image.resize((320,180))
    photo = ImageTk.PhotoImage(image)
    imglabel.config(image=photo)

def downloadButton():  # starting the download
    global downloadEntry, DownloadingProgress,yt,downask
    try:
        yt = YouTube(downloadEntry.get())
        progressLabel.place(x=110,y=300)
        progvid = "Downloading "+yt.title
        DownloadingProgress.set(progvid)
        downloadEntry.delete(0,'end')

        root2.deiconify()
        progvid2 = "Do you want to download "+yt.title
        downask.set(progvid2)
        url = yt.thumbnail_url
        display_thumbnail(url)

    except:
        DownloadingProgress.set("Paste a valid link")
        progressLabel.place(x=145,y=300)

def disable_event():  # disabling the "X" button in download popup, not doing this caused issues
   pass

def close_win():  # function for the cancel button in download popup
   global DownloadingProgress
   root2.withdraw()
   DownloadingProgress.set("Downloading cancelled")

def SetRes(resolutionget):  # changing the resolution (only 2 options right now)
    global resolution
    if (resolutionget == "480p"):
        resolution = "480p"
        res2Btn.config(bg="gray") 
        res1Btn.config(bg="white")
    elif (resolutionget == "max"):
        resolution ="max"
        res1Btn.config(bg="gray")
        res2Btn.config(bg="white")

# creating and setting up windows
        
root = Tk()  # main window
root.geometry("500x450")
root.resizable("False","False")
root.title("YT Downloader")
root.config(background="#393d47")

root2 = Toplevel()  # download popup
root2.geometry("550x450+100+50")
root2.resizable("False","False")
root2.title("download?")
root2.config(background="#393d47")
root2.withdraw()
root2.protocol("WM_DELETE_WINDOW", disable_event)

DownloadingProgress = StringVar()  # stringvar showing the state of downloading (click accept to start/downloading/cancelled)
DownloadingProgress.set("Click Accept to download")
downask = StringVar()  # var for asking about downloading in the popup
resolution = "360p"  # default video resolution

# main window graphics
textLabel = Label(root, text="Paste a YouTube link",font=("Comic Sans MS",20,"bold","italic"),width=30,height=5,bg="#393d47")
textLabel.place(x=-5,y=0)

progressLabel = Label(root,textvariable=DownloadingProgress,font=("Comic Sans MS",20),justify=CENTER,wraplength=350,bg="#393d47",fg="white")
progressLabel.place(x=90,y=300)

downloadask = Label(root2,textvariable=downask,font=("Comic Sans MS",20),wraplength=350,bg="#393d47")
downloadask.pack()

downloadEntry = Entry(root,width=41,background="lightgray",font=("Comic Sans MS",11))
downloadEntry.place(x=18,y=170)

downloadBtn = Button(root,text="Download",font=("Comic Sans MS", 10),width=10,command=lambda:downloadButton())
downloadBtn.place(x=390,y=165)

# popup graphics
imglabel = Label(root2)
imglabel.place(x=30,y=100)

AcceptButton = Button(root2,text="Download video",font=("Comic Sans MS", 15),width=15,command=lambda:downloading())
AcceptButton.place(y=350,x=105)

CloseButton = Button(root2,text="Cancel",font=("Comic Sans MS", 12),width=10,command=lambda:close_win())
CloseButton.place(y=420)

res1Btn = Button(root2, text="Highest \nresolution", font=("Comic Sans MS", 14, "bold", 'italic'),width=13 ,command=lambda:SetRes("max"))
res1Btn.place(x=370,y=105)

res2Btn = Button(root2, text="480p", font=("Comic Sans MS", 16, "bold", 'italic'),width=12,height=2, command=lambda:SetRes("480p"))
res2Btn.place(x=370,y=200)

root.mainloop()