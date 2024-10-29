import customtkinter as ctk
from settings import *
import tkintermapview
from geopy.geocoders import Nominatim

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    ctk.set_appearance_mode('dark')
    self.geometry('1200x800+100+50')
    self.minsize(800,600)
    self.title('Map Viewer')
    self.iconbitmap('map.ico')

    self.input_string = ctk.StringVar()
    self.rowconfigure(0, weight = 1, uniform = 'a')
    self.columnconfigure(0, weight = 2, uniform = 'a')
    self.columnconfigure(1, weight = 8, uniform = 'a')
    
    self.map_widget = MapWidget(self, self.input_string, self.submit_location)

    self.mainloop()

  def submit_location(self, event):
    geolocator = Nominatim(user_agent = 'NimiraTech')
    location = geolocator.geocode(self.input_string.get())
    if location:
      self.map_widget.set_address(location.address)
      self.input_string.set('')
    else:
      self.map_widget.location_entry.error_animation()

class MapWidget(tkintermapview.TkinterMapView):
  def __init__(self, parent, input_string, submit_location):
    super().__init__(master = parent)
    self.grid(row = 0, column = 1, sticky = 'nsew')

    self.location_entry = LocationEntry(self, input_string, submit_location)
    # self.set_tile_server(TERRAIN_URL)

class LocationEntry(ctk.CTkEntry):
  def __init__(self, parent, input_string, submit_location):
    self.colour_index = 15
    colour = COLOUR_RANGE[self.colour_index]
    self.error = False

    super().__init__(
      master = parent, 
      textvariable = input_string,
      corner_radius = 0,
      border_width = 4,
      fg_color = ENTRY_BG,
      border_color = f'#f{colour}{colour}',
      text_color = TEXT_COLOUR,
      font = ctk.CTkFont(family = TEXT_FONT, size = TEXT_SIZE))
    self.place(relx = 0.5, rely = 0.95, anchor = 'center')
    self.bind('<Return>', submit_location)
    input_string.trace('w', self.remove_error)

  def error_animation(self):
    self.error = True
    if self.colour_index > 0:
      self.colour_index -= 1
      border_colour = f'f#{COLOUR_RANGE[self.colour_index]}{COLOUR_RANGE[self.colour_index]}'
      text_colour = f'#{COLOUR_RANGE[-self.colour_index - 1]}00'
      self.configure(border_colour = border_colour, text_colour = text_colour)
      self.after(40, self.error_animation)

  def remove_error(self, *args):
    if self.error:
      self.configure(border_colour = ENTRY_BG, text_color = TEXT_COLOUR)
      self.colour_index = 15

App()