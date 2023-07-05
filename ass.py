#1. Calculate the sum of all numbers from 1 to a given number.
given_number = 10
total = 0
for i in range(1, given_number + 1):
    total += i

print("The sum of all numbers from 1 to", given_number, "is", total)
#2. Write a program to print multiplication table of a given number.

given_number = int(input("Enter a number: "))

print("Multiplication Table of", given_number)
for i in range(1, 11):
    print(given_number, "x", i, "=", given_number * i)

#3: Display numbers from a list using loop


numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)



#4: Count the total number of digits in a number



number = 12345

num_str = str(number)
count = len(num_str)

print("The total number of digits in", number, "is", count)


number = 12345

count = 0
temp = number

while temp != 0:
    temp //= 10
    count += 1

print("The total number of digits in", number, "is", count)

#7: Print list in reverse order using a loop .
my_list = [1, 2, 3, 4, 5]

index = len(my_list) - 1
while index >= 0:
    print(my_list[index])
    index -= 1


#8: Display numbers from -10 to -1 using for loop
for number in range(-10, 0):
    print(number)
#9: Use else block to display a message “Done” after successful execution of for loop.


for number in range(1, 6):
    print(number)
else:
    print("Done")


#10: Write a program to display all prime numbers within a range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

#11: Display Fibonacci series up to 10 terms.
num_terms = 10

term1 = 0
term2 = 1

print("Fibonacci series up to", num_terms, "terms:")
print(term1) 
print(term2)  

for _ in range(num_terms - 2):
    next_term = term1 + term2
    print(next_term)
    term1, term2 = term2, next_term
#12: Find the factorial of a given number.
number = int(input("Enter a number: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print("The factorial of", number, "is", factorial)
#13: Reverse a given integer number.
number = int(input("Enter a number: "))
reversed_number = 0
temp = number

while temp != 0:
    digit = temp % 10
    reversed_number = (reversed_number * 10) + digit
    temp //= 10

print("The reversed number is:", reversed_number)
#14: Use a loop to display elements from a given list present at odd index positions.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in range(1, len(my_list), 2):
    print(my_list[index])
#15: Calculate the cube of all numbers from 1 to a given number.
number = int(input("Enter a number: "))


for i in range(1, number + 1):
    cube = i ** 3
    print("Cube of", i, "is", cube)
#16: Find the sum of the series upto n terms
n = int(input("Enter the number of terms: "))


series_sum = 0
for i in range(1, n + 1):
    series_sum += i ** 2

print("The sum of the series is:", series_sum)
#17: Append new string in the middle of a given string.
given_string = input("Enter a string: ")
new_string = input("Enter the new string to append: ")

middle_index = len(given_string) // 2

result_string = given_string[:middle_index] + new_string + given_string[middle_index:]

print("Result:", result_string)
#19: Count all letters, digits, and special symbols from a given string.
input_string = input("Enter a string: ")

letter_count = 0
digit_count = 0
special_count = 0

for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print("Letter count:", letter_count)
print("Digit count:", digit_count)
print("Special symbol count:", special_count)
#20: Find all occurrences of a substring in a given string by ignoring the case.
input_string = input("Enter a string: ")
substring = input("Enter a substring to find: ")

input_string_lower = input_string.lower()
substring_lower = substring.lower()

occurrences = []
start_index = 0

while True:
    index = input_string_lower.find(substring_lower, start_index)
    if index == -1:
        break
    occurrences.append(index)
    start_index = index + 1

print("Occurrences of the substring:", occurrences)
#21: Calculate the sum and average of the digits present in a string.
input_string = input("Enter a string: ")

sum_digits = 0
count_digits = 0

for char in input_string:
    if char.isdigit():
        sum_digits += int(char)
        count_digits += 1

average_digits = sum_digits / count_digits if count_digits > 0 else 0

print("Sum of digits:", sum_digits)
print("Average of digits:", average_digits)
#22: Write a program to count occurrences of all characters within a string.
string = input("Enter a string: ")
character_count = {}

for char in string:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1

for char, count in character_count.items():
    print(f"{char}: {count}")
#24: Split a string on hyphens.
string = "Hello-world-I-am-ChatGPT"

split_string = string.split("-")

print(split_string)
#25: Remove empty strings from a list of strings.
strings = ["Hello", "", "World", "", "Python", ""]

filtered_strings = [string for string in strings if string]

print(filtered_strings)
#26: Removal all characters from a string except integers.
input_string = input("Enter a string: ")
output_string = ""

for char in input_string:
    if char.isdigit():
        output_string += char

print("Input string:", input_string)
print("Extracted integers:", output_string)
#27: Reverse a list in Python.
my_list = [1, 2, 3, 4, 5]

my_list.reverse()

print("Reversed list:", my_list)
#28: Concatenate two lists index-wise.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

concatenated_list = []
for i in range(min(len(list1), len(list2))):
    concatenated_list.append(list1[i] + list2[i])

print("Concatenated list:", concatenated_list)
#29: Turn every item of a list into its square.
my_list = [1, 2, 3, 4, 5]
squared_list = []
for x in my_list:
    squared_list.append(x**2)

print("Squared list:", squared_list)




