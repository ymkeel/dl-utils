import pyminizip, os

password = "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"
zipfile = "music.zip" 
output = os.path.join(os.getcwd(), 'music')

pyminizip.uncompress(zipfile, password, output, 1)