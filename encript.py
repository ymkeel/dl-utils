import pyminizip, os

compression_level = 5 # 1-9
zipfile = "music.zip" 
password = "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"
newlist = []

for file in os.listdir("./folder"):
    newlist.append(os.path.join('./folder', file))

pyminizip.compress_multiple(newlist, [], zipfile, password, compression_level)