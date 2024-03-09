
# 5. Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

word_list = ['Car', 'Book', 'House', 'Bag', 'Door']

# [expression for item in iterable if condition]

# odd_word = [word for word in word_list if (len(word) % 2) != 0]

odd_word = []
for word in word_list:
    if len(word) % 2 != 0:
        odd_word.append(word)

print(odd_word)


# 4. Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

set1_input = input('write a list of intergers separated with comma')
set2_input = input('write another list of intergers separated with comma')

set1_integer = set(map(int, set1_input.split(',')))
set2_integer = set(map(int, set2_input.split(',')))

unionSet = set1_integer.union(set2_integer)

commonSet = set1_integer.intersection(set2_integer)

print(f'Union Set: {unionSet}')
print(f'Common Set: {commonSet}')


# 3. Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

person = {}

getName = input('what is your name: ?')
getAge = input('what is your age: ?')
getFavColor = input('what is your favorite color: ?')

person['name'] = getName
person['age'] = getAge
person['favourite color'] = getFavColor

print('person_information:')
for key, value in person.items():
    print(f'{key} : {value}')


# 2. Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

myFavorite_book_tuple = ('Bible', 'Believer\'s Authority', 'Failing Forward')
for book in myFavorite_book_tuple:
    print(book)



# 1. Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

#Second Approach

list_of_input = input('Enter a list of numbers separated with comma: ')

string_input = list_of_input.split(',')

int_input = [int(number) for number in string_input]

sum_list = sum(int_input)


print(sum_list)


#First Approach

total_score_lists = []

math = input('what is your math score?').strip()
total_score_lists.append(int(math))

english = input('what is your english score?').strip()
total_score_lists.append(int(english))

physics = input('what is your physics score?').strip()
total_score_lists.append(int(physics))

biology = input('what is your biology score?').strip()
total_score_lists.append(int(biology))

print(total_score_lists)
print(sum(total_score_lists))