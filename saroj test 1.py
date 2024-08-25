'''Python Section'''
'''No 1'''
'''What is decorator , write a decorator?'''
'''.a decorator is way to modify or enhance the behaviour of function or class with out modify the original function or class it self.
    . it is function who take another function as an argument.
def decore(calculator):
    def substraction(a,b)
        sub=a-b
        return sub, calculator(a,b)
    return substraction

@decore
def calculator(a,b):
    add=a+b
    return add
print(calculator(120,30))'''


'''What is lambda expression, write a lambda expression?'''
'''Lambda functions, also known as anonymous functions, are a feature in Python that allows the creation of small,
one-expression functions without a name. They are defined using the lambda keyword.



What is exception handling , how handel the exception in python , explain with each
block
Exception handling in Python is a mechanism to manage errors that occur during the execution of a program
Python uses a try block to catch exceptions and an except block to handle them. Optionally you can include else and finally blocks for additional control.

try block
 Contains the code that might raise an exception. If an error occurs within this block, the rest of the code in the try block is skipped, and the program jumps to the except block'''

'''except Block
Catches and handles specific exceptions raised in the try block. You can have multiple except blocks to handle different types of exceptions.'''

'''else Block
 Executes if no exceptions are raised in the try block. It is optional and can be used to run code that should only execute if the try block was successful.'''


''' Sort a list integer element without using inbuilt function?'''

'''Bubble Sort
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.'''

'''Selection Sort
Selection Sort repeatedly finds the minimum element from the unsorted portion of the list and moves it to the beginning.'''

'''Insertion Sort
Insertion Sort builds the sorted array one item at a time. It picks elements from the unsorted portion and places them in their correct position in the sorted portion.'''




'''Li = [1,2,3,4], Li2 = [10,20,30]
Result = {1:10,2:20,3:30}

result = {li[i]:li2[i] for i in range (len(Li2))}
print(result)'''


'''Difference between Moudle and Packages (3 diff)'''
'''moudel
1 A module is a single file that contains Python code. It can define functions, classes, and variables and can include runnable code.
2 Modules are imported using their filename
3 Modules are used for defining reusable components like functions and classes in a single file.'''

'''package
1  A package is a directory (folder) that contains multiple Python modules and a special file named __init__.py. The __init__.py
2  A package is a directory that contains multiple modules and possibly other sub-packages
3 Packages are imported using the package name and dot notation to access sub-packages and modules.'''

 '''What is Garbage Collection?
Garbage Collection means when in a variable if any data is alrady stored abd it we assign a new data that same variable :python will automatically delete old data and store tha new data.'''


'''Difference between Shallow copy vs Deep Copy?
Shallow Copy:
1 A shallow copy creates a new object, but it does not create copies of the objects that are nested within the original object
2 If the original object contains nested objects (like lists within lists), the shallow copy will reference the same nested objects as the original
3 Copies the outer object, but references the same nested objects.

Deep Copy:
1 A deep copy creates a new object and also recursively copies all objects nested within the original object.
2 Changes to the deep copy do not affect the original object, and vice versa even for nested objects.
3 Copies the outer object and all nested objects, creating independent duplicates.'''


'''.Difference between List vs tuple vs set vs dictionary?
1. List
- An ordered, mutable (changeable) collection of items.
-Defined using square brackets [].

2. Tuple
- An ordered, immutable collection of items.
- Defined using parentheses ().

3. Set
-An unordered collection of unique items.
-Defined using curly braces {}.

4. Dictionary
-An unordered collection of key-value pairs.
-Defined using curly braces {},'''



 '''Explain break, continue, pass with code?
 break:


.Explain break, continue, pass with code?
break=it is used to terminate the loop or statement in which it is present.
for loop:
 if condition:
        break
 continue=Continue is also a loop control statement just like the break statement.
 for loop:
     if condition:
         continue
 pass=The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

function/ condition /loop:pass'''


'''What is list comprehension , write code in list comprehension?
-List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable and optionally filtering items with a condition
-List comprehension is more compact and often more readable than traditional loops for creating lists'''



'''SQL'''


'''What is join, explain about the all joins?

-A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

INNER JOIN:
The INNER JOIN keyword selects records that have matching values in both tables.

LEFT JOIN:
The LEFT JOIN keyword returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.

RIGHT JOIN:
The RIGHT JOIN keyword returns all records from the right table (table2), and the matching records from the left table (table1). The result is 0 records from the left side, if there is no match.

FULL OUTER JOIN
The FULL OUTER JOIN keyword returns all records when there is a match in left (table1) or right (table2) table records.

Self Join
A self join is a regular join, but the table is joined with itself.'''


'''Difference between Joins vs Subquery?
joins:
-A join is an SQL operation that combines columns from two or more tables based on a related column between them.
-Joins are best when you need to retrieve and combine related data from multiple tables into a single result set.

Subquery:
-A subquery (or inner query) is a query nested within another query
-Subqueries are useful when you need to filter results or calculate an aggregate based on another query.'''


'''Explain about the DML,DDL,TCL,DQL commands?
-DML
DML commands are used to manipulate and manage data within existing database tables. They are essential for performing operations like inserting, updating, and deleting data.

DDL
DDL commands are used to define and manage database structures, including tables, schemas, and indexes. They focus on the schema and structure of the database rather than the data itself.

TCL
TCL commands manage transactions in a database. A transaction is a sequence of operations performed as a single logical unit of work, ensuring data integrity and consistency.

DQL
DQL commands are used to query and retrieve data from a database. They focus on querying the data and do not modify it.'''


'''Difference between Rank vs Dense_rank?
Rank:
- The RANK() function assigns a unique rank to each distinct value in the result set. When there are ties (multiple rows with the same value), RANK() will assign the same rank to all tied rows, but the next rank(s) will be skipped.
-If there are tied rows, they receive the same rank.
-The ranks of subsequent rows are adjusted to account for the number of tied rows.

Dense_rank:
-The DENSE_RANK() function also assigns ranks to rows but does not skip any ranks when there are ties. All tied rows receive the same rank, and the next rank is the immediate next number.
-If there are tied rows, they receive the same rank.
-If there are tied rows, they receive the same rank.'''



