#!/usr/bin/env python
# Python 3
from tkinter import *
from tkinter import ttk

def one(code_entry):
	code_entry.insert(END,"1")
def two(code_entry):
	code_entry.insert(END,"2")
def three(code_entry):
	code_entry.insert(END,"3")
def four(code_entry):
	code_entry.insert(END,"4")
def five(code_entry):
	code_entry.insert(END,"5")
def six(code_entry):
	code_entry.insert(END,"6")
def seven(code_entry):
	code_entry.insert(END,"7")
def eight(code_entry):
	code_entry.insert(END,"8")
def nine(code_entry):
	code_entry.insert(END,"9")
def zero(code_entry):
	code_entry.insert(END,"0")
def clear(code_entry):
	code_entry.delete(0, END)
def delete(code_entry):
	start = len(code_entry.get()) -1
	code_entry.delete(start, END)
	
