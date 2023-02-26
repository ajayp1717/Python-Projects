from tkinter import *
from time import *
from datetime import *

root = Tk()
root.geometry('900x500')
root.resizable(3, 4)
root.title("Website Blocker")
root.iconbitmap('C:\\Users\\ajayp\\Downloads\\final.ico')

Label(root, text='Web Blocker', font='arial 20 bold').pack()
host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'
Label(root, text='Enter Websites :', font='arial 13 bold').place(x=5, y=60)
Label(root, text='Start at :   ', font='arial 13 bold').place(x=5, y=120)
Label(root, text=' End at :   ', font='arial 13 bold').place(x=5, y=180)
Websites = Text(root, font='arial 10', height='2', width='80')
Websites.place(x=140, y=60)
global strt_Time, end_Time

strt_Time = int(0)
Entry(root, textvariable=strt_Time, font='arial 10', width='80').place(x=140, y=120)
end_Time = int(1)
Entry(root, textvariable=end_Time, font='arial 10', width='80').place(x=140, y=180)


# convert1=datetime.strptime(strt_Time,'%I:%M')
# convert2=datetime.strptime(end_Time,'%I:%M')

def Blocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    while True:

        if datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                    strt_Time) < datetime.now() < datetime(datetime.now().year, datetime.now().month,
                                                           datetime.now().day, end_Time):
            with open(host_path, "r+") as fileptr:
                content = fileptr.read()
                for website in Websites:
                    if website in content:
                        Label(root, text='Already Blocked', font='arial 12 bold').place(x=230, y=320)
                else:
                    fileptr.write(ip_address + "        " + website + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines();
            file.seek(0)
            for line in content:
                if not any(website in line for website in Websites):
                    file.write(line)
                    Label(root, text="Blocked", font='arial 12 bold').place(x=230, y=320)
            file.truncate()

    sleep(5)


block = Button(root, text='Block', font='arial 12 bold', pady=5, command=Blocker, width=6, bg='royal blue1',
               activebackground='sky blue')
block.place(x=400, y=250)
root.mainloop()