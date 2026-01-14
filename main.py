part = input("Enter your input : ").split()

if(len(part) != 4):
   print ("Invalid Input ")
   

else:
   inhr,inmin,outhr,outmin = map(int,part)
   if(inhr> 23 or outhr >23):
      print("Invalid Input ")
   elif(inmin > 59 or outmin > 59):
         print("Invalid Input ")
   else:
      incar = (inhr*60)+inmin
      outcar = (outhr*60)+outmin

      if(incar < 420 or outcar > 1380):
         print("Invalid Input ")
      elif(outcar-incar <= 0 ):
         print("Invalid Input ")
      elif(0 < outcar-incar <= 15):
         print("0")
      elif(15 < outcar-incar <= 60 ):
         print("10")
      elif(60 < outcar-incar <= 120 ):
         print("20")
      elif(120 < outcar-incar <= 180 ):
         print("30")
      elif(180 < outcar-incar <= 240 ):
         print("50")   
      elif(240 < outcar-incar <= 300 ):
         print("70")
      elif(300 < outcar-incar <= 360 ):
         print("90")
      else:
         print("200")     