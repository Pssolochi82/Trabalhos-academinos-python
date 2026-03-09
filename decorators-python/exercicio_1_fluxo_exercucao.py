def announce(f):
    # announce recebe a função original (ola)
    
    def wrapper():
        # wrapper é a função que vai "substituir" a função original
        
        print("Sobre o correr a função ...")
        # executa antes da função original
        
        f()
        # chama a função original (ola)
        
        print("Está feito a função.")
        # executa depois da função original
    
    return wrapper
    # devolve a função wrapper
