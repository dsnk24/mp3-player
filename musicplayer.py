from tkinter import *
import pygame
import os

root = Tk()

class MusicPlayer:
	def __init__(self, root):
		self.root = root
		self.root.title("Music Player")
		self.root.geometry("1000x200+200+200")
		pygame.init()
		pygame.mixer.init()
		self.track = StringVar()
		self.status = StringVar()
		
		trackframe = LabelFrame(self.root, text="Song Track", font=("Montserrat Black 900", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
		trackframe.place(x=0, y=0, width="600", height="100")
		
		songtrack = Label(trackframe, textvariable=self.track, width=20, font=("Montserrat Black 900", 24, "bold"), bg="grey", fg="gold").grid(row=0, column=0, padx=10, pady=5)
		
		trackstatus = Label(trackframe, textvariable=self.status, font=("Montserrat Black 900", 24, "bold"), bg="grey", fg="gold").grid(row=0, column=1, padx=10, pady=5)
		
		buttonFrame = LabelFrame(self.root, text="Controls", font=("Montserrat Black 900", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
		
		buttonFrame.place(x=0, y=100, width=600, height=100)
		
		playbutton = Button(buttonFrame, text="PLAY", command=self.playsong, height=1, font=("Montserrat Black 900", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=0, padx=10, pady=5)
		
		playbutton = Button(buttonFrame, text="PAUSE", command=self.pausesong, width=8, height=1, font=("Montserrat Black 900",16,"bold"), fg="navyblue", bg="gold").grid(row=0, column=1, padx=10, pady=5)
		
		playbutton = Button(buttonFrame, text="UNPAUSE", command=self.unpausesong, width=10, height=1, font=("Montserrat Black 900", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=2, padx=10, pady=5)
		
		playbutton = Button(buttonFrame, text="STOP", command=self.stopsong, width=6, height=1, font=("Montserrat Black 900", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=3, padx=10, pady=5)
		
		exitButton = Button(buttonFrame, text="EXIT", command=self.exit, width=5, height=1, font=("Montserrat Black 900", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=4, padx=10, pady=5)
		
		songsframe = LabelFrame(self.root, text="Song Playlist", font=("Montserrat Black 900", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
		songsframe.place(x=600, y=0, width=400, height=200)
		
		scroll = Scrollbar(songsframe, orient=VERTICAL)
		
		self.playlist = Listbox(songsframe, yscrollcommand=scroll.set, selectbackground="gold", selectmode=SINGLE, font=("new times roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
		
		scroll.pack(side=RIGHT, fill="y")
		scroll.config(command=self.playlist.yview)
		self.playlist.pack(fill=BOTH)
		
		os.chdir("/Users/Eric/Desktop/py music")
		
		songtracks = os.listdir()
		
		for track in songtracks:
			self.playlist.insert(END, track)
	
	def playsong(self):
		self.track.set(self.playlist.get(ACTIVE))
		self.status.set("-Playing")
		pygame.mixer.music.load(self.playlist.get(ACTIVE))
		pygame.mixer.music.play()
	
	def stopsong(self):
		self.status.set("-Stopped")
		pygame.mixer.music.stop()
	
	def pausesong(self):
		self.status.set("-Paused")
		pygame.mixer.music.pause()
	
	def unpausesong(self):
		self.status.set("-Playing")
		pygame.mixer.music.unpause()
	
	def exit(self):
		root.destroy()

MusicPlayer(root)

root.mainloop()