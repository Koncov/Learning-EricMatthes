file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Yes")
else:
    print("No")

print(f"{pi_string[:52]}...")
print(len(pi_string))
