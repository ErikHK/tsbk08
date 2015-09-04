from math import *
import pdb, copy
#string to be encoded
tstring = "hej jag heter erik"

#define alphabet
totlen = len(tstring);
dic = {};
alphabet = list(set(tstring))
print alphabet

alphabet.sort()
print len(alphabet)
#number of unique symbols
numsym = len(alphabet)
print numsym

#build dictionary with probabilities
def buildprobdict():
  for i,j in enumerate(alphabet):
    print i,j
    dic[j] = float(tstring.count(alphabet[i]))/totlen;


buildprobdict()
print dic
#del dic[min(dic, key=dic.get)]
#print dic
print sum(dic.values())

#fetch most common
print max(dic, key=dic.get)

def bwt(string):
	j=-1;
	#tmp = tstring;
	bwt_list = [];
	for i in string:
		bwt_list.append(string[j+1:len(string)]+string[0:j+1]);
		j=j+1;
	

	bwt_string = "";
	for word in sorted(bwt_list):
		bwt_string = bwt_string + word[-1]
	return bwt_string

def invbwt(string):
	newstrlist = list(copy.copy(string));
	newstrlistupd = copy.copy(newstrlist);
	for i in range(len(string)-1):
		newstrsorted = copy.copy(sorted(newstrlistupd));
		#sorted.sort()
		for j in range(len(string)):
			newstrlistupd[j] = newstrlist[j] + newstrsorted[j];
		#newstrlist.sort()
		print newstrlistupd
	
def mtf(string):
	code = []
	alf = copy.copy(alphabet);
	for i in string:
		ind = alf.index(i);
		code.append(ind)
		alf.pop(ind)
		alf = [i] + alf;
	return code
	
def invmtf(code):
	alf = copy.copy(alphabet);
	#pdb.set_trace()
	stri = "";
	for c in code:
		cc = alf[c];
		stri = stri + str(cc);
		ind = alf.index(cc)
		alf.pop(ind)
		alf = [cc] + alf;
	return stri

print bwt(tstring)
mt = mtf(bwt(tstring))
print mt
stri = invmtf(mt)
print stri
recovered = invbwt(stri)

#print mt
#print max(mt)
#print alphabet.index('h')