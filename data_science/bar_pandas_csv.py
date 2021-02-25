import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')
data = pd.read_csv('/home/vivek/Desktop/survey_results_public.csv')

ids = data['Respondent']
lang_response = data['Country']

langauge_counter = Counter()

for res in lang_response:
    langauge_counter.update(res)

lang = []
popularty = []


for item in langauge_counter.most_common(15):
    lang.append(item[0])
    popularty.append(item[1])

lang.reverse()
popularty.reverse()

# plt.bar(ages_x,js_dev_y, label="javascript", color='#da1235', linestyle='--',linewidth='3')
plt.bar(lang,popularty)

plt.xlabel("Salary USD")
plt.ylabel("MEdian Salary")

plt.xticks(ticks=ages_x_index,labels=ages_x)
plt.title(" Employee visulisations data")
plt.legend()
plt.tight_layout()
plt.savefig('plot3.png')
plt.show()