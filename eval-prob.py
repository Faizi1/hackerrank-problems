# Enter your code here. Read input from STDIN. Print output to STDOUT
def solution(x, k, expr):
  return "True" if eval(expr) == k else "False"

def main():
  x, k = map(int, input().strip().split())
  expr = input()
  print(solution(x, k, expr))

if __name__ == "__main__":
  main()