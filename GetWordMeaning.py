import json
from difflib import get_close_matches

def fetchMeaning(jsonfile,meaningFor):
    data = json.load(open(jsonfile))
    data = {k.lower(): v for k,v in data.items()}
    if meaningFor.lower() in data.keys():
        return data.get(meaningFor.lower())
    elif len(get_close_matches(meaningFor.lower(),data.keys())) > 0:
        return "Did you mean",get_close_matches(meaningFor.lower(),data.keys())   
    else :
        return "Word",meaningFor.upper(),"dosent exists, please try again"   

word = input("Enter the word:")
print (fetchMeaning("dataset.json",word))