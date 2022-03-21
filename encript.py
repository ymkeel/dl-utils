import pyminizip, os

class dl():
    def __init__(self, zipName, level, password, folder):
        self.zipName = zipName
        self.level = level
        self.password = password
        self.folder = folder


    def withEncrypt(self):
        newlist = []
        for file in os.listdir(self.folder):
            newlist.append(os.path.join(self.folder, file))
        pyminizip.compress_multiple(newlist, [], self.zipName, self.password, self.level)


# zipfile = "music.zip" 
# password = "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"