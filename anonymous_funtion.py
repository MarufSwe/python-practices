# Normal Function Example
def sumTowNum(a,b):
    return a+b
result = sumTowNum(5, 5)
print(result)


# Anonymous/Lambda Function Example 1
multiplyTowNum = lambda x,b : x*b
ans = multiplyTowNum(5,10)
print(ans)

# Anonymous/Lambda Function Example 2
full_name = lambda fn, ln: fn.strip().title() + '' + ln.strip().title()
full_name("khan", "MARUF")
print(full_name)
