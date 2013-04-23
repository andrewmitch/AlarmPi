#!/usr/bin/env python3.2.3

from tkinter import *
from tkinter import ttk
from entry import ConstrainedEntry
import tkinter.messagebox
import functions
import alarm
import time

AlarmCode = "2222"

root = Tk()
root.title("Alarm Interface")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

code_entered = IntVar()
sensoroptions = ("Both", "Front", "Back")
sensor_choice = StringVar()

#Add Entry field for  code data, calls class Constrained Entry for validation
code_entry= ConstrainedEntry(mainframe, width=7, textvariable=code_entered, show="*")
code_entry.delete(0, END)
code_entry.grid(columnspan = 2, column=2, row=5, sticky=(W, E))

#Add buttons to frame using grid layout
ttk.Button(mainframe, text="1", command=lambda: functions.one(code_entry)).grid(column=1, row=1, sticky=NW)
ttk.Button(mainframe, text="2", command=lambda: functions.two(code_entry)).grid(column=2, row=1, sticky=NW)
ttk.Button(mainframe, text="3", command=lambda: functions.three(code_entry)).grid(column=3, row=1, sticky=NW)
ttk.Button(mainframe, text="4", command=lambda: functions.four(code_entry)).grid(column=1, row=2, sticky=NW)
ttk.Button(mainframe, text="5", command=lambda: functions.five(code_entry)).grid(column=2, row=2, sticky=NW)
ttk.Button(mainframe, text="6", command=lambda: functions.six(code_entry)).grid(column=3, row=2, sticky=NW)
ttk.Button(mainframe, text="7", command=lambda: functions.seven(code_entry)).grid(column=1, row=3, sticky=NW)
ttk.Button(mainframe, text="8", command=lambda: functions.eight(code_entry)).grid(column=2, row=3, sticky=NW)
ttk.Button(mainframe, text="9", command=lambda: functions.nine(code_entry)).grid(column=3, row=3, sticky=NW)
ttk.Button(mainframe, text="Clear", command=lambda: functions.clear(code_entry)).grid(column=1, row=4, sticky=NW)
ttk.Button(mainframe, text="0", command=lambda: functions.zero(code_entry)).grid(column=2, row=4, sticky=NW)
ttk.Button(mainframe, text="Delete", command=lambda: functions.delete(code_entry)).grid(column=3, row=4, sticky=NW)

ttk.Button(mainframe, width=12, text="Disable Alarm", command =lambda: alarm.disableCode(code_entry)).grid(column=5, row=4, sticky=SE)
ttk.Button(mainframe, width=12,text="Enable Alarm", command =lambda: alarm.enableCode(code_entry, sensor_option, root)).grid(column=5, row=5, sticky=SE)

ttk.Label(mainframe, text="Alarm Code:").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Sensor Option:").grid(column =4, row =1, sticky=NE)

sensor_option=Spinbox(mainframe, values=(sensoroptions), textvariable=sensor_choice)
sensor_option.grid(column =5, row =1, sticky=(N,E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()


