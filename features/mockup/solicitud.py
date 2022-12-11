class Solicitud:

    estado = "abierto"
    fecha = "01.01.1970"
    miembros_comision = []
    motivo_rechazo = ""

    def change_status(self, usuario, nueva_estado):
        if usuario.tipo == "SECRETARIA_ESCUELA" or usuario.tipo == "SECRETARIA_ACADEMICA":
            self.estado  = nueva_estado
        else:
            print("Prohibido de cambiar estado!")
