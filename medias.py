from connection import *
from tabulate import tabulate

def createMedia():
    mediaName = input("Mention type of media")
    mTable = get_media()
    mediaQuery = {"media_name" : mediaName}
    resp = mTable.insert_one(mediaQuery)
    if resp.acknowledged:
        print("Media Added Succsessfully!")

def updateMedia():
    all_data = viewAllMedia()
    selOpt = input("Please enter ID to update name")
    try:
        selOpt = int(selOpt)
        selectedName = all_data[selOpt]
        print("Leave blank if don't want to update name")
        albumName = input(f'Update name for {selectedName[1]} : ')
        myQuery = { 
        "$set": { 
            "media_name" : selectedName[1] if not albumName else albumName
            }
        }
        oroginalVal = {"media_name" : selectedName[1]}
        fetch_collection = get_media()
        fetch_collection.update_one(oroginalVal,myQuery)

    except :
        print("Number must be integer")


def viewAllMedia():
    mtable = get_media()
    fetch_data = mtable.find()
    all_rows = []
    for index, x in enumerate(fetch_data):
        rows = [index,x["media_name"]]
        all_rows.append(rows)
    col_headers = ["ID","Media Name"]
    print(tabulate(all_rows,col_headers,tablefmt="grid"))
    return all_rows

def deleteMedia():
    all_data = viewAllMedia()
    selecopt = input("Enter ID to delete Media")
    try:
        selecopt = int(selecopt)
        selectedVal = all_data[selecopt]
        msgConfirm ="""Do you really want to Delete this entry?
            Warning: It will remove all dependant entries from other places too
            By typing "Yes", please confirm it.(yes/no)"""
        confirmVal = input(msgConfirm)
        if confirmVal.lower() == "yes":
            myQuery = {"media_name" : selectedVal[1]}
            mtable = get_media()
            mtable.delete_one(myQuery)
        else:
            print("Deletion Cancelled")

    except :
        print("Wrong ID mentioned")

def checkMedias(mediaAction):
    if mediaAction == 1:
        # print(1)
        createMedia()
    elif mediaAction ==2 :
        # print(2)
        updateMedia()
    elif mediaAction == 3:
        # print(3)
        deleteMedia()
    elif mediaAction == 4:
        # print(4)
        viewAllMedia()
    else:
        print("we have only 4 options.")