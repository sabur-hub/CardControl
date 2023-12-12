import os
import re
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import time
# from tkinter import font


def Main():
    for i in os.listdir('./DATA/'):
        with open(f"DATA/{i}", 'r+') as fy:
            content = fy.read()
            date_pattern = r"\d{4}-\d{2}-\d{2}"
            date_match = re.search(date_pattern, content)
            if time.strftime("%Y:%m:%d") != date_match.group():
                pass
    def AddCard():
        if len(addentry.get()) == 11:
            input_data = addentry.get()
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            with open(f"DATA/{input_data}", "w") as file:
                file.write(f"{current_time}\n")
                file.write(f"{current_date}\n")
                file.write("$$100000\n")
                file.write("%0\n")
                file.write("$$$30000\n")
        else:
            labelInfo = ctk.CTkLabel(root, text="input the correct card number")
            labelInfo.place(x=980, y=845)

    def search_name_file():
        search_term = search.get()
        esults_text.delete(0, tk.END)
        for filename in os.listdir(directory):
            if search_term in filename:
                esults_text.insert(tk.END, filename)

    def showAddWindows():
        if esults_text.curselection():
            select_filename = esults_text.get(esults_text.curselection())
            with open(os.path.join(directory, select_filename), 'r+') as f:
                content = f.read()
            # print(content)
            match = re.search(r'\$\$\$\s*\s*(\d+)', content)
            match1 = re.search(r'%\s*\s*(\d+)', content)
            match2 = re.search(r'\$\$\s*\s*(\d+)', content)
            # print(match, match1, match2)
            # print(match.group(1), match2.group(1), match1.group(1))
            AddDay = match.group(1)
            AddMount = match2.group(1)
            Add = match1.group(1)
            # regular expression to match "xx:xx:x0"
            time_pattern = r"\d{2}:\d{2}:\d{2}"
            # regular expression to match "xxxx-xx-xx"
            date_pattern = r"\d{4}-\d{2}-\d{2}"
            time_match = re.search(time_pattern, content)
            date_match = re.search(date_pattern, content)
            # print(time_match, date_match)
            entryAddGet = AddAdnSendEntry.get()
            resultAddDay = int(AddDay) - int(entryAddGet)
            resultAddMount = int(AddMount) - int(entryAddGet)
            resultAdd = int(Add) + int(entryAddGet)
            with open(os.path.join(directory, select_filename), "w+") as file:
                con = file.write(f'{time_match.group()}\n'
                                 f'{date_match.group()}\n$${resultAddMount}\n'
                                 f'%{resultAdd}\n$$${resultAddDay}')
        else:
            messagebox.showerror("Error", "Please select an item from the listbox.")
            return

    def showSendWindows():
        if esults_text.curselection():
            select_filename = esults_text.get(esults_text.curselection())
            with open(os.path.join(directory, select_filename), 'r+') as f:
                content = f.read()
            # print(content)
            match = re.search(r'\$\$\$\s*\s*(\d+)', content)
            match1 = re.search(r'%\s*\s*(\d+)', content)
            match2 = re.search(r'\$\$\s*\s*(\d+)', content)
            # print(match, match1, match2)
            # print(match.group(1), match2.group(1), match1.group(1))
            AddDay = match.group(1)
            AddMount = match2.group(1)
            Add = match1.group(1)
            # regular expression to match "xx:xx:x0"
            time_pattern = r"\d{2}:\d{2}:\d{2}"
            # regular expression to match "xxxx-xx-xx"
            date_pattern = r"\d{4}-\d{2}-\d{2}"
            time_match = re.search(time_pattern, content)
            date_match = re.search(date_pattern, content)
            # print(time_match, date_match)
            entryAddGet = AddAdnSendEntry.get()
            resultAddDay = int(AddDay) - int(entryAddGet)
            resultAddMount = int(AddMount) - int(entryAddGet)
            resultAdd = int(Add) - int(entryAddGet)
            with open(os.path.join(directory, select_filename), "w+") as file:
                con = file.write(f'{time_match.group()}\n'
                                 f'{date_match.group()}\n$${resultAddMount}\n'
                                 f'%{resultAdd}\n$$${resultAddDay}')
        else:
            messagebox.showerror("Error", "Please select an item from the listbox.")
            return

    def search_files():
        search_term = search_entry.get()
        results = []
        for filename in os.listdir(directory):
            if search_term in filename:
                with open(os.path.join(directory, filename)) as f:
                    content = f.read().replace('\n', '\t\t\t').replace('$', '').replace("%", '')
                results.append((filename, content.strip()))
        results.sort(key=lambda x: x[0])
        if results:
            try:
                results.sort(key=lambda x: int(x[1].split('\t')[4]))
            except ValueError:
                pass  # Handle the error by doing nothing (or logging it)
            output = '\n'.join([f'{filename}\t\t\t\t{content}' for filename, content in results])
            results_text.delete('1.0', ctk.END)
            results_text.insert(ctk.END, output)
        else:
            results_text.delete('1.0', ctk.END)
            results_text.insert(ctk.END, 'No results found.')

    root = ctk.CTk()
    root.title('File Search')
    root.geometry("1850x900")

    directory = './DATA/'

    search_label = ctk.CTkLabel(root, text='For search all data')
    search_label.pack()
    searchlabel = ctk.CTkLabel(root, text='For search card number')
    searchlabel.place(x=1605, y=0)
    search = ctk.CTkEntry(root, font=('Helvetica', 14))
    search.place(x=1600, y=25)
    search_entry = ctk.CTkEntry(root, font=('Helvetica', 14))
    search_entry.pack()

    labelCard = ctk.CTkLabel(root, text="card number")
    labelCard.place(x=5, y=90)

    labelTime = ctk.CTkLabel(root, text="Time")
    labelTime.place(x=240, y=90)

    labelData = ctk.CTkLabel(root, text="Data")
    labelData.place(x=420, y=90)

    labelLimitInMount = ctk.CTkLabel(root, text="Limit for Mount", text_color="white")
    labelLimitInMount.place(x=550, y=90)

    labelhowManyMoneyHave = ctk.CTkLabel(root, text="How many have")
    labelhowManyMoneyHave.place(x=700, y=90)

    labelhowManyMoneyCanAddInOneDay = ctk.CTkLabel(root, text="How many can add today")
    labelhowManyMoneyCanAddInOneDay.place(x=850, y=90)
    labelCardNumber = ctk.CTkLabel(root, text="card number")
    labelCardNumber.place(x=1500, y=90)

    search_button = ctk.CTkButton(root, text='Search', command=lambda: search_files())
    search_button.pack()
    searchbutton = ctk.CTkButton(root, text='Search', command=lambda: search_name_file())
    searchbutton.place(x=1600, y=55)

    # create a CTkFont instance with a size of 30
    my_font = ctk.CTkFont(family="Helvetica", size=17)

    # create the CTkTextbox widget and set the font
    results_text = ctk.CTkTextbox(root, width=1400, height=730, bg_color="#151818", font=my_font)
    results_text.place(x=0, y=120)

    # set the font size to 50
    my_font.configure(size=17)

    # apply the modified font to the CTkTextbox widget
    results_text.configure(font=my_font)
    esults_text = tk.Listbox(root, width=38, height=33, background="#151818", fg="white", font=my_font)
    esults_text.place(x=1500, y=120)
    AddAdnSendEntry = ctk.CTkEntry(root, width=350)
    AddAdnSendEntry.place(x=1500, y=800)
    AddButton = ctk.CTkButton(root, text="Add", command=lambda: showAddWindows())
    AddButton.place(x=1500, y=845)
    SendButton = ctk.CTkButton(root, text="Send", command=lambda: showSendWindows())
    SendButton.place(x=1710, y=845)
    addentry = ctk.CTkEntry(root, width=250)
    addentry.place(x=560, y=845)
    AddLabel = ctk.CTkLabel(root, text="there you can add new card")
    AddLabel.place(x=390, y=845)
    btnAdd = ctk.CTkButton(root, text='Add', command=lambda: AddCard())
    btnAdd.place(x=830, y=845)
    btnClose = ctk.CTkButton(root, text='exit', command=lambda: exit())
    btnClose.place(x=0, y=845)
    root.mainloop()


if __name__ == '__main__':
    Main()
