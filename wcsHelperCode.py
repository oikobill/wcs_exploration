# this demo code shows how to import data (e.g. naming, foci, chip information) from WCS into Python
# Code provided by Joshua Abbott and should not be redistributed without permission
# It assumes files such as term.txt are uploaded in the folder 'WCS_data' under the same directory where the script is

import numpy as np
from pprint import pprint

# load WCS data
import wcsHelperFunctions as wcs

# read in the WCS naming data into a format of namingDictionary[languageNumber][speakerNumber][chipNumber] = languageTerm
namingDictionary = wcs.readNamingData('./WCS_data_partial/term.txt')

# read in the WCS foci data into a format of fociDictionary[languageNumber][speakerNumber][languageTerm].append(WCSgridCoord)
fociDictionary = wcs.readFociData('./WCS_data_partial/foci-exp.txt')

# read in WCS chip data (330 chips) into two formats: cnumDictionary[row/col] = chipNumber, and cnameDictionary[chipNumber] = (row,col)
cnumDictionary, cnameDictionary = wcs.readChipData('./WCS_data_partial/chip.txt')

# read in speaker information
speakerDictionary = wcs.readSpeakerData('./WCS_data_partial/spkr-lsas.txt')


# read in cielab coordinates
clabDictionary = wcs.readClabData('./WCS_data_partial/cnum-vhcm-lab-new.txt')

