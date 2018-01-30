def temp_converter():
    while True:
        try:
            temp = int(raw_input("Please enter a number: "))
            break
        except (ValueError, RuntimeError, TypeError, NameError):
            print "You need to enter a number for the temperature"
    celcius = int(5.0 / 9.0 * (temp - 32))
    print str(celcius) + ' degrees celcius'

temp_converter()
