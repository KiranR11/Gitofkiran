import mysql.connector

class MyDatabase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="kiran",
            password="kiran@123",
            database="Employee"
        )
        self.cur = self.db.cursor()
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS emp11 (
            slno INT PRIMARY KEY,
            name VARCHAR(30),
            address VARCHAR(40),
            empcode VARCHAR(10),
            dob DATE,
            age INT,
            mobile BIGINT,
            status INT,
            des VARCHAR(10)
        )"""
        self.cur.execute(query)
        self.db.commit()

    def insert(self, slno, name, address, empcode, dob, age, mobile, status, des):
        query = """INSERT INTO emp11 (slno, name, address, empcode, dob, age, mobile, status, des)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (slno, name, address, empcode, dob, age, mobile, status, des)
        self.cur.execute(query, values)
        self.db.commit()

    def show(self):
        self.cur.execute("SELECT * FROM emp11")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def modify(self, des, slno):
        query = """UPDATE emp11 SET des = %s WHERE slno = %s"""
        values = (des, slno)
        self.cur.execute(query, values)
        self.db.commit()
        print("MODIFIED")

    def delete(self, slno):
        query = """DELETE FROM emp11 WHERE slno = %s"""
        values = (slno,)
        self.cur.execute(query, values)
        self.db.commit()
        print("DELETED")

def main():
    db = MyDatabase()

    while True:
        print("1.INSERT\n2.SHOW\n3.MODIFY\n4.DELETE\n5.EXIT\n")
        choice = int(input("Enter your option: "))
        
        if choice == 1:
            slno = int(input("Enter Serial No: "))
            name = input("Enter name: ")
            address = input("Enter address: ")
            empcode = input("Enter empcode: ")
            dob = input("Enter DOB (YYYY-MM-DD): ")
            age = int(input("Enter age: "))
            mobile = int(input("Enter mobile number: "))
            status = int(input("Enter status: "))
            des = input("Enter designation: ")
            db.insert(slno, name, address, empcode, dob, age, mobile, status, des)

        elif choice == 2:
            db.show()

        elif choice == 3:
            slno = int(input("Enter serial number: "))
            des = input("Enter new designation: ")
            db.modify(des, slno)

        elif choice == 4:
            slno = int(input("Enter slno for deletion: "))
            db.delete(slno)

        elif choice == 5:
            break

        else:
            print("Invalid option! Please choose a valid option.")

if __name__ == "__main__":
    main()
