import csv

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Чтение максимальных температур
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)

# Нанесение данных на диаграмму
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Формирование диаграммы
plt.title("Daily high temperatures, Jule 2018", fontsize=24)
plt.xlabel('', fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
