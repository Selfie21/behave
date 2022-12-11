Feature: El sistema deberá enviar la solicitud a Secretaría Académica en caso de que la solicitud del estudiante sea aprobada por su Secretaria de Escuela.

  Scenario: un estudiante se conecta al sistema para ver el estado de su solicitud
     Given un estudiante se encuentra en la página de inicio en https://siveducmd.uach.cl/
      When ese estudiante se conecta al sistema
      And ese estudiante haga clic en la página de la licitación
      And ese estudiante haga clic para realizar su Examen de Titulación
      And la Secretaria de Escuela aprueba la solicitud
      Then la secretaria academica puede ver la solicitud