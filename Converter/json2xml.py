from xml.etree import cElementTree


def json2xml(data, name):
    """Функция преобразования json файла в xml, используя заданный стандарт json файла"""

    root_name = input('Введите название корня: ')
    root = cElementTree.Element(root_name)    # корень XML-файла

    for key in data.keys():
        person = cElementTree.SubElement(root, key)

        cElementTree.SubElement(person, "Organization").text = data[key]["Organization"]
        cElementTree.SubElement(person, "First_Name").text = data[key]["First_Name"]
        cElementTree.SubElement(person, "Last_Name").text = data[key]["Last_Name"]
        cElementTree.SubElement(person, "Age").text = str(data[key]["Age"])
        cElementTree.SubElement(person, "Vacancy").text = data[key]["Vacancy"]
        cElementTree.SubElement(person, "Salary").text = str(data[key]["Salary"])
        projects = cElementTree.SubElement(person, "Courses")

        for i in range(len(data[key]['Courses'])):
            course = cElementTree.SubElement(projects, f"Course{i}")
            cElementTree.SubElement(course, "Course_Name").text = data[key]["Courses"][i]["Course_Name"]
            cElementTree.SubElement(course, "Category").text = data[key]["Courses"][i]["Category"]
            cElementTree.SubElement(course, "Rating").text = str(data[key]["Courses"][i]["Rating"])

    xml_tree = cElementTree.ElementTree(root)
    xml_tree.write(f"ConvertedFiles/{name}.xml")