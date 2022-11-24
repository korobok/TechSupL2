import sys
import datetime
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Проверяем был ли передан аргумент с именем сервера и формируем имя файла
if len(sys.argv) <= 1:
    servername = 'SERVER'
else:
    servername = sys.argv[1]

date = datetime.datetime.today()
date = date.strftime('%d_%m_%Y')

# Качаем и создаем файл с необходимыми именем SERVER_DATE_running.out
url = 'https://raw.githubusercontent.com/GreatMedivack/files/master/list.out'
filename = servername + '_' + date + '_running' + '.out'
urllib.request.urlretrieve(url, filename)
# Открываем файл и ищем все строки где присутствует Running, отсекаем лишнее и пишем в список.
f = open(filename)
servicerun = []
for line in f:
    if 'Running' in line:
        servicerun.append((line[:line.find(' ')]))
f.close()
# Снова открываем файл на запись и пишем в него список
f = open(filename, 'w')
servicerun = map (lambda x: x + '\n', servicerun)
f.writelines (servicerun)
f.close ()
