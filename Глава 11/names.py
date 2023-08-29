from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    lsat = input("\nPlease give me a last name: ")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first, lsat)
    print(f"\tNeatly formatted name: {formatted_name}.")
