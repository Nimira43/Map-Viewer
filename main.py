import customtkinter as ctk
from settings import *
import tkintermapview

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    ctk.set_appearance_mode('light')
    self.geometry('1200x800+100+50')
    self.minsize(800,600)
    self.title('Map Viewer')
    self.iconbitmap('map.ico')

    self.input_string = ctk.StringVar()
    self.rowconfigure(0, weight = 1, uniform = 'a')
    self.columnconfigure(0, weight = 2, uniform = 'a')
    self.columnconfigure(1, weight = 8, uniform = 'a')
    self.map_widget = MapWidget(self, self.input_string)

    self.mainloop()

class MapWidget(tkintermapview.TkinterMapView):
  def __init__(self, parent, input_string):
    super().__init__(master = parent)
    self.grid(row = 0, column = 1, sticky = 'nsew')

    LocationEntry(self, input_string)
    # self.set_tile_server(TERRAIN_URL)

class LocationEntry(ctk.CTkEntry):
  def __init__(self, parent, input_string):
    super().__init__(master = parent, textvariable = input_string)
    self.place(relx = 0.5, rely = 0.95, anchor = 'center')



App()