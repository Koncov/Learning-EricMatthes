# Упражнение 8.12
def sandwich_make(*args):
    print("Ваш сэндвич состоит из:")
    for sandwich in args:
        print(f"-- {sandwich}")


sandwich_make('Булка', 'Котлета')
sandwich_make('Булка', 'Котлета', 'Лук', 'Кетчуп')
sandwich_make('Булка', 'Котлета', 'Лук', 'Кетчуп', 'Капуста', 'Кунжут')


# Упражнение 8.13
def build_profile(first, last, age, children, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['age'] = age
    user_info['children'] = children
    return user_info


user_profile = build_profile('Концов', 'Евгений', 46, True,
                             Marital_status='Married',
                             location='Новокубанск',
                             state='Краснодарский край',
                             citizenship='Россия')
print(user_profile)


# Упражнение 8.14
def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs


car = make_car('audi', 'A100', color='blue', tow_package=True)
print(f"\nCar {car}")

