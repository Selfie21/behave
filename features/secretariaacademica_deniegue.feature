Feature: El sistema deberá permitir a la Secretaría Académica ingresar un motivo en caso de que se deniegue la solicitud.

  Scenario: un estudiante se conecta al sistema para ver el estado de su solicitud
     Given un estudiante se encuentra en la página de inicio en https://siveducmd.uach.cl/
      When ese estudiante se conecta al sistema
      And ese estudiante haga clic en la página de la licitación
      And ese estudiante haga clic para realizar su Examen de Titulación
      And la Secretaria de Escuela aprueba la solicitud
      And la Secretaría Académica deniega la solicitud
      Then la Secretaría Académica puede dar un motivo para denegar