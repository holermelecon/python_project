#This is the beginning of the program
#this program is to calculate the rate at which land is sold per meter square.

print ("Welcome")

#user to select if he is a buyer or seller
print ("Select B for Buyer and S for Seller")

#user enters string for seller or buyr respectively
user =  str (input("Enter S for Seller or Enter B for Buyer: "))

#user to enter the agreed amount and size before the land is being measured
print ("Enter the agreed amount and size before measurement")

#user enters the agreed amount and size before the land is being measured
amount = int (input("Enter Amount to be paid in ₦: "))
size = int (input ("Enter Size of land in m2: "))

#program automatically calculates the amount per m2
Total_1 = amount/size
print ("Values Saved")

#user enters the actual size of land after measurement provided the amount is constant
size_2 = int (input ("Enter Actual Size of land in m2: "))

#program calculates the the actual size and amount
Total_2 = amount/size_2

#program prints the amount per m2
print (Total_2)
print ("The amount per m2 is ₦"+str(Total_2))
print ("Thank You")
#end
