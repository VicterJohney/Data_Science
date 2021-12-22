import matplotlib.pyplot as plt
import numpy as np

#xaxis = np.array([300, 450, 150, 400, 650])
#yaxis = np.array([400, 500, 350, 300, 500])

#plot1
xaxis = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'])
yaxis = np.array([300, 450, 150, 400, 650])
plt.subplot(1, 2, 1)
plt.plot(xaxis, yaxis, ':c', )
plt.plot(xaxis,yaxis,'Hm',mec='k')
plt.grid(color = 'blue', linestyle = 'dotted')
plt.title("Sales Data1", loc='right')
plt.xlabel("Days of Week")
plt.ylabel("Sale of Drinks")
plt.show()

#plot2
xaxis = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'])
yaxis = np.array([400, 500, 350, 300, 500])
plt.subplot(1, 2, 1)
plt.plot(xaxis, yaxis)
plt.plot(xaxis,yaxis,'--y')
plt.plot(xaxis,yaxis,'Dg',mec='r')
plt.grid(color = 'blue', linestyle = 'dotted')
plt.title("Sales Data2", loc='center')
plt.xlabel("Days of Week")
plt.ylabel("Sale of Food")
plt.show()