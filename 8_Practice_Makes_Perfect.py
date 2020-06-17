# Practice! Practice Practice!


# is_even

  
def is_even(x):
    if x % 2 == 0: 
        return True 
    else: 
        return False
        
 
 # is_int


  
def is_int(x):
    if x==0:
      return True
    elif (x/int(x)) ==1:
      return True
    else:
      return False

print is_int(7.0)   # True    
print is_int(7.5)   # False    
print is_int(-1)    # True  
 
 
 
# digit_sum
  
def digit_sum(n):
    digit = []
    n = str(n)
    for i in n:
            i = int(i)
            digit.append(i)

    return sum(digit)



print digit_sum(123)
 
 
 
# factorial

  
def factorial(x):
    n = x - 1
    while n > 0:
        x = x * n
        n -= 1
    return x

print factorial(4)  # 24 = 4*3*2*1
print factorial(1)  # 1
print factorial(3)  # 6  = 3*2*1


# is_prime
  
def is_prime(x):
    isPrime = False
    if (x < 2):
       isPrime = False
    elif (x == 2):
        isPrime = True
    else:
        for n in range(2,x):
            if ( x % n) == 0:
                isPrime = False
                break
            else:
                isPrime = True
    return isPrime

print is_prime (2)
print is_prime (4)
print is_prime(9) 



# reverse

""" Great work so far! Let’s practice writing some functions that work with strings. """

  
def reverse(text):
    stringg=''
    x=len(text)
    while(x>0):
        stringg=stringg+text[x-1]
        x=x-1
    return stringg

print reverse("hello")

 
# anti_vowel

def anti_vowel(text):
    vowels = 'aeiou'
    new_text = ''
    for i in text:
        if i.lower() not in vowels:
            new_text += i
    return new_text

print anti_vowel("Hey You!")  # Hy Y!
 
 
 
# scrabble_score

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}


         
def scrabble_score(word):
    word = word.lower()
    total=0
    for char in word:
        total = total + (score[char])
    return total   

print scrabble_score("pie")     # 5
print scrabble_score("guwtSEA") # 11
print scrabble_score("zz")      # 20
 
 
 
# censor

  
def censor(text, word):
    lst = text.split()
    lst2 = []
    for w in lst:
        if w == word:
            lst2.append("*"*len(w))
        else:
            lst2.append(w)
    print " ".join(lst2)
    return " ".join(lst2)

print censor("this hack is wack hack", "hack")
 
 
 
 
# count

def count (sequence, item):
    count = 0
    for i in sequence:
        if type (item) != list:
            if i == item:
                count += 1
        else:
            for n in item:
                if n == i:
                    count += 1
    return count 

print count([1, 2, 1, 1], 1) # 3
print count([1, 2, 1, 1], 2) # 1
print count([1, 2, 1, 2], 2) # 2
 
 
# purify
""" 홀수 제거 """
  
def purify(n):
    n_even=[]
    for i in n:
        if i%2==0:
            n_even.append(i)
    return n_even

print purify([1,2,3])    # [2]
print purify([4,5,5,4])  # [4,4]
print purify([2,4,6,8])  # [2,4,6,8]
print purify([2, 3, 5, 7, 10])  #[2, 10]
 
 
# product

def product(numbers):
    total = 1
    for each in numbers:
        total *= each
    return total

print product([4, 5, 5]) # 100 (because 4 * 5 * 5 is 100).
 
 
# remove_duplicates

def remove_duplicates(nimbs):
    noDup=[]
    marks={}
    for j in nimbs:
            marks[j]=False
    for i in nimbs:
        if marks[i]==False:
            noDup.append(i)
            marks[i]=True
    return noDup

print remove_duplicates([1, 1, 2, 2])  # return [1, 2]
print remove_duplicates([1, 2, 3]) 
 
 
 
 
 # median
""" 정렬 된 숫자 순서의 중간 숫자입니다. """
  
def median(list_num):
    s = sorted(list_num)
    if len(s)%2 == 0:
        return (s[len(s)/2] + s[(len(s)/2) - 1]) / 2.0
    else: 
        return s[(len(s)-1)/2]


print median([1, 1, 2])
print median([1,1,2])  

print median([4, 5, 5, 4,2,5,6,9,10]) # 5

test = [1, 45, 9, 91, 8, 8]
print (median(test))  # 8.5

test2 = [4, 5, 5, 4]
print (median(test2))  # 4.5
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
