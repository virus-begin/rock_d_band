
from albums import *
from medias import *
from pymongo import MongoClient



def firstSelection():
    message = """Hi Quinn. Welcome to Album Area
    what you want to do?
    1. Add new Album.
    2. Update exiting Album.
    3. Delete Album.
    4. List all Albums."""
    albumsel = input(message)
    # try:
    albumsel = int(albumsel)
    checkalbums(albumsel)
    selection()
    # except:
    #     print("Enter number 1 or 2 or 3 or 4....")

def secondSelection():
    message = """Hi Quinn, Welcome to Media room.
    Select option for action
    1. Add new Media
    2. Update Media
    3. Delete Media
    4. View all Media"""
    mediaSel = input(message)
    try:
        mediaSel = int(mediaSel)
        checkMedias(mediaSel)        
        selection()
    except:
        print("Enter number 1 or 2 or 3 or 4")
def selection():
    startMessage = """Hi Quinn,
    Select main area to check.
    1. Album
    2. Media
    3. Venue
    4. Records Sellings
    5. Exit
    Enter Number : """
    firstOpt = input(startMessage)
    try:
        firstOpt  = int(firstOpt)
    except :
        print("Enter number 1 or 2 or 3 or 4")
    if firstOpt ==1 :
        firstSelection()
    elif firstOpt == 2:
        print("Option 2 selected")
        # secondSelection()
    elif firstOpt ==3:
        print("Option 3 selected")
        # thirdSelection()
    elif firstOpt ==4:
        print("Option 4 selected")
        # forthSelection()
    elif firstOpt == 5:
        exit(0)
    else:
        print("Number must be between 1-4! ")


if __name__ == "__main__":
    selection()