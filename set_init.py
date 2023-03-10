import os

def init_file_name():
    dirPath = os.getcwd().replace('\\', '/')
    dirPath = str(dirPath) + '/functions'
    file_list = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    file_name = []
    for i in file_list:
      j = i.strip('.py')
      file_name.append(j)

    file_name.remove("__init__")
    for i in file_name:
        if ((".sw" in i) or (".pyc" in i)):
            file_name.remove(i)
        
    #write ./function/__init__.py
    file = open('./functions/__init__.py', 'w')
    file.write("__all__ = ")
    file.write(str(file_name))
    file.close()
