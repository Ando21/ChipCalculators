# program to calculate DOC and WOC numbers
import math

def WOCcalc():
    # get user input to set variables 
    Diameter = float(input("Diameter: "))
    TeethNum = float(input("Number of Teeth: "))
    SFM = float(input("SFM: "))
    WOC = float(input("WOC: "))
    DOC = float(input("DOC: "))
    Desired_Chip_Thickness = float(input("Desired Chip Thickness:"))
    Feed_Distance = float(input("Feed Distance:"))

    # calculations
    Chip_Thin_Factor = math.sqrt((1-(1-((2*WOC)/Diameter))**2))
    RPM = SFM * 3.82 / Diameter
    Regular_Feed_Rate = TeethNum * Desired_Chip_Thickness * RPM
    Median_Chip_Thickness = Desired_Chip_Thickness * Chip_Thin_Factor
    WOC_FR_Multiplier = Desired_Chip_Thickness / Median_Chip_Thickness
    Adjusted_Feedrate = TeethNum * Desired_Chip_Thickness * RPM * WOC_FR_Multiplier
    MRR = WOC * DOC * Adjusted_Feedrate
    Feed_Time_minutes = Feed_Distance / Adjusted_Feedrate
      
    # prints
    print('Median Chip Thickness: ' + str(Median_Chip_Thickness))
    print('WOC FR Multiplier: ' + str(WOC_FR_Multiplier))
    print('RPM: ' + str(RPM))
    print('Regular Feed Rate: ' + str(Regular_Feed_Rate))
    print('Adjusted Feed Rate: ' + str(Adjusted_Feedrate))
    print('MRR: ' + str(MRR))
    print('Feed Time (min): ' + str(Feed_Time_minutes))
    
def DOCcalc():
    # get user input to set variables 
    CutterDiam = float(input("Cutter Diameter DA: "))
    NumTeeth = float(input("Number of Teeth: "))
    InsertRadius = float(input("Radius of Insert: "))
    SFMd = float(input("SFM: "))
    DOCd = float(input("DOC: "))
    ChipThick = float(input("Chip Thickness: "))
    
    #calculations
    DiameterDOC = (CutterDiam-(2*InsertRadius))+(2*(math.sqrt(((InsertRadius**2)-DOCd**2))))
    Blank = CutterDiam-(2*(math.sqrt(((InsertRadius**2)-(DOCd**2)))))
    ActualChipThick = math.sqrt(DOCd/InsertRadius)*ChipThick
    DOC_FR_Multiplier = ChipThick / ActualChipThick
    RegRPM = (SFMd*3.82)/CutterDiam
    RegFeedRate = NumTeeth * RegRPM * ChipThick
    AdjRPM = (SFMd * 3.82)/(CutterDiam-(2*(math.sqrt((InsertRadius**2)-(DOCd**2)))))
    AdjFeedRate = NumTeeth * RegRPM * ChipThick * DOC_FR_Multiplier
    MRRd = AdjFeedRate * CutterDiam * DOCd
    
    # prints
    print('Diameter @ DOC: ' + str(DiameterDOC))
    print('Not Used: ' + str(Blank))
    print('Actual Chip Thickness: ' + str(ActualChipThick))
    print('DOC FR Multiplier: ' + str(DOC_FR_Multiplier))
    print('Regular RPM: ' + str(RegRPM))
    print('Regular Feed Rate: ' + str(RegFeedRate))
    print('Adjusted RPM: ' + str(AdjRPM))
    print('Adjusted Feed Rate: ' + str(AdjFeedRate))
    print('MRR: ' + str(MRRd))

# control flow
def ChipCalc():
    DOCchoice = (input("DOC Calculator? Y / N: "))
    if DOCchoice == ('Y' or 'y'):
        DOCcalc()
    elif (DOCchoice != 'Y' or 'y'):
        print('Running WOC Calculator instead')
        WOCcalc()


ChipCalc()

# used PyInstall to create a .exe version
# Process:
# Go to terminal and working directory of ChipCalc
# Type: Pyinstaller 'ChipCalc.py' -F
# This creates the .exe in the working directory 



  