
import numpy as np

print("-----Exercise1-------")


students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}


print("-----1----")
average_scores = {}
for student, scores in students.items():
    average_scores[student] = sum(scores) / len(scores)
    print(f"{student}s average score is {average_scores}.")

print("-----2-----")
highest_average_student = max(average_scores, key=average_scores.get)
print(highest_average_student)

print("-----3-----")
lowest_average_student = min(average_scores, key=average_scores.get)
print(lowest_average_student)

print("-----4-----")
students["Frank"]=[80,90,85]
print(students)



print("-----Exercise2-------")

inventory = {
"apple": (50, 0.5),
"banana": (100, 0.2),
"orange": (75, 0.3),
"pear": (20, 0.4)
}

print("-----1-----")

for name,details in inventory.items():
    print(f"Product: {name} | Amounts: {details[0]} items |Price: ${details[1]}")

print("-----2-----")

total = 0
for _,details in inventory.items():
    value = details[0] * details[1]
    total += value

print(f"${total}")


print("-----3-----")
inventory["mango"]=30, 0.6
print(inventory)


print("-----4-----")

inventory["banana"]=120,0.2
print(inventory)


print("-----5-----")
del inventory["pear"]
print(inventory)


print("-----Exercise3-------")

employees = [
("John Doe", "Accounting", "john.doe@example.com"),
("Jane Smith", "Marketing", "jane.smith@example.com"),
("Emily Davis", "HR", "emily.davis@example.com"),
("Michael Brown", "IT", "michael.brown@example.com")
]

print("-----1-----")
department = [(employee[0],employee[1]) for employee in employees]
print(department)

print("-----2-----")
email = [(employee[2]) for employee in employees]

alphabet_email_sorted =sorted(email)

for emails in alphabet_email_sorted:
    print(emails)


print("-----3-----")
employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
print(employees)

print("-----4-----")

for employee in employees:
    if employee[0] == "Jane Smith":
        jane_department = employee[1]
        print(jane_department)


print("-----Exercise4-------")

library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye",
"author": "J.D. Salinger", "year": 1951},"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird",
"author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}

print("-----1-----")

for k,v in library.items():
    print(f"ISBN {k}, title {library[k]["title"]}, author {library[k]["author"]}, year {library[k]["year"]}.")


print("-----2-----")

print(library["978-0-14-028329-7"])

print("-----3-----")
library["978-1-4028-9462-6"] = {"title":"The Great Gatsby", "author":"F. Scott Fitzgerald", "year":"1925"}
print(library)

print("-----4-----")

library["978-0-7432-7356-5"] = {"title": "To Kill a Mockingbird","author": "Harper Lee", "year": 1961}
print(library)


print("-----5-----")

del library["978-0-452-28423-4"]
print(library)


print("-----Exercise5-------")

cities = {
"New York": 8419000,
"Los Angeles": 3980000,
"Chicago": 2716000,
"Houston": 2328000,
"Phoenix": 1690000
}


print("-----1-----")
for name,population in cities.items():
    print(f"The population of {name} is {population}.")

print("-----2-----")

max_value = max(cities.values())
print(max_value)

print("-----3-----")
min_value = min(cities,key=cities.get)
print(min_value)

print("-----4-----")
cities["Phoenix"]= 1700000
print(cities)

print("-----5-----")
cities["San Francisco"]=884000
print(cities)



print("-----Exercise6-------")
movies = {

"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},"The Godfather": {"year": 1972, "rating": 9.2, "genre":"Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre":"Action"},"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}


print("-----1-----")

for k, v in movies.items():
    print(f"Title:{k} | year: {movies[k]["year"]} |rating: {movies[k]["rating"]} | genre: {movies[k]["genre"]}.")

print("-----2-----")
new_dic = {}
for k, v in movies.items():
    new_dic[k] = movies[k]["rating"]

print(max(new_dic, key = new_dic.get))

print("-----3-----")
movies["The Matrix"]= {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}
print(movies)


print("-----4-----")
movies["Inception"]["rating"]=9.0
print(movies)

print("-----5-----")
del movies["Pulp Fiction"]
print(movies)



print("-----Exercise7-------")

countries = {
"USA": "Washington, D.C.",
"Canada": "Ottawa",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo"
}

print("-----1-----")
for k, v in countries.items() :
    print(f"The capital of {k} is {v}.")

print("-----2-----")
print(countries["Germany"])

print("-----3-----")
countries["Australia"] = "Canberra"
print(countries)

print("-----4-----")
countries["USA"] = "New Washington"
print(countries)

print("-----5-----")
del countries["France"]
print(countries)



print("-----Exercise8-------")

cart = [
{"item": "apple", "quantity": 3, "price_per_unit": 0.5},
{"item": "banana", "quantity": 6, "price_per_unit": 0.2},
{"item": "orange", "quantity": 4, "price_per_unit": 0.3},
{"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]


print("-----1-----")
for i in range(4) :
    print(f"{cart[i]["item"]} with quantity {cart[i]["quantity"]} at each price ${cart[i]["price_per_unit"]}.")

print("-----2-----")
total_cost = 0
for i in range(4) :
    each_cost = cart[i]["quantity"] * cart[i]["price_per_unit"]
    total_cost += each_cost
print(f"${total_cost}")

print("-----3-----")
grape = {"item": "grape", "quantity": "5", "price_per_unit": "0.6"}
cart.append(grape)
print(cart)

print("-----4-----")
cart[1]["quantity"] = 10
print(cart)

print("-----5-----")
del cart[3]
print(cart)



print("-----Exercise9-------")

weather = {
"Monday": {"temperature": 20, "humidity": 60},
"Tuesday": {"temperature": 22, "humidity": 55},
"Wednesday": {"temperature": 19, "humidity": 65},
"Thursday": {"temperature": 23, "humidity": 50},
"Friday": {"temperature": 21, "humidity": 70}
}

print("-----1-----")
for k, v  in weather.items():
    print(f"The temperature of {k} is {weather[k]["temperature"]} degree and the humidity is {weather[k]["humidity"]}%." )

print("-----2-----")
temp_dic = {}
for k, v in weather.items() :
    temp_dic[k] = weather[k]["temperature"]

highest_temp_day = max(temp_dic, key = temp_dic.get)
highest_temp = temp_dic[highest_temp_day]
print(f"{highest_temp_day} has the highest temperature which is {highest_temp} degree.")

print("-----3-----")
hum_dic = {}
for k, v in weather.items() :
    hum_dic[k] = weather[k]["humidity"]

lowest_hum_day = min(hum_dic, key = hum_dic.get)
lowest_hum = hum_dic[lowest_hum_day]
print(f"{lowest_hum_day} has the lowest humidity which is {lowest_hum}%.")


print("---- 4-----")
weather["Wednesday"]["temperature"] = 25
print(weather)

print("-----5-----")
weather["Saturday"] = {"temperature": 24, "humidity": 60}
print(weather)




print("-----Exercise10-------")

members = [
{"name": "Alice", "age": 25, "books_borrowed": ["1984","To Kill a Mockingbird"]},
{"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
{"name": "Charlie", "age": 22, "books_borrowed": ["BraveNew World", "1984"]},{"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]

print("-----1-----")
name_age =[{"name":member["name"],"age":member["age"]} for member in members]
print(name_age)

print("-----2-----")
print(members[2]["books_borrowed"])

print("-----3-----")
members.append({"name":"Eve","age":28,"books_borrowed":["Pride and Prejudice"]})
print(members)

print("-----4-----")
members[1]["age"]=31
print(members)

print("-----5-----")
del members[3]
print(members)

