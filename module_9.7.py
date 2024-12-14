 # "Декораторы"
 #


def is_prime(func):
    def wrapper(*args,**kwargs):
        rez = func(*args,**kwargs)
        if (isinstance(rez, int) and (rez > 0)):
            for i in range(2, int(rez**0.5)+1):
                if rez % i == 0:
                    print('Составное')
                    return rez
            print('Простое')        
            return rez
        print("Ошибка, результат - не натуральное число ") 
        return rez          
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)


result = sum_three(20, 1, 5)
print(result)


result = sum_three(0, 1, 0)
print(result)


result = sum_three(20, 1, 4)
print(result)

result = sum_three(0, 0, 0)
print(result)

result = sum_three(1.5, 0, 0.1)
print(result)

result = sum_three(-1, 0, -2)
print(result)