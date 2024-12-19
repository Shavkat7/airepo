universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list):
    student_enrolment = [val[1] for val in list]
    tution_fees = [val[2] for val in list]
    return student_enrolment, tution_fees

student_enrolment = enrollment_stats(universities)[0]
tuition_fees = enrollment_stats(universities)[1]

def mean(list):
    return f"{sum(list)/len(list):.2f}"
def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[len(list)/2] + list[len(list)/2 + 1])/2
    return list[int(len(list)/2)]


print("******************************")
print("Total students:", sum(student_enrolment))
print("Total tuition: $", sum(tuition_fees), "\n")
print("Student mean:", mean(student_enrolment))
print("Student median:", median(student_enrolment), "\n")
print("Tuition mean: $", mean(tuition_fees))
print("Tuition median: $", median(tuition_fees))
print("******************************")
