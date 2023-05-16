#Q1
def count_vowels(string):
  """
    This function takes a string as input and returns the count of vowels in the string.
    """
  vowels = 'aeiouAEIOU'
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count
# Example usage:
if __name__ == "__main__":

  print(count_vowels('Hello, World!'))
  print(count_vowels('python!'))
  
  
 


#Q2
  for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        
        
        
#Q3
def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Check if the reversed string is equal to the original string
    return string == string[::-1]
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # Output: True

#Q4
def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev1 = 0
        prev2 = 1
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        return prev2
n = 10
result = fibonacci(n)
print(f"The {n}th number in the Fibonacci sequence is: {result}")  



#Q5
def largest_element(numbers):
    if not numbers:
        raise ValueError("List must not be empty.")
        
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest
numbers = [5, 9, 2, 11, 3, 8]
result = largest_element(numbers)
print(f"The largest element in the list is: {result}")  


