def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100!=0:
            if year%400==0:
                return True
    return leap

year = int(input())
print(is_leap(year))

# if __name__ == '__main__':
#     n = int(input())
    
#     r = list(range(1,n+1))
#     val = ''.join(str(e) for e in r)
#     print(val)


