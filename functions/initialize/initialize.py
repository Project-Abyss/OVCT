from functions import data_processing
from functions.initialize import webcrawler

def get_current_list(All_Source_Path):
    print("\n[ Initializing... ]")
    Updated_Source = webcrawler.load_table()
    data_processing.list_reload(Updated_Source, All_Source_Path)
    return Updated_Source
