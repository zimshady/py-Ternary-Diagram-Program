import ternary
import os
import matplotlib as mpl
from matplotlib import *
import matplotlib.cm as cmx
import csv

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
tax.gridlines(multiple=10, color="blue")

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

count=0
cmap=get_cmap(len(list2)+1)
#Boundary lines for Pettijohn 1987 arenite classification:
qtzAren1, qtzAren2, qtzAren3 = (0,95,5),(5,90,5),(5,95,0)
subArk, middle, subLith = (0,75,25),(25,50,25),(25,75,0)
noQtz = (50,0,50)
# Plot a few different styles with a legend
#has to be a tuple in a list (lithics,quartz,feldspar)
for i in tup_percent:
    print "i=" + str(i)
    tax.scatter([i], marker='p', color='black', label=list2[count])
    count+=1

tax.line(qtzAren1,qtzAren2,linewidth=1.0,color='black')
tax.line(qtzAren3,qtzAren2,linewidth=1.0,color='black')
tax.line(subArk,middle,linewidth=1.0,color='black')
tax.line(subLith,middle,linewidth=1.0,color='black')
tax.line(noQtz,qtzAren2,linewidth=1.0,color='black')
#tax.legend()
tax.ticks(axis='lbr', linewidth=1, multiple=10)

tax.show()
