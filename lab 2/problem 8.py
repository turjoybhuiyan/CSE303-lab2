nums=[i for i in range (1,1001)]
divisor = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
print(divisor)