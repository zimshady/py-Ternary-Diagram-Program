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
tax.set_title("Tectonic setting", fontsize=20)
tax.boundary(linewidth=1.0,solid_capstyle='round')
tax.gridlines(multiple=5, color="black")

# Load some data, tuples (x,y,z)
with open(path + "\\" + "Brenton_points_all_Lt-Qm-Ft.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list1 = []

    for row in reader:
        list1.append(row)

    list2 = list1.pop(0)
    list1 = [map(float, x) for x in list1]
    tup_percent = zip (*list1)
    csvfile.close()

with open(path + "\\" + "Dingle_all_Lt-Qm-Ft.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list3 = []

    for row in reader:
        list3.append(row)

    list4 = list3.pop(0)
    list3 = [map(float, x) for x in list3]
    tup_percent2 = zip (*list3)
    csvfile.close()

with open(path + "\\" + "WMunster_all_Lt-Qm-Ft.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list5 = []

    for row in reader:
        list5.append(row)

    list6 = list5.pop(0)
    list5 = [map(float, x) for x in list5]
    tup_percent3 = zip (*list5)
    csvfile.close()

with open(path + "\\" + "EMunster_all_Lt-Qm-Ft.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list7 = []

    for row in reader:
        list7.append(row)

    list8 = list7.pop(0)
    list7 = [map(float, x) for x in list7]
    tup_percent4 = zip (*list7)
    csvfile.close()

#Boundary lines for tectonic setting using monocrystalline quartz:
leftmost1, leftmost2 = (11,89,0),(23,0,77)
midline1, midline2 = (0,57,43),(87,13,0)
rightmost1, rightmost2 = (0,80,20),(87,0,13)
upperdotted1, upperdotted2 = (68,32,0),(0,18,82)
lowerdotted1, lowerdotted2 = (82,18,0),(55,0,45)

tax.line(leftmost1,leftmost2,linewidth=1.0,color='black',solid_capstyle='round')
tax.line(midline1,midline2,linewidth=1.0,color='black',solid_capstyle='round')
tax.line(rightmost1,rightmost2,linewidth=1.0,color='black',solid_capstyle='round')
tax.line(upperdotted1,upperdotted2,linewidth=1.0,color='black', linestyle='--',solid_capstyle='round')
tax.line(lowerdotted1,lowerdotted2,linewidth=1.0,color='black',linestyle='--',solid_capstyle='round')

#plot data - has to be a tuple in a list (lithics,quartz,feldspar)
tax.scatter(tup_percent2,marker='*',color='black')
tax.scatter(tup_percent3,marker='o',color='blue')
tax.scatter(tup_percent4,marker='s',color='green')
tax.scatter(tup_percent,marker='p',color='red')

ax = tax.get_axes()
ax.axis('Off')
ax.figure.savefig("tectonic_setting_mono_qtz.pdf")


tax.show()
