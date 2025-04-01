#Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


print(sampleDict.get("class","student","marks","history"))#can use both ways!
print(sampleDict["class"]["student"]["marks"]["history"])#can use both ways!