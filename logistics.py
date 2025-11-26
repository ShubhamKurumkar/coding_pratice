# A logistics company needs to track the daily delivery times (in hours) for 7 different routes. 
# Design a Python program using arrays/lists to store the data, calculate the average delivery time, 
# and display routes with delivery times greater than the average. Extend your program to handle sparse 
# data (some days may have no entries).


class logistics:
    def __init__(self):
        self.s=[]
    
    def inp(self,i=0):
        self.s.append(i)
    def enter_delivery_time(self):
        j=1
        while True:
            k=int(input(f"enter the delivery time for {j} route\n"))
            if k<=24:
                self.inp(k)
                j+=1
            else:
                print("enter the valid hour/time ,it must be under 24 hrs")
            if j==7:
                break
    
    def display_greater_then_avg(self):
        av=sum(self.s)//len(self.s)
        print(f"the avg delivery time is {av}")
        for i in self.s:
            if i>av:
                print(f"the number above avg is {i}")
    
lo =logistics()
lo.enter_delivery_time()
lo.display_greater_then_avg()
