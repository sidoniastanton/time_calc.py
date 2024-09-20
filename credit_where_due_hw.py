'''
process:

ask for amount of 3 credit hour classes user is taking
(create variable for credit_hours and multiply by 3)

ask how many days a week they work (work_days)
ask how long a work shift is (work_shift)
ask how many minutes it takes to get to work (multiply by 2 for return trip) (work_travel)

multiply credit hours by 2 to include study hours
multiply work_days by work_shift. multiply work_travel by work_days
add the new work_shift and work_travel results to get total_work_time (might be a float)

ask how many hours they sleep at night (sleep)
ask how long on average a meal takes (meal_time) and multiply by 3 per day

168 - credit_hours - total_work_time - sleep - meal_time = free time

'''

print("Welcome to the Class Credit Calculator!")
print("Please provide the following information:")

credit_hours = int(input("How many 3-credit classes are you taking right now?: "))
total_credit_hours = credit_hours * 3 
study_time = total_credit_hours * 2
total_academic_time = total_credit_hours + study_time
print("Total hours spent on academics: " + str(total_academic_time))

work_days = int(input("How many days a week do you work?: "))
work_shift = int(input("How many hours is your work shift?: "))
work_oneway = int(input("How many minutes does it take to get to work?: "))
work_travel = (work_oneway / 60) * 2

total_work_time = (work_days * work_shift) + (work_days * work_travel)
print("Total hours spent on work: " + str(total_work_time))