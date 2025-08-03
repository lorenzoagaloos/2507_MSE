#Week 1 - Rainfall Analysis (lorenzoagaloos-270729354)

#Tasks: 
#Convert the list to a NumPy array and print it.
#Print the total rainfall for the week.
#Print the average rainfall for the week.
#Count how many days had no rain (0 mm).
#Print the days (by index) where the rainfall was more than 5 mm.

import numpy as np

# Sample rainfall data
Sample_Data = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

# Convert the list to a NumPy array
DailyRainfall_arr = np.array(Sample_Data)

# Calculate the total rainfall, average rainfall, and count of days with no rain
Total_Rainfall = np.sum(DailyRainfall_arr)  # Calculate total rainfall
Average_Rainfall = np.round(np.mean(DailyRainfall_arr), 2)  # Calculate average rainfall
Days_No_Rain = np.sum(DailyRainfall_arr == 0)  # Count days with no rain

# Convert the rainfall data to a list of days with more than 5 mm of rain
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
Days_Over_5mm = [days[i] for i in range(len(DailyRainfall_arr)) if DailyRainfall_arr[i] > 5]

# Print all the results
if __name__ == "__main__":
    print(f"Sample Data converted to Numpy array: {DailyRainfall_arr}") # Displaying the converted NumPy array
    print(f"The total rainfall for the week is: {Total_Rainfall:.2f} mm") # Displaying the total rainfall for the week
    print(f"The average rainfall for the week is: {Average_Rainfall} mm") # Displaying the average rainfall for the week
    print(f"Number of days with no rain: {Days_No_Rain}") # Displaying the number of days with no rain
    print(f"Days with more than 5 mm of rain: {Days_Over_5mm}") # Displaying the days with more than 5 mm of rain