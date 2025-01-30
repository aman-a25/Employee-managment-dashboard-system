import pymysql

class connectDb:

    def __init__(self):
        self.con = pymysql.Connect(host='localhost',database='project1',user='root',password='Admin@123')
                                   
    def _del_(self):
        self.con.close()

    def insert(self,e):
        sql=f"insert into emp values({e.e_id},'{e.e_name}','{e.post}',{e.e_sal})"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
        print("Employee Data inserted into emp table successfully")
        print(f"{e.e_name} Welcome to the Company")

    def update_name(self,e_id,newname):
        sql=f"update emp set e_name='{newname}' where e_id={e_id}"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
    
    def update_post(self,e_id,post):
        sql=f"update emp set post='{post}' where e_id={e_id}"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
    
    def update_salary(self,e_id,sal):
        sql=f"update emp set e_sal={sal} where e_id={e_id}"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
    
    def display(self):
        cur=self.con.cursor()
        cur.execute("select * from emp")
        for row in cur:
            print(row)
        self.con.commit()
        print("Data Displayed Successfully")

    def delete_employee(self,e_id):
        sql=f"delete from emp where e_id={e_id}"
        cur=self.con.cursor()
        cur.execute(sql)
        self.con.commit()
        print("Employee Data Deleted Successfully")
        print(f"Employee with ID {e_id} is no longer with the Company")

    def check_employee(self,e_id):
        sql=f"select * from emp where e_id={e_id}"
        cur=self.con.cursor()
        cur.execute(sql)
        return cur.rowcount==1