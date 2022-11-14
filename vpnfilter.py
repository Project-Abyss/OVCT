import pandas
import csv

def filter(result):
    selection = input("Please enter the number for selecting one of the criteria to filter.\n1. Country \t2. Speed \t3. Without filtering (default) \n\n=> ")

    # Enter 1: country
    if selection == "1":
        print('\n---------------------\n')
        result = filter_country(result)
        filtered_csv_path = Export(result)
        return filtered_csv_path

    # Enter 2: speed
    elif selection == "2":
        print('\n---------------------\n')
        result = filter_speed(result)
        filtered_csv_path = Export(result)
        return filtered_csv_path

    # Enter 3: without filtering
    else:
        print('\n---------------------\n')
        result = no_filter(result)
        filtered_csv_path = Export(result)
        return filtered_csv_path
        
def filter_country(Source):
    Country_list = Source.filter(items=['CountryLong'])
    Country_list = Country_list.astype(str)
    Country_list = Country_list['CountryLong'].values.tolist()
    Country_Set = set(Country_list)
    Country_Set.remove('nan')
    while(True):
        print('There are some countries you can choose: ')
        print(Country_Set)
        Input_Country = input("Please enter the country: \n\n=> ")
        print('\n---------------------\n')
        if(Input_Country in Country_Set):
            break
        else:
            print('Your input is not in the list, please enter it again.')
    Source = Source[Source.CountryLong.eq(Input_Country)]
    return Source

def filter_speed(Source):
    Speed_list = Source.filter(items=['Speed'])
    SpeedMax = Speed_list.max()
    SpeedMax /= 1000000    
    SpeedMin = Speed_list.min()
    SpeedMin /= 1000000
    print('The Speed Range: ' + SpeedMin.to_string(index=False) + ' Mbps' + ' ~ ' + SpeedMax.to_string(index=False) + ' Mbps')
    Speed = int(input("How fast the VPN would you prefer: \n\n=> "))
    print('\n---------------------\n')
    Speed *= 1000000
    Source = Source.query('Speed >= {}'.format(Speed))
    return Source

def no_filter(Source):
    return Source

def Export(Source):
    Path = input("Where would you like to save the CSV file (Please enter the absolute path and the \"file name\" (E.g. /home/user/Desktop/[choose a file_name]): \n\n=> ")
    Path += '.csv'
    Source.to_csv(Path, sep=',', index=False)
    print("\n[The result has outputted!]")
    print('\n---------------------\n')
    return Path
