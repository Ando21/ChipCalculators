# program to calculate DOC and WOC numbers
import math
from guizero import *
####################################################################################
# Define functions

def WOCcalc():
    Chip_Thin_Factor = float( math.sqrt((1-(1-((2*(float( WOC.get() ))/float( Diameter.get() ))**2)))) )
    RPM = float(SFM.get()) * float( 3.82 ) / float( Diameter.get() )
    Regular_Feed_Rate = float(TeethNum.get()) * float(Desired_Chip_Thickness.get()) * float(RPM)
    Median_Chip_Thickness = float( Desired_Chip_Thickness.get() ) * float( Chip_Thin_Factor )
    WOC_FR_Multiplier = float( Desired_Chip_Thickness.get() ) / float( Median_Chip_Thickness )
    Adjusted_Feedrate = float( TeethNum.get() ) * float( Desired_Chip_Thickness.get() ) * float( RPM ) * float( WOC_FR_Multiplier )
    MRR = float(WOC.get()) * float(DOC.get()) * float(Adjusted_Feedrate)
    Feed_Time_minutes = float( Feed_Distance.get() ) / float( Adjusted_Feedrate )
    result.set(str(Median_Chip_Thickness))
    result1.set(str(WOC_FR_Multiplier))
    result2.set(str(RPM))
    result3.set(str(Regular_Feed_Rate))
    result4.set(str(Adjusted_Feedrate))
    result5.set(str(MRR))
    result6.set(str(Feed_Time_minutes))
    
def DOCcalc():
    #calculations
    if float(DOCd.get()) > float(InsertRadius.get()):
        Error = 'ERROR: DOC must be smaller'
        Error2 = 'than Insert Radius'
        result15.set(str(Error))
        result16.set(str(Error2))
        DOCcalc()
    elif float(DOCd.get()) <= float(InsertRadius.get()):
        result15.set(str(''))
        result16.set(str(''))
    DiameterDOC = float((float(CutterDiam.get())-(2*float(InsertRadius.get())))+(2*(math.sqrt(((float(InsertRadius.get())**2)-float(DOCd.get())**2)))))
    Blank = float(CutterDiam.get())-(2*(math.sqrt(((float(InsertRadius.get())**2)-(float(DOCd.get())**2)))))
    ActualChipThick = math.sqrt(float(DOCd.get())/float(InsertRadius.get()))*float(ChipThick.get())
    DOC_FR_Multiplier = float(ChipThick.get()) / float(ActualChipThick)
    RegRPM = (float(SFMd.get())*3.82)/float(CutterDiam.get())
    RegFeedRate = float(NumTeeth.get()) * float(RegRPM) * float(ChipThick.get())
    AdjRPM = (float(SFMd.get()) * 3.82)/(float(CutterDiam.get())-(2*(math.sqrt((float(InsertRadius.get())**2)-(float(DOCd.get())**2)))))
    AdjFeedRate = float(NumTeeth.get()) * RegRPM * float(ChipThick.get()) * float(DOC_FR_Multiplier)
    MRRd = float(AdjFeedRate) * float(CutterDiam.get()) * float(DOCd.get())
    result7.set(str(DiameterDOC))
    result8.set(str(ActualChipThick))
    result9.set(str(DOC_FR_Multiplier))
    result10.set(str(RegRPM))
    result11.set(str(RegFeedRate))
    result12.set(str(AdjRPM))
    result13.set(str(AdjFeedRate))
    result14.set(str(MRRd))

####################################################################################
# Set up app
app = App("Chip Caclulators", layout='grid', height=500, width=600)

####################################################################################
# WOC  GUI Section
# Labels and inputs
WOC_app_label = Text(app, text='WOC Calculator:', grid=[0,0], align='left', size=20, color='#34495E')
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

