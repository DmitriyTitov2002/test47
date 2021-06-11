from Converter.json2xml import json2xml
from Converter.xml2json import Xml2Json
import json


if __name__ == '__main__':
    deal = input('Конвертер xml <-> json.\nВ какой файл вы хотите преобразовать json/xml: ')
    file = input('Введите название файла, который находится в категории Files (без разрешения): ')

    try:
        if deal == 'json':
            xml = open(f"Files/{file}.xml", 'r', encoding='UTF-8').read()
            result = Xml2Json(xml).result

            outputfile = open(f"ConvertedFiles/{file}.json", 'w', encoding='UTF-8')
            outputfile.write(str(result))
            outputfile.close()

        if deal == 'xml':

            with open(f"Files/{file}.json") as j_file:
                data = json.load(j_file)

            json2xml(data, file)

        print("Готово!")

    except FileNotFoundError:
        print("Такого файла не существует!")