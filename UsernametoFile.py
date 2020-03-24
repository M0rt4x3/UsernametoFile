name = input("What is your name?")
age = input("What is your age?")
age = age

username = name[0] + name[1] + name[2] + age
username = username

print("Hello ", name, ", your username is: ", username)

file = open("username.txt", "a")
file.write("Name: " + name + ", Age: " + age + ", Username: " + username + "\n")
file.close()

print("Details written to file successfully")