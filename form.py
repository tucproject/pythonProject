import tkinter as tk
from tkinter import ttk
import record
import main
from tkhtmlview import HTMLLabel
import pandas as pd
from tkinter import filedialog
bgcolor = '#E6E6FA'
df = pd.DataFrame(columns=['link', 'titile', 'fairness'])

def search_result():
    q = query.get()
    text = main.search_zenodo(q)
    tk.Label(text='Zenodo ID', bg=bgcolor, font=('Calibri', 14, 'bold'), borderwidth=1, relief='groove').grid(row=3, column=0)
    tk.Label(text='Title of Dataset', bg=bgcolor, font=('Calibri', 14, 'bold'), borderwidth=1, relief='groove').grid(row=3, column=1)
    tk.Label(text='Fairness', bg=bgcolor, font=('Calibri', 14, 'bold'), borderwidth=1, relief='groove').grid(row=3, column=2)
    tk.Label(text='Missed metrics', bg=bgcolor, font=('Calibri', 14, 'bold'), borderwidth=1, relief='groove').grid(row=3, column=3)
    for i in range(len(text)):
        # get data about the record by id
        rec = record.search_data(text[i])
        #form string wiht missed features
        missed = ''
        for j in rec:
            if rec[j] == False: missed += ' ' + j

        url = 'https://zenodo.org/record/'+text[i]
        id_text = 'zenodo document id: ' + text[i]
        ur = HTMLLabel(win, html='<a href=' + url + '>' + id_text + '</a>', width=30, height=3, background=bgcolor)
        ur.grid(row=i+4, column=0, stick='e')
        field_title = tk.Text(width=40, height=3, wrap='word', bg=bgcolor)
        field_title.insert('1.0', rec['title'])
        field_title.grid(row=i + 4, column=1, stick='w')
        tk.Label(text=rec['fairness'], bg=bgcolor, font=('Calibri', 12)).grid(row=i + 4, column=2)
        tk.Label(text=missed, bg=bgcolor, font=('Calibri', 12)).grid(row=i + 4, column=3)

        #forming dataframe
        df.loc[len(df)] = [url, rec['title'], rec['fairness']]


def save_button(df):
    # SAVING_PATH = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv('search_result.csv')



win = tk.Tk()
win.title('FAIRness assessment')
win.geometry(f"700x700+200+10")
photo = tk.PhotoImage(file='exam.png')
win.iconphoto(False, photo)
win.config(bg=bgcolor)

#adding a menu
menubar = tk.Menu(win, tearoff=0)
win.config(menu=menubar)
file_menu = tk.Menu(menubar)
file_menu.add_command(label='save', command=save_button(df))
file_menu.add_command(label='about program')
menubar.add_cascade(label='File', menu=file_menu)

label_title = tk.Label(win, text='''This application helps you
to find dataset with true fairness''',
                       bg=bgcolor,
                       font=('Calibri', 20, 'bold'),
                       padx=10,
                       pady=10
                       )
label_title.grid(row=0, columnspan=4, stick='we')
tk.Label(win, text='Put your search query here ->', bg='#E6E6FA').grid(row=1, column=0, stick='w')

query = tk.Entry(win)
query.insert(0, 'covid vector')
query.grid(row=1, column=1, stick='w')

btn_find = tk.Button(win, text='find data',
                      command=search_result
                      )
btn_find.grid(row=2, columnspan=4)


win.grid_columnconfigure(0, minsize=50)
win.grid_columnconfigure(1, minsize=200)
win.grid_columnconfigure(2, minsize=30)
win.grid_columnconfigure(3, minsize=50)

win.mainloop()
