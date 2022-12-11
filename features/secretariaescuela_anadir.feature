Feature: El sistema deberá permitir a la Secretaria de Escuela ingresar a los miembros de la Comisión del examen.

  Scenario: un estudiante se conecta al sistema para ver el estado de su solicitud
     Given un estudiante se encuentra en la página de inicio en https://siveducmd.uach.cl/
      When ese estudiante se conecta al sistema
      And ese estudiante haga clic en la página de la licitación
      And ese estudiante haga clic para realizar su Examen de Titulación
      Then la correspondiente Secretaria de Escuela puede ingresar a los miembros de la Comisión del examen