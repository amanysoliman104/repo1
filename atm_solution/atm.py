import os 
def atm_task(requst):

	 
	atm_list = []
	while requst > 0 :
		if requst > 100 :
			atm_list.append(100) 
			requst = requst - 100
		else :
			if requst > 50 :
				atm_list.append(50)
				requst = requst - 50
			else :
				if requst > 10 :
					atm_list.append(10)
					requst = requst - 10
				else :
					if requst > 5 :
						atm_list.append(5) 
						requst = requst - 5
					else : 
						atm_list.append(requst) 
						requst = requst - requst

	return atm_list					

    
read_atm = atm_task(577)
for count in read_atm :
	print "give" + "  "+ str(count )

  



						
					


			    


				




			
		

