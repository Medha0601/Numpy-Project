import numpy as np

# with open('nyc_taxis.csv') as f:
#      data = f.read()
    #  print(data)
    
# 
data = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=True)
     
     
# FIRST QUESTION:
# CALCULATE THE MEAN SPEED OF THE CAB RIDES
    #  speed = dis/time
    
speed = data[:, 7]/(data[:,8]/3600)
mean = speed.mean()
print(mean)

# SECOND QUESTION
# CALCULATE THE NUMBER OF RIDES TAKEN IN THE MONTH OF FEBRUARY.
month = data[data[:,1] ==2,1]
print(month.shape[0]) 


# THIRD QUESTION
# CALCULATE THE NUMBER OF RIDES WITH A TRIP(TRIP AMOUNT) GREATER THAN $50
amount = data[data[:,-3] > 50,-3]
print(amount.shape[0])

# FOURTH QUESTION
# CALCULATE THE NUMBER OF RIDES WHERE DROP WAS JFK AIRPORT(CODE = 2)
dropOff = data[data[:,6] ==2,6]
print(dropOff.shape[0])
