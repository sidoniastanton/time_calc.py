'''
Sidonia Stanton
September 20 2024
"Credit Where It's Due"

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

desired_credit_hours = int(input("How many credit hours do you want?: "))
x = desired_credit_hours / 3
y = x
x = int(x)
leftover_credits = y - x
print("Total classes that can be taken: " + str(x))
print("Total leftover credit hours: " + str(leftover_credits))

study_time = desired_credit_hours * 2
total_academic_time = desired_credit_hours + study_time
print("Total hours per week spent on academics: " + str(total_academic_time))
not_academic_time = 168 - total_academic_time
print("Total non-academic hours per week: " + str(not_academic_time))


work_days = int(input("How many days a week do you work?: "))
work_shift = int(input("How many hours is your work shift?: "))
work_oneway = int(input("How many minutes does it take to get to work?: "))
work_travel = (work_oneway / 60) * 2

total_work_time = (work_days * work_shift) + (work_days * work_travel)
print("Total hours per week spent on work: " + str(total_work_time))

sleep_hours = int(input("How many hours of sleep do you get each night?: "))
total_sleep_hours = sleep_hours * 7
print("Total hours per week spent sleeping: " + str(total_sleep_hours))

prep_time = int(input("How many minutes does it take you to get ready every day?: "))
total_prep_time = (prep_time * 7) /60
print("Total hours per week spent preparing for the day: " + str(total_prep_time))

single_meal = int(input("How many minutes does it take you to eat a meal?: "))
meal_hours = (single_meal * 3) / 60
total_meal_hours = meal_hours * 7
print("Total hours per week spent on meals: " + str(total_meal_hours))

free_time = 168 - total_meal_hours - total_academic_time - desired_credit_hours - total_sleep_hours - total_work_time - total_prep_time
print("Total free hours left over per week: " + str(free_time))