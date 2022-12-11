from mockup.user import Usario
from mockup.solicitud import Solicitud

class Sistema:
    MAXIMO_NO_USARIOS = 50
    errors_encountered = False
    usarios = []
    VALIDO_PAGINAS = ["HOME", "LOGGED_IN", "ESTUDIANTE_SOLICITUD", "ESTUDIANTE_HORARIOS_DISPONSIBLE",
                      "ESTUDIANTE_PROPONER_SOLICITUD", "ESTUDIANTE_CONFIRMO_FECHA", "SECRETARIA_APROBAR_SOLICITUD"]

    @staticmethod
    def __init__():
        pass

    @staticmethod
    def conectando_usario(nuevo_usuario):
        if Sistema.get_numero_usarios() + 1 < Sistema.MAXIMO_NO_USARIOS:
            nuevo_usuario.pagina_ahora = "LOGGED_IN"
            Sistema.usarios.append(nuevo_usuario)
        else:
            print("error: número máximo de usuarios alcanzado")
            Sistema.errors_encountered = True

    @staticmethod
    def accion_usario(accion, usuario):
        if accion not in Sistema.VALIDO_PAGINAS:
            print("error: accion no disponsible")
            Sistema.errors_encountered = True
        elif Sistema.VALIDO_PAGINAS.index(accion) < Sistema.VALIDO_PAGINAS.index(usuario.pagina_ahora):
            print("error: accion no en correcto orden")
            Sistema.errors_encountered = True
        elif accion == "ESTUDIANTE_PROPONER_SOLICITUD":
            new_solicitud = Solicitud()
            usuario.solicitudes.append(new_solicitud)
            Sistema.usarios[0].solicitudes.append(new_solicitud)
            usuario.pagina_ahora = accion
        elif accion == "SECRETARIA_APROBAR_SOLICITUD":
            solicitation = Sistema.usarios[0].solicitudes[0]
            solicitation.estado = 'aprobar_escuela'
            Sistema.usarios[1].solicitudes.append(solicitation)
        else:
            usuario.pagina_ahora = accion

    @staticmethod
    def get_numero_usarios():
        return len(Sistema.usarios)
