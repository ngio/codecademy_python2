# Let's look at those grades!

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades


# Print those grades
_grades(grades)

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for i in grades:
        print i
    return
print

# Review

print "Let's compute some stats!"


# The sum of scores

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
        total = 0
        for score in scores:
            total += score
        print total
        return total

grades_sum(grades)


# Computing the Average

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total_score = 0
    for score in scores:
        total_score += score
    return total_score

def grades_average(grades):
    average = grades_sum(grades) / float(len(grades))
    return average

print "Total Score", grades_sum(grades)
print "Average Score", grades_average(grades)



#  The Variance

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(grades):
    variance = 0
    for g in grades:
        variance += ((grades_average(grades) - g) ** 2) 
    return variance / len(grades)

print grades_variance(grades)


#  Standard Deviation

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    result = variance / len(scores)
    return result

def grades_std_deviation(variance):
    return (variance ** (0.5))

variance = grades_variance(grades)

print grades_std_deviation(variance)



# Review 9:9 

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    result = variance / len(scores)
    return result

print grades_variance(grades)

def grades_std_deviation(variance):
    result = variance ** 0.5
    return result

variance = grades_variance(grades)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)






# end

