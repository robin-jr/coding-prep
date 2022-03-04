# TODO: Complete the get_ruler function
def isVowel(char):
    return char in ['a','e','i','o','u','A','E','I','O','U']
def get_ruler(kingdom):
  ruler = 'Alice' if isVowel(kingdom[-1]) else 'Bob' if kingdom[-1]!='y' and kingdom[-1]!='Y' else 'nobody'
  # TODO: Add logic to determine the ruler of the kingdom
  # It should be either 'Alice', 'Bob' or 'nobody'.
  return ruler

def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()
