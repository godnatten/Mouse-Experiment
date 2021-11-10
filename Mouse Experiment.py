
### Mouse Experiment ###
## Portfolio 3 ##
# 
# 19-11-2021


# Load relevant packages
from psychopy import core, visual, event, gui, data

#Import relevant packages
import glob  #Import package that can group filename from a folder (like list.files in R)
import random #import package to randomize stimuli
import pandas as pd  #import package that enable dataframes

# DEfining gui 
dialog = gui.Dlg (title = "The ... Experiment")
dialog.addField("Participant ID:")
dialog.addField("Age:")
dialog.addField("Gender:", choices = ["female", "male", "other"]) #making a drop down menu
dialog.show()
if dialog.OK: 
    ID = dialog.data[0]
    Age = dialog.data[1]
    Gender = dialog.data[2]
elif dialog.Cancel:
    core.quit
print(ID,Age,Gender)


#Defining window
win = visual.Window(color = "black", fullscr = True)

#Defining columns for dataframe
cols = ["Participant ID", "Age","Gender", "Word"]

#define empty dataframe
logfile = pd.DataFrame(columns = cols)

#defining date to make a unique string for each dataframe - avoiding overwrites
date = data.getDateStr()

#Save data to harddrive
logfile_name = "logfiles/logfile_{}_{}.csv".format(ID,date)

#defining date
date = data.getDateStr() 

#Define instruction message
instruction = '''Welcome to our Experiment! Thank you for participating!
In a moment you will see a picture and will be asked to rate this picture on a scale from 0-10, with 10 being the most positive and 0 being the most negative.

Press any key when you are ready. If you have any questions or feell any discomfort during the test please contact the researcher. 
'''

#Defining goodbye message
goodbye = ''' 
The experiment is done. Thank you for your participation.'''

#defining functions - show text and wait for key press
def msg(txt):
    message = visual.TextStim(win, text = txt, alignText = "left", height = 0.05)
    message.draw()
    win.flip()
    event.waitKeys()

#Show instructions
msg(instruction)

#Defining stimulus
path = "folder/"
stimuli = glob.glob("folder/mouse.jpg")
print(stimuli)

#Get 
def = show(image): 
    img = visual.ImageStim(win,stimuli):
    img.draw()
    win.flip()
    event.waitKeys()

show(stimuli)