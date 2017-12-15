# program to calculate DOC and WOC numbers
import math
from guizero import *

# Define function
def WOCcalc():
    Chip_Thin_Factor = float( math.sqrt((1-(1-((2*(float( WOC.get() ))/float( Diameter.get() ))**2)))) )
    RPM = float(SFM.get()) * float( 3.82 ) / float( Diameter.get() )
    Regular_Feed_Rate = float(TeethNum.get()) * float(Desired_Chip_Thickness.get()) * float(RPM)
    Median_Chip_Thickness = float( Desired_Chip_Thickness.get() ) * float( Chip_Thin_Factor )
    WOC_FR_Multiplier = float( Desired_Chip_Thickness.get() ) / float( Median_Chip_Thickness )
    Adjusted_Feedrate = float( TeethNum.get() ) * float( Desired_Chip_Thickness.get() ) * float( RPM ) * float( WOC_FR_Multiplier )
    MRR = float(WOC.get()) * float(DOC.get()) * float(Adjusted_Feedrate)
    Feed_Time_minutes = float( Feed_Distance.get() ) / float( Adjusted_Feedrate )
    result.set(str('Median Chip Thickness: ' + str(Median_Chip_Thickness)))
    

# Set up app
app = App("Chip Caclulators", layout='grid')

# WOC  GUI Section
# Labels and inputs
WOC_app_label = Text(app, text='WOC Calculator:', grid=[0,0], align='left')
Diamter_label = Text(app, text='Diameter:', grid=[1,0], align='left')
Diameter = TextBox(app, grid=[1,1], align='left', width=10)
TeethNum_label = Text(app, text='Number of Teeth:', grid=[2,0], align='left')
TeethNum = TextBox(app, grid=[2,1], align='left', width=10)
SFM_label = Text(app, text='SFM:', grid=[3,0], align='left')
SFM = TextBox(app, grid=[3,1], align='left', width=10)
WOC_label = Text(app, text='WOC:', grid=[4,0], align='left')
WOC = TextBox(app, grid=[4,1], align='left', width=10)
DOC_label = Text(app, text='DOC:', grid=[5,0], align='left')
DOC = TextBox(app, grid=[5,1], align='left', width=10)
Desired_CT_label = Text(app, text='Desired Chip Thickness:', grid=[6,0], align='left')
Desired_Chip_Thickness = TextBox(app, grid=[6,1], align='left', width=10)
FeedDist_label = Text(app, text='Feed Distance:', grid=[7,0], align='left')
Feed_Distance = TextBox(app, grid=[7,1], align='left', width=10)


# Calculate and results
WOCButton = PushButton(app, WOCcalc, text="Calculate WOC", grid=[8,0])
Result_label = Text(app, text='Results:', grid=[9,0], align='left')
result = TextBox(app, grid=[10,0], align='left', width=20)


# Display app
app.display()

####
##    # prints
##    #print('Median Chip Thickness: ' + str(Median_Chip_Thickness))
##    print('WOC FR Multiplier: ' + str(WOC_FR_Multiplier))
##    print('RPM: ' + str(RPM))
##    print('Regular Feed Rate: ' + str(Regular_Feed_Rate))
##    print('Adjusted Feed Rate: ' + str(Adjusted_Feedrate))
##    print('MRR: ' + str(MRR))
##    print('Feed Time (min): ' + str(Feed_Time_minutes))





















