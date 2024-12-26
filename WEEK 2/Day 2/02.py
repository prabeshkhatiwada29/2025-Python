# public and private attribute methods
class Account:
    def __init_(self,acc_no,acc_pass):
     self.__acc_no = acc_no
     self.__acc_pass = acc_pass


     def reset_pass(self):
        print(self._acc_pass)


acc1= Account("1234","prabesh")
print(acc1.acc_no)
print(acc1.reset_pass())
