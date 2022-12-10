from behave import *
from mockup.system import Sistema

@given('9 differentes usarias usan el sistema (3 estudiantes, 3 secretarias, 3 professores) utilizan el sistema')
def step_impl(context):
    for i in range(3):
        Sistema.conectando_usario('ESTUDIANTE')

    for i in range(3):
        Sistema.conectando_usario('SECRETARIA')

    for i in range(3):
        Sistema.conectando_usario('PROFESSOR')

@when('un estudiante se conecta al sistema')
def step_impl(context):
    Sistema.conectando_usario('ESTUDIANTE')

@then('el sistema funcionará a ritmo normal ya que 10 usuarios es menos que el máximo de usuarios')
def step_impl(context):
    assert Sistema.errors_encountered is False