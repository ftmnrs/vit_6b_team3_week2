students = {
    "Ahmet Yilmaz": [85, 90, 78],
    "Mehmet Demir": [92, 88, 76],
    "Ayse Kaya": [78, 98, 95],
    "Zeynep Celik": [65, 70, 80],
    "Ali Kara": [50, 60, 55],
    "Fatma Yildiz": [88, 85, 90],
    "Murat Aydin": [72, 68, 74],
    "Elif Aksoy": [95, 90, 88],
    "Hakan Ozturk": [45, 50, 55],
    "Canan Tas": [80, 75, 82],
}

for student, grades in students.items():
    gpa = sum(grades) / len(grades)  
    students[student] = {"Notlar": grades, "Ortalama": round(gpa, 2)} 

isim_tuple=()
for key in students.keys():
    yeni_isim= key.split(" ")
    isim_tuple= isim_tuple + (yeni_isim, students.get(key),)


converted_tuple= list(isim_tuple)
for i in converted_tuple:
    print (i)




    

