import matplotlib.pyplot as plt
import math
print("Enter initial velocity (m/s):")
u = float(input())
print("Enter launch angle (degrees):")
angle = float(input())
angle_rad = math.radians(angle)
ymax = (u ** 2) * (math.sin(angle_rad) ** 2) / (2 * 9.81)
print("Maximum height reached:", ymax)
time_to_max_height = (u * math.sin(angle_rad)) / 9.81
print("Time to reach maximum height:", time_to_max_height)
total_time = (2 * u * math.sin(angle_rad)) / 9.81
print("Total time of flight:", total_time)
t = [i * 0.1 for i in range(int(total_time * 10) + 1)]
x = [u * math.cos(angle_rad) * ti for ti in t]
y = [u * math.sin(angle_rad) * ti - 0.5 * 9.81 * ti ** 2 for ti in t]
plt.plot(x, y)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("2D Motion of a Projectile")
plt.grid(True)
plt.show()

