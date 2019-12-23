from connection import *


def createAlbum():
    print("Please mention following details:")
    albumName = input("Album Name: ")
    albumYear = input("Album Year")
    albumsongs = input("Total Songs in it")
    albumLength = input("CDs Length")
    tableName = get_album()
    albumDetails = {
        "name": albumName,
        "year": albumYear,
        "totalSongs": albumsongs,
        "cds": albumLength
    }
    # print(albumDetails, tableName)
    resp = tableName.insert_one(albumDetails)
    if resp.acknowledged:
        print("Album entry created Successfully.")

def viewAlbums():
    arr_rows =[]
    fetch_collection = get_album()
    fetch_data = fetch_collection.find()
    for index,x in enumerate(fetch_data):
        rows = [index,x["name"],x["year"],x["totalSongs"],x["cds"]]
        arr_rows.append(rows)
    
    col_headers = ["ID","Album Name","Year", "Total Tracks", "CDs"]
    print(tabulate(arr_rows,col_headers,tablefmt="grid"))
    return arr_rows

def updateAlbum():
    all_data = viewAlbums()
    selOpt = input("Please enter ID to update Album entry")
    # try:
    selOpt = int(selOpt)
    updateVal = all_data[selOpt]
    print("Leave blank if nothing want to change")
    albumName = input(f'Mention updated Album Name for {updateVal[1]} : ')
    albumYear = input(f'Mention updated year for Year {updateVal[2]} : ')
    tracks = input(f'Mentione tracks in current albums {updateVal[3]} : ')
    cdsVal = input(f'Mention Updated CDs count for Album {updateVal[4]} : ')
    query = {"$set":
        {
            "name": updateVal[1] if not albumName else albumName,
            "year": updateVal[2] if not albumYear else int(albumYear),
            "totalSongs":updateVal[3] if not tracks else int(tracks),
            "cds": updateVal[4] if not cdsVal else int(cdsVal)
        }   
    }
    originalValue = {
        "name":updateVal[1],
        "year":updateVal[2],
        "totalSongs":updateVal[3],
        "cds":updateVal[4]
    }
    # print(query,originalValue)
    fetch_collection = get_album()
    fetch_collection.update_one(originalValue,query)

    # except:
    #     print("Please Enter value in integer")

def deleteAlbum():
    all_data = viewAlbums()
    selOpt = input("Please Enter ID to Delete Album Entry")
    try:
        selOpt = int(selOpt)
        selctedID = all_data[selOpt]
        confirmMesg ="""Do you really want to Delete this entry?
        Warning: It will remove all dependant entries from other places too
        By typing "Yes", please confirm it.(yes/no)"""
        confirmval = input(confirmMesg)
        if confirmval.lower() == "yes":
            myquery = {"name": selctedID[1]}
            fetch_album = get_album()
            # fetch_records = get_records()
            # fetch_records.delete_many({"albumName": selctedID[1]})
            fetch_album.delete_one(myquery)
        else:
            print("Delete operation Cancelled")

    except:
        print("Please mention only integer Value")

def checkalbums(albumAction):
    if albumAction == 1:
        createAlbum()
    elif albumAction == 2:
        # print("Option 2 selected")
        updateAlbum()
    elif albumAction == 3:
        # print("Option 2 selected")
        deleteAlbum()
    elif albumAction == 4:
        # print("Option 2 selected")
        viewAlbums()
    else:
        print("Album Actions selection must be between 1-4! ")
