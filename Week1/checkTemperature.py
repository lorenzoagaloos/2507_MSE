#Week 1 - Check Temperature (lorenzoagaloos-270729354)
# This script calculates the average, maximum, and minimum temperatures from a given array
import numpy as np

# Sample temperature data (in Celsius)
arrTemp = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# Calculate average, max, min, convert to Fahrenheit, and check for temperatures exceeding 20 degrees
average_Temp = np.round(np.mean(arrTemp), 2)
max_Temp = np.max(arrTemp)
min_Temp = np.min(arrTemp)
converted_Temp = np.round(arrTemp * 9/5 + 32, 2)  # Convert the temperatures from Celsius to Fahrenheit

# Check for temperatures exceeding 20 degrees Celsius and then return the days where temperature exceeded 20 degrees
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hot_days = [days[i] for i in range(len(arrTemp)) if arrTemp[i] > 20]

# Print all the results
if __name__ == "__main__":
    print(f"The average temperature in Celsius is: {average_Temp} °C") # Displaying the average temperature from the array
    print(f"The maximum temperature in Celsius is: {max_Temp} °C") # Displaying the maximum temperature
    print(f"The minimum temperature in Celsius is: {min_Temp} °C") # Displaying the minimum temperature
    print("The temperatures in Fahrenheit are: ", converted_Temp) # Displaying the converted temperatures in Fahrenheit
    print("Days where temperature exceeded 20 degrees Celsius : ", hot_days)  # Displaying only the days where temperatures exceedingexceeded 20 degrees