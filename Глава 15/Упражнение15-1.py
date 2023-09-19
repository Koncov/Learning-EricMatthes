import matplotlib.pyplot as plt


x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение шрифта делений на осях.
ax.tick_params(axis='both', labelsize=14)

# Назначение диапазона для каждой оси.
ax.axis([0, 5500, 0, 900000000000])
plt.show()