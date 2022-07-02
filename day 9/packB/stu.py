class Student:
    def __init__(self,sid,sname,grade):
        self.sid=sid
        self.sname = sname
        self.grade=grade
    def displaystu(self):
        print(self.sid,self.sname,self.grade)