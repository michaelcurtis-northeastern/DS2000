#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
            Michael Curtis
            DS2000
            Homework 2
            Spring 2023
            avg_grade.py
            
            Test case:
                HW Grades: 91, 86, 86 Avg. -- 87.66
                Quiz Grade: 95, 95, 90 Avg. -- 93.33
                Viz Grade: 90
                    Overall grade: 87.66 (.75) + 93.33 (.20) + 90 (.05) = 
                        88.905
                    
                
"""
GRADE_FILE = "ds2000_grades.txt"


HW_WEIGHT = .75
QUIZ_WEIGHT = .2
VIZ_WEIGHT = .05

def main():
    
    
    
    number_assignment_hw = 0
    number_assignment_quiz = 0
    
    hw_grade = 0
    quiz_grade = 0
    viz_grade = 0 

    
    
    # Gather data -- read in 'ds2000_grades.txt' 
    
    with open(GRADE_FILE, "r") as infile:
        
        while True:
            assignment_type = infile.readline().strip()
            assignment_grade = infile.readline().strip()
            
           
            if assignment_type == "":
                break
            
            assignment_grade = float(assignment_grade)
    
            if assignment_type == "HW":
                number_assignment_hw +=  1
                hw_grade += assignment_grade
                
            if assignment_type == "Quiz":
                number_assignment_quiz += 1
                quiz_grade += assignment_grade
                
            if assignment_type == "Viz":
                viz_grade += assignment_grade
                
        # Compute -- find the average hw & quiz grade 
        
        avg_hw = hw_grade / number_assignment_hw
        avg_quiz = quiz_grade / number_assignment_quiz
            
        # Compute -- find the average 
        
        overall_avg = (avg_hw * HW_WEIGHT) + (avg_quiz * QUIZ_WEIGHT)\
            + (viz_grade * VIZ_WEIGHT)
            
    print("The Average HW grade is:", round(avg_hw, 2))
    print("The Average Quiz grade is:", round(avg_quiz, 2))
    print("The  Viz grade is: ", round(viz_grade, 2))
    print("The Average HW grade is:", round(overall_avg, 2))
        
            
            
            
    


main()
