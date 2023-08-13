from tkinter import filedialog
import pygame
from tkinter import *
root = Tk()
class MusicPlayer:
 def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("MusicPlayer")
    # Window Geometry
    self.root.geometry("800x400")
    self.root.iconbitmap("img.ico")
    # Initiating Pygame
    pygame.init()
    # Initiating Pygame Mixer
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()
    # Declaring Status Variable
    self.status = StringVar()

    # Creating the Track Frames for Song label & status label
    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=800,height=100,anchor=NW)
    # Inserting Song Track Label
    songtrack = Label(trackframe,textvariable=self.track,width=25,font=("times new roman",24,"bold"),bg="black",fg="white",anchor="w").grid(row=0,column=0,padx=1,pady=5)
    # Inserting Status Label
    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="black",fg="white").grid(row=0,column=1,padx=10,pady=5)

    # Creating Button Frame
    buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman",15,"bold"), bg="white", fg="black", bd=5, relief=GROOVE,labelanchor="n")
    buttonframe.place(x=0,y=400,width=800,height=100,anchor=SW)
    # Inserting Play Button
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=10,height=1,font=("times new roman",11),fg="black", bg="silver").grid(row=0,column=0,padx=12,pady=15)
    # Inserting Pause Button
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",11),fg="black", bg="silver").grid(row=0,column=1,padx=12,pady=15)
    # Inserting Unpause Button
    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",11),fg="black", bg="silver").grid(row=0,column=2,padx=12,pady=15)
    # Inserting Stop Button
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=10,height=1,font=("times new roman",11),fg="black", bg="silver").grid(row=0,column=3,padx=12,pady=15)

    playbtn = Button(buttonframe, text="ADD", command=self.add, width=10, height=1,font=("times new roman", 11),fg="black", bg="silver").grid(row=0, column=4, padx=12,pady=15)

    playbtn = Button(buttonframe, text="NEXT", command=self.next, width=10, height=1,font=("times new roman", 11),fg="black", bg="silver").grid(row=0, column=5, padx=12,pady=15)

    playbtn = Button(buttonframe, text="PREVIOUS", command=self.pre, width=10, height=1,font=("times new roman", 11),fg="black", bg="silver").grid(row=0, column=6, padx=12,pady=15)
    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",18,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=0,y=200,width=800,height=200,anchor=W)
    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="black",selectmode=SINGLE,font=("times new roman",15,"bold"),bg="silver",fg="black",bd=5,relief=GROOVE)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
 def playsong(self):
     if self.playlist:
        self.playlist.selection_set(0, last=None)
        self.status.set("-playing")
        song=self.playlist.get(0)
        self.track.set(song)
        song=f"C:/Users/Asus/Downloads/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

 def add(self):
     songs = filedialog.askopenfilenames(initialdir="music/", filetypes=(("mp3 Files", "*.mp3"),))
     playlist1 = []
     for song in songs:
         song = song.replace("C:/Users/Asus/Downloads/Music/", "")
         song = song.replace(".mp3", "")
         playlist1.append(song)
     self.playlist.delete(0, END)
     for song in playlist1:
         self.playlist.insert(END, song)
 def next(self):
     nextone = self.playlist.curselection()
     if nextone[0]==self.playlist.size()-1:
         self.playlist.select_clear(0, END)
         self.playlist.selection_set(0, last=None)
         song = self.playlist.get(0)
         self.track.set(song)
         song = f"C:/Users/Asus/Downloads/Music/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play(loops=0)
     else:
         nextone=nextone[0]+1
         song=self.playlist.get(nextone)
         self.track.set(song)
         song = f"C:/Users/Asus/Downloads/Music/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play(loops=0)
         self.playlist.select_clear(0,END)
         self.playlist.activate(nextone)
         self.playlist.selection_set(nextone, last=None)
 def pre(self):
     nextone = self.playlist.curselection()
     if nextone[0]==0:
         self.playlist.select_clear(0, END)
         self.playlist.selection_set(self.playlist.size()-1, last=None)
         song = self.playlist.get(self.playlist.size()-1)
         self.track.set(song)
         song = f"C:/Users/Asus/Downloads/Music/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play(loops=0)
     else:
         nextone = nextone[0] - 1
         song = self.playlist.get(nextone)
         self.track.set(song)
         song = f"C:/Users/Asus/Downloads/Music/{song}.mp3"
         pygame.mixer.music.load(song)
         pygame.mixer.music.play(loops=0)
         self.playlist.select_clear(0, END)
         self.playlist.activate(nextone)
         self.playlist.selection_set(nextone, last=None)
 def stopsong(self):
    # Displaying Status
    self.status.set("-Stopped")
    # Stopped Song
    pygame.mixer.music.stop()
    self.playlist.select_clear(ACTIVE)
 def pausesong(self):
    # Displaying Status
    self.status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()
 def unpausesong(self):
    # It will Display the  Status
    self.status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()


if __name__ == "__main__":
    app = MusicPlayer(root)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    root.mainloop()