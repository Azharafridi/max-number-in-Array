# this program display the km from 10 to 80 with 10 increment
# Also its equivalence miles

km_start = 10  # for the start of the range of km
km_end = 80     # for the end of the km range
print("KM \t MILES ")
for km in range(km_start,km_end + 1,10) :
    mile = 1.6034*km

    print(km , '\t' , format(mile , '.2f'))     # the format is for the float value rounded upto 2 decimal point
