# def name():
#     print('Hello world')
# user = input('Введите свое имя: ')

# name()

#пример№1


# name = lambda: print('Hello World')
# name()

my_list = [1,2,3,4]
def number(number):
    for num in number:
        print(num * 2)
# number(my_list)
    
#пример№2

# lambda_bumbers = list(map(lambda numbers:numbers * 2, my_list))
# print(lambda_bumbers)

# num1 = [56,34,48]

# lambda_bum = list(map(lambda numbers:numbers / 2, num1))
# print(lambda_bum)




# #пример
# def multiply(x,y):
#     print(x*y)

# multiply(6,9)


# multiply = lambda x,y:x*y
# print(multiply(6,3))


#пример№4
# a = lambda x,y: [x+y, x-y, x*y, x/y]
# print(a(456,72))
# a = lambda x,y: x*y
# print(a(456,72))
# a = lambda x,y: x+y
# print(a(456,72))
# a = lambda x,y: x/y
# print(a(456,72))


#модули




#зфбота с файлами


#№1 пример
# text = open('lesson.txt', 'w')  #w - write
# text.write("print(5+5)")
# text.close

#№2 пример

# text = open('Meergul.txt','r')  # r - read
# result = text.read()
# print(result)


#№3пример
# with open('geeks.txt','w') as text:
#     text.write('Hello geeks')


#№4пример
with open('geeks.txt' , 'r') as text:
    content = text.read()
    print(content)