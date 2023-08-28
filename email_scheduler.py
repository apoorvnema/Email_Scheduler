# Importing necessary Libraries
from tkinter import *
from tkinter import ttk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import tkinter.messagebox as msg
from datetime import datetime
import sys

# Changing system settings
sys.setrecursionlimit(10 ** 6)

# GUI Settings
root = Tk()
root.geometry("700x700+0+50")
root.minsize(700, 700)
root.maxsize(700, 700)
root.title("Email Scheduler")
root.wm_iconbitmap("icon.ico")

# Miscellaneous Variables
flag = 0
curr_day = datetime.now()
current_day = curr_day.strftime("%a")
temp_day = current_day
today = 0
btn_disable = 0

# TODO: TBA
# mon_fri_loop = " "

# Frame 1 starts
f1 = Frame(root)

# Adding Widgets
# From
from_lb = Label(f1, text="From: ", font="Helvetica 16 bold", padx=5, pady=5).grid(row=0, column=0, sticky=W)
from_value = StringVar()
from_tb = Entry(f1, textvar=from_value, font="Helvetica 16 bold", width=45).grid(row=0, column=1, sticky=W)

# Password
pass_lb = Label(f1, text="Password: ", font="Helvetica 16 bold", padx=5, pady=5).grid(row=1, column=0, sticky=W)
pass_value = StringVar()
pass_tb = Entry(f1, textvar=pass_value, font="Helvetica 16 bold", width=45, show="*").grid(row=1, column=1, sticky=W)

# To
to_lb = Label(f1, text="To: ", font="Helvetica 16 bold", padx=5, pady=5).grid(row=2, column=0, sticky=W)
to_value = StringVar()
to_tb = Entry(f1, textvar=to_value, font="Helvetica 16 bold", width=45).grid(row=2, column=1, sticky=W)

# Subject
sub_lb = Label(f1, text="Subject: ", font="Helvetica 16 bold", padx=5, pady=5).grid(row=3, column=0, sticky=W)
sub_value = StringVar()
sub_tb = Entry(f1, textvar=sub_value, font="Helvetica 16 bold", width=45).grid(row=3, column=1, sticky=W)

# Message Box
msg_lb = Label(f1, text="Type Message Below: ", font="Helvetica 10", padx=5, pady=5).grid(row=4, column=0, sticky=W)
scrollbar = Scrollbar(f1)
msg_tb = Text(f1, height=15, font="Helvetica 10", width=95, yscrollcommand=scrollbar.set)
scrollbar.config(command=msg_tb.yview)
scrollbar.grid(row=5, column=1, sticky="nse")
msg_tb.grid(row=5, column=0, sticky=W, padx=5, columnspan=2)

# Frame 1 ends
f1.pack(anchor="nw", fill=X)

# Frame 2 starts
f2 = Frame(root)

# Select Time
time_lb = Label(f2, text="Select Time: ", font="Helvetica 10", padx=5, pady=5).grid(row=0, column=0, sticky=W)

