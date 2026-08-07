import matplotlib.pyplot as plt

# Monthly data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = [24, 26, 29, 32, 35, 37, 36, 35, 33, 30, 27, 25]

rainfall = [20, 15, 10, 30, 50, 80, 120, 100, 90, 60, 40, 25]

# 1. Line Plot - Temperature
plt.figure(figsize=(8, 5))
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# 2. Scatter Plot - Rainfall
plt.figure(figsize=(8, 5))
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()
