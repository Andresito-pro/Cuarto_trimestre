def validarTexto(texto):
    return texto.strip() != ""
def validarNumero(numero):
    try:
        int(numero)
        return True
    except:
        return False