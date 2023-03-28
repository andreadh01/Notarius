from re import L
from PyQt5 import uic, QtWidgets, QtCore
from pages.EditarPrivilegios import EditarPrivilegios
import os
from tabnanny import check
from bdConexion import obtener_conexion
from functools import partial
from PyQt5.QtWidgets import QCheckBox, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
from pages.VerUsuarios import VerUsuarios
from usuarios import getListaTablas, getPermisos, getUsuarioLogueado, updateTable
from deployment import getBaseDir

base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','registrar-usuario.ui'))

class RegistrarUsuario(Form, Base):
    checkboxList=[]
    diccionario_permisos = {'read':{},
                            'write':{}}
    diccionario_tramites = {'read': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence_td': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': False, 'fecha_honorarios': True, 'monto_honorarios': False, 'monto_impuestos': False, 'saldo': True, 'pago_de_comision': True, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': False, 'isr_enajenacion': False, 'fecha_aviso_renap': False, 'iva': False, 'uif_poder_irrevocable': False, 'fecha_aviso_dir_not_tpa': False, 'numeracion_folios': False, 'fecha_minuta': False, 'contrato_en_extracto': False, 'minuta': False, 'pendientes': False, 'fecha_entrega_juridico': False, 'otorgamiento': False, 'fecha_cierre_antilavado': False, 'autorizacion': False, 'isr_adquisicion': False, 'fecha_envio_dircc': False, 'fecha_aviso_reloat': False, 'folios': False, 'folio_cancelado': False, 'fecha_apendice': False, 'firmas_en_extracto': False, 'apendice': False, 'no_paso': False, 'fecha_aviso_portal': False, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'vencimiento_td': True, 'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'monto_impuestos': True, 'fecha_honorarios': True, 'saldo': True, 'pago_de_comision': True}, 'pagos_presupuesto': {}, 'no_facturas': {'id': True, 'id_relacion': True, 'no_factura': True}, 'juridico': {}, 'fechas_rpp': {'id': True, 'id_fechas': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_fechas': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_catastro_calif': {'id': True, 'id_fechas': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'escritura_id': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'escritura_id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}}, 'write': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence_td': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': False, 'fecha_honorarios': True, 'monto_honorarios': False, 'monto_impuestos': False, 'saldo': True, 'pago_de_comision': True, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': False, 'isr_enajenacion': False, 'fecha_aviso_renap': False, 'iva': False, 'uif_poder_irrevocable': False, 'fecha_aviso_dir_not_tpa': False, 'numeracion_folios': False, 'fecha_minuta': False, 'contrato_en_extracto': False, 'minuta': False, 'pendientes': False, 'fecha_entrega_juridico': False, 'otorgamiento': False, 'fecha_cierre_antilavado': False, 'autorizacion': False, 'isr_adquisicion': False, 'fecha_envio_dircc': False, 'fecha_aviso_reloat': False, 'folios': False, 'folio_cancelado': False, 'fecha_apendice': False, 'firmas_en_extracto': False, 'apendice': False, 'no_paso': False, 'fecha_aviso_portal': False, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'vencimiento_td': True, 'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': False, 'pagos': False, 'depositos': False}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': False, 'monto_honorarios': False, 'monto_impuestos': False, 'fecha_honorarios': False, 'saldo': True, 'pago_de_comision': True}, 'pagos_presupuesto': {}, 'no_facturas': {'id': True, 'id_relacion': True, 'no_factura': True}, 'juridico': {}, 'fechas_rpp': {'id': True, 'id_fechas': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_fechas': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_catastro_calif': {'id': True, 'id_fechas': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'escritura_id': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'escritura_id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}}}
    diccionario_presupuesto = {'read': {'aviso_definitivo': {'id': False, 'folio_rpp': False, 'fecha_presentado': False, 'fecha_salida': False, 'fecha_vence': False}, 'bitacora_depositos': {'id': True, 'id_relacion': True, 'fecha': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'id_relacion': True, 'fecha': True, 'concepto': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}, 'desgloce_ppto': {'id': True, 'id_relacion': True, 'concepto': True, 'cantidad': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence_td': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'escritura_id': True}, 'no_facturas': {'id': True, 'id_relacion': True, 'no_factura': True}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'monto_impuestos': True, 'fecha_honorarios': True, 'saldo': True, 'pago_de_comision': True}, 'rpp': {'id': False, 'no_presupuesto': False, 'escritura_id': False, 'folio_rpp': False, 'observaciones': False, 'registrada': False}, 'rpp_fechas_rpp': {'id': False, 'id_rpp': False}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'vencimiento_td': True, 'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}}, 'write': {'aviso_definitivo': {'id': False, 'folio_rpp': False, 'fecha_presentado': False, 'fecha_salida': False, 'fecha_vence': False}, 'bitacora_depositos': {'id': True, 'id_relacion': True, 'fecha': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'id_relacion': True, 'fecha': True, 'concepto': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}, 'desgloce_ppto': {'id': True, 'id_relacion': True, 'concepto': True, 'cantidad': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': False, 'infonavit': False, 'entrega_testimonio': False, 'observaciones': True, 'fecha_vence_td': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'escritura_id': True}, 'no_facturas': {'id': True, 'id_relacion': True, 'no_factura': True}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'monto_impuestos': True, 'fecha_honorarios': True, 'saldo': True, 'pago_de_comision': True}, 'rpp': {'id': False, 'no_presupuesto': False, 'escritura_id': False, 'folio_rpp': False, 'observaciones': False, 'registrada': False}, 'rpp_fechas_rpp': {'id': False, 'id_rpp': False}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'vencimiento_td': True, 'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}}}
    diccionario_juridico ={'read': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'usuario': {}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'vencimiento_td': True, 'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}, 'bitacora_depositos': {}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'escritura_id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence_td': True}, 'juridico': {'id': True, 'escritura_id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}}, 'write': {'aviso_definitivo': {}, 'usuario': {}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': False, 'monto_honorarios': False, 'monto_impuestos': False, 'saldo': False, 'pago_de_comision': False, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': False, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': False, 'fecha_envio_escritura': False, 'fecha_solicitud_busqueda_testa_rpp': False, 'fecha_solicitud_busqueda_testa_dircc': False, 'fecha_publicacion_periodico': False, 'fecha_publicacion_boletin': False, 'vencimiento_td': False, 'observaciones_cat_calif': False, 'cat_rev': False, 'fechas_catastro_calif': False, 'cat_terminado': False, 'observaciones_cat_td': False, 'fechas_catastro_td': False, 'folio_rpp': False, 'observaciones_rpp': False, 'registrada': False, 'fechas_rpp': False, 'fecha_presentado': False, 'fecha_salida': False, 'fecha_vence': False, 'desgloce_ppto': False, 'pagos': False, 'depositos': False}, 'bitacora_depositos': {}, 'catastro_calificacion': {}, 'catastro_td': {}, 'direccion_notarias_seguimiento_juicios': {}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence_td': True}, 'juridico': {'id': True, 'escritura_id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'rpp': {}}}
    diccionario_proyectista = {'read': {'usuario': {'id': False, 'nombre_usuario': False, 'rol': False}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'gestor': True, 'proyecto': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'pago_de_comision': True, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': False, 'firma': True, 'monto_honorarios': False, 'monto_impuestos': False, 'saldo': False, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'vencimiento_td': True, 'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': False, 'pagos': False, 'depositos': False}, 'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'bitacora_depositos': {}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'depositos_presupuesto': {}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'escritura_id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence_td': True}, 'facturas': {'id': False, 'no_presupuesto': False, 'escritura_id': False}, 'fechas_catastro_calif': {'id': True, 'id_fechas': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_fechas': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_fechas': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'juridico': {'id': True, 'escritura_id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'no_facturas': {}, 'pagos_presupuesto': {'id': False, 'no_presupuesto': False}, 'presupuesto': {}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}}, 'write': {'usuario': {'id': False, 'nombre_usuario': False, 'rol': False}, 'tabla_final': {}, 'aviso_definitivo': {}, 'bitacora_depositos': {}, 'catastro_calificacion': {}, 'catastro_td': {}, 'cc_fechas_cc': {}, 'ctd_fechas_ctd': {}, 'depositos_presupuesto': {}, 'direccion_notarias_seguimiento_juicios': {}, 'escritura': {}, 'facturas': {}, 'fechas_catastro_calif': {}, 'fechas_catastro_td': {}, 'fechas_rpp': {}, 'juridico': {}, 'no_facturas': {}, 'pagos_presupuesto': {}, 'presupuesto': {}, 'rpp': {}, 'rpp_fechas_rpp': {}}}
    diccionario_armadores = {'read': {'rpp_fechas_rpp': {'id': False, 'id_rpp': False}, 'tabla_final': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'gestor': True, 'proyecto': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'pago_de_comision': True, 'no_escritura': True, 'bis': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence_td': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': False, 'monto_impuestos': False, 'fecha_honorarios': False, 'saldo': False, 'pago_de_comision': True}}, 'write': {'rpp_fechas_rpp': {}, 'tabla_final': {}, 'escritura': {}, 'presupuesto': {}}}
    diccionario_admin = {'read': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'bitacora_depositos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto_id': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'cat_conceptos_pago': {'id': True, 'concepto': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'desgloce_ppto': {'id': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'pagado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'juridico': {'id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'fecha_honorarios': True, 'cantidad': True, 'mes_de_pago': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'usuario': {'id': True, 'nombre_usuario': True, 'rol': True}}, 'write': {'aviso_definitivo': {'id': True, 'folio_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True}, 'bitacora_depositos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'observaciones': True, 'banco': True, 'tipo': True}, 'bitacora_pagos': {'id': True, 'fecha': True, 'no_presupuesto': True, 'concepto_id': True, 'cantidad': True, 'autorizado_por': True, 'observaciones': True}, 'cat_conceptos_pago': {'id': True, 'concepto': True}, 'catastro_calificacion': {'id': True, 'vencimiento_td': True, 'no_presupuesto': True, 'escritura_id': True, 'observaciones': True, 'cat_rev': True}, 'catastro_td': {'id': True, 'escritura_id': True, 'observaciones': True, 'cat_terminado': True}, 'desgloce_ppto': {'id': True, 'no_presupuesto': True, 'concepto': True, 'cantidad': True, 'pagado': True}, 'direccion_notarias_seguimiento_juicios': {'id': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_publicacion_boletin': True, 'fecha_publicacion_periodico': True}, 'escritura': {'id': True, 'no_escritura': True, 'bis': True, 'no_presupuesto': True, 'volumen': True, 'fecha': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones': True, 'fecha_vence': True}, 'facturas': {'id': True, 'no_presupuesto': True, 'no_factura': True, 'escritura_id': True}, 'fechas_catastro_calif': {'id': True, 'id_cat_calif': True, 'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True}, 'fechas_catastro_td': {'id': True, 'id_cat_td': True, 'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True}, 'fechas_rpp': {'id': True, 'id_rpp': True, 'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True}, 'juridico': {'id': True, 'contrato_en_extracto': True, 'firmas_en_extracto': True, 'pendientes': True, 'no_paso': True, 'otorgamiento': True, 'firma': True, 'autorizacion': True, 'fecha_aviso_renap': True, 'fecha_envio_dircc': True, 'uif_poder_irrevocable': True, 'fecha_aviso_reloat': True, 'fecha_aviso_dir_not_tpa': True, 'folios': True, 'numeracion_folios': True, 'folio_cancelado': True, 'fecha_minuta': True, 'fecha_apendice': True, 'minuta': True, 'apendice': True, 'fecha_entrega_juridico': True, 'fecha_aviso_portal': True, 'fecha_cierre_antilavado': True, 'isr_enajenacion': True, 'isr_adquisicion': True, 'iva': True}, 'presupuesto': {'id': True, 'no_presupuesto': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'enajentante': True, 'adquiriente': True, 'valor_operacion': True, 'monto_honorarios': True, 'fecha_honorarios': True, 'cantidad': True, 'mes_de_pago': True}, 'rpp': {'id': True, 'no_presupuesto': True, 'escritura_id': True, 'folio_rpp': True, 'observaciones': True, 'registrada': True}, 'usuario': {'id': True, 'nombre_usuario': True, 'rol': True}}}
    foreign_keys = {}

    def __init__(self, parent=None):
        super(self.__class__,self).__init__(parent)
        self.setupUi(self)
        # se mandan llamar los metodos al correr el programa
        self.setupTables(self)
        self.setupColumns(self)
        self.llavesForaneas()
        # cada que se actualice el combobox de tablas, se actualizan los checkbox de las columnas
        self.tablaslist.currentTextChanged.connect(self.setupColumns)
        self.lineEdit_contrasenausuario.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.accioneslist.currentTextChanged.connect(self.resetCheckboxes)
        self.button_guardar.clicked.connect(self.crearUsuario)
        self.pushButton_cancelar.clicked.connect(self.cancelarRegistro)
        self.checkBoxAllVer.stateChanged.connect(partial(self.checkAll,"read"))
        self.checkBoxAllEscribir.stateChanged.connect(partial(self.checkAll,"write"))
        self.comboBox_roles.currentTextChanged.connect(self.cargarPermisosdeRol)


    def llavesForaneas(self):
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute("SELECT TABLE_NAME,COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE CONSTRAINT_SCHEMA = 'notarius' AND REFERENCED_TABLE_NAME IS NOT NULL")
        for table_name, column_name, referenced_table_name, referenced_column_name in cur:
            if table_name not in self.foreign_keys:
                self.foreign_keys[table_name] = []
            self.foreign_keys[table_name].append((column_name, referenced_table_name, referenced_column_name)) # agregar los valores en una tupla
        cur.close()
        conn.close()
    

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
            diccionario_usar = self.diccionario_juridico
        elif rol == 'Trámites':
            diccionario_usar = self.diccionario_tramites
        else:
            diccionario_usar = self.diccionario_permisos
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
        self.checkBoxAllVer.setChecked(False)
        self.checkBoxAllEscribir.setChecked(False)
        tabla_seleccionada = self.tablaslist.currentText()
        columnas = getPermisos(tabla_seleccionada)["read"]
        lista_columnas = columnas.split(',')
        
        # aqui se crea el widget del checkbox y se agrega al gui
        for i, col in enumerate(lista_columnas):
            name_ver = f"acceso_{i}_read"
            name_escritura = f"acceso_{i}_write"
            setattr(self, name_ver, QtWidgets.QCheckBox(Form))
            setattr(self, name_escritura, QtWidgets.QCheckBox(Form))
            checkbox_ver = getattr(self,name_ver)
            checkbox_ver.setStyleSheet("\n"
            "font: 75 11pt;\n"
            "color: white;")
            checkbox_ver.setObjectName(name_ver)
            
            checkbox_escritura = getattr(self,name_ver)
            checkbox_escritura.setText(col)
            checkbox_escritura = getattr(self,name_escritura)
            checkbox_escritura.setStyleSheet("\n"
            "font: 75 11pt;\n"
            "color: white;")
            checkbox_escritura.setObjectName(name_escritura)
            checkbox_escritura.setText(col)
            # permisos de read
            self.verLayout.addWidget(checkbox_ver)
            # permisos de write
            self.escribirLayout.addWidget(checkbox_escritura)
            self.checkboxList.append(checkbox_ver)
            self.checkboxList.append(checkbox_escritura)
        # aqui se le asignan los metodos a cada checkbox y se llena el diccionario con las columnas de la tabla - Jared
        self.connectCheckboxes(self)
        self.resetCheckboxes(self)

    def checkAll(self,tipo_permiso):
        for checkbox in self.checkboxList:
            permiso = checkbox.objectName()
            permiso = permiso.split('_')[2]
            if tipo_permiso == permiso:
                checkbox.setChecked(True)
        print(self.diccionario_permisos)

    def resetCombobox(self, Form):
        for obj in self.checkboxList:
            permiso = obj.objectName()
            permiso = permiso.split('_')[2]
            if 'read' in permiso: self.verLayout.removeWidget(obj)
            else: self.escribirLayout.removeWidget(obj)
            obj.deleteLater()
            del obj
        self.checkboxList = []

	# este metodo le asigna un metodo a cada checkbox que ejecuta guardar_opcion al ser activado/desactivado - Jared
    def connectCheckboxes(self, Form):
        for obj in self.checkboxList:
            obj.stateChanged.connect(partial(self.guardar_opcion,obj))

	# este metodo revisa el diccionario de permisos y activa aquellas columnas que estan guardadas como true -Jared
    def resetCheckboxes(self, Form):
        
        for permiso in self.diccionario_permisos:
            for obj in self.checkboxList:
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
    Acciones (Guardar,read,Modificar) -> Nombre de tabla -> Columna: True/False
    -Jared
    '''
    def guardar_opcion(self, obj):
        permiso = obj.objectName()
        permiso = permiso.split('_')[2]
        tabla = self.tablaslist.currentText()
        columna = obj.text()
        self.diccionario_permisos[permiso][tabla][columna] = obj.isChecked()

        for tabla_p, lista_foreignkey in self.foreign_keys.items():
            lista_tabla_col = lista_foreignkey[0]
            columna_p = lista_tabla_col[0]
            tabla_secundaria = lista_tabla_col[1]
            columna_secundaria = lista_tabla_col[2]
            if tabla == tabla_p:
                if columna == columna_p:
                    if tabla_secundaria not in self.diccionario_permisos['write']:
                        self.diccionario_permisos['write'][tabla_secundaria] = {}
                    self.diccionario_permisos['write'][tabla_secundaria][columna_secundaria] = True

        if permiso == 'write':
            if tabla not in self.diccionario_permisos['read']:
                self.diccionario_permisos['read'][tabla] = {}
            if columna not in self.diccionario_permisos['read'][tabla]:
                self.diccionario_permisos['read'][tabla][columna] = self.diccionario_permisos['write'][tabla][columna]
            if self.diccionario_permisos['read'][tabla][columna] == False and self.diccionario_permisos['write'][tabla][columna]:
                self.diccionario_permisos['read'][tabla][columna] = True
        
 

    #este metodo borra todos los datos del diccionario y desactiva todas las checkboxes. se utiliza al cambiar de usuario a modificar -Jared
    def limpiarDict(self):
        self.diccionario_permisos = {'read':{},
                                'write':{}}
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
                query = f"INSERT INTO usuario(nombre_usuario,rol) VALUES('{nombre_usuario}','{rol}')"
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
                self.checkThreadTimer.setInterval(10000)
                self.checkThreadTimer.start()
                self.checkThreadTimer.timeout.connect(partial(self.mensaje.setText,''))
                updateTable('usuario')
                self.checkBoxAllVer.setChecked(False)
                self.checkBoxAllEscribir.setChecked(False)
                self.parent().findChild(EditarPrivilegios).usuarioslist.addItem(nombre_usuario)
                self.parent().findChild(VerUsuarios).setupTable(self.parent().findChild(VerUsuarios))
                self.limpiarDict()
                
                self.comboBox_roles.setCurrentIndex(0)
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(3000)
        self.checkThreadTimer.start()
        self.checkThreadTimer.timeout.connect(partial(self.label_error.setText,''))

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
                print(columnas)
                for nombre_columna,checked in columnas.items():
                    if checked:
                        if llave == 'read':
                            query=f"GRANT SELECT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query)
                        else:
                            query=f"GRANT INSERT ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query)
                            query=f"GRANT UPDATE ({nombre_columna}) ON notarius.{nombre_tabla} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query)
                            for tabla_principal, lista_foreignkey in self.foreign_keys.items():
                                lista_tabla_col = lista_foreignkey[0]
                                columna_principal = lista_tabla_col[0]
                                tabla_secundaria = lista_tabla_col[1]
                                columna_secundaria = lista_tabla_col[2]

                                if tabla_principal == nombre_tabla:
                                    if columna_principal == nombre_columna:
                                        query=f"GRANT INSERT ({columna_secundaria}) ON notarius.{tabla_secundaria} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                                        cur.execute(query)
                                        query=f"GRANT UPDATE ({columna_secundaria}) ON notarius.{tabla_secundaria} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                                        cur.execute(query)

                        if rol == 'admin':
                            query=f"GRANT ALL PRIVILEGES ON mysql.* TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                            cur.execute(query) 
                        
        cur.close()
        conn.close()
    
    def cancelarRegistro(self):
        self.checkBoxAllVer.setChecked(False)
        self.checkBoxAllEscribir.setChecked(False)
        self.lineEdit_nombreusuario.setText("")
        self.lineEdit_contrasenausuario.setText("")
        self.limpiarDict()

    def formatRol(self,rol_unformat):
        if rol_unformat == 'Administrador':
            return 'admin'
        elif rol_unformat == 'Armadores':
            return 'armadores'
        elif rol_unformat == 'Juridico':
            return 'juridico'
        elif rol_unformat == 'Trámites':
            return 'tramites'
        elif rol_unformat == 'Proyectista':
            return 'proyectista'
        elif rol_unformat == 'Presupuesto':
            return 'presupuesto'
        else:
            return 'otro' 

    def isUsuarioRepetido(self,nombre_usuario,cur):
        query = f"SELECT * FROM usuario WHERE nombre_usuario ='{nombre_usuario}'"
        cur.execute(query)
        usuarios = cur.fetchall()
        query = f"SELECT * FROM mysql.user WHERE user ='{nombre_usuario}'"
        cur.execute(query)
        mysql_user = cur.fetchall()
        if len(usuarios) == 0 and len(mysql_user) == 0:
            repetido = False
        else:
            repetido = True
        return repetido

    def reject(self) -> None:
        return
