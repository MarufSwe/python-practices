def person(name, **data):
    print(name)

    for i, j in data.items():
        print(i, j)

person('maruf', age=25, city='Dhaka', mob=1711111)

# When pass multiple data as parameter that time use double ** keyword