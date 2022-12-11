from behave import *
from mockup.system import Sistema, Usario

@when('la Secretaria de Escuela aprueba la solicitud')
def step_impl(context):
    Sistema.accion_usario('SECRETARIA_APROBAR_SOLICITUD', Sistema.usarios[0])

@when('la Secretaría Académica deniega la solicitud')
def step_impl(context):
    secretaria_academica = Sistema.usarios[1]
    secretaria_academica.solicitudes[0].estado = "denegado"
    secretaria_academica.solicitudes[0].motivo_rechazo = "ejemplo motivo"
    Sistema.accion_usario('SECRETARIA_APROBAR_SOLICITUD', Sistema.usarios[0])

@then('la correspondiente Secretaria de Escuela puede ingresar a los miembros de la Comisión del examen')
def step_impl(context):
    secretaria_escuela = Sistema.usarios[0]
    secretaria_escuela.solicitudes[0].miembros_comision.append("Cristian Olivares-Rodríguez")
    assert secretaria_escuela.solicitudes[0] is not None

@then('la secretaria academica puede ver la solicitud')
def step_impl(context):
    secretaria_academica = Sistema.usarios[1]
    assert secretaria_academica.solicitudes[0] is not None
    assert secretaria_academica.solicitudes[0].estado is 'aprobar_escuela'

@then('la Secretaría Académica puede dar un motivo para denegar')
def step_impl(context):
    secretaria_academica = Sistema.usarios[1]
    assert secretaria_academica.solicitudes[0].motivo_rechazo is not None