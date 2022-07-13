def Palindrome(str1):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str1)/2)):
        if str1[i] != str1[len(str1)-i-1]:
            print("No")
    print("Yes")

str1 = input("Enter a word:")
Palindrome(str1)
 
