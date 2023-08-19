import restaurant

restaurant_info = restaurant.Restaurant('Moskov', 'tradicion')

restaurant_info.describe_restaurant()
restaurant_info.open_restaurant()
restaurant_info.restaurant_name = "Russia"
restaurant_info.cuisine_type = "japan"
restaurant_info.describe_restaurant()
restaurant_info.open_restaurant()
