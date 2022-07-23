# Different type of functions used in for lists in Python:
# x.append() >> adds a new element at the end of the list
# x.extend() >> can add another list to a previously existing list
# x.insert() >> can insert an element at a specified index in a list
# x.remove() >> can remove the element passed in 
# x.clear() >> can remove all items from a list

lucky_numbers = [4, 8, 15, 16, 23, 42, 83, 54, 67]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#lucky_numbers.extend(friends)
lucky_numbers.append(234)
#print(lucky_numbers)

# What are Tuples in Python?
# Container where you can store multiple pieces of information
coordinates = [(2, 3), (6, 7)]
#print(coordinates[1])
# Dictionaries in Python
# Allows us to store information in key value pairs
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November", 
    "Dec": "December",
    "Jan": "hello"
}
 
print(monthConversions["Jan"])