#Week 1 - Check Temperature (lorenzoagaloos)
# This script calculates the average, maximum, and minimum temperatures from a given array
import numpy as np

# Sample temperature data (in Celsius)
arr1d = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
    
average_Temp = np.round(np.mean(arr1d), 2)
max_Temp = np.max(arr1d)
min_Temp = np.min(arr1d)
converted_Temp = np.round(arr1d * 9/5 + 32, 2)  # Convert to Fahrenheit
exceeded_Temp = np.where(arr1d > 20, arr1d, 0)  # Temperatures exceeding 25 degrees
non_zero_values = [arr1d for arr1d in exceeded_Temp if arr1d != 0]
   
if __name__ == "__main__":
    print("The average temperature in Celsius is: ", average_Temp)
    print("The maximum temperature in Celsius is: ", max_Temp)
    print("The minimum temperature in Celsius is: ", min_Temp)
    print("The temperatures in Fahrenheit are: ", converted_Temp)
    print("Temperatures exceeding 20 degrees Celsius: ", non_zero_values)

   
  