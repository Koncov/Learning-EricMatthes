def locations(country, city, population=''):
    """Формирует строку типа 'Страна, город'."""
    if population:
        location = f"{country}, {city} - population = {population}"
    else:
        location = f"{country}, {city}"
    return location


loc_full = locations('Россия', 'Киров', 500000)
print(loc_full)
loc = locations('Россия', 'Киров')
print(loc)
