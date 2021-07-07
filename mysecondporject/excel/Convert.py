import csv
from django.conf import settings
import os

def ConvertCsvToList(file_path):
    file_path_media = os.path.join(settings.MEDIA_ROOT, str(file_path))
    list = []
    with open(file_path_media, newline='') as csvfile:
        print(csv.__file__)
        rows = csv.reader(csvfile, delimiter=';', quotechar='|')
        headers = next(rows)
        list.append({'headers' :[ headers[0], headers[1]]})
        for row in rows:
            diccionario_aux = {headers[0] : row[0], headers[1] : row[1]}
            list.append(diccionario_aux)
    return list

def DeleteFile(file_path):
    file_path_media = os.path.join(settings.MEDIA_ROOT, str(file_path))
    os.remove(file_path_media)



