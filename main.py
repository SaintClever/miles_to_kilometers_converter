from tkinter import *


window = Tk()
window.title('Mile to kilometers converter')
window.config(padx=5, pady=5)


# functions
def miles_to_km():
    result = int(miles_entry.get()) * 1.60934
    kilo_label_output['text'] = '{:.2f}'.format(result)


# label
equal_to_label = Label(text='is equal to')
equal_to_label.grid(column=0, row=1)

# entry
miles_entry = Entry(text='0', width=10)
miles_entry.grid(column=1, row=0)

# label
kilo_label_output = Label(text='0')
kilo_label_output.grid(column=1, row=1)

# button
calculate_btn = Button(text='calculate', command=miles_to_km)
calculate_btn.grid(column=1, row=2)

# label
miles_label = Label(text='miles')
miles_label.grid(column=2, row=0)

kilometers_label = Label(text='kilometers')
kilometers_label.grid(column=2, row=1)


window.mainloop()