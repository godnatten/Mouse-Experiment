
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

#Define instruction message
instruction = '''Welcome to our Experiment!
In a moment 