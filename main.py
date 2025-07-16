with open('/Users/macbookrik/Desktop/response', 'r') as file:
    lst = file.readlines()
    count = 0
    for i in lst:
        if i == '"Активность": false,\n':
            count += 1

    print(count)
