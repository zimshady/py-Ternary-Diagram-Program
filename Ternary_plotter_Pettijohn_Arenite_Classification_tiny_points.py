import ternary, os, csv
import matplotlib as mpl
from matplotlib import *
import numpy as np

mpl.rcParams['pdf.fonttype'] = 42 # ensures editable text in illustrator

### Get current directory
path = os.getcwd()

### Scatter Plot
scale = 100
figure, tax = ternary.figure(scale=scale)
tax.set_title("Arenite Classification", fontsize=20)
tax.boundary(linewidth=1.0,solid_capstyle='round')
tax.gridlines(multiple=5, color="black")

# Load some data, tuples (x,y,z)
with open(path + "\\" + "L-Q-F_arenites.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list1 = []

    for row in reader:
        list1.append(row)

    list2 = list1.pop(0)
    list1 = [map(float, x) for x in list1]
    tup_percent = zip (*list1)
    csvfile.close()

with open(path + "\\" + "Dingle_arenite_point_L-Q-F.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list3 = []

    for row in reader:
        list3.append(row)

    list4 = list3.pop(0)
    list3 = [map(float, x) for x in list3]
    tup_percent2 = zip (*list3)
    csvfile.close()

with open(path + "\\" + "WMunster_arenite_point_L-Q-F.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list5 = []

    for row in reader:
        list5.append(row)

    list6 = list5.pop(0)
    list5 = [map(float, x) for x in list5]
    tup_percent3 = zip (*list5)
    csvfile.close()

with open(path + "\\" + "EMunster_arenite_point_L-Q-F.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list7 = []

    for row in reader:
        list7.append(row)

    list8 = list7.pop(0)
    list7 = [map(float, x) for x in list7]
    tup_percent4 = zip (*list7)
    csvfile.close()

#Boundary lines for Pettijohn 1987 arenite classification:
qtzAren1, qtzAren2, qtzAren3 = (0,95,5),(5,90,5),(5,95,0)
subArk, middle, subLith = (0,75,25),(25,50,25),(25,75,0)
noQtz = (50,0,50)

tax.line(qtzAren1,qtzAren2,linewidth=1.0,color='black',solid_capstyle='round')
tax.line(qtzAren3,qtzAren2,linewidth=1.0,color='black',solid_capstyle='round')
tax.line(subArk,middle,linewidth=1.0,color='black',solid_capstyle='round')
tax.line(subLith,middle,linewidth=1.0,color='black',solid_capstyle='round')
tax.line(noQtz,qtzAren2,linewidth=1.0,color='black',solid_capstyle='round')

#plot data - has to be a tuple in a list (lithics,quartz,feldspar)
tax.scatter(tup_percent2, marker='*', color='black',s=3)
tax.scatter(tup_percent3, marker='o', color='blue',s=3)
tax.scatter(tup_percent4, marker='s', color='green',s=3)
tax.scatter(tup_percent, marker='p', color='red',s=3)

#tax.ticks(axis='lbr', linewidth=1, multiple=10)

ax = tax.get_axes()
ax.axis('Off')
ax.figure.savefig("arenite_classification_tiny_points.pdf")
tax.show()
