from connection import *
from datetime import date,datetime

def createVenue():
    print("Please mention following Details: ")
    vname = input("Venue Name")
    vlocation = input("Venue location")
    vaddress = input("Venue Address")
    vdate = input("Venue Perfomance Date (YYYY/DD/MM)")
    # try:
    vdate = datetime.strptime(vdate,'%Y/%d/%m')
    myquery = {
        "venue_name" : vname,
        "venue_location" : vlocation,
        "venue_add" : vaddress,
        "venue_date" : vdate
    }
    vtable = get_venue()
    resp = vtable.insert_one(myquery)
    if resp.acknowledged:
        print("Venue Details added successfully.")

    # except ValueError:
    #     print("Please enter valid date")

def updateVenue():
    all_data = viewAllVenue()
    selOpt = input("please enter ID to update venue details")
    # try:
    selOpt = int(selOpt)
    selectVal = all_data[selOpt]
    print("Mention values to Update. Keep blank if not to change")
    vname = input(f'Old Value {selectVal[1]} change to :')
    vloc = input(f'Old Value {selectVal[2]} change to :')
    vadd = input(f'Old Value {selectVal[3]} change to :')
    vdate = input(f'Old value {selectVal[4]} change to :')
    updateVal = {
        "$set":{
            "venue_name" :selectVal[1] if not vname else vname,
            "venue_location" : selectVal[2] if not vloc else vloc,
            "venue_add" : selectVal[3] if not vadd else vadd,
            "venue_date" : selectVal[4] if not vdate else vdate
        }
    }
    orgVal = {
        "venue_name" : selectVal[1],
        "venue_location" : selectVal[2],
        "venue_add" : selectVal[3],
        "venue_date" :selectVal[4]
    }
    fetch_collection = get_venue()
    fetch_collection.update_one(orgVal,updateVal)

    # except :
        # print("Error message")


def viewAllVenue():
    all_rows = []
    fetch_collection = get_venue()
    all_data = fetch_collection.find()
    for i,x in enumerate(all_data):
        rows = [i,x["venue_name"],x["venue_location"],x["venue_add"],x["venue_date"]]
        all_rows.append(rows)
    col_headers = ["ID","Venue Name", "Location", "Address" ,"Date"]
    print(tabulate(all_rows,col_headers,tablefmt="grid"))
    return all_rows

def deleteVenue():
    all_data = viewAllVenue()
    selOpt = input("Enter ID for delete Venue")
    # try:
    selOpt = int(selOpt)
    selctedID = all_data[selOpt]
    confirmMesg ="""Do you really want to Delete this entry?
    Warning: It will remove all dependant entries from other places too
    By typing "Yes", please confirm it.(yes/no)"""
    confirmAns = input(confirmMesg)
    if confirmAns.lower() == 'yes':
        myquery = {"venue_name" : selctedID[1]}
        fetch_collection = get_venue()
        fetch_collection.delete_one(myquery)
    # except:
    #     print("Error message")

def checkVenues(selAction):
    if selAction ==1 :
        createVenue()
    elif selAction == 2:
        updateVenue()
    elif selAction == 3:
        deleteVenue()
    elif selAction == 4:
        viewAllVenue()
    else:
        print("Please Check entered option")