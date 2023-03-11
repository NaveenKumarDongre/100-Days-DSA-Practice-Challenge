class Employee:
    # class Variable
    compName = "gfg"
    
    def __init__(self, id):
        # Instance variable
        self.id = id 


if __name__ == "__main__":
          
    e = Employee(101)
    print(e.compName)
    print(e.id)
    Employee.compName = "Google"
    print(Employee.compName) 

    e1 = Employee(102)
    print(e1.compName)
    e1.name = "Rahul"
    # print(help(e1)) 
    print(e1.__dict__)
    # print(e1.__weakref__)
    
    
    # Instace member get more priority than
    # that of the class memeber
    e2 = Employee(1001)
    Employee.officeAdd = "Noida"
    e2.officeAdd = "NCR"
    print( Employee.officeAdd )
    print( e2.officeAdd )
   
