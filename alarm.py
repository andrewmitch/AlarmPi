from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import RPi.GPIO as GPIO
import time


GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)

alarmTriggered = False
alarmStatus = "Off"
alarmCode = "2222"
flash = True


def redLED(pin, mode):
        GPIO.output(pin, mode)
        
def greenLED(pin, mode):
        GPIO.output(pin, mode)
        
def enableCode(code_entry, sensor_option, root):
        global sensorChoice
        global alarmStatus
        global userEntered
        global alarmTriggered
        userEntered = (code_entry.get())
        print(userEntered)
        code_entry.delete(0, END)
        if (userEntered == alarmCode) and (alarmStatus == "Off"):
                tkinter.messagebox.showinfo("Alarm Code","Code Accepted, enabling alarm.")
                alarmStatus = "On"
                writeStatus(alarmTriggered, alarmStatus)
                print(alarmStatus)
                sensorChoice = (sensor_option.get())
                print(sensorChoice)
                alarmActive(root)
        elif (userEntered == alarmCode) and (alarmStatus == "On"):
                tkinter.messagebox.showinfo("Alarm Code","Alarm is already activated")
        elif len(userEntered) <4:
                tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
        else:
                tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")
                
def disableCode(code_entry):
        global alarmStatus
        global userEntered
        userEntered = (code_entry.get())
        print(userEntered)
        code_entry.delete(0, END)
        if (userEntered == alarmCode) and (alarmStatus == "On"):
                tkinter.messagebox.showinfo("Alarm Code","Code Accepted, Disabling alarm")
                alarmStatus = "Off"
                writeStatus(alarmTriggered, alarmStatus)
                alarmDisable(11, TRUE)
        elif (userEntered == alarmCode) and (alarmStatus == "Off"):
                tkinter.messagebox.showwarning("Alarm Code", "Unable to disable alarm. Alarm is not enabled.")
        elif len(userEntered) <4:
                tkinter.messagebox.showwarning("Alarm Code", "Code must be four digits long")
        else: 
                tkinter.messagebox.showwarning("Alarm Code", "Code incorrect,please try again")


def alarmActive(root,period=0):
        global flash
        redLED(11, FALSE)
        if(period <30) and (alarmStatus is "On"):
                greenLED(15, flash)
                flash = not flash
                period +=1
                print(period)
                root.after(500, lambda: alarmActive(root, period))
        elif (alarmStatus == "Off"):
                print("Alarm disabled before activation")
                alarmDisable(11, TRUE)
        
        else:
                greenLED(15, TRUE)
                print("Alarm now active")
                alarmLive(root)
                
                
               
def alarmDisable(pin, mode):
        print ("Alarm Disabled")
        alarmTriggered = False
        writeStatus(alarmTriggered, alarmStatus)
        greenLED(15, FALSE)
        redLED(pin, mode)

def alarmLive(root):
        global alarmTriggered
        frontSensor = GPIO.input(16)
        backSensor = GPIO.input(18)
        print(frontSensor, backSensor)
        while (alarmStatus is 'On'):
                if (sensorChoice == 'Both') and (frontSensor == True) or (backSensor == True):
                        alarmTriggered = True
                        break
                elif (sensorChoice == 'Front') and (frontSensor == True):
                        alarmTriggered = True
                        break
                elif (sensorChoice == 'Back') and (backSensor == True):
                        alarmTriggered = True
                        break
                else:
                        alarmTriggered = False
                        break
        writeStatus(alarmTriggered, alarmStatus)

        if (alarmTriggered is True):
                motionDetected(root)
        elif (alarmStatus is 'On'):
                root.after(1000, lambda: alarmLive(root))
        
        elif (alarmStatus == "Off"):
                alarmDisable(11, TRUE)

def motionDetected(root, period=0):
        global flash
        if (alarmStatus is 'On') and (period <15):
                period +=1
                print(period)
                root.after(1000, lambda: motionDetected(root, period))
        if (alarmStatus is 'On') and (period >=15):
                greenLED(15, FALSE)
                redLED(11, flash)
                flash = not flash
                period +=1
                print(period, '2')
                root.after(500, lambda: motionDetected(root, period))
        elif (alarmStatus == "Off"):
                alarmDisable(11, TRUE)
                
                
                        
        
def writeStatus(alarmTriggered, alarmStatus):
        triggered = str(alarmTriggered)
        status = str(alarmStatus)
        try:
                f = open("alarm.txt", "w")
                try:
                        f.write(status + "\n" + triggered)
                finally:
                        f.close()
        except IOError:
                pass
        
        
        
        
        
        
        
        


                
                
        
