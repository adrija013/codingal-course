def TwoOdd(arr, size):
   xorof2, x, y,SetBit = arr[0],0,0,0

   for i in range(1, size):
      xorof2 = xorof2 ^ arr[i]
   SetBit = xorof2 & ~(xorof2-1)

   for i in range(size):
     if(arr[i] & SetBit):
        x = x ^ arr[i]
     else:
        y = y ^ arr[i]#000 ^ 110 = 110, 110^110 = 000, 000^110 = 110 = 6  
   return(x,y)

arr = []
arr_size = int(input("Enter the size of the array: "))
for i in range(0, arr_size):
     z = int(input("Enter element:"))
     arr.append(z)

x, y = TwoOdd(arr, arr_size)  
print("TwoOdd elements are", x, "&", y)  


