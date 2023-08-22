file_name = "learning_python.txt"
with open(file_name) as file_object:
    string_data = file_object.readlines()
    for _ in range(3):
        print(string_data)

for _ in string_data:
    print(_.rstrip())
