class Student:
  def __init__(self, name,marks):
    self._name=name
    self._marks=marks

  def get_avg(self):
      sum=0
      for val in self._marks:
        sum+=val
        print('hi',self.name,"your avg score is:",sum/3)

s1=Student("John",[90,80,70])
s1.get_avg()

