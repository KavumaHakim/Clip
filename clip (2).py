import pyperclip as clip
import customtkinter as ctk
import CTkMessagebox as msg
import tkinter as tk
from tkinter.messagebox import *


window = ctk.CTk()
window.title('Clipboard Manager')
window.iconbitmap('clip.ico')
ctk.set_appearance_mode('system')
window.geometry('460x252')
window.resizable(0, 1)
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme(r'Hades.json')


def add_clipboard_item():
    item_frame = ctk.CTkFrame(contents, height=2, border_color='white', border_width=2)
    check = ctk.CTkCheckBox(item_frame, text=None)
    data = clip.paste()
    item = ctk.CTkLabel(item_frame, text=data)
    check.pack(side=ctk.LEFT, padx=10)
    item.pack(pady=5)
    item_frame.pack(pady=5, padx=1, fill='x')


def load_to_clip():
    # Get the selected item from the clipboard manager
    selected_item = get_selected_item()
    
    if selected_item:
        # Open the clipboard and set the data
        clip.copy(selected_item)
        msg.CTkMessagebox(master=window, message = 'Item added to Clipboard', icon='info', title='Clip', corner_radius=15, font=('georgia', 15))


def add_clipboard_item():
    item_frame = ctk.CTkFrame(contents, height=2, border_color='white', border_width=2)

    # Use tk.StringVar 
    check_var = tk.StringVar()
    check = ctk.CTkCheckBox(item_frame, text=None, variable=check_var)

    data = clip.paste()
    if data == ' ':
        msg.CTkMessagebox(master=window, message = 'Clip board Empty', icon='info', title='Clip')
    item = ctk.CTkLabel(item_frame, text=data, wraplength=300)

    check.pack(side=ctk.LEFT, padx=10)
    item.pack(pady=5)
    item_frame.pack(pady=5, padx=1, fill='x')

def get_selected_item():
    # Find the selected item in the contents frame
    for child in contents.winfo_children():
        if isinstance(child, ctk.CTkFrame):
            checkbox = child.winfo_children()[0]
            label = child.winfo_children()[1]

            # Check if the checkbox is selected
            if checkbox.cget('variable').get() == '1':
                return label.cget('text')

    return None

# Frame with the buttons...
buttons = ctk.CTkFrame(window)

add_button = ctk.CTkButton(buttons, text='ADD ITEM', cursor='hand2', command=add_clipboard_item)
add_button.pack(side=ctk.RIGHT, padx=20, pady=10)

load_button = ctk.CTkButton(buttons, text='LOAD TO CLIP', cursor='hand2', command=load_to_clip)
load_button.pack(side=ctk.LEFT, padx=20, pady=10)

buttons.pack(fill='x')

#Frame with the items
contents = ctk.CTkScrollableFrame(window)
contents.pack(fill=ctk.BOTH, expand=True)
window.after(500, lambda: msg.CTkMessagebox(master = window,fade_in_duration=2, title='HOW TO USE?', message = 'Click the "ADD ITEM" button to add text from the clipboard. \n To load an item to Clipboard, check the item box and click the "LOAD TO CLIP" button.\n Contents Will remain until the program is closed.\n WINDOWS_KEY + LEFT_ARROW_KEY to maximise to the left\n side.\n BY HAKIM...', width=500, sound=1))

window.mainloop()
