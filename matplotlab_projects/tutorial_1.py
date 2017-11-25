import numpy
#import matplotlib as mpl

# If your script depends on a specific backend you can use the use() function:
# If you use the use() function, this must be done before importing matplotlib.pyplot. 
# Calling use() after pyplot has been imported will have no effect. 
# Using use() will require changes in your code if users want to use a different backend. 
# Therefore, you should avoid explicitly calling use() unless absolutely necessary.

#mpl.use('TkAgg')
import matplotlib.pyplot as plt

plt.plot([1,2,3])

plt.ylabel('some numbers')
plt.show()

