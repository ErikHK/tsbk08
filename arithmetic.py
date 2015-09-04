from math import *
#string to be encoded
tstring = "heeeeeej"
#interval
intval = [0]
#multiplier
multip = 1;
dic = {};
totlen = len(tstring);

#define alphabet
alphabet = list(set(tstring))
#number of unique symbols
numsym = len(alphabet)
print numsym

#build dictionary with probabilities
def buildprobdict():
  for i,j in enumerate(alphabet):
    print i,j
    dic[j] = float(tstring.count(alphabet[i]))/totlen;


print tstring
print intval

buildprobdict()
print dic
#del dic[min(dic, key=dic.get)]
#print dic
print sum(dic.values())
#fetch most common
print max(dic, key=dic.get)

acc = 0
tmpdic = dic.copy()
#new interval
for n in dic:
  acc = acc + tmpdic[max(tmpdic, key=dic.get)]
  del tmpdic[max(tmpdic, key=dic.get)]
  intval.append(acc)


def determine_maxmin(prob, list):
  low = min(list)
  high = max(list)
  for n in list:
      mindist = abs(prob-high)
      if prob >= n:
        low = n
      if prob < n and abs(prob-n) < mindist:
        high = n
  return [low, high]
  
def determine_intval(maxmin):
  minn = min(maxmin)
  maxx = max(maxmin)
  inc = (maxx)/numsym
  
  list = []
  for i in range(numsym):
    list.append(minn+intval[i]*maxx)
  list.append(maxx)
  return list
  

print intval
#origintval = intval.copy()

acc = 0
cnt = 0
newmaxmin=[0,1]
newintval = intval
#start coding!
for n in tstring:
  acc = acc + dic[n]*(max(newmaxmin)-min(newmaxmin))
  #current probability
  currprob = dic[n]*max(newmaxmin)
  #currprob = acc
  print currprob
  #print acc
  newmaxmin = determine_maxmin(currprob, newintval)
  print newmaxmin
  newintval = determine_intval(newmaxmin)
  print newintval
  #print intval
  #intval = [dic[n] * i for i in intval]

  

#print intval
print acc
print dic