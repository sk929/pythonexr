#profanity checker

import urllib

def read_text():
    quotes = open('C:\\Python27\\file\\prof.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
        connection =urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
        output = connection.read()
        connection.close
        
        if "true" in output:
            print("AlERT!!  ........PROFANITY FOUND")
        elif "false" in output:
            print("READY TO GO......DOCUMENT IS CURSEWORD FREE")
        else:
            print("could not open the file")
            
        

read_text()
