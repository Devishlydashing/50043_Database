# ADDING LOGS
import time

def add_log(query_type, query, response, response_code, col):
    time_stamp = time.time()
    # insert into collection of database
    insert_in = {
        "time_stamp": time_stamp, # TIME
        "query_type": query_type, # POST or GET
        "query": query, # URL of request
        "response": response, # book title added (for adding book) / Name of book searched (for searching book)
        "response_code": response_code # add user
    }
    # insert into collection of database
    col.insert_one(insert_in)
    
