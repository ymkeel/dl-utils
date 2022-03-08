import os, shutil

limit = 295000000 # 300.0 MB
source = "all"
destino = "mega"

# funcion de ayuda (no ejecutar explicitamnete)
def set_counter():
    old = open("reg.txt","r")
    count = old.read()
    new = open("reg.txt", "w")
    new.write(str(int(count) + 1))
    new.close()
    
# funcion de ayuda (no ejecutar explicitamnete)
def get_counter():
    old = open("reg.txt","r")
    count = old.read()
    old.close()
    return int(count)

# funcion de ayuda (no ejecutar explicitamnete)
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

# funcion de ayuda (no ejecutar explicitamnete)
def get_size_per_folder(source):
    total = 0
    for file in os.listdir(source):
        file_info = os.stat(os.path.join(source, file))
        total += int(file_info.st_size)
    return total

# funcion de ayuda (no ejecutar explicitamnete)
def distr_folders(destino):
    temps = []    
    for fl in os.listdir("./"):
        if fl.startswith(destino):
            temps.append(os.path.join("./", fl))
    
    return sorted(temps)

# funcion de ayuda (no ejecutar explicitamnete)
def full_path_file(source):
    with os.scandir(source) as it:
        list_folder = []
        for entry in it:
            list_folder.append(entry)

    return list_folder

def create_foders(source, destino):
    size_total = get_size_per_folder(source)
    number_of_folder = int(size_total/limit)
    
    while number_of_folder > 0:
        current_folder = f'{destino}{get_counter()}' 
        
        if not os.path.exists(current_folder):
            os.makedirs(current_folder)
            set_counter()
        
        number_of_folder -= 1

def to_distribute(source, destino):
    for folder in distr_folders(destino):
        for file in full_path_file(source):
            if get_size_per_folder(folder) < limit:
                shutil.move(file.path, f'{folder}/{file.name}')

create_foders(source, destino)
to_distribute(source, destino)