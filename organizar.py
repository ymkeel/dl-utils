import os, shutil

# limit = 335544320
# source = "all"
# destino = "mega"
class Organizar():
    def __init__(self, limit, source, destino):
        self.limit = limit
        self.source = source
        self.destino = destino

    # funcion de ayuda (no ejecutar explicitamnete)
    def set_counter(self):
        old = open("reg.txt","r")
        count = old.read()
        new = open("reg.txt", "w")
        new.write(str(int(count) + 1))
        new.close()

    # funcion de ayuda (no ejecutar explicitamnete)
    def get_counter(self):
        old = open("reg.txt","r")
        count = old.read()
        old.close()
        return int(count)

    # funcion de ayuda (no ejecutar explicitamnete)
    def get_size_per_folder(self):
        total = 0
        for file in os.listdir(self.source):
            file_info = os.stat(os.path.join(self.source, file))
            total += int(file_info.st_size)
        return total

    # funcion de ayuda (no ejecutar explicitamnete)
    def distr_folders(self):
        temps = []    
        for fl in os.listdir("./"):
            if fl.startswith(self.destino):
                temps.append(os.path.join("./", fl))

        return sorted(temps)

    # funcion de ayuda (no ejecutar explicitamnete)
    def full_path_file(self):
        with os.scandir(self.source) as it:
            list_folder = []
            for entry in it:
                list_folder.append(entry)

        return list_folder

    def create_foders(self):
        size_total = self.get_size_per_folder(self.source)
        number_of_folder = int(size_total/self.limit)

        while number_of_folder > 0:
            current_folder = f'{self.destino}{self.get_counter()}' 

            if not os.path.exists(current_folder):
                os.makedirs(current_folder)
                self.set_counter()

            number_of_folder -= 1

    def to_distribute(self, source, destino):
        self.create_foders(self.source, self.destino)
        for folder in self.distr_folders(self.destino):
            for file in self.full_path_file(self.source):
                if self.get_size_per_folder(folder) < self.limit:
                    shutil.move(file.path, f'{folder}/{file.name}')