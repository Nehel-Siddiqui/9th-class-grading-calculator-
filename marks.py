print("****** GRADES CALCULATOR OF 9TH CLASS ********")
sindhi = float(input("marks obtain in Sindhi out of 75 is "))
english = float(input("marks obtain in english out of 75 is  "))
chemistry = float(input("marks obtain in chemistry out of 100 is  "))
pakistan_studies = float(input("marks obtain in pakistan studies out of 75 is  "))
computer = float(input("marks obtain in computer out of 100 is  "))
print ("Obtain marks out of 425 is  : ")
print(computer + sindhi + english + chemistry + pakistan_studies) 
a = computer + sindhi + english + chemistry + pakistan_studies
b = 425
c = 100
print ("Percentage: ")
c= (a / b * c )
print(c) 
if c >= 80 :
     print("A+ GRADE")
elif c >= 70 :
     print("A GRADE")
elif 70 > c >= 60 :
     print("B GRADE")
elif 60 > c >= 50 :
     print("C GRADE")
elif 50 > c >= 40 :
     print(" D GRADE")
else :
     print ("fail")