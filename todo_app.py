import tkinter as tk
from tkinter import ttk

ui = tk.Tk()
ui.title('Todo App')
ui.geometry('500x600')
ui_title = tk.Label(master=ui,text="What's on your mind?", font='Tahoma 20 bold',pady=15)
ui_title.pack()


#DICTIONARY CONTAINER FOR NOTES
created_notes = {}
#INCREMENT NOTE ID
note_id = 0
def create_note(event=None):
    #used global bcoz it's just a simple program
    user_input = note_entry_text.get()


    if not user_input == '':
        # GETS USER INPUT AND DISPLAY NEWLY CREATED NOTE
        note_id = generate_note_id()
        # make container for created notes
        created_notes_frame = tk.Frame(master=ui)
        created_notes_frame['borderwidth'] = 5
        created_notes_frame['relief'] = 'groove'

        # display new note and delete button
        note_content = tk.Label(master=created_notes_frame, text=f'{note_entry_text.get()}', font='Tahoma 16', pady=5)
        delete_button = tk.Button(master=created_notes_frame, text='x', command=lambda: delete_note(note_id), pady=5)
        note_content.pack(side='left', padx=5)
        delete_button.pack()
        created_notes_frame.pack(pady=2)

        # GENERATE NOTE ID


        # ADD NOTE CONTENT INTO DICTIONARY
        created_notes[note_id] = created_notes_frame

        # Clear text_field_input
        clear_input()



def generate_note_id():
    global note_id
    note = f'note_id{note_id}'
    print(f'CREATED NOTE',note_id)
    note_id += 1


    return note


def clear_input():
    note_entry_text.set('')



def delete_note(unique_note_id):
    created_notes[unique_note_id].destroy()












#TEXTIELD CONTAINER
note_input_container = tk.Frame(master=ui)

#VARIABLE HANDLER FOR INPUT
note_entry_text = tk.StringVar()

#textfield
text_field = ttk.Entry(master=note_input_container, textvariable= note_entry_text,font='Tahoma 15 ')
text_field.bind('<Return>', create_note)
#BUTTON
create_button = tk.Button(master=note_input_container,text="+",command=create_note)

#ADD WIDGETS TO THE UI

text_field.pack(side ='left',padx=5)
create_button.pack(side ='left',padx=5)
note_input_container.pack(pady=25)













ui.mainloop()