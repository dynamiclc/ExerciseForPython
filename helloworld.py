#!/usr/bin/python3

#
# Example file for HelloWorld
#

def someFunction():
  # Global F
  globalF = "def";
  print(globalF)

def main():
  print("Hello World!")
  # Declare a variable and initialize it
  f = 0;
  print(f)
  
  # Re-declaring the variable works
  f = "abc"
  print(f)

  # Different types cannot be combined
  # print("string type" + 123) gives error
  print("string type" + str(123))
  someFunction()
  print(globalF)

if __name__ == "__main__":
  main()

print("END")