# Hour
hour_list = ["HH", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
hour = ttk.Combobox(f2, values=hour_list, width=5, state='readonly')
hour.current(0)
hour.grid(row=0, column=1, padx=2)

# Minutes
minutes_list = ["MM", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
                "16",
                "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33",
                "34",
                "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51",
                "52",
                "53", "54", "55", "56", "57", "58", "59"]
minutes = ttk.Combobox(f2, values=minutes_list, width=5, state='readonly')
minutes.current(0)
minutes.grid(row=0, column=2, padx=2)

# AM or PM
am_pm_list = ["AM", "PM"]
am_pm = ttk.Combobox(f2, values=am_pm_list, width=5, state='readonly')
am_pm.current(0)
am_pm.grid(row=0, column=3)


# Now
def now():
    curr_time = datetime.now()
    hour_now = curr_time.strftime("%I")
    minutes_now = curr_time.strftime("%M")
    am_pm_now = curr_time.strftime("%p")
    if str(hour['state']) != 'disabled':
        hour.config(state='disabled')
        hour.current(0)
        hour.set(hour_now)
    if hour['state'] == 'disabled':
        hour.config(state='readonly')
        hour.set(hour_list[0])

    if str(minutes['state']) != 'disabled':
        minutes.config(state='disabled')
        minutes.current(0)
        minutes.set(minutes_now)
    if minutes['state'] == 'disabled':
        minutes.config(state='readonly')
        minutes.set(minutes_list[0])

    if str(am_pm['state']) != 'disabled':
        am_pm.config(state='disabled')
        am_pm.current(0)
        am_pm.set(am_pm_now)
    if am_pm['state'] == 'disabled':
        am_pm.config(state='readonly')
        am_pm.set(am_pm_list[0])


now_var = IntVar()
now_var.set(0)
now_cb = Checkbutton(f2, text="Current Time", variable=now_var, command=now)

# TODO: TBA
"""
# Repeat Functionality
# Frame 3 starts
f3 = Frame(root)

mon_cb = IntVar()
tue_cb = IntVar()
wed_cb = IntVar()
thu_cb = IntVar()
fri_cb = IntVar()
sat_cb = IntVar()
sun_cb = IntVar()
cb1 = Checkbutton(f3, text="Monday", variable=mon_cb, state=DISABLED)
cb2 = Checkbutton(f3, text="Tuesday", variable=tue_cb, state=DISABLED)
cb3 = Checkbutton(f3, text="Wednesday", variable=wed_cb, state=DISABLED)
cb4 = Checkbutton(f3, text="Thursday", variable=thu_cb, state=DISABLED)
cb5 = Checkbutton(f3, text="Friday", variable=fri_cb, state=DISABLED)
cb6 = Checkbutton(f3, text="Saturday", variable=sat_cb, state=DISABLED)
cb7 = Checkbutton(f3, text="Sunday", variable=sun_cb, state=DISABLED)
"""

# TODO: TBA
"""
def once_cb():
    cb1.configure(state='disabled')
    cb1.deselect()
    cb2.configure(state='disabled')
    cb2.deselect()
    cb3.configure(state='disabled')
    cb3.deselect()
    cb4.configure(state='disabled')
    cb4.deselect()
    cb5.configure(state='disabled')
    cb5.deselect()
    cb6.configure(state='disabled')
    cb6.deselect()
    cb7.configure(state='disabled')
    cb7.deselect()


def daily_cb():
    cb1.configure(state='disabled')
    cb1.deselect()
    cb2.configure(state='disabled')
    cb2.deselect()
    cb3.configure(state='disabled')
    cb3.deselect()
    cb4.configure(state='disabled')
    cb4.deselect()
    cb5.configure(state='disabled')
    cb5.deselect()
    cb6.configure(state='disabled')
    cb6.deselect()
    cb7.configure(state='disabled')
    cb7.deselect()


def mon_fri_cb():
    cb1.configure(state='disabled')
    cb1.deselect()
    cb2.configure(state='disabled')
    cb2.deselect()
    cb3.configure(state='disabled')
    cb3.deselect()
    cb4.configure(state='disabled')
    cb4.deselect()
    cb5.configure(state='disabled')
    cb5.deselect()
    cb6.configure(state='disabled')
    cb6.deselect()
    cb7.configure(state='disabled')
    cb7.deselect()


# TODO: To Work on
def custom_cb():
    cb1.configure(state='normal')
    cb1.deselect()
    cb2.configure(state='normal')
    cb2.deselect()
    cb3.configure(state='normal')
    cb3.deselect()
    cb4.configure(state='normal')
    cb4.deselect()
    cb5.configure(state='normal')
    cb5.deselect()
    cb6.configure(state='normal')
    cb6.deselect()
    cb7.configure(state='normal')
    cb7.deselect()"""

repeat_lb = Label(f2, text="Repeat: ", font="Helvetica 10", padx=5, pady=5).grid(row=1, column=0, sticky=W)
radio_var = IntVar()
radio_var.set(1)
Radiobutton(f2, text="Once", variable=radio_var, value=1).grid(row=1, column=1)
Radiobutton(f2, text="Daily", variable=radio_var, value=2).grid(row=1, column=2)

# TODO: TBA
"""
Radiobutton(f2, text="Monday to Friday", variable=radio_var, value=3, command=mon_fri_cb).grid(row=1,
                                                                                               column=3)
Radiobutton(f2, text="Custom", variable=radio_var, value=4, command=custom_cb).grid(row=1, column=4)"""

# Frame 2 ends
f2.pack(anchor="nw", fill=X)

# TODO: TBA
"""
# Frame 3 ends
f3.pack(anchor="nw", fill=X)"""

# Frame 4 starts
f4 = Frame(root)

# Attach file
attach_lb = Label(f4, text="Attach File (.zip only): ", font="Helvetica 10", padx=5, pady=5).grid(row=1, column=0,
                                                                                                  sticky=W)
attach_var = IntVar()
attach_var.set(1)
Radiobutton(f4, text="None", variable=attach_var, value=1).grid(row=2, column=0, sticky=W)
Radiobutton(f4, text="Auto Select from root", variable=attach_var, value=2).grid(row=3, column=0,
                                                                                 sticky=W)
Radiobutton(f4, text="Browse File", variable=attach_var, value=3).grid(row=4, column=0, sticky=W)

# Keep File
keep_lb = Label(f4, text="Do you want to keep the zip file: ", font="Helvetica 10", padx=5, pady=5).grid(row=5,
                                                                                                         column=0,
                                                                                                         sticky=W)
keep_var = IntVar()
keep_var.set(1)
Radiobutton(f4, text="Yes", variable=keep_var, value=1).grid(row=5, column=1, sticky=W)
Radiobutton(f4, text="No", variable=keep_var, value=2).grid(row=5, column=2, sticky=W)

# File Location
# Frame 5 starts
f5 = Frame(root)

# File Location Label
file_loc = Label(f5, text="File Location: ", font="Helvetica 9", padx=5, pady=5).grid(row=0,
                                                                                      column=0,
                                                                                      sticky=W)

# Frame 5 ends
f5.pack(anchor="nw", fill=X)

# Frame 4 ends
f4.pack(anchor="nw", fill=X)

# Frame 6 starts
f6 = Frame(root)


# Main Buttons
def reset():
    from_value.set("")
    pass_value.set("")
    to_value.set("")
    sub_value.set("")
    msg_tb.delete("1.0", "end")
    hour.config(state='readonly')
    hour.current(0)
    minutes.config(state='readonly')
    minutes.current(0)
    am_pm.config(state='readonly')
    am_pm.current(0)
    now_cb.deselect()
    radio_var.set(1)

    # TODO: TBA
    """
    cb1.configure(state='disabled')
    cb1.deselect()
    cb2.configure(state='disabled')
    cb2.deselect()
    cb3.configure(state='disabled')
    cb3.deselect()
    cb4.configure(state='disabled')
    cb4.deselect()
    cb5.configure(state='disabled')
    cb5.deselect()
    cb6.configure(state='disabled')
    cb6.deselect()
    cb7.configure(state='disabled')
    cb7.deselect()
    attach_var.set(1)
    keep_var.set(1)


cb1.grid(row=0, column=0)
cb2.grid(row=0, column=1)
cb3.grid(row=0, column=2)
cb4.grid(row=0, column=3)
cb5.grid(row=0, column=4)
cb6.grid(row=0, column=5)
cb7.grid(row=0, column=6)
"""


now_cb.grid(row=0, column=4, sticky=W)


# Convert 12 hour to 24 hour
def convert24(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:6]


def send():
    global btn_disable
    status_lb.config(text="Uploading")
    f6.update()
    sender_address = from_value.get()
    sender_pass = pass_value.get()
    receiver_address = to_value.get()

    # instance of MIMEMultipart
    data = MIMEMultipart()

    # storing the senders email address
    data['From'] = sender_address

    # storing the receivers email address
    data['receiver_address'] = receiver_address

    # storing the subject
    data['Subject'] = sub_value.get()

    # string receiver_address store the body of the mail
    body = msg_tb.get("1.0", END)

    # attach the body with the msg instance
    data.attach(MIMEText(body, 'plain'))

    # open the file receiver_address be sent
    filename = "1.zip"
    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # receiver_address change the payload into encoded form
    p.set_payload(attachment.read())

    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' receiver_address instance 'msg'
    data.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_address, sender_pass)

    # Converts the Multipart msg into a string
    text = data.as_string()

    # sending the mail
    s.sendmail(sender_address, receiver_address, text)

    # terminating the session
    s.quit()
    time.sleep(0.3)
    status_lb.config(text="Send Successfully")
    f6.update()
    time.sleep(0.3)
    status_lb.config(text="Ready")
    f6.update()
    if btn_disable == 1 and submit['state'] == "disabled":
        submit['state'] = "normal"
        submit['background'] = "dim grey"
        btn_disable = 0
    time.sleep(0.3)


