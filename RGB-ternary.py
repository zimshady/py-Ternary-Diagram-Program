import ternary, os, csv
import matplotlib as mpl
from matplotlib import *
import numpy as np

mpl.rcParams['pdf.fonttype'] = 42 # ensures editable text in illustrator

### Get current directory
path = "C:\\Google Drive\\PhD\\Data\\CL data\\Second session"

### Scatter Plot
scale = 100
figure, tax = ternary.figure(scale=scale)
tax.set_title("CL RGB", fontsize=20)
tax.boundary(linewidth=1.0,solid_capstyle='round')
tax.gridlines(multiple=5, color="black")

# Load some data, tuples (x,y,z)
with open(path + "\\" + "BF7-perc.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list1 = []

    for row in reader:
        list1.append(row)

    list2 = list1.pop(0)
    list1 = [map(float, x) for x in list1]
    tup_percent = zip (*list1)
    csvfile.close()

with open(path + "\\" + "BF8-perc.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list3 = []

    for row in reader:
        list3.append(row)

    list4 = list3.pop(0)
    list3 = [map(float, x) for x in list3]
    tup_percent2 = zip (*list3)
    csvfile.close()

with open(path + "\\" + "BF12-perc.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list5 = []

    for row in reader:
        list5.append(row)

    list6 = list5.pop(0)
    list5 = [map(float, x) for x in list5]
    tup_percent3 = zip (*list5)
    csvfile.close()

with open(path + "\\" + "BF13-perc.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list7 = []

    for row in reader:
        list7.append(row)

    list8 = list7.pop(0)
    list7 = [map(float, x) for x in list7]
    tup_percent4 = zip (*list7)
    csvfile.close()

#plot data - has to be a tuple in a list (lithics,quartz,feldspar)
tax.scatter(tup_percent2, marker='*', color='black',s=3)
tax.scatter(tup_percent3, marker='o', color='blue',s=3)
tax.scatter(tup_percent4, marker='s', color='green',s=3)
tax.scatter(tup_percent, marker='p', color='red',s=3)

#tax.ticks(axis='lbr', linewidth=1, multiple=10)

ax = tax.get_axes()
ax.axis('Off')
ax.figure.savefig("CL_RGB.pdf")
tax.show()
