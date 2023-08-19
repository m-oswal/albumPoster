import csv

def prompt():
    li=[]
    with open("albums.csv") as file:
        x = csv.reader(file)
        for i in x:
            li.append((i[0],i[1]))
    return li