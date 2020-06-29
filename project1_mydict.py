#Making my own dictionary
import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    w=w.title()
    if w in data:
        return data[w]
    elif w.upper() in data: #in case user enters words like USA
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        var= input("Did you mean %s instead?Press Y for Yes to Continue and N for No : "%get_close_matches(w,data.keys())[0])
        if var == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "Please enter the correct word"


    else:
        return "The word doesn't exist"
word=input("Enter word:")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
