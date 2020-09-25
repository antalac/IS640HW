# 3.11

avgmpg_list = []

while True:
    gallons_used = float(input('Enter the gallons used:'))
    if gallons_used == -1:
        break 
    miles_driven = float(input('Enter the miles driven:'))
    avg_mpg = miles_driven / gallons_used
    avgmpg_list.append(avg_mpg)
    print("The miles per gallon for this tank was", avg_mpg) 
            
overall_avg = sum(avgmpg_list) / len(avgmpg_list)

print('The overall average miles per gallon was:', overall_avg)