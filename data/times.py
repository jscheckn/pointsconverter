import csv
import json

def make_json(csvFilePath, jsonFilePath):
    
    # create a dictionary
    data = {}
    
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
            
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['Entries']
            data[key] = rows

    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        
# Driver Code

# Decide the two file paths according to your 
# computer system
csvFilePath = 'SwimTimes.csv'
jsonFilePath = 'Times.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)