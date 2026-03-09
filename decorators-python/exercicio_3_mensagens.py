def announce(f):
    def wrapper():
        print("[INFO] Iniciando execução da função...")
        f()
        print("[INFO] Execução concluída com sucesso!")
    return wrapper
