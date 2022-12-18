import tkinter as tk
import matplotlib.pyplot as plt
import sorts

root = tk.Tk()
root.title('Sort visualiser')

root.configure(bg='#2b2b2b')

root.geometry('600x600')

frame = tk.Frame(root, bg='#2b2b2b')
frame.pack()

button_bubble_sort = tk.Button(frame, text='Bubble Sort', command=lambda: sorts.bubble_sort('Bubble Sort'))
button_quick_sort = tk.Button(frame, text='Quick Sort', command=lambda: sorts.quick_sort('Quick Sort'))
button_selection_sort = tk.Button(frame, text='Selection Sort', command=lambda: sorts.selection_sort('Selection Sort'))
button_heap_sort = tk.Button(frame, text='Heap Sort', command=lambda: sorts.heap_sort('Heap Sort'))

button_bubble_sort.configure(bg='#545454', fg='white', activebackground='#767676', activeforeground='white', relief='flat', bd=0, font=('Arial', 16))
button_quick_sort.configure(bg='#545454', fg='white', activebackground='#767676', activeforeground='white', relief='flat', bd=0, font=('Arial', 16))
button_selection_sort.configure(bg='#545454', fg='white', activebackground='#767676', activeforeground='white', relief='flat', bd=0, font=('Arial', 16))
button_heap_sort.configure(bg='#545454', fg='white', activebackground='#767676', activeforeground='white', relief='flat', bd=0, font=('Arial', 16))

button_bubble_sort.grid(row=1, column=0, padx=50, pady=50, sticky='nsew')
button_quick_sort.grid(row=1, column=1, padx=50, pady=50, sticky='nsew')
button_selection_sort.grid(row=2, column=0, padx=50, pady=50, sticky='nsew')
button_heap_sort.grid(row=2, column=1, padx=50, pady=50, sticky='nsew')

label = tk.Label(frame, text='Sort visualiser', bg='#2b2b2b', fg='white', font=('Arial', 24))
label.grid(row=0, column=0, columnspan=2, pady=50, sticky='nsew')

button_bubble_sort.grid(row=1, column=0, padx=50, pady=50, sticky='nsew')
button_quick_sort.grid(row=1, column=1, padx=50, pady=50, sticky='nsew')
button_selection_sort.grid(row=2, column=0, padx=50, pady=50, sticky='nsew')
button_heap_sort.grid(row=2, column=1, padx=50, pady=50, sticky='nsew')

button_exit = tk.Button(frame, text='Exit', command=root.destroy)
button_exit.configure(bg='#545454', fg='white', activebackground='#767676', activeforeground='white', relief='flat', bd=0, font=('Arial', 16))
button_exit.grid(row=3, column=0, columnspan=2, padx=50, pady=50, sticky='nsew')

root.mainloop()