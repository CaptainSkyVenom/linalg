import json

def cleanName(oldname): 
	#print(oldname.rpartition("/")[2].replace('.mp3','').split(' ', 1))
	newname = oldname.rpartition("/")[2].replace('.mp3','').split(' ', 1)[1]
	return newname

with open('Names.txt') as names:
    oldnames = names.readlines()
    oldnames = [x.strip() for x in oldnames] 


def cleanNames(oldnames):

	newnamesDict = {}

	for oldname in oldnames:
		newnamesDict[cleanName(oldname)] = oldname.split('\t', 1)[1]

	return newnamesDict

newnamesDict = cleanNames(oldnames)

with open('newnamesDict.json', 'w') as outfile:
    json.dump(newnamesDict, outfile, indent=4)

def namesID(oldnames):

	newnamesID = ''

	for oldname in oldnames:
		newnamesID += oldname.split('\t', 1)[0] + '\t' + cleanName(oldname) + '\n'

	return newnamesID

newnamesID = open("newnamesID.txt", "w")
newnamesID.write(namesID(oldnames))
newnamesID.close()