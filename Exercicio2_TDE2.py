def mefd_l0(entrada):
    """Cada 0 deve ser seguido de pelo menos um 1."""
    estado = 's0'
    for s in entrada:
        if estado == 's0':
            if s == '0': estado = 's1'
            elif s == '1': estado = 's0'
            else: return False
        elif estado == 's1':
            if s == '0': estado = 's_erro'
            elif s == '1': estado = 's0'
            else: return False
        elif estado == 's_erro':
            estado = 's_erro'
    return estado == 's0'


def mefd_l1(entrada):
    """String deve terminar com 00."""
    estado = 's0'
    for s in entrada:
        if estado == 's0':
            if s == '0': estado = 's1'
            elif s == '1': estado = 's0'
            else: return False
        elif estado == 's1':
            if s == '0': estado = 's2'
            elif s == '1': estado = 's0'
            else: return False
        elif estado == 's2':
            if s == '0': estado = 's2'
            elif s == '1': estado = 's0'
            else: return False
    return estado == 's2'


def mefd_l2(entrada):
    """String deve conter exatamente 3 zeros."""
    estado = 's0'
    for s in entrada:
        if estado == 's0':
            if s == '0': estado = 's1'
            elif s == '1': estado = 's0'
            else: return False
        elif estado == 's1':
            if s == '0': estado = 's2'
            elif s == '1': estado = 's1'
            else: return False
        elif estado == 's2':
            if s == '0': estado = 's3'
            elif s == '1': estado = 's2'
            else: return False
        elif estado == 's3':
            if s == '0': estado = 's_erro'
            elif s == '1': estado = 's3'
            else: return False
        elif estado == 's_erro':
            estado = 's_erro'
    return estado == 's3'


def mefd_l3(entrada):
    """String deve iniciar com 1."""
    estado = 's0'
    for s in entrada:
        if estado == 's0':
            if s == '0': estado = 's_erro'
            elif s == '1': estado = 's1'
            else: return False
        elif estado == 's1':
            estado = 's1'
        elif estado == 's_erro':
            estado = 's_erro'
    return estado == 's1'


def mefd_l4(entrada):
    """String nao deve iniciar com 1."""
    estado = 's0'
    for s in entrada:
        if estado == 's0':
            if s == '0': estado = 's1'
            elif s == '1': estado = 's_erro'
            else: return False
        elif estado == 's1':
            estado = 's1'
        elif estado == 's_erro':
            estado = 's_erro'
    return estado == 's1'


def testar(nome, func, validos, invalidos):
    print(f"\n=== {nome} ===")
    print("Aceitos:")
    for s in validos:
        print(f"  {s!r} -> {func(s)}")
    print("Rejeitados:")
    for s in invalidos:
        print(f"  {s!r} -> {func(s)}")


testar("L0 - cada 0 seguido de 1",     mefd_l0, ["010111","1111","01110111011"], ["00","010","0","1001"])
testar("L1 - termina com 00",          mefd_l1, ["00","100","1100","0100"],      ["001","010","0","1"])
testar("L2 - exatamente 3 zeros",      mefd_l2, ["000","10100","0111101101"],    ["001","0000","1010111"])
testar("L3 - inicia com 1",            mefd_l3, ["100","10100","1"],             ["001","010","0"])
testar("L4 - nao inicia com 1",        mefd_l4, ["00","0100","0111101101"],      ["110","1010","1"])
