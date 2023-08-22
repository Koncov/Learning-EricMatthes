file_name = "learning_python.txt"
with open(file_name) as file_object:
    string_data = file_object.readlines()

for _ in string_data:
    print(_.rstrip().replace('Python', '\"C\"'))
