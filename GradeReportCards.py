'''
Created on Mar 12, 2019

@author: aspuckti22
'''

str= 0
grades= {"Alex":["A","A","B","A","B"], "Emily":["A","B","A","A","A"], "NAV":["C","D","B","E","C"], "Aiden":["B","D","B","A","A"], "Leopold":["A","A","A","A","A"]}

while str != '':
    print("__/Main Menu\__")
    print("Press 1 to view all of your students")
    print("Press 2 to view a specific student")
    print("Press 3 to add a grade to a students list")
    print("Press 4 to add a new student to the grade book")
    print("Press 5 to delete a student from the grade book")
    str= input("Enter a grade")
    
    if str== "1":
        print(grades.keys())
        input("Press enter to continue")
        
    if str== "2":
        students= input("Which student would you like to view?")
        while students in str:
            print(grades(students))
            input("Please press enter to return to the main menu")
            
    if str== "3":
        addgrades= input("Please enter the name of the student you would like to alter grades to")
        letgrades= input("What letter grade would you like to put in")
        while addgrades not in grades:
            add= input("The student is not included in the list, please enter the name corectly (This is case sensitive)")
        grades[addgrades].append(letgrades)
    
    if str== "4":
        newstud= input("What is the name of the student you would like to add?")
        grades[newstud]= ()
        input("Please press enter to return to the main menu")
        
    if str== "5":
        delstud= input("What student would you like to delete?")
        del grades.pop(delstud)
        input("Please press enter to return to the main menu")
        
        
            
        