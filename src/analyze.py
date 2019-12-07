import json
from os import listdir
from os.path import isfile, join

PATH = "../messages/inbox/ErraticBrainletPlansMax48hrNotice_ApawlGe7wQ"


def mergeMessages(jsons):
  for i in range(len(jsonDicts)):
    if (i != 0):
      jsons[0]["messages"].extend(jsons[i]["messages"])

  # Get rid of additional jsons to save space in memory
  for i in range(len(jsons)-1, 0, -1):
    jsons.pop(i)


def countWords(s):
  return len(s.split())


def countMessages(jsonDict):
  participantDict = {}
  total_words = 0
  for p in jsonDict["participants"]:
    participantDict[p["name"]] = [0, 0] 

  for msg in jsonDict["messages"]:
    if (msg["sender_name"] in participantDict):
      participantDict[msg["sender_name"]][0]+=1
      if ("content" in msg):
        participantDict[msg["sender_name"]][1]+=countWords(msg["content"])
        total_words += countWords(msg["content"]) 
  
  # Output information
  for participant in participantDict:
    print("{0} has sent {1} messages to this group, which is {2}% of the total messages.".format(participant, participantDict[participant][0], (participantDict[participant][0] * 100 / len(jsonDict["messages"]))))
    print("{0} has sent {1} words in total, or {2}% of the total words.".format(participant, participantDict[participant][1], (100 * participantDict[participant][1]/(total_words))))
    if (participantDict[participant][0] != 0):
      print("{0}'s average word-to-message ratio is {1}.".format(participant, (participantDict[participant][1]/participantDict[participant][0])))
    print("")


def countReaccs(jsonDict):
  out = 0
  participantDict = {}
  for p in jsonDict["participants"]:
    participantDict[p["name"]] = {}
  reaccs = {}

  #for msg in jsonDict["messages"]:
  #  if ("reactions" in msg):
      
  return out


'''
if __name__ == "__main__":
  onlyjson = [join(PATH, f) for f in listdir(PATH) if (isfile(join(PATH, f)) and ("json" in f))] 
  print(onlyjson)
  jsonDicts = []
  for js in onlyjson:
    f = open(js, 'r')
    jsonDicts.append(json.load(f))
    f.close()
  mergeMessages(jsonDicts)
  countMessages(jsonDicts[0])
  #print(countReaccs(jsonDicts[0]))
'''
