# 24.	The educational course finished with a test checking the participants' knowledge. 
# Here are the results obtained by the students:
# [37,51,44,23,78,92,39,84,83,51]
# Write a program that calculates and displays student scores that are equal to or greater than the following 
# minimum number of points to pass the course:
# a.	70
# b.	40
# c.	30
# Use the filter() function and the following higher order function:
# def min_pts(limit):
#     return lambda pts: pts>=limit
# Sample result:
# Min 70 pts: [78, 92, 84, 83]
# Min 40 pts: [51, 44, 78, 92, 84, 83, 51]
# Min 30 pts: [37, 51, 44, 78, 92, 39, 84, 83, 51]

def min_pts(limit):
    return lambda pts: pts >= limit

student_scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

min_points_criteria = [70, 40, 30]

for limit in min_points_criteria:
    filtered_scores = list(filter(min_pts(limit), student_scores))
    print(f"Min {limit} pts:", filtered_scores)