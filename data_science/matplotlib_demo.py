import numpy as np
from matplotlib import pyplot as plt

# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')
plt.xkcd()
ages_x = [25,26,27,28,29,30,31,32,33,34,35]

ages_x_index = np.arange(len(ages_x))

width = 0.25

dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]

# plt.bar(ages_x,dev_y, label="All Dev")
plt.bar(ages_x_index-width,dev_y, width=width,label="All Dev")

py_dev_y = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
# plt.bar(ages_x,py_dev_y, label="python")

plt.bar(ages_x_index,py_dev_y, width=width, label="python")


js_dev_y = [37810,40389,53850,57287,59089,620167,64123,651234,67452,68553,70231]

# plt.bar(ages_x,js_dev_y, label="javascript", color='#da1235', linestyle='--',linewidth='3')
plt.bar(ages_x_index+width,js_dev_y, width=width, label="javascript", color='#da1235', linestyle='--',linewidth='3')

plt.xlabel("Salary USD")
plt.ylabel("MEdian Salary")

plt.xticks(ticks=ages_x_index,labels=ages_x)
plt.title(" Employee visulisations data")
plt.legend()
plt.tight_layout()
plt.savefig('plot3.png')
plt.show()