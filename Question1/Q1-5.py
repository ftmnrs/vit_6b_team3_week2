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

for ogrenci, grades in students.items():
    gpa = sum(grades) / len(grades)  
    students[ogrenci] = {"Notlar": grades, "Ortalama": round(gpa, 2)} 


tembeller = set()

for x,y in students.items():
    if y["Ortalama"] <=70:
        tembeller.add(x)

print(tembeller)



    

