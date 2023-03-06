from PyQt5 import uic, QtWidgets, QtCore
from pages.EditarPrivilegios import EditarPrivilegios
import os
from bdConexion import obtener_conexion
from functools import partial
from ui.icons import imagenes
from pages.VerUsuario import VerUsuario
from usuarios import getListaTablas, getPermisos, getUsuarioLogueado, updateTable

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir,("../ui/registrar-usuario.ui")))

class RegistrarUsuario(Form, Base):
    cols=[]
    diccionario_permisos = {'ver':{},
                            'escritura':{}}
    diccionario_tramites = {'ver': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'fecha_honorarios': True, 'cantidad': True, 'mes_de_pago': True}}, 'escritura': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': False, 'monto_honorarios': False, 'fecha_honorarios': False, 'cantidad': False, 'mes_de_pago': True}}}
    diccionario_juridico = {'ver': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'juridico': {'id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': False, 'monto_honorarios': False, 'fecha_honorarios': False, 'cantidad': False, 'mes_de_pago': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'cat_conceptos_pago': {}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'facturas': {}, 'desgloce_ppto': {}}, 'escritura': {'aviso_definitivo': {}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': False, 'clave_catastral': False, 'infonavit': False, 'entrega_testimonio': False, 'observaciones': True, 'fecha_vence': True}, 'juridico': {'id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': False, 'monto_honorarios': False, 'fecha_honorarios': False, 'cantidad': False, 'mes_de_pago': False}, 'fechas_catastro_calif': {}, 'fechas_catastro_td': {}, 'fechas_rpp': {}, 'cat_conceptos_pago': {}, 'catastro_calificacion': {}, 'catastro_td': {}, 'direccion_notarias_seguimiento_juicios': {}, 'rpp': {}, 'facturas': {}, 'desgloce_ppto': {}}}
    diccionario_presupuesto = {'ver': {'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'bitacora_depositos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto_id': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'cat_conceptos_pago': {'id': True, 'concepto': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'desgloce_ppto': {'id': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'pagado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'juridico': {}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'fecha_honorarios': True, 'cantidad': True, 'mes_de_pago': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}}, 'escritura': {'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'observaciones': True, 'fecha_vence': True, 'sr': False, 'clave_catastral': False, 'infonavit': False, 'entrega_testimonio': False}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'bitacora_depositos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto_id': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'cat_conceptos_pago': {'id': True, 'concepto': True}, 'catastro_calificacion': {}, 'catastro_td': {}, 'desgloce_ppto': {'id': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'pagado': True}, 'direccion_notarias_seguimiento_juicios': {}, 'fechas_catastro_calif': {}, 'fechas_catastro_td': {}, 'fechas_rpp': {}, 'juridico': {}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'fecha_honorarios': True, 'cantidad': True, 'mes_de_pago': False}, 'rpp': {}}}
    diccionario_proyectista = {'ver': {'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': False, 'cat_terminado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': False, 'registrada': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': False, 'monto_honorarios': False, 'fecha_honorarios': False, 'cantidad': False, 'mes_de_pago': False}}, 'escritura': {'escritura': {'id': False, 'no_escritura': False, 'bis': False, 'no_presupuesto': False, 'volumen': False, 'fecha': False, 'no_expediente': False, 'observaciones': False, 'fecha_vence': False}, 'catastro_calificacion': {}, 'catastro_td': {}, 'direccion_notarias_seguimiento_juicios': {}, 'rpp': {}, 'fechas_rpp': {}, 'fechas_catastro_td': {}, 'fechas_catastro_calif': {}, 'presupuesto': {}}}
    diccionario_armadores = {'ver': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': False, 'monto_honorarios': False, 'fecha_honorarios': False, 'cantidad': False, 'mes_de_pago': False}, 'desgloce_ppto': {'id': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': False, 'pagado': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': False, 'cat_terminado': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': False, 'cat_rev': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': False}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': False}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': False, 'registrada': True}}, 'escritura': {'aviso_definitivo': {}, 'presupuesto': {}, 'desgloce_ppto': {}, 'catastro_td': {}, 'catastro_calificacion': {}, 'fechas_catastro_td': {}, 'fechas_rpp': {}, 'rpp': {}}}
    diccionario_admin = {'ver': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'bitacora_depositos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto_id': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'cat_conceptos_pago': {'id': True, 'concepto': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'desgloce_ppto': {'id': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'pagado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'juridico': {'id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'fecha_honorarios': True, 'cantidad': True, 'mes_de_pago': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'usuario': {'id': True, 'nombre_usuario': True, 'rol': True}}, 'escritura': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'bitacora_depositos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto_id': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'cat_conceptos_pago': {'id': True, 'concepto': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'desgloce_ppto': {'id': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'pagado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'juridico': {'id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'fecha_honorarios': True, 'cantidad': True, 'mes_de_pago': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'usuario': {'id': True, 'nombre_usuario': True, 'rol': True}}}

    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupTables(self)
        self.setupColumns(self)
        # cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
        self.tablaslist.currentTextChanged.connect(self.setupColumns)
        #self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
        self.button_guardar.clicked.connect(self.crearUsuario)
        self.pushButton_cancelar.clicked.connect(self.cancelarRegistro)
        self.comboBox_roles.currentTextChanged.connect(self.cargarPermisosdeRol)



    #
    def cargarPermisosdeRol(self):
        rol = self.comboBox_roles.currentText()
        if self.comboBox_roles.currentText() == 'Selecciona un rol...':
            self.button_guardar.setEnabled(False)
        else:
            self.button_guardar.setEnabled(True)
        if rol == 'Administrador':
            diccionario_usar = self.diccionario_admin
        elif rol == 'Armadores':
            diccionario_usar = self.diccionario_armadores
        elif rol == 'Proyectista':
            diccionario_usar = self.diccionario_proyectista
        elif rol == 'Presupuesto':
            diccionario_usar = self.diccionario_presupuesto
        elif rol == 'Juridico':
            diccionario_usar = self.diccionario_tramites
        else:
            diccionario_usar = {}
        self.limpiarDict() 
        self.diccionario_permisos = diccionario_usar
        self.resetCheckboxes(Form)

        

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
    def setupTables(self, Form):
        lista_tablas = getListaTablas()
        self.tablaslist.addItems(lista_tablas)
    
 	# en esta funcion se van a actualizar los checkbox de las columnas de la pantalla editar privilegios
    def setupColumns(self, Form):
        # se eliminan los combobox anteriores
        self.resetCombobox(self)

        tabla_seleccionada = self.tablaslist.currentText()
        columnas = getPermisos(tabla_seleccionada)["ver"]
        lista_columnas = columnas.split(',')

        # aqui se crea el widget del checkbox y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_ver = f"acceso_{i}_ver"
            name_escritura = f"acceso_{i}_escritura"
            setattr(self, name_ver, QtWidgets.QCheckBox(Form))
            setattr(self, name_escritura, QtWidgets.QCheckBox(Form))
            checkbox_ver = getattr(self,name_ver)
            checkbox_ver.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: white;")
            checkbox_ver.setObjectName(name_ver)
            
            checkbox_escritura = getattr(self,name_ver)
            checkbox_escritura.setText(col)
            checkbox_escritura = getattr(self,name_escritura)
            checkbox_escritura.setStyleSheet("\n"
            "font: 75 16pt;\n"
            "color: white;")
            checkbox_escritura.setObjectName(name_escritura)
            checkbox_escritura.setText(col)
            # permisos de ver
            self.verLayout.addWidget(checkbox_ver)
            # permisos de escritura
            self.escribirLayout.addWidget(checkbox_escritura)
            self.cols.append(checkbox_ver)
            self.cols.append(checkbox_escritura)
        # aqui se le asignan los metodos a cada checkbox y se llena el diccionario con las columnas de la tabla - Jared
        self.connectCheckboxes(self)
        self.resetCheckboxes(self)

    def resetCombobox(self, Form):
        for obj in self.cols:
            permiso = obj.objectName()
            permiso = permiso.split('_')[2]
            if 'ver' in permiso: self.verLayout.removeWidget(obj)
            else: self.escribirLayout.removeWidget(obj)
            obj.deleteLater()
            del obj
        self.cols = []

	# este metodo le asigna un metodo a cada checkbox que ejecuta guardar_opcion al ser activado/desactivado - Jared
    def connectCheckboxes(self, Form):
        for obj in self.cols:
            obj.stateChanged.connect(partial(self.guardar_opcion,obj))

	# este metodo revisa el diccionario de permisos y activa aquellas columnas que estan guardadas como true -Jared
    def resetCheckboxes(self, Form):
        
        for permiso in self.diccionario_permisos:
            for obj in self.cols:
                permiso = obj.objectName()
                permiso = permiso.split('_')[2]
                if self.tablaslist.currentText() not in self.diccionario_permisos[permiso]:
                    self.diccionario_permisos[permiso][self.tablaslist.currentText()] = {}
                if obj.text() in self.diccionario_permisos[permiso][self.tablaslist.currentText()]:
                    obj.setChecked(self.diccionario_permisos[permiso][self.tablaslist.currentText()][obj.text()])
                else:
                    obj.setChecked(False)

    '''
    En este metodo se guarda si el checkbox fue activado o no.
    El diccionario se compone por:
    Acciones (Guardar,ver,Modificar) -> Nombre de tabla -> Columna: True/False
    -Jared
    '''
    def guardar_opcion(self, obj):
        permiso = obj.objectName()
        permiso = permiso.split('_')[2]
        tabla = self.tablaslist.currentText()
        columna = obj.text()
        self.diccionario_permisos[permiso][tabla][columna] = obj.isChecked()
        if permiso == 'escritura':
            if tabla not in self.diccionario_permisos['ver']:
                self.diccionario_permisos['ver'][tabla] = {}
            if columna not in self.diccionario_permisos['ver'][tabla]:
                self.diccionario_permisos['ver'][tabla][columna] = self.diccionario_permisos['escritura'][tabla][columna]
            if self.diccionario_permisos['ver'][tabla][columna] == False and self.diccionario_permisos['escritura'][tabla][columna]:
                self.diccionario_permisos['ver'][tabla][columna] = True
        print(self.diccionario_permisos)
 

    #este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
    def limpiarDict(self):
        self.diccionario_permisos = {'ver':{},
                                'escritura':{}}
        self.resetCheckboxes(Form)

    def crearUsuario(self):
        nombre_usuario = self.lineEdit_nombreusuario.text()
        contrasena = self.lineEdit_contrasenausuario.text()
        rol = self.formatRol(self.comboBox_roles.currentText())
        if len(nombre_usuario) > 100:
            self.label_error.setText("El nombre de usuario no debe superar 100 caracteres")
            self.mensaje.setText("")
        elif len(contrasena) > 300:
            self.label_error.setText("La contraseña no debe superar los 300 caracteres")
            self.mensaje.setText("")
        elif len(contrasena)==0 or len(nombre_usuario)==0:
            self.label_error.setText("Por favor ingrese datos en ambas casillas")
            self.mensaje.setText("")
        else:
            user, pwd = getUsuarioLogueado()
            conn = obtener_conexion(user,pwd)
            cur = conn.cursor()
            if self.isUsuarioRepetido(nombre_usuario, cur):
                self.label_error.setText("El usuario ingresado ya existe")
                self.mensaje.setText("")
            else:
                query = f"INSERT INTO usuario(nombre_usuario,contrasena,rol) VALUES('{nombre_usuario}','{contrasena}','{rol}')"
                cur.execute(query)
                query = f"CREATE USER '{nombre_usuario}'@'localhost' IDENTIFIED BY '{contrasena}'"
                cur.execute(query)
                self.generarGrants(nombre_usuario)
                cur.close()
                conn.close()
                
                self.lineEdit_nombreusuario.setText("")
                self.lineEdit_contrasenausuario.setText("")
                self.mensaje.setText("Usuario registrado exitosamente")
                self.checkThreadTimer = QtCore.QTimer(self)
                self.checkThreadTimer.setInterval(3000)
                self.checkThreadTimer.start()
                self.checkThreadTimer.timeout.connect(partial(self.mensaje.setText,''))
                updateTable('usuario')
                self.parent().findChild(EditarPrivilegios).usuarioslist.addItem(nombre_usuario)
                self.parent().findChild(VerUsuario).setupTable(self.parent().findChild(VerUsuario))
                self.limpiarDict()

    def generarGrants(self,nombre_usuario):
        query = f""
        user, pwd = getUsuarioLogueado()
        conn = obtener_conexion(user,pwd)
        cur = conn.cursor()
        query=f"SELECT rol FROM usuario WHERE nombre_usuario='{nombre_usuario}'"
        cur.execute(query)
        rol = cur.fetchall()
        rol = rol[0][0]
        for llave,accion in self.diccionario_permisos.items():
            for nombre_tabla,columnas in accion.items():
                for nombre_columna,checked in columnas.items():
                    if checked:
                        if llave == 'ver':
                            query=f"GRANT SELECT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query)
                        else:
                            query=f"GRANT INSERT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query)
                            query=f"GRANT UPDATE ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query)
                        if rol == 'admin':
                            query=f"GRANT ALL PRIVILEGES ON mysql.* TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query) 
                        
        cur.close()
        conn.close()
    
    def cancelarRegistro(self):
        self.lineEdit_nombreusuario.setText("")
        self.lineEdit_contrasenausuario.setText("")
        self.limpiarDict()

    def formatRol(self,rol_unformat):
        if rol_unformat == 'Administrador':
            return 'admin'
        elif rol_unformat == 'Armadores':
            return 'armadores'
        elif rol_unformat == 'Proyectista':
            return 'proyectista'
        elif rol_unformat == 'Presupuesto':
            return 'juridico'
        elif rol_unformat == 'Tramites':
            return 'tramites'
        else:
            return 'otro' 

    def isUsuarioRepetido(self,nombre_usuario,cur):
        query = f"SELECT * FROM usuario WHERE nombre_usuario ='{nombre_usuario}'"
        cur.execute(query)
        usuarios = cur.fetchall()
        if len(usuarios) == 0:
            repetido = False
        else:
            repetido = True
        return repetido
