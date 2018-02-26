def withdrow(balance,requst):
    
    print " current balance = " + str(balance) 
    print " balance after refactored  " + str(balance - requst)
    atm_list = []
    if  requst > balance :
        print("Can't give you all this money !!")
    elif requst < 0 :
        print("More than zero plz!")
    else :
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
 
     

withdrow(500,277) 
              
