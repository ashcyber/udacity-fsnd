"""
    Udacity fsnd
    practice problem 1
    lesson 6 

"""

import urllib

def read_text():
    quotes = open("movie_quotes.txt") 
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    print
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print("Profanity Status: " + output)
    connection.close()


read_text()
