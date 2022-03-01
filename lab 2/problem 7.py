nums=[i for i in range (1,1001) if i%8==0]
divisor = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(divisor)