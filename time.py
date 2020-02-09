current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

currentTimeInt = int(current_time_str)
waitTimeInt = int(wait_time_str)

finalTime_Int = currentTimeInt + waitTimeInt
print(finalTime_Int)

#Corrected the missing perenthesis on line 2
#Corrected the capitalization and underscores on variable "current_time_str" on line 1
#Corrected the capitalization and underscores on variable "wait_time_str" on line 2
#Added the underscore to finalTimeInt variable on line 7
