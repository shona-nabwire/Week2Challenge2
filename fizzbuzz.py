def fizzbuzz(a, b):
    try:
        
        sumoflists = len(a + b)
        if(sumoflists % 5 == 0 and sumoflists % 3 == 0):
            return "fizzbuzz"

        elif (sumoflists % 5 == 0):
            return "buzz"

        elif (sumoflists % 3 == 0):
            return "fizz"
        else:
            return sumoflists

    except TypeError:
        print("please enter a numerical list")