from functions import webcrawler, data_processing

def get_current_list(All_Source_Path):
    print("\n[ Initilizing... ]")
    Updated_Source = webcrawler.load_table()
    data_processing.list_reload(Updated_Source, All_Source_Path)
    return Updated_Source
