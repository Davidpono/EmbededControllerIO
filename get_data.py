
import xml.etree.ElementTree as ET
import csv
import os
import re

from BaseIO import BaseIO
from makexml import makexml


# Define the process_string function
global script_dir
script_dir = os.path.dirname(os.path.abspath(__file__))
from datetime import datetime

def current_datetime_with_seconds():
    return datetime.now().strftime("%Y%m%d_%H%M%S.xml")  # Using underscores (_) instead of spaces, removing colon (:)
def iopinString(iopin):
    letters = re.findall('[A-Za-z]+', iopin)  # Extract letters
    numbers = re.findall('[0-9]+', iopin)  # Extract numbers
    return ' '.join(letters) + " " + ' '.join(numbers)
    

def get_data(filename):
    
    """
    Parses a CSV file and checks if a condition is met, then edits the XML file accordingly.

    Args:
        filename: The filename of the CSV file.
        NewVaVName: The new name to replace in the XML file.
        XMLFILE: The filename of the XML file to edit.

    Returns:
        The number of rows in the CSV file (excluding header).
    """
    output = current_datetime_with_seconds()
    newxmlIOfolder = fr"C:\Users\ponced\IO Creator\CreatedIO\{output}"
    makexml(newxmlIOfolder)
    ListOfVals=[]
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            type = "0"  # Initialize type variable
            iopin = "0"  # Initialize iopin variable
            COVIncrement = "1"  # Initialize COVIncrement variable
            MaxPresValue = "0"  # Initialize MaxPresValue variable
            MinPresValue = "0"  # Initialize MinPresValue variable
            VarName = "0"  # Initialize VarName variable
            Description = "0"  # Initialize Description variable
            offset = "0"  # Initialize offset variable
            ElecTopOfScale = "0"  # Initialize ElecTopOfScale variable
            EngBottomOfScale = "0"  # Initialize EngBottomOfScale variable
            EngTopOfScale = "0"  # Initialize EngTopOfScale variable
            ThermistorType = "0"  # Initialize ThermistorType variable
            ActiveText =  "ALARM"
            InactiveText = "NORMAL"
            
            # Skip the header row
            next(reader, None)
            i = 0
            for row in reader:
                i += 1
                
                if row[8] in ListOfVals:
                    print("Duplicated value")
                    
                else:
                    iopin=iopinString(row[6])
                    VarName=row[8]
                    type=row[14]
                    EngBottomOfScale=row[16]
                    EngTopOfScale = row[17]
                    ThermistorType=row[15]
                    ActiveText=row[19]
                    InactiveText=row[20]
                    BaseIO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder)
                    ListOfVals.append(row[8])

                 
            
            return i  # Count the rows excluding header
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return 0  # Indicate error by returning 0

# Example usage

