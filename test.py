# # # import math
# # # def isPrime(n):
# # # 	if n==1:
# # # 		return True
# # # 	if n%2==0 and n>2:
# # # 		return False

# # # 	sqrt_n = int(math.sqrt(n))
# # # 	for i in range(3,sqrt_n):		
# # # 		if (n%i ==0):
# # # 			return False 
# # # 	return True



# # # print(isPrime(49))

# # # def isPrime(num):
# # # 	if num > 1:


# # # 		for i in range(2,num):
# # # 			if (num % i) == 0:
# # # 				return False
# # # 				break
			
# # # 		return True
# # # # 	else :
# # # # 		return False

# # # # print(isPrime(198491329))


# # def isPrime(num):

# # 	if num > 1:
# # 	   # check for factors
# # 	   for i in range(2,num):
# # 	       if (num % i) == 0:
# # 	           return False
# # 	           break
# # 	   else:
# # 	       return True
	       
# # 	# if input number is less than
# # 	# or equal to 1, it is not prime
# # 	else:
# # 	   return False

# # # print(isPrime(49))




# # def getSumOfDigits(n):
# #     # Your Code Here
# #     count=0
# #     if n >0:
# # 	    while(n != 0):
# # 	    	c=n%10
# # 	    	count = count + c
# # 	    	n=n//10
# # 	    return count
# #     else:
# #     	return count


# # def main():
# # 	print(getSumOfDigits(123))



 

# # if __name__=='__main__':
# #     from timeit import Timer
# #     t = Timer(lambda: getSumOfDigits(123))
# #     print(t.timeit(number=1))




# # def printSecondHighest(arr):
# # 	print(arr) 

# # #print(printSecondHighest([1,20,19,2,3,4,5,6,9,21]))





# # if __name__ == '__main__':
# #     t = int(input())
# #     for i in range(0, t):
# #         arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:t]          
# #     printSecondHighest(arr)



# #NOTE:  Use FOUR SPACES (Dont USE TABS) for indentation
# from sys import stdin, stdout  
  
# # suppose a function called main() and 
# # all the operations are performed 
# def main(): 
  
#     # input via readline method 
#     n = stdin.readline() 
  
#     # array input similar method 
#     arr = [int(x) for x in stdin.readline().split()] 	
  
#     #initialize variable 
#     summation = 0
      
#     # calculate sum 
#     for x in arr: 
#         summation += x 
  
#     # could use inbuilt summation = sum(arr) 
  
#     # print answer via write 
#     # write method writes only 
#     # string operations 
#     # so we need to convert any 
#     # data into string for input 
#     stdout.write(str(summation)) 
  
# # call the main method 
# if __name__ == "__main__": 
#     main()     




# 
# import collections
# from sys import stdin, stdout	
# def printMostFrequentCharacterAndOccuranceCount(s):
# 	d = collections.defaultdict(int)
# 	for c in s:
# 		d[c] += 1
# 	print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0])




# def printMostFrequentCharacterAndOccuranceCount(s):
# 	max = 0 
# 	chh = ''
# 	count = [0] * 256 
# 	for ch in s :
# 		count[ord(ch)] += 1
# 	for ch in s :
# 		if(count[ord(ch)] > max):
# 			mx = count[ord(ch)] 
# 			chh = ch
# 	return chh , mx
    
    
# if __name__=="__main__":
# 	testSize = int(input())
# 	for _ in range(testSize):
# 		if(testSize>0):
# 			nArr=input()
# 			print(printMostFrequentCharacterAndOccuranceCount(nArr))

# def printMostFrequentCharacterAndOccuranceCount(s):
# 	max = 0 
# 	chh = ''
# 	count = [0] * 256 
# 	for ch in s :
# 		count[ord(ch)] += 1
# 	for ch in s :
# 		if(count[ord(ch)] > max):
# 			max = count[ord(ch)] 
# 			chh = ch
# 	print(chh , max)
# printMostFrequentCharacterAndOccuranceCount("Hellooooo")

# def absoluteDistinctValues(arr):
# 	print(len(list(set([abs(a) for a in arr]))))


# absoluteDistinctValues([-1,3,1,2,3,4,7,9])



def num(n):
	if n == 0:
		return 0
	elif n==1:
		return 1
	else:
		num(n-1)
		return n
	
		

print(num(5))
