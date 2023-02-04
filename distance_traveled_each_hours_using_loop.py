# this program uses loop for to enter value from the user and then calculate distance traveled each hour
# and print whole table

speed_of_vehicle = int(input("enter the speed : "))
number_of_hours = int(input("Enter the hours you traveled : "))

print('Hours \t Distance traveled ')

for hours in range(1 , number_of_hours+1):
    distance_traveled = hours * speed_of_vehicle
    print(hours, '\t\t', distance_traveled)