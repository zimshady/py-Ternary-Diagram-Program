import ternary
import os
import matplotlib as mpl
from matplotlib import *
import matplotlib.cm as cmx
import csv
from Convex_hull import make_conv_hull as make_hull
import numpy as np
import scipy.spatial
import matplotlib.pyplot as plt


mpl.rcParams['pdf.fonttype'] = 42 # ensures editable text in illustrator

def get_cmap(N):
    '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct
    RGB color.'''
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color
### Get current directory
path = os.getcwd()
### Scatter Plot
scale = 100
figure, tax = ternary.figure(scale=scale)
tax.set_title("Scatter Plot", fontsize=20)
tax.boundary(linewidth=2.0)
tax.gridlines(multiple=5, color="black")

points = []
# Load some data, tuples (x,y,z)
with open(path + "\\" + "all_ternary_data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list1 = []

    for row in reader:
        list1.append(row)

    list2 = list1.pop(0)
    list1 = [map(float, x) for x in list1]
    tup_percent = zip (*list1)
    csvfile.close()

with open(path + "\\" + "all_Dingle_point_data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list3 = []

    for row in reader:
        list3.append(row)

    list4 = list3.pop(0)
    list3 = [map(float, x) for x in list3]
    tup_percent2 = zip (*list3)
    csvfile.close()

with open(path + "\\" + "All_WMunster_point_data_L-Q-F.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list5 = []

    for row in reader:
        list5.append(row)

    list6 = list5.pop(0)
    list5 = [map(float, x) for x in list5]
    tup_percent3 = zip (*list5)
    csvfile.close()

with open(path + "\\" + "All_EMunster_point_data_L-Q-F.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    list7 = []

    for row in reader:
        list7.append(row)

    list8 = list7.pop(0)
    list7 = [map(float, x) for x in list7]
    tup_percent4 = zip (*list7)
    csvfile.close()

count=0
count1=0
count2=0
count3=0


cmap=get_cmap(len(list2)+1)
#Boundary lines for Pettijohn 1987 arenite classification:
qtzAren1, qtzAren2, qtzAren3 = (0,95,5),(5,90,5),(5,95,0)
subArk, middle, subLith = (0,75,25),(25,50,25),(25,75,0)
noQtz = (50,0,50)
# Plot a few different styles with a legend
#has to be a tuple in a list (lithics,quartz,feldspar)


for i in tup_percent2:
    print "j=" + str(i)
    tax.scatter([i], marker='*', color='black', label=list4[count1])
    count1+=1

for i in tup_percent3:
    print "j=" + str(i)
    tax.scatter([i], marker='o', color='blue', label=list6[count2])
    count2+=1

for i in tup_percent4:
    print "j=" + str(i)
    tax.scatter([i], marker='s', color='green', label=list8[count3])
    count3+=1

for i in tup_percent:
    print "i=" + str(i)
    tax.scatter([i], marker='p', color='red', label=list2[count])
    count+=1

tax.line(qtzAren1,qtzAren2,linewidth=1.0,color='black')
tax.line(qtzAren3,qtzAren2,linewidth=1.0,color='black')
tax.line(subArk,middle,linewidth=1.0,color='black')
tax.line(subLith,middle,linewidth=1.0,color='black')
tax.line(noQtz,qtzAren2,linewidth=1.0,color='black')
#tax.legend()
tax.ticks(axis='lbr', linewidth=1, multiple=10)

tax.show()
