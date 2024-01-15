---
icon: graph
---
# Matplotlib

## Scientific Notations on Axes

```python
%matplotlib inline
import matplotlib.pyplot as plt

# Sample data
x = [1,2,3,4,5]
y = [10000,20000,30000,40000,50000]

# Using an old style string formatter
# (Results in the graph on the left hand side below)
plt.plot(x,y)
axes = plt.gca()  # get the axes
myformatter = plt.FormatStrFormatter("%.1e")  # format the ticks
axes.yaxis.set_major_formatter(myformatter)

# Use scalar formatter to create an axis label
# (Results in the graph on the right hand side below)
plt.plot(x,y)
axes = plt.gca()
myformatter = plt.ScalarFormatter(useMathText=True)
# Any numbers larger than 10^3 or smaller than 10^-3 will be formatted
myformatter.set_powerlimits((-3,3))
axes.yaxis.set_major_formatter(myformatter)
```

![](/images/matplotlib_sn.png)
