class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print("Hi",self.name,"your avg score is:",sum/3)

s1= student("prabesh",[99,3,4,])
s1.get_avg()