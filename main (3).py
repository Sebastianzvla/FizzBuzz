# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for count in range(1,101):
  if count %3 == 0 and count %5 == 0:
    print("FizzBuzz")
  elif count %5 == 0:
    print("Buzz")
  elif count %3 == 0:
    print("Fizz")
  else:
    print(count)
