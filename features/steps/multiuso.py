from behave import *
from mockup.system import Sistema, Usario

@given('9 differentes usarias usan el sistema (3 estudiantes, 3 secretarias, 3 professores) utilizan el sistema')
def step_impl(context):
    for i in range(3):
        nuevo_usuario = Usario('ESTUDIANTE')
        Sistema.conectando_usario(nuevo_usuario)

    for i in range(3):
        nuevo_usuario = Usario('SECRETARIA_ESCUELA')
        Sistema.conectando_usario(nuevo_usuario)

    for i in range(3):
        nuevo_usuario = Usario('PROFESSOR')
        Sistema.conectando_usario(nuevo_usuario)


@when('un estudiante se conecta al sistema')
def step_impl(context):
    nuevo_usuario = Usario('ESTUDIANTE')
    Sistema.conectando_usario(nuevo_usuario)

@then('el sistema funcionará a ritmo normal ya que 10 usuarios es menos que el máximo de usuarios')
def step_impl(context):
    assert Sistema.errors_encountered is False