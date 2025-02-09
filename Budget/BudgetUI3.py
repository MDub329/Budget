'''
Created 10/5/16
Matthew W
'''
'''
Changelog
*Integrate UI Main Push
*Custom % 2.0 Push
*Check for valid Input 2.0 Push
'''
from tkinter import *
import tkinter as tk
from tkinter import ttk

def Main(wrongentry, def_settings):
    win = tk.Tk()

    checkVariable = tk.IntVar()
    giveVariable = tk.DoubleVar()
    saveVariable = tk.DoubleVar()
    spendVariable = tk.DoubleVar()
    settingsVariable = tk.IntVar()

    #settingsVariable.set(1)

    checkLabel = ttk.Label(win,text = "  Check Amount  ", foreground = "blue")
    checkLabel.grid(row = 0 , column = 1)
    checkEntry = ttk.Entry(win, textvariable = checkVariable)
    checkEntry.grid(row = 1, column = 1, sticky = 'w')      

    if (def_settings == False):
        givelabel = ttk.Label(win,text = " Give %(Use Decimal) ", foreground = "blue")
        givelabel.grid(row = 3, column = 1, sticky = 'w')
        giveEntry = ttk.Entry(win, textvariable = giveVariable)
        giveEntry.grid(row = 4, column = 1, sticky = 'w')
    
        savelabel = ttk.Label(win,text = " Save %(Use Decimal) ", foreground = "blue")
        savelabel.grid(row = 3, column = 2, sticky = 'w')
        saveEntry = ttk.Entry(win, textvariable = saveVariable)
        saveEntry.grid(row = 4, column = 2, sticky = 'w')

        spendlabel = ttk.Label(win,text = " Spend %(Use Decimal) ", foreground = "blue")
        spendlabel.grid(row = 3, column = 3, sticky = 'w')
        spendEntry = ttk.Entry(win, textvariable = spendVariable)
        spendEntry.grid(row = 4, column = 3, sticky = 'w')

        gobutton = ttk.Button(text = "Go", command = lambda: Calc_Budget(checkVariable.get(), win, spendVariable.get(), giveVariable.get(), saveVariable.get()))
        gobutton.grid(row = 5, column = 3, sticky = 'w')
    else:
        settingsLabel = ttk.Label(win, text = "Default Settings: ")
        settingsEntry = ttk.Checkbutton(win, variable = settingsVariable) 
        settingsLabel.grid(row = 4 , column = 2 , sticky = 'w')
        settingsEntry.grid(row = 4, column = 3 , sticky = 'e')

        gobutton = ttk.Button(text = "Go", command = lambda: Choose_Settings(checkVariable.get(), win, spendVariable.get(), giveVariable.get(), saveVariable.get(), settingsVariable.get()))
        gobutton.grid(row = 5, column = 3, sticky = 'w')

    if(wrongentry == True):
        wrongentryLabel = ttk.Label(win, text = "  Error Make sure %'s &", foreground = "red")
        wrongentryLabel.grid(row = 0, column = 2, stick = 'w')
        wrongentryLabel2 = ttk.Label(win, text = "check amounts are valid ", foreground = "red")
        wrongentryLabel2.grid(row = 0, column = 3, stick = 'w')

    win.mainloop()

def Choose_Settings(check, win, spendpercent, givepercent, savepercent, settings):
       
    if (settings == 1):
        spendpercent = .4
        savepercent = .5
        givepercent = .1
        Calc_Budget(check,win,spendpercent,givepercent,savepercent)
    else:
        win.destroy()
        def_settings = False
        entry = False
        Main(entry,def_settings)

def Calc_Budget(check, win, spendpercent, givepercent, savepercent):
    
    win.destroy()
    win = tk.Tk()
    
        #If inputs are invalid call back and display error message on window
    if (((spendpercent + givepercent + savepercent) > 1) or (spendpercent + givepercent + savepercent) <= 0) or (check <= 0):
        win.destroy()
        entry = True
        def_settings = False
        Main(entry,def_settings)

    spend = spendpercent
    tithe = givepercent
    save = savepercent

    check = float(check) + 144.0 
    #money put into stock plan

    tithe_Total = float(check) * tithe
    spend_Total = float(check) * spend 
    save_Total = float(check) * save - 144
    #stock plan money out of saveings 
    if save_Total <= 0:
        savelabel = ttk.Label(win, text = "Save: Not enough to save")
        savelabel.grid(row = 0, column = 0, sticky = 'w')
    else:
        savelabel = ttk.Label(win, text =( "Save: $%.2f" % save_Total))
        savelabel.grid(row = 0, column = 0, sticky = 'w')
    tithelabel = ttk.Label(win, text = ("Give: $%.2f" % tithe_Total))
    tithelabel.grid(row = 1, column = 0, sticky = 'w')
    savelabel = ttk.Label(win, text = ("Spend: $%.2f" % spend_Total))
    savelabel.grid(row = 2, column = 0, sticky = 'w')
 
Main(wrongentry = False, def_settings = True)