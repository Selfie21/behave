class Usario:

    VALIDO_TIPOS = {"ESTUDIANTE", "SECRETARIA_ESCUELA", "SECRETARIA_ACADEMICA", "PROFESSOR"}
    puede_utilizar_trazibilidad = False

    solicitudes = []
    pagina_ahora = "HOME"

    def __init__(self, tipo):
        self.tipo = tipo

        if tipo in self.VALIDO_TIPOS:
            self.puede_utilizar_trazibilidad = True
