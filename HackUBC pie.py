#!/usr/bin/env python
# coding: utf-8

# In[4]:


from canvasapi import Canvas
import json
import plotly
plotly.tools.set_credentials_file(username='jemusi', api_key='4gDYcNCbrJ8bGWGIfxU4')
import plotly.plotly as py
import plotly.graph_objs as go


# In[14]:


def isCourse(course):
    temp = course.name;
    temp = temp[0:3]
    if (temp.isupper()):
        return True
    return False

def produceScores(dictionary):
    for d in dictionary:
        list1.append(d[0:8])
        if (dictionary[d[0:8]] >= 80):
            list2.append(dictionary[d[0:8]]/4)
        else: list2.append(dictionary[d[0:8]])
    


# In[6]:


API_KEY=open(".canvas_api_key").readline().rstrip('\n')
API_URL = "https://canvas.ubc.ca"


# In[15]:


canvas = Canvas(API_URL,API_KEY)
dict = {}
dict2 = {}
dict3 = {}
list1 = []
list2 = []
all_courses = list(canvas.get_courses())
curr_courses = list(filter(lambda c: hasattr(c,'name') and isCourse(c),all_courses))

#Get submissions and assignments
for c in curr_courses:
    dict[c.name[0:8]] = list(c.get_assignments())
    dict2[c.name[0:8]] = list(c.get_multiple_submissions())
    

for c in curr_courses:
    print(c.name[0:8])
    counter = 0.0
    sumsub = 0.0
    for d1 in dict[c.name[0:8]]:
        for d2 in dict2[c.name[0:8]]:
            if (d1.id == d2.assignment_id):
                if (d2.grade is not None and d1.points_possible != 0):
                    temp = 100*float(d2.grade)/d1.points_possible
                else: temp = 0
                if (d1.points_possible != 0 ) :
                    sumsub += temp
                    counter += 1
                print("Submissions: ",d2.grade,"Assignments: ",d1.points_possible, "Percentage: ", temp)
    if (counter != 0):
        dict3[c.name[0:8]] = sumsub/counter   
        print(dict3[c.name[0:8]])
    print("\n")
    
produceScores(dict3)

#Produce pie chart
labels = list1
values = list2
trace = go.Pie(labels=labels, values=values)
py.iplot([trace],filename='output')


# In[ ]:




