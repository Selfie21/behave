from behave import *
from mockup.system import Sistema


@given('el usuario está conectado al sistema, pero no se le permite ver el sistema de licitación')
def step_impl(context):
    Sistema.conectando_usario('INVITADO')
    context.actual_usario = Sistema.usarios[-1]

@then('el sistema no muestra la página de solicitud')
def step_impl(context):
    assert context.actual_usario.puede_utilizar_trazibilidad is False