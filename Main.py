# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?



def minutes_to_seconds(minutes):
    return minutes * 60


def hours_to_seconds(hours):
    return hours * 3600


def seconds_in_a_day():
    return hours_to_seconds(24)


def hours_in_june():
    return 30 * 24


def minutes_in_august():
    return 31 * 24 * 60


def minutes_in_a_year():
    return 365 * 24 * 60

# Test the functions
print(minutes_to_seconds(1))        
print(minutes_to_seconds(5))        
print(hours_to_seconds(1))          
print(seconds_in_a_day())           
print(hours_in_june())              
print(minutes_in_august())          
print(minutes_in_a_year())          



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


def mid(string):
    length = len(string)
    if length % 2 == 0:
        return ""
    else:
        return string[length // 2]

# Test the function
print(mid("abc"))     
print(mid("aaaa"))    


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


def hide_credit_card(card_number):
    return '*' * (len(card_number) - 4) + card_number[-4:]

# Test the function
print(hide_credit_card("1234567894444"))   # "*********4444"



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


def online_count(statuses):
    return sum(1 for status in statuses.values() if status == "online")

# Test the function
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}
print(online_count(statuses))  # 2



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

def apply_discount(price, discount):
    return price * (1 - discount / 100)

# Test the function
print(apply_discount(100, 20))   # 80


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


import math

def hypotenuse(adjacent, opposite):
    return math.sqrt(adjacent**2 + opposite**2)

# Test the function
print(hypotenuse(3, 4))  # 5.0


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

def fibonacci_sequence(n1, n2):
    fib_sequence = [n1, n2]
    for _ in range(9):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Test the function
print(fibonacci_sequence(0, 1))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
