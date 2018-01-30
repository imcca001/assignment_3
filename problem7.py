num_list = [1,4,5,6,100]

# Approach 1
def centered_average_with_iteration(numbers):
    numbers.sort()
    numbers.pop(0)
    numbers.pop()
    total = 0
    count = 0
    for num in numbers:
        total += float(num)
        count += 1
    average = total / count
    print average
    return average

# Approach 2
def centered_average(numbers):
    numbers.sort()
    #print numbers
    numbers.pop(0)
    #print numbers
    numbers.pop()
    #print numbers
#Think python mentioned reduce, map and filter but did not show how to impliment them
#I went and looked these up as I was familiar with their functionality from working
#with the Javascript underscore.js library, I'm guessing that these built in functions or 
    total = reduce(lambda x, y: x + y, numbers)
    average = (float(total) / len(numbers))
    print average
    return average

centered_average(num_list)
centered_average_with_iteration(num_list)
