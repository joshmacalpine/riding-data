f = open("CR2016Geo.json", "r")
y = open("geo.csv", "w")
x=f.read()

x=x.split("[[")[1].split("]]")[0].split("],[")

for item in x:
	y.write(item + "\n")


y.close()
f.close()