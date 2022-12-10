class Usario:

    VALIDO_TIPOS = {"ESTUDIANTE", "SECRETARIA", "PROFESSOR"}
    puede_utilizar_trazibilidad = False

    def __init__(self, tipo):
        if tipo in self.VALIDO_TIPOS:
            self.tipo = tipo
            puede_utilizar_trazibilidad = True