# WOC Output and labels
MCT_label = Text(app, text='Median Chip Thickness:', grid=[10,0], align='left')
WOC_FR_label = Text(app, text='WOC FR Multiplier:', grid=[11,0], align='left')
RPM_label = Text(app, text='RPM:', grid=[12,0], align='left')
RFR_label = Text(app, text='Regular Feed Rate:', grid=[13,0], align='left')
AFR_label = Text(app, text='Adjusted Feed Rate:', grid=[14,0], align='left')
MRR_label = Text(app, text='MRR:', grid=[15,0], align='left')
FTmin_label = Text(app, text='Feed Time (min):', grid=[16,0], align='left')

# WOC Calculate and results
WOCButton = PushButton(app, WOCcalc, text="Calculate WOC", grid=[8,0])
Result_label = Text(app, text='WOC Results:', grid=[9,0], align='left', size=16, color='#D35400')
result = Text(app, grid=[10,1], align='left')
result1 = Text(app, grid=[11,1], align='left')
result2 = Text(app, grid=[12,1], align='left')
result3 = Text(app, grid=[13,1], align='left')
result4 = Text(app, grid=[14,1], align='left')
result5 = Text(app, grid=[15,1], align='left')
result6 =Text(app, grid=[16,1], align='left')

####################################################################################
# DOC GUI Section
# Labels and inputs
DOC_app_label = Text(app, text='DOC Calculator:', grid=[0,3], align='left', size=20, color='#34495E')
CutterDiam_label = Text(app, text='Cutter Diameter:', grid=[1,3], align='left')
CutterDiam = TextBox(app, grid=[1,4], align='left', width=10)
NumTeeth_label = Text(app, text='Number of Teeth:', grid=[2,3], align='left')
NumTeeth = TextBox(app, grid=[2,4], align='left', width=10)
InsertRadius_label = Text(app, text='Insert Radius:', grid=[3,3], align='left')
InsertRadius = TextBox(app, grid=[3,4], align='left', width=10)
SFMd_label = Text(app, text='SFM:', grid=[4,3], align='left')
SFMd = TextBox(app, grid=[4,4], align='left', width=10)
DOCd_label = Text(app, text='DOC:', grid=[5,3], align='left')
DOCd = TextBox(app, grid=[5,4], align='left', width=10)
ChipThick_label = Text(app, text='Chip Thickness:', grid=[6,3], align='left')
ChipThick = TextBox(app, grid=[6,4], align='left', width=10)

# DOC output labels
DiameterDOC_label = Text(app, text='Diameter @ DOC:', grid=[10,3], align='left')
ActualChipThick_label = Text(app, text='Actual Chip Thickness:', grid=[11,3], align='left')
DOC_FR_Multiplier_label = Text(app, text='DOC FR Multiplier:', grid=[12,3], align='left')
RegRPM_label = Text(app, text='Regular RPM:', grid=[13,3], align='left')
RegFeedRate_label = Text(app, text='Regular Feed Rate:', grid=[14,3], align='left')
AdjRPM_label = Text(app, text='Adjusted RPM:', grid=[15,3], align='left')
AdjFeedRate_label = Text(app, text='Adjusted Feed Rate:', grid=[16,3], align='left')
MRRd_label = Text(app, text='MRR:', grid=[17,3], align='left')

# DOC Caclucate and results
DOCButton = PushButton(app, DOCcalc, text="Calculate DOC", grid=[8,3])
Result_label2 = Text(app, text='DOC Results:', grid=[9,3], align='left', size=16, color='#D35400')
result7 = Text(app, grid=[10,4], align='left')
result8 = Text(app, grid=[11,4], align='left')
result9 = Text(app, grid=[12,4], align='left')
result10 = Text(app, grid=[13,4], align='left')
result11 = Text(app, grid=[14,4], align='left')
result12 = Text(app, grid=[15,4], align='left')
result13 = Text(app, grid=[16,4], align='left')
result14 = Text(app, grid=[17,4], align='left')
result15 = Text(app, grid=[18,3], align='left', color='red', size=12)
result16 = Text(app, grid=[19,3], align='left', color='red', size=12)

# Display app
app.display()
