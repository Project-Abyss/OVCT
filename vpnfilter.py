import pandas
import csv

def filter(result):
    print('\n-----------------------------------\n')
    selection = input("【 Please enter the number for selecting one of the criteria to filter. 】\n\n1. Country \n2. Speed \n3. Without filtering (default) \n\n=> ")

    # Enter 1: country
    if selection == "1":
        result = filter_country(result)
        filtered_csv_path = Export(result)
        return filtered_csv_path

    # Enter 2: speed
    elif selection == "2":
        result = filter_speed(result)
        filtered_csv_path = Export(result)
        return filtered_csv_path

    # Enter 3: without filtering
    else:
        #print('\n-----------------------------------\n')
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
        print('\n-----------------------------------\n')
        print('There are some countries you can choose: \n')
        print((str(list(Country_Set)).replace(',','\n')))
        Input_Country = input("\n\n【 Please enter the country 】 \n\n=> ")
        if(Input_Country in Country_Set):
            break
        else:
            print('\n[Your input is not in the list, please enter it again.]')
    Source = Source[Source.CountryLong.eq(Input_Country)]
    return Source

def filter_speed(Source):
    Speed_list = Source.filter(items=['Speed'])
    SpeedMax = Speed_list.max()  
    SpeedMin = Speed_list.min()
    print('\n-----------------------------------\n')
    print('The Speed Range: ' + SpeedMin.to_string(index=False) + ' Mbps' + ' ~ ' + SpeedMax.to_string(index=False) + ' Mbps')
    Speed = int(input("\n【 How fast the VPN would you prefer 】\n\n=> "))
    Source = Source.query('Speed >= {}'.format(Speed))
    return Source

def no_filter(Source):
    return Source

def Export(Source):
    print('\n-----------------------------------\n')
    Path = input("【 Where would you like to save the CSV file? 】 \n\nPlease enter the absolute path and the \"file name\" (E.g. /home/user/Desktop/[choose a file_name]) \n\n=> ")
    Path += '.csv'
    # columns = ['HostName', 'Country', 'IP', 'Speed (Mbps)', 'OpenVPN_ConfigData_Base64']
    # source_CSV = Source.reindex(columns=columns)
    Source.to_csv(Path, sep=',', index=False)
    print("\n[The result has outputted!]\n")
    return Path
