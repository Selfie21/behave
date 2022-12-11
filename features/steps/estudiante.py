from behave import *
from mockup.system import Sistema, Usario

@given('un estudiante se encuentra en la página de inicio en https://siveducmd.uach.cl/')
def step_impl(context):
    Sistema.conectando_usario(Usario('SECRETARIA_ESCUELA'))
    Sistema.conectando_usario(Usario('SECRETARIA_ACADEMICA'))

    nuevo_usuario = Usario('ESTUDIANTE')
    context.actual_usario = nuevo_usuario
    Sistema.conectando_usario(nuevo_usuario)

@when('ese estudiante se conecta al sistema')
def step_impl(context):
    Sistema.conectando_usario(context.actual_usario)

@when('ese estudiante haga clic en la página de la licitación')
def step_impl(context):
    Sistema.accion_usario('ESTUDIANTE_SOLICITUD', context.actual_usario)

@when('ese estudiante haga clic para realizar su Examen de Titulación')
def step_impl(context):
    Sistema.accion_usario('ESTUDIANTE_PROPONER_SOLICITUD', context.actual_usario)

@then('ese estudiante puede enviar una solicitud para realizar su Examen de Titulación')
def step_impl(context):
    Sistema.accion_usario('ESTUDIANTE_PROPONER_SOLICITUD', context.actual_usario)
    assert Sistema.errors_encountered is False

@then('el sistema es capaz de mostrar la página de la licitación para ese estudiante')
def step_impl(context):
    Sistema.accion_usario('ESTUDIANTE_SOLICITUD', context.actual_usario)
    assert Sistema.errors_encountered is False

@then('ese estudiante puede ver el estado de su solicitud')
def step_impl(context):
    assert context.actual_usario.solicitudes[0] is not None
    assert context.actual_usario.solicitudes[0].estado is 'abierto'
