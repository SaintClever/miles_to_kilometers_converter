from tkinter import *


window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)



#Label
my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack() # pack(), place(), or grid() 'grid is the best'
my_label.grid(column=0, row=0)
my_label['text'] = 'New text'
my_label.config(text='Newer text')
my_label.config(padx=50, pady=50)


# Button
def button_clicked():
    # print('I got clicked')
    # my_label['text'] = 'I got clicked'
    # my_label.config(text='I got clicked too')
    my_label['insert'] = input.get()


def new_clicked():
    new_button.config(text='Ouch!')


button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text='new click me', command=new_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
input.insert(END, string='hi')
input.get()



window.mainloop()