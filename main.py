import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import urllib3
from io import BytesIO

'''
Confirm all tkinter stuff has moved to ttkbootstrap | ttkbootstrap.readthedocs.io
figure out if I can scale window better?
height / weight math 
history?
'''

#window = tk.Tk()
window = tb.Window(themename="minty")
window.iconbitmap('images/pokedex.ico')
window.geometry("800x700")
window.title("PokeDex")
window.config(padx=10, pady=10)




title_label = tb.Label(window, text="Pokedex", font=("Helvetica", 32))
# title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tb.Label(window, font=("Helvetica", 10))
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tb.Label(window, font=("Helvetica", 10))
# pokemon_information.config(font=("Arial", 10))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tb.Label(window, font=("Helvetica", 10))
# pokemon_types.config(font=("Arial",10))
pokemon_types.pack(padx=10, pady=10)

pokemon_height = tb.Label(window, font=("Helvetica", 10))
# pokemon_height.config(font=("Arial", 10))
pokemon_height.pack(padx=10, pady=10)

pokemon_weight = tb.Label(window, font=("Helvetica", 10))
# pokemon_weight.config(font=("Arial", 10))
pokemon_weight.pack(padx=10, pady=10)

#FUNCTION Load Pokemon
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    
    img= PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img
    
    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
    pokemon_height.config(text=f"Height: {pokemon.height}".title())
    pokemon_weight.config(text=f"Weight: {pokemon.weight}".title())
    


label_id_name = tb.Label(window, text="ID or Pokemon Name", font=("Helvetica", 28))
# label_id_name.config(font=("Arial",20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tb.Text(window, height=1)
# text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tb.Button(window, text="Enter", bootstyle=DEFAULT, command=load_pokemon)
# btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()

#Testing what can actually be pulled.  
# pokemon = pypokedex.get(name="charmander")
# print(pokemon.dex)
# print(pokemon.name)
# print(pokemon.abilities)
# print(pokemon.height)
# print(pokemon.weight)
# print(pokemon.types)
# print(pokemon.sprites.front.get("default"))