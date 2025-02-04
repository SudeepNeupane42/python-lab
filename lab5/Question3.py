class Employee:
    def calculate_salary(self):
        pass
    
class Fulltimeemployee(Employee):
    def calculate_salary(self,sal):
        return sal*12
    
class Freelancer(Employee):
    def calculate_salary(self,rate,wage):
        return rate*wage
    
full=Fulltimeemployee()
print("the fulltime employee salary is ",full.calculate_salary(12000))

part=Freelancer()
print("The parttime employee salary is ",part.calculate_salary(2000,3))