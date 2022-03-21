data2021 = []
data2019 = []

def first(lst):
	return lst[0]
	
def second(lst):
	return float(lst[1])

def partyRank(item):
	if (str(item) == item):
		return 101
	else:
		return float(item[1])

	

def partyResult(party, lst):
	for item in lst:
		if(party==item[0]):
			return item[1]
	return 0
def ridingSearch():
	thing = input("Search for a riding:  ")
	for num in range(338):		
		if(data2021[num][0].find(thing)!=-1):
			print("2019:")
			print(data2019[num])
			print("2021:")
			print(data2021[num])
			#result = float(partyResult(thing2,data2021[num][1:]))-float(partyResult(thing2,data2019[num][1:]))
			#if(result>0):
			#	print("+" + str(result))
			#else:
			#	print(result)
			
def partySearch():
	thing2 = input("Enter a party: ")	
	lst2 = []
	for num in range(338):
		if ((partyResult(thing2,data2021[num][1:])!=0) or (partyResult(thing2,data2019[num][1:])!=0)):
			result = float(partyResult(thing2,data2021[num][1:]))-float(partyResult(thing2,data2019[num][1:]))
			if(result>0):
				result = "+" + str(result)[0:5]
			else:
				result = str(result)[0:6]
			lst2.append((data2021[num][0], result))
	lst2.sort(key=second)	
	for item in lst2:
		print(item)


with open("2021.csv") as infile:
	indep = 0
	riding = []
	for line in infile:
		app = True
		details = line.split(",")
		name = details[1].split("/")[0]
		if not riding:
			riding.append(name)
		elif riding[0] != name:
			if(indep>0):
				riding.append(("Other", str(indep)))
			data2021.append(riding.copy())
			riding.clear()
			indep = 0
			riding.append(name)
		percent = details[-3]
		party = details[3]
		if(party.find("Liberal")!=-1):
			party = "Liberal"
		elif(party.find("Conservative")!=-1):
			party = "Conservative"
		elif(party.find("NDP")!=-1):
			party = "NDP"
		elif(party.find("Green Party")!=-1):
			party = "Green"
		elif(party.find("People's")!=-1):
			party = "PPC"
		elif(party.find("Bloc Q")!=-1):
			party = "Bloc"
		else:
			party = "Other"
			indep+=float(percent)
			app = False
		if app:
			riding.append((party, str(percent)))
	if(indep>0):
		riding.append(("Other", str(indep)))
	data2021.append(riding.copy())

with open("2019.csv") as infile:
	indep = 0
	riding = []
	for line in infile:
		app = True
		details = line.split(",")
		name = details[1].split("/")[0]
		if not riding:
			riding.append(name)
		elif riding[0] != name:
			if(indep>0):
				riding.append(("Other", str(indep)))
			data2019.append(riding.copy())
			riding.clear()
			indep = 0
			riding.append(name)
		percent = details[-3]
		party = details[3]
		if(party.find("Liberal")!=-1):
			party = "Liberal"
		elif(party.find("Conservative")!=-1):
			party = "Conservative"
		elif(party.find("NDP")!=-1):
			party = "NDP"
		elif(party.find("Green Party")!=-1):
			party = "Green"
		elif(party.find("People's")!=-1):
			party = "PPC"
		elif(party.find("Bloc Q")!=-1):
			party = "Bloc"
		else:
			party = "Other"
			indep+=float(percent)
			app = False
		if app:
			riding.append((party, str(percent)))
	if(indep>0):
		riding.append(("Other", str(indep)))
	data2019.append(riding.copy())


	


data2019.sort(key=first)
data2021.sort(key=first)


for item in data2019:
	item.sort(key=partyRank,reverse=True)
	
	
for item in data2021:
	item.sort(key=partyRank,reverse=True)


boo = input("Riding or party search(1 or 2): ")



if(int(boo) == 1):
	ridingSearch()
else:
	partySearch()

