# from pymongo import MongoClient
# from tabulate import tabulate
#
# client = MongoClient('localhost', 27017)
# db_name = client.jobs_list
# lists = db_name.job_entries


from pymongo import MongoClient
from tabulate import tabulate

clientConn = MongoClient('localhost', 27017)
db_name = clientConn.clubRecords


def get_album():
    album_tables = db_name.albums
    return album_tables

def get_venue ():
    venue_tables = db_name.venue
    return venue_tables

def get_records():
    records_tables = db_name.records
    return records_tables

def get_media():
    media_tables = db_name.media
    return media_tables