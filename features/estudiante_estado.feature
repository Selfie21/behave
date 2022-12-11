Feature: El sistema deberá mostrar el estado actual de la solicitud del estudiante.

  Scenario: un estudiante se conecta al sistema para ver el estado de su solicitud
     Given un estudiante se encuentra en la página de inicio en https://siveducmd.uach.cl/
      When ese estudiante se conecta al sistema
      And ese estudiante haga clic en la página de la licitación
      And ese estudiante haga clic para realizar su Examen de Titulación
      Then ese estudiante puede ver el estado de su solicitud