from mega import Mega

EMAIL = 'kesselyanniel@gmail.com'
PASS = 'yk15.EL+TIGRE'
LIMIT = 2684354560 # 2.5 GB
CURRENT_SIZE = 0

mega = Mega()
m = mega.login(EMAIL, PASS)


while CURRENT_SIZE < LIMIT:
    folder = m.find('vids')
    m.get_files(folder)