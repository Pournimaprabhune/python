emp=["john",102,"USA"]
dep1=["cs",10]
dep2=["IT",11]
hod_cs=[10,"mrs.komal"]
hod_IT=[11,"mrs.pournima"]
print("printing employee data ...")
print("name:%s \tid:%d \tcountry:%s\t"%(emp[0],emp[1],emp[2]))
print("print department...")
print("department1:\ndeparment_name:%s\tid:%d\ndepartment2:\ndepartment_name:%s\tid:%d"%(dep1[0],dep1[1],dep2[0],dep2[1]))
print("HOD details")
print("HOD1:\nHOD_ID:%d\tHOD_Name:%s\nHOD2:\nHOD_ID:%d\tHOD_Name:%s"%(hod_cs[0],hod_cs[1],hod_IT[0],hod_IT[1]))
print(type(emp), type(dep1),type(dep2),type(hod_cs),type(hod_IT))
 