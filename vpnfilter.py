def filter(result):
    selection = input("Please enter the number for selecting one of the criteria to filter.\n1. Country \t2. Speed \t3. Without filtering (default) \n\n=> ")

    # Enter 1: country
    if selection == "1":
        result = filter_country()

    # Enter 2: speed
    elif selection == "2":
        result = filter_speed()

    # Enter 3: without filtering
    else:
        result = no_filter()

def filter_country():
    pass

def filter_speed():
    pass

def no_filter():
    pass
