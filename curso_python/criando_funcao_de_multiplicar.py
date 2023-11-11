# 1 forma de fazer

'''
def criar_multiplicador(multiplicador):
    def multiplicar(*args):
        for numero in args:
            print (numero * multiplicador, end=' ')
            
    return multiplicar

        
duplicador = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadriplicador = criar_multiplicador(4)

duplicador(2,3,4,5)
print()
triplicador(2,3,4,5)
print()
quadriplicador(2,3,4,5)
'''

# 2 forma de fazer

def criar_multiplicador(multiplicador):
    def multiplicar(*args):
        return [numero * multiplicador for numero in args]
            
    return multiplicar

        
duplicador = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadriplicador = criar_multiplicador(4)

print(*duplicador(2,3,4,5))
print(*triplicador(2,3,4,5))
print(*quadriplicador(2,3,4,5))

