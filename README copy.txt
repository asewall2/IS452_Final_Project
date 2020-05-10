This program is designed to extract the data from tweets on one's twitter timeline and create a human readable
csv file with them to be used for text analysis. Below are the steps to use this code:

1.) set up a Twitter developer account and create a new application. Then go to the "keys and tokens" page to extract
the information you need to connect to your own Twitter API.

2.) Install python 3.6 using a console of your choice.

3.)Open the twittercraping.py file.

4.) Make sure you have tweepy, json, and pathlib modules installed. If you do not already have them, go to your
computer's terminal and type "pip install tweepy" to install the module.

5.) Once all the packages are installed, go to lines 8-11 and insert your own Twitter API keys into the spaces labeled
the values area of the dictionary.

6.) Run the program. It should create a new file in your directory called "jsontweetchunks.json", this is a cleaned up
version of the json data from the twitter timeline presented as a list.

7.) Now that you have generated the json file, open the jsonparsing.py file. This file will take the data in the json
 file, parse it, and export it as a csv with the the "text" and "str_id" data points only.

8.) Run the program jsonparsing.py and generate the csv file.

9.) OPTIONAL, If there are other data points you want included in the csv, add a new datapoint after line 32 and insert the name
of the data point listed in the dictionary in the json file as a string. It will look something like:
 datapointX = clean_missing('name of data point', tweet)
