'''
Problem:

Write a Python function calculate_average_grade that takes a list of student grades as input and returns the average grade. 
However, the function should also handle the following edge cases:

Invalid Input: If the input is not a list, the function should return None.
Empty List: If the input list is empty, the function should return None.
Non-numeric Grades: If the list contains any non-numeric values (e.g., strings), the function should return None.
Your task:

Implement the calculate_average_grade function according to the specifications.
Test the function with various input lists, including valid and invalid cases, to ensure it handles all scenarios correctly.
Print the results of your tests.

len(list) = number of items in a list

'''
grades = [10,24,30,22,34,35]


def calculate_average_grade(grades):
    if not isinstance(grades, list):
        print("Invalid data structure, please provide a list")
        return None
    if len(grades) == 0:
        print("Empty list, please provide values")
        return None
    
    sum_grade = 0
    for grade in grades:
        if not isinstance(grade, (int, float)):
            print("Wrong data type, please only provide integers")
            return None
        sum_grade += grade
    
    average_grade = sum_grade/len(grades)
    final_value = round(average_grade,0)
    return final_value
    
calculate_average_grade(grades)


'''
Scenario 1: inputs a tuple grades = (10,24,30,22,34,35)
Scenario 2: Empty list grades = []
Scenario 3: Non-numeric value  grades = [1, 2, 3, 'A']
Scenario 4: Expected input  grades = [10,24,30,22,34,35]
'''