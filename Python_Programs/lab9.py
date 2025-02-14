import mysql.connector

class myDatabase:
    def __init__(self):
        # Use appropriate user, password, and database values
        self.db = mysql.connector.connect(
            host="172.16.34.43",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        self.cur = self.db.cursor()
        self.createtable()

    def createtable(self):
        query = """CREATE TABLE IF NOT EXISTS emp11(
                slno INT PRIMARY KEY,
                name VARCHAR(30),
                address VARCHAR(40),
                empcode VARCHAR(10),
                dob DATE,
                age INT,
                mobile VARCHAR(15),
                status INT,
                des VARCHAR(10)
            )"""
        self.cur.execute(query)
        self.db.commit()

    def insert(self, slno, name, address, empcode, dob, age, mobile, status, des):
        query = """INSERT INTO emp11(slno, name, address, empcode, dob, age, mobile, status, des) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (slno, name, address, empcode, dob, age, mobile, status, des)
        self.cur.execute(query, values)
        self.db.commit()

    def show(self):
        self.cur.execute("SELECT * FROM emp11")
        rows = self.cur.fetchall()
        for r in rows:
            print(r)

    def modify(self, des, slno):
        query = """UPDATE emp11 SET des=%s WHERE slno=%s"""
        values = (des, slno)
        self.cur.execute(query, values)
        self.db.commit()
        print("MODIFIED")

    def delete(self, slno):
        query = """DELETE FROM emp11 WHERE slno=%s"""
        values = (slno,)
        self.cur.execute(query, values)
        self.db.commit()
        print("DELETED")

# Create an instance of the myDatabase class
d = myDatabase()

while True:
    print("1.INSERT\n2.SHOW\n3.MODIFY\n4.DELETE\n5.EXIT\n")
    c = int(input("Enter your option:"))
    if c == 1:
        slno = int(input("Enter Serial No:"))
        name = input("Enter name:")
        address = input("Enter address:")
        empcode = input("Enter empcode:")  # Changed to input to accept string
        dob = input("Enter DOB (YYYY-MM-DD):")
        age = int(input("Enter age:"))
        mobile = input("Enter mobile number:")  # Changed to input to accept string
        status = int(input("Enter status:"))
        des = input("Enter designation:")
        d.insert(slno, name, address, empcode, dob, age, mobile, status, des)
    elif c == 2:
        d.show()
    elif c == 3:
        slno = int(input("Enter serial number:"))
        des = input("Enter new designation:")
        d.modify(des, slno)
    elif c == 4:
        slno = int(input("Enter slno for deletion:"))
        d.delete(slno)
    else:
        break
