import json
from difflib import get_close_matches

def fetchMeaning(jsonfile,meaningFor):
    data = json.load(open(jsonfile))
    data = {k.lower(): v for k,v in data.items()}
    if meaningFor.lower() in data.keys():
        return data.get(meaningFor.lower())
    elif len(get_close_matches(meaningFor.lower(),data.keys())) > 0:
        yesOrNo = input("Did you mean {} instead? Enter Yes Or No".format(get_close_matches(meaningFor.lower(),data.keys())))
        if  yesOrNo == "Yes":
            return data.get(meaningFor.lower()[0])
        elif  yesOrNo == "No":
            return "Word {} dosent exists, please try again".format(meaningFor.upper()) 
        else :
            return "wrong option entered"        
    else :
        return "Word {} dosent exists, please try again".format(meaningFor.upper())   

word = input("Enter the word:")
print (fetchMeaning("dataset.json",word))