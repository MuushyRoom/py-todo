import tkinter as tk
from tkinter import ttk

notes = {}
note_id = 0
def create_label():
    global note_id
    print("created label")
    note_container = tk.Label(master=ui, text=f'{note_entry_text.get()}')
    note_container.pack()
    note = f'note_id{note_id}'
    note_id+=1
    notes[note] = note_container
    print(notes)
    print(notes[note])


#ui const
ui = tk.Tk()
ui.title('TEST UI')
ui.geometry('500x600')

title = tk.Label(master=ui,text="CREATING WIDGETS")
title.pack()



#MAKE A FRAME FOR INPUT
note_input_frame = ttk.Frame(master = ui)
#VARIABLE HANDLER FOR INPUT
note_entry_text = tk.StringVar()
entry = ttk.Entry(master=note_input_frame, textvariable= note_entry_text)
#BUTTON
create_button = tk.Button(master=note_input_frame,text="Create a label",command=create_label)
create_button.pack()
entry.pack()
note_input_frame.pack()
















# } OR LIKE RETURN 0 IN CPP
ui.mainloop()