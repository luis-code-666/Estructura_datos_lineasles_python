'''fruits = []
print (fruits)
#aumenta donde la lista y va agregando con el append
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melos")
print (fruits)
#acomoda de forma alfavetica con el sort
fruits.sort()
print (fruits)
#seleccional lo ultimo de la lista con el pop
fruits.pop()
print (fruits)
#agregando a un espacio determinado insert
fruits.insert(0,"Apple")
print (fruits)
fruits.insert(0,"Atrawberry")
print (fruits)
#se puede quitat tambien con pop y buscando la posiscion
fruits.pop(0)
print (fruits)
#esta parte puyede remover una de las cosas de la listas
fruits.remove("Apple")
print(fruits)
'''
def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, upper,lower )
    if lower>upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
    
pyramid_sum(1, 4)