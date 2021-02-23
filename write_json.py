import json

data = {}

data['class'] = 'COE332'
data['title'] = 'Softaware Engineering'
data['inperson'] = False

data['subject'] = []
subject.append({'week':1, 'topic': ['linux', 'python']})

with open('class.jason','w') as out: 
	json.dump(data,out, indent=2)
