Feature: El sistema deberá permitir al estudiante enviar una solicitud para realizar su Examen de Titulación.

  Scenario: un estudiante se conecta al sistema para ver la página de solicitud
     Given un estudiante se encuentra en la página de inicio en https://siveducmd.uach.cl/
      When ese estudiante se conecta al sistema
      And ese estudiante haga clic en la página de la licitación
      Then ese estudiante puede enviar una solicitud para realizar su Examen de Titulación