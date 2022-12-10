from mockup.user import Usario


class Sistema:
    # TODO: qué es la maximo (tenemos que definir eso)
    MAXIMO_NO_USARIOS = 50
    errors_encountered = False
    usarios = []

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def conectando_usario(tipo):
        if Sistema.get_numero_usarios() + 1 < Sistema.MAXIMO_NO_USARIOS:
            nuevo_usuario = Usario(tipo)
            Sistema.usarios.append(nuevo_usuario)
        else:
            print("error: número máximo de usuarios alcanzado")
            Sistema.errors_encountered = True

    @staticmethod
    def get_numero_usarios():
        return len(Sistema.usarios)
