Feature: Seguridad: Como mencionamos anteriormente respecto a la información, nos preocupamos bastante de la seguridad de ésta. Por lo que el software contará con un sistema de credenciales para brindar confidencialidad e integridad a la información almacenada.

  Scenario: un usuario que no tiene acceso al sistema intenta utilizarlo
     Given el usuario está conectado al sistema, pero no se le permite ver el sistema de licitación
      Then el sistema no muestra la página de solicitud