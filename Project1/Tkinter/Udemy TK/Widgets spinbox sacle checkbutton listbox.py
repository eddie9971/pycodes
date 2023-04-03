from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title('Widge Examples')
window.minsize(width=500, height=500)

# Labels
label = Label(text='This is old text')
label.config(text='This is new text')
label.pack()

# Buttons
def action():
    print('Hello World')

# Calls action() when pressed
button = Button(text='Click', command=action)
button.pack()

# Entries
entry = Entry(width=30)
# Add some etext to begin with
entry.insert(END, string='Some text to begin with')
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(END, 'Example of multi-line text entry')

# Get current value in text box at line 1 character 0
print(text.get('1.0', END))
text.pack()

# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5,command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    # prints 1 if on button checked, otherwise 0
    print(checked_state.get())

# variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text='Is On?',variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())

# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1',value=1,variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option2',value=2,variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

window.mainloop()