
class ATM():
    
    """docstring for ClassName"""
    def __init__(self, balance,bank_name):
        
        self.balance = balance 
        self.bank_name = bank_name
        self.withdrow_list = []

    def withdrow(self,requst):


        print " welcom " + str(self.bank_name)
        print " current balance =" + str(self.balance) 
        print " balance after refactored  " + str(self.balance - requst)
        atm_list = []

        if  requst > self.balance :
            print("Can't give you all this money !!")
        elif requst < 0 :
            print("More than zero plz!")
        else :
            self.balance = self.balance - requst
            self.withdrow_list.append(requst)
            while requst > 0 :
                if requst >= 100 :
                    atm_list.append(100) 
                    requst = requst - 100
                    print ("give 100")
                elif requst >= 50 :
                    atm_list.append(50)
                    requst = requst - 50
                    print ("give 50")
                elif requst >= 10 :
                    atm_list.append(10)
                    requst = requst - 10
                    print ("give 10")
                elif requst >= 5 :
                    atm_list.append(5) 
                    requst = requst - 5
                    print("give 5")
                else : 
                    atm_list.append(requst) 
                    print "give" + " " + str(requst)
                    requst = requst - requst

    def show_withdrow_list (self):
        print("reciept for all withdrow")
        for i in self.withdrow_list :
            print(i)

                    
     
atm1 = ATM(1000,"sara bank")
atm1.withdrow(530)
atm1.withdrow(344)
atm1.withdrow(100)
atm2 = ATM(500,"baraka bank")
atm2.withdrow(220)
atm2.withdrow(100)
atm2.withdrow(90)
atm1.show_withdrow_list()
atm2.show_withdrow_list()



     


              
