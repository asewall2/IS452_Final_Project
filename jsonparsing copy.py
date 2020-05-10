# 1.) import all the packages I need
import csv
import json


# 2.) write a function that will print missing if there is a missing data point using if else statements. Used to prevent
# code from breaking because of a missing value
def clean_missing(key, record):
    '''function will check if a provided key is inside a record
    and return either that value or the string value of missing.'''
    if key in record:
        result = record[key]
    else:
        result = 'missing'
    return result

# 3.) read in the json file I made in the twitterscraping.py file. This code is basically copied from the JSON lecture notes
# on the class github

infile = open('jsontweetchunks.json', 'r')
data = json.load(infile)
infile.close()

# 4.) write out the parsed json file into a csv file
outfile = open('twitter_data.csv', 'w', newline = '')
csvout = csv.writer(outfile)

# 5.) Create the headers for the csv file
csvout.writerow(['text', 'id_str'])

# 6.) Loop through it all, be sure to call on the function created earlier to debug missing values. This loop extracts
# the data points we want and puts them into the csv
for tweet in data:
    datapoint1 = clean_missing('text', tweet)
    datapoint2 = clean_missing('id_str', tweet)
    row = [datapoint1,datapoint2]
    csvout.writerow(row)



