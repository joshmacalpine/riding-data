y = open("2021.csv", "w")

csv = ","

with open("EventResults.txt") as infile:
    for line in infile:
        x = line.split("	")
        if(x[3]=="validated"):
            y.write(x[0] + csv + x[1] + csv + x[3] +  csv + x[8] + csv + x[11] + csv + x[10] + csv + x[13])
        
    
for item in x:
	y.write(item + "\n")


y.close()