def once():
    global flag, btn_disable
    if flag == 1:
        if btn_disable == 1 and submit['state'] == "disabled":
            submit['state'] = "normal"
            submit['background'] = "dim grey"
        flag = 0
        return
    time_cb = hour.get() + ":" + minutes.get() + " " + am_pm.get()
    curr_time = datetime.now()
    current_time = curr_time.strftime("%I:%M %p")
    if time_cb == current_time:
        send()
        flag = 1
    root.after(1000, once)


def daily():
    global temp_day, current_day, curr_day, today
    curr_day = datetime.now()
    time_cb = hour.get() + ":" + minutes.get() + " " + am_pm.get()
    current_day = curr_day.strftime("%a")
    time_check = curr_day.strftime("%I:%M %p")
    if today == 0:
        if convert24(time_check) <= convert24(time_cb):
            once()
        today = 1
    if temp_day != current_day and today == 1:
        today = 1
        once()
        temp_day = current_day
    root.after(45000, daily)


# TODO: TBA
"""def mon_fri():
    daily()"""


def scheduler():
    if hour.get() == "HH" or minutes.get() == "MM":
        msg.showerror("Error in time", "Please select valid time")
    else:
        global btn_disable, current_day, curr_day

        curr_day = datetime.now()
        current_day = curr_day.strftime("%a")
        if radio_var.get() == 1:
            submit['state'] = "disabled"
            submit['background'] = "white"
            once()
            btn_disable = 1
        if radio_var.get() == 2:
            btn_disable = 0
            submit['state'] = "disabled"
            submit['background'] = "white"
            daily()

    # TODO: TBA
    """if radio_var.get() == 3:
        global mon_fri_loop
        mon_fri_loop = root.after(5000, scheduler)
        btn_disable = 0
        submit['state'] = "disabled"
        submit['background'] = "white"
        if current_day != "Sat" and current_day != "Sun":
            mon_fri()
        else:
            root.after_cancel(mon_fri_loop)

    if radio_var.get() == 4:
        btn_disable = 0"""


reset_btn = Button(f6, text="Reset", font="Helvetica 12 bold", background="dim grey", foreground="white",
                   command=reset).grid(row=0,
                                       column=0,
                                       sticky=W)
stop = Button(f6, text="Cancel", font="Helvetica 12 bold", background="dim grey", foreground="white",
              command=reset)
stop['state'] = "disabled"
stop['background'] = "white"
stop.grid(row=0,
          column=1,
          sticky=W, padx=225)
submit = Button(f6, text="Schedule Now", font="Helvetica 12 bold", background="dim grey", foreground="white",
                command=scheduler)
submit.grid(row=0, column=2, sticky=W)

# Frame 6 ends
f6.pack(anchor=NW, fill=X)

# Frame 7 starts
f7 = Frame(root)

# Status bar
status_var = StringVar()
status_lb = Label(f7, text="Ready", font="Helvetica 8", relief=SUNKEN, anchor="w")
status_lb.grid(row=0, column=0)

# Frame 7 ends
f7.pack(side=BOTTOM, fill=X)

# End of Program
root.mainloop()
