import ternary
from matplotlib import *

### Scatter Plot
scale = 100
figure, tax = ternary.figure(scale=scale)
tax.set_title("Scatter Plot", fontsize=20)
tax.boundary(linewidth=2.0)
tax.gridlines(multiple=10, color="blue")

# Plot a few different styles with a legend
Brentonpoints = [(float(11.82),float(80),float(8.81))] #has to be a tuple in a list (lithics,quartz,feldspar)
tax.scatter(Brentonpoints, marker='s', color='red', label="Brenton")
Mikepoints = [(float(11.82),float(76.09),float(10.77))]
tax.scatter(Mikepoints, marker='D', color='green', label="Mike")
tax.legend()
tax.ticks(axis='lbr', linewidth=1, multiple=10)

tax.show()
