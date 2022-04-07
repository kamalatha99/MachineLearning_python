"""
matplotlib is a 2d plotting library
used to create high quality graphs,charts etc...
pyplot
Pyplot is one of the module of matplotlib
Pyplot contains collection of methods which is simple user interface for constructing graphs.
types of plots
line plot---bar plot
scatter plot---pie chart---so on
"""
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
print("line plot")
print((plt.plot(x,y)))
plt.show()
print("------------------------")
#with some modifications
print("line plot modified")
z=[25,35,45,55]
plt.plot(y,z,label='Line')
plt.ylabel('y-axis')
plt.xlabel('z-axis')
plt.show()
print("--------------------------")
print("scatter plot")
plt.scatter(x,y,color='red')
plt.show()
print("---------------------------")
print("bar plot")
year=['2020','2021','2022']
placements=[123,180,213]
plt.bar(year,placements, color='orange')
plt.show()
print("----------------------------")
print("diff color bar plot")
sales=[50,150,300]
plt.bar(year,sales,color=['red','blue','green'])
plt.show()
print("------------------------------")
print("pie chart")
plt.pie(year,labels=sales,colors=['red','orange','green'])
plt.show()

