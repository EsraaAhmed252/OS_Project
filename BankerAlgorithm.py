from operator import add

PN = 5
RN = 3

def detect(process, allocation, request, available):
    
    counter = 0
    flag = 1
    finish = [0]*PN 
    tempavail = [0]*RN
    
    for r in range (RN):
        tempavail[r] = available[r]
        
    while(flag):
        
        flag = 0
        for p in range(PN):
            if(finish[p] == 0):
                n=1
                for r in range(RN):
                    if(request[p][r] > tempavail[r]):
                        n=0
                        break
                    
                if (n):
                    finish[p] = 1
                    print("Process", p+1 , " is executing")
                    for r in range(RN):
                        tempavail[r] += allocation[p][r]
                        print(tempavail[r])
                    flag = 1
                    counter = counter+1

                
    if(counter == PN):
        return True
    else:
        return False
        
if __name__=='__main__':
	'''
	n=int(input('Enter number of processes: '))
	process=list(range(n))

	r=int(input('Enter number of resources: '))

	allocation=input('Enter allocation: ').split()
	request=input('Enter request: ').split()
	available=input('Enter available resources: ')
	'''
    
process=[0, 1, 2, 3, 4]
allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
available=[0, 0, 0]

print("System is safe") if (detect(process, allocation, request, available)) else print("System is unsafe") 
