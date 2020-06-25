import json
from difflib import get_close_matches
word=str(input("Enter the word you want to search - "))
obj = json.load(open("original.json"))
word = word.lower()
if word in obj: 
         print(word,"means:-")
         if type(obj[word]) == list:
          for item in obj[word]:
            print(item)
         else:
             print(obj[word])
elif len(get_close_matches(word , obj.keys())) > 0 :
              print("did you mean",get_close_matches(word, obj.keys())[0],"instead")
              decide = input("press y for yes or n for no - ")
              if decide == "y":
                  print(word,"means:-")
                  if type(obj[get_close_matches(word , obj.keys())[0]]) == list:
                      for item in obj[get_close_matches(word , obj.keys())[0]]:
                          print (item)
              elif decide=="n":
                  print("word does not exist")
else:
    print("word does not exist")