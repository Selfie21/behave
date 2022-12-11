Feature: El sistema deberá mostrar al estudiante los horarios disponibles para realizar un examen.

  Scenario: un estudiante se conecta al sistema para ver la página de solicitud
     Given un estudiante se encuentra en la página de inicio en https://siveducmd.uach.cl/
      When ese estudiante se conecta al sistema
      Then el sistema es capaz de mostrar la página de la licitación para ese estudiante