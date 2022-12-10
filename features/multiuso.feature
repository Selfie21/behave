Feature: El software tendrá la capacidad de soportar la cantidad necesaria de usuarios simultáneos con el fin de que puedan acceder múltiples alumnos, secretarias y profesores al mismo tiempo sin tener que perjudicar el rendimiento o disponibilidad del software.

  Scenario: 10 usuarios diferentes se conectan al sistema al mismo tiempo
     Given 9 differentes usarias usan el sistema (3 estudiantes, 3 secretarias, 3 professores) utilizan el sistema
      When un estudiante se conecta al sistema
      Then el sistema funcionará a ritmo normal ya que 10 usuarios es menos que el máximo de usuarios