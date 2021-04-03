import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1KBA6C8\\TEST;'
                      'Database=Testdb;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute(' SELECT CONTACTNUM  FROM Testdb.dbo.RESTABLE$ WHERE CONTACTNUM != \'\' ')

list = []

for row in cursor:
    list.append(row[0])
    
print(list)

#for list in cursor: 
#    print (list)
#  print(row[0])


string = '.jpg'
extension_list = [x + string for x in list] #appending ".jpg" extension over elements
print (extension_list)






