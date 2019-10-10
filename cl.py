school_class = ''
while not school_class.isdigit():
    school_class = input('В каком ты классе')

school_class = int(school_class)

while school_class <= 11:
    print(school_class)
    school_class += 1

print('end')
