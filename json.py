import json
def write_json(new_data,filename='data.json'):
    with open(filename,'r+') as file:
#The next line produces an error, says load is not a valid attribute:
        file_data=json.load(file)
        file_data["contacts"].append(new_data)
        file.seek(0)
        json.dump(file_data,file,indent=4)
y={ "fname":"Sam",
   "lname":"Cooke",
   "phone":"404-123-0005",
   "email":"scooke@noemail.com"
   }
write_json(y)
