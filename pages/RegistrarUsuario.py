from re import L
from PyQt5 import uic, QtWidgets, QtCore
from pages.EditarPrivilegios import EditarPrivilegios
import os
from bdConexion import obtener_conexion
from functools import partial
from pages.VerUsuarios import VerUsuarios
from usuarios import getNombreCompleto, getPermisos, getUsuarioLogueado, updateTable
from deployment import getBaseDir

base_dir = getBaseDir()
Form, Base = uic.loadUiType(os.path.join(base_dir,'ui','registrar-usuario.ui'))

class RegistrarUsuario(Form, Base):
    checkboxList=[]
    diccionario_permisos = {'read':{'tabla_final':{'id':True,'color':True,'vencimiento_color':True}},'write':{}}
    diccionario_tramites = {'read': {'tabla_final': {'id':True,'color':True,'vencimiento_color':True, 'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': False, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': False, 'isr_enajenacion': False, 'fecha_aviso_renap': False, 'iva': False, 'uif_poder_irrevocable': False, 'fecha_aviso_dir_not_tpa': False, 'numeracion_folios': False, 'fecha_minuta': False, 'contrato_en_extracto': False, 'minuta': False, 'pendientes': False, 'fecha_entrega_juridico': False, 'otorgamiento': False, 'fecha_cierre_antilavado': False, 'autorizacion': False, 'isr_adquisicion': False, 'fecha_envio_dircc': False, 'fecha_aviso_reloat': False, 'folios': False, 'folio_cancelado': False, 'fecha_apendice': False, 'firmas_en_extracto': False, 'apendice': False, 'no_paso': False, 'fecha_aviso_portal': False, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'id_cc': True,  'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'id_ctd': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'id_rpp': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}, 'no_facturas': {'no_factura': True, 'id': True, 'id_relacion': True}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': True, 'cantidad': False, 'id': True, 'id_relacion': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'pagos': {'concepto': True, 'cantidad': False, 'autorizado_por': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'depositos': {'concepto': True, 'cantidad': False, 'tipo': True, 'banco': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}}, 'write': {'tabla_final': {'id': True, 'color':True,'vencimiento_color':True,'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': False, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': False, 'isr_enajenacion': False, 'fecha_aviso_renap': False, 'iva': False, 'uif_poder_irrevocable': False, 'fecha_aviso_dir_not_tpa': False, 'numeracion_folios': False, 'fecha_minuta': False, 'contrato_en_extracto': False, 'minuta': False, 'pendientes': False, 'fecha_entrega_juridico': False, 'otorgamiento': False, 'fecha_cierre_antilavado': False, 'autorizacion': False, 'isr_adquisicion': False, 'fecha_envio_dircc': False, 'fecha_aviso_reloat': False, 'folios': False, 'folio_cancelado': False, 'fecha_apendice': False, 'firmas_en_extracto': False, 'apendice': False, 'no_paso': False, 'fecha_aviso_portal': False, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'id_cc': True,  'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'id_ctd': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'id_rpp': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': False, 'pagos': False, 'depositos': False}, 'no_facturas': {'no_factura': True, 'id': True, 'id_relacion': True}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': False, 'cantidad': False, 'id': False, 'id_relacion': False}, 'desgloce_ppto_presupuesto': {'id': False, 'no_presupuesto': False}, 'pagos': {'concepto': False, 'cantidad': False, 'autorizado_por': False, 'fecha': False, 'observaciones': False, 'id': False, 'id_relacion': False}, 'pagos_presupuesto': {'id': False, 'no_presupuesto': False}, 'depositos': {'concepto': False, 'cantidad': False, 'tipo': False, 'banco': False, 'fecha': False, 'observaciones': False, 'id': False, 'id_relacion': False}, 'depositos_presupuesto': {'id': False, 'no_presupuesto': False}}}
    diccionario_presupuesto = {'read': {'tabla_final': {'id':True,'color':True,'vencimiento_color':True, 'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': False, 'isr_enajenacion': False, 'fecha_aviso_renap': False, 'iva': False, 'uif_poder_irrevocable': False, 'fecha_aviso_dir_not_tpa': False, 'numeracion_folios': False, 'fecha_minuta': False, 'contrato_en_extracto': False, 'minuta': False, 'pendientes': False, 'fecha_entrega_juridico': False, 'otorgamiento': False, 'fecha_cierre_antilavado': False, 'autorizacion': False, 'isr_adquisicion': False, 'fecha_envio_dircc': False, 'fecha_aviso_reloat': False, 'folios': False, 'folio_cancelado': False, 'fecha_apendice': False, 'firmas_en_extracto': False, 'apendice': False, 'no_paso': False, 'fecha_aviso_portal': False, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'id_cc': True,  'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'id_ctd': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'id_rpp': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}, 'no_facturas': {'no_factura': True, 'id': True, 'id_relacion': True}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': True, 'cantidad': True, 'id': True, 'id_relacion': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'pagos': {'concepto': True, 'cantidad': True, 'autorizado_por': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'depositos': {'concepto': True, 'cantidad': True, 'tipo': True, 'banco': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}}, 'write': {'tabla_final': {'id': True, 'color':True,'vencimiento_color':True,'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': False, 'firma': False, 'isr_enajenacion': False, 'fecha_aviso_renap': False, 'iva': False, 'uif_poder_irrevocable': False, 'fecha_aviso_dir_not_tpa': False, 'numeracion_folios': False, 'fecha_minuta': False, 'contrato_en_extracto': False, 'minuta': False, 'pendientes': False, 'fecha_entrega_juridico': False, 'otorgamiento': False, 'fecha_cierre_antilavado': False, 'autorizacion': False, 'isr_adquisicion': False, 'fecha_envio_dircc': False, 'fecha_aviso_reloat': False, 'folios': False, 'folio_cancelado': False, 'fecha_apendice': False, 'firmas_en_extracto': False, 'apendice': False, 'no_paso': False, 'fecha_aviso_portal': False, 'no_oficio_escritura': False, 'fecha_envio_escritura': False, 'fecha_solicitud_busqueda_testa_rpp': False, 'fecha_solicitud_busqueda_testa_dircc': False, 'fecha_publicacion_periodico': False, 'fecha_publicacion_boletin': False, 'id_cc': True,  'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'id_ctd': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'id_rpp': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}, 'no_facturas': {'no_factura': False, 'id': False, 'id_relacion': False}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': True, 'cantidad': True, 'id': True, 'id_relacion': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'pagos': {'concepto': True, 'cantidad': True, 'autorizado_por': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'depositos': {'concepto': True, 'cantidad': True, 'tipo': True, 'banco': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}}}
    diccionario_juridico ={'read': {'tabla_final': {'id':True,'color':True,'vencimiento_color':True, 'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': False, 'fecha_envio_escritura': False, 'fecha_solicitud_busqueda_testa_rpp': False, 'fecha_solicitud_busqueda_testa_dircc': False, 'fecha_publicacion_periodico': False, 'fecha_publicacion_boletin': False, 'id_cc': False,  'observaciones_cat_calif': False, 'cat_rev': False, 'fechas_catastro_calif': False, 'id_ctd': False, 'cat_terminado': False, 'observaciones_cat_td': False, 'fechas_catastro_td': False, 'id_rpp': False, 'folio_rpp': False, 'observaciones_rpp': False, 'registrada': False, 'fechas_rpp': False, 'fecha_presentado': False, 'fecha_salida': False, 'fecha_vence': False, 'desgloce_ppto': False, 'pagos': False, 'depositos': False}, 'no_facturas': {'no_factura': True, 'id': True, 'id_relacion': True}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': False, 'cat_regreso_calif': False, 'observaciones': False, 'id': False, 'id_fechas': False}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': False, 'cat_regreso_td': False, 'observaciones': False, 'id': False, 'id_fechas': False}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': False, 'regreso_rpp': False, 'observaciones': False, 'id': False, 'id_fechas': False}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': False, 'cantidad': False, 'id': False, 'id_relacion': False}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'pagos': {'concepto': False, 'cantidad': False, 'autorizado_por': False, 'fecha': False, 'observaciones': False, 'id': False, 'id_relacion': False}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'depositos': {'concepto': False, 'cantidad': False, 'tipo': False, 'banco': False, 'fecha': False, 'observaciones': False, 'id': False, 'id_relacion': False}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}}, 'write': {'tabla_final': {'id': True, 'color':True,'vencimiento_color':True,'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': False, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': False, 'fecha_envio_escritura': False, 'fecha_solicitud_busqueda_testa_rpp': False, 'fecha_solicitud_busqueda_testa_dircc': False, 'fecha_publicacion_periodico': False, 'fecha_publicacion_boletin': False, 'id_cc': False,  'observaciones_cat_calif': False, 'cat_rev': False, 'fechas_catastro_calif': False, 'id_ctd': False, 'cat_terminado': False, 'observaciones_cat_td': False, 'fechas_catastro_td': False, 'id_rpp': False, 'folio_rpp': False, 'observaciones_rpp': False, 'registrada': False, 'fechas_rpp': False, 'fecha_presentado': False, 'fecha_salida': False, 'fecha_vence': False, 'desgloce_ppto': False, 'pagos': False, 'depositos': False}, 'no_facturas': {'no_factura': False, 'id': False, 'id_relacion': False}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': False, 'cat_regreso_calif': False, 'observaciones': False, 'id': False, 'id_fechas': False}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': False, 'cat_regreso_td': False, 'observaciones': False, 'id': False, 'id_fechas': False}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': False, 'regreso_rpp': False, 'observaciones': False, 'id': False, 'id_fechas': False}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': False, 'cantidad': False, 'id': False, 'id_relacion': False}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'pagos': {'concepto': False, 'cantidad': False, 'autorizado_por': False, 'fecha': False, 'observaciones': False, 'id': False, 'id_relacion': False}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'depositos': {'concepto': False, 'cantidad': False, 'tipo': False, 'banco': False, 'fecha': False, 'observaciones': False, 'id': False, 'id_relacion': False}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}}}
    diccionario_proyectista = {'read': {'tabla_final': {'id':True,'color':True,'vencimiento_color':True, 'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'fecha_honorarios': True, 'pago_de_comision': True, 'volumen': True, 'no_expediente': True, 'fecha_escritura': True, 'sr': True, 'facturas': True, 'fecha_vence_td': True, 'observaciones_escritura': True, 'entrega_testimonio': True, 'infonavit': True, 'clave_catastral': True, 'desgloce_ppto': True, 'fecha_vence': False}, 'no_facturas': {'no_factura': True, 'id': True, 'id_relacion': True}, 'facturas': {'id': True, 'no_presupuesto': True}, 'desgloce_ppto': {'concepto': True, 'cantidad': False, 'id': True, 'id_relacion': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}}, 'write': {'tabla_final': {'volumen': False, 'sr': False, 'fecha_vence': False}, 'desgloce_ppto': {'cantidad': False}}}
    diccionario_armadores = {'read': {'tabla_final': {'id':True,'color':True,'vencimiento_color':True, 'pago_de_comision': True, 'fecha_escritura': True, 'fecha_vence_td': True, 'observaciones_escritura': True, 'entrega_testimonio': True, 'infonavit': True, 'clave_catastral': True, 'sr': True, 'no_expediente': True, 'volumen': True, 'fecha_honorarios': True, 'valor_operacion': True, 'enajentante': True, 'adquiriente': True, 'gestor': True, 'proyecto': True, 'proyectista': True, 'bis': True, 'no_escritura': True, 'no_presupuesto': True}}, 'write': {'tabla_final': {}}}
    diccionario_admin = {'read': {'tabla_final': {'id':True,'color':True,'vencimiento_color':True, 'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'id_cc': True,  'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'id_ctd': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'id_rpp': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}, 'no_facturas': {'no_factura': True, 'id': True, 'id_relacion': True}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': True, 'cantidad': True, 'id': True, 'id_relacion': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'pagos': {'concepto': True, 'cantidad': True, 'autorizado_por': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'depositos': {'concepto': True, 'cantidad': True, 'tipo': True, 'banco': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}}, 'write': {'tabla_final': {'id': True, 'no_presupuesto': True, 'no_escritura': True, 'bis': True, 'proyectista': True, 'proyecto': True, 'gestor': True, 'adquiriente': True, 'enajentante': True, 'valor_operacion': True, 'fecha_honorarios': True, 'monto_honorarios': True, 'monto_impuestos': True, 'saldo': True, 'pago_de_comision': True, 'volumen': True, 'fecha_escritura': True, 'no_expediente': True, 'sr': True, 'clave_catastral': True, 'infonavit': True, 'entrega_testimonio': True, 'observaciones_escritura': True, 'fecha_vence_td': True, 'facturas': True, 'firma': True, 'isr_enajenacion': True, 'fecha_aviso_renap': True, 'iva': True, 'uif_poder_irrevocable': True, 'fecha_aviso_dir_not_tpa': True, 'numeracion_folios': True, 'fecha_minuta': True, 'contrato_en_extracto': True, 'minuta': True, 'pendientes': True, 'fecha_entrega_juridico': True, 'otorgamiento': True, 'fecha_cierre_antilavado': True, 'autorizacion': True, 'isr_adquisicion': True, 'fecha_envio_dircc': True, 'fecha_aviso_reloat': True, 'folios': True, 'folio_cancelado': True, 'fecha_apendice': True, 'firmas_en_extracto': True, 'apendice': True, 'no_paso': True, 'fecha_aviso_portal': True, 'no_oficio_escritura': True, 'fecha_envio_escritura': True, 'fecha_solicitud_busqueda_testa_rpp': True, 'fecha_solicitud_busqueda_testa_dircc': True, 'fecha_publicacion_periodico': True, 'fecha_publicacion_boletin': True, 'id_cc': True,  'observaciones_cat_calif': True, 'cat_rev': True, 'fechas_catastro_calif': True, 'id_ctd': True, 'cat_terminado': True, 'observaciones_cat_td': True, 'fechas_catastro_td': True, 'id_rpp': True, 'folio_rpp': True, 'observaciones_rpp': True, 'registrada': True, 'fechas_rpp': True, 'fecha_presentado': True, 'fecha_salida': True, 'fecha_vence': True, 'desgloce_ppto': True, 'pagos': True, 'depositos': True}, 'no_facturas': {'no_factura': True, 'id': True, 'id_relacion': True}, 'facturas': {'id': True, 'no_presupuesto': True}, 'fechas_catastro_calif': {'cat_envio_calif': True, 'cat_regreso_calif': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'cc_fechas_cc': {'id': True, 'id_cc': True}, 'fechas_catastro_td': {'cat_envio_td': True, 'cat_regreso_td': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'ctd_fechas_ctd': {'id': True, 'id_ctd': True}, 'fechas_rpp': {'envio_rpp': True, 'regreso_rpp': True, 'observaciones': True, 'id': True, 'id_fechas': True}, 'rpp_fechas_rpp': {'id': True, 'id_rpp': True}, 'desgloce_ppto': {'concepto': True, 'cantidad': True, 'id': True, 'id_relacion': True}, 'desgloce_ppto_presupuesto': {'id': True, 'no_presupuesto': True}, 'pagos': {'concepto': True, 'cantidad': True, 'autorizado_por': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'pagos_presupuesto': {'id': True, 'no_presupuesto': True}, 'depositos': {'concepto': True, 'cantidad': True, 'tipo': True, 'banco': True, 'fecha': True, 'observaciones': True, 'id': True, 'id_relacion': True}, 'depositos_presupuesto': {'id': True, 'no_presupuesto': True}}}
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
            diccionario_usar = {'read':{'tabla_final':{'id':True}},'write':{}}
        self.limpiarDict() 
        self.diccionario_permisos = diccionario_usar
        self.resetCheckboxes(Form)

        

	# en esta funcion se van a cargar las tablas de la base de datos al combobox de tablas
    def setupTables(self, Form):
        lista_tablas = ['tabla_final','desgloce_ppto','pagos','depositos','fechas_rpp','fechas_catastro_td','fechas_catastro_calif']
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
            # if col == 'color' or col == 'vencimiento_color':
            #     continue 
            name_ver = f"acceso_{i}_read"
            name_escritura = f"acceso_{i}_write"
            setattr(self, name_ver, QtWidgets.QCheckBox(Form))
            setattr(self, name_escritura, QtWidgets.QCheckBox(Form))
            checkbox_ver = getattr(self,name_ver)
            checkbox_ver.setStyleSheet("\n"
            "font: 75 14pt;\n"
            "color: white;")
            checkbox_ver.setObjectName(name_ver)
            
            checkbox_escritura = getattr(self,name_ver)
            checkbox_escritura.setText(col)
            checkbox_escritura = getattr(self,name_escritura)
            checkbox_escritura.setStyleSheet("\n"
            "font: 75 14pt;\n"
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
        #print(self.diccionario_permisos)

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
        subtablas = {'facturas':['no_facturas','no_factura'],'fechas_catastro_calif':['fechas_catastro_calif','cat_envio_calif,cat_regreso_calif,observaciones'],'fechas_catastro_td':['fechas_catastro_td','cat_envio_td,cat_regreso_td,observaciones'],'fechas_rpp':['fechas_rpp','envio_rpp,regreso_rpp,observaciones'],'desgloce_ppto':['desgloce_ppto','concepto,cantidad'],'pagos':['pagos','concepto,cantidad,autorizado_por,fecha,observaciones'],'depositos':['depositos','concepto,cantidad,tipo,banco,fecha,observaciones']}
        relacionadas = {'no_facturas':'facturas','fechas_catastro_calif':'cc_fechas_cc','fechas_catastro_td':'ctd_fechas_ctd','fechas_rpp':'rpp_fechas_rpp','desgloce_ppto':'desgloce_ppto_presupuesto','pagos':'pagos_presupuesto','depositos':'depositos_presupuesto'}
        permiso = obj.objectName()
        permiso = permiso.split('_')[2]
        tabla = self.tablaslist.currentText()
        columna = obj.text()
        self.diccionario_permisos[permiso][tabla][columna] = obj.isChecked()
        if permiso == 'write':
            if tabla not in self.diccionario_permisos['read']:
                self.diccionario_permisos['read'][tabla] = {}
            if columna not in self.diccionario_permisos['read'][tabla]:
                self.diccionario_permisos['read'][tabla][columna] = self.diccionario_permisos['write'][tabla][columna]
            if self.diccionario_permisos['read'][tabla][columna] == False and self.diccionario_permisos['write'][tabla][columna]:
                self.diccionario_permisos['read'][tabla][columna] = True
        if permiso == 'read' and not obj.isChecked():
            if tabla not in self.diccionario_permisos['write']:
                 self.diccionario_permisos['write'][tabla] = {}
            self.diccionario_permisos['write'][tabla][columna] = obj.isChecked()
        #tabla_relacionada = getTablaRelacionada(columna)
        
        # en este metodo se agrega o modifica los permisos de las columnas de las subtablas
        if columna in subtablas.keys():
            subtabla = subtablas[columna][0]
            columna_subtabla = subtablas[columna][1].split(',')
            columna_subtabla.append('id')
            if "fecha" in columna: columna_subtabla.append('id_fechas') 
            else: columna_subtabla.append('id_relacion')
            if subtabla not in self.diccionario_permisos[permiso]:
                self.diccionario_permisos[permiso][subtabla] = {}
            if relacionadas[subtabla] not in self.diccionario_permisos[permiso]:
                cols = getPermisos(relacionadas[subtabla])['read'].split(',')
                self.diccionario_permisos[permiso][relacionadas[subtabla]] = {cols[0]:obj.isChecked(),cols[1]:obj.isChecked()}

            for col in columna_subtabla:
                if subtabla not in self.diccionario_permisos[permiso]:
                    self.diccionario_permisos[permiso][subtabla] = {}
                elif col not in self.diccionario_permisos[permiso][subtabla]: 
                    self.diccionario_permisos[permiso][subtabla][col] = True
                elif obj.isChecked() and columna not in 'facturas':
                    self.diccionario_permisos[permiso][subtabla][col] = self.diccionario_permisos[permiso][subtabla][col] 
                else:
                    self.diccionario_permisos[permiso][subtabla][col] = obj.isChecked()

                
        # en este metodo se agregan o modifican los permisos de las tablas relacionadas a la tabla final
        # for registro in tabla_relacionada:
        #     for tabla_val in registro.values():
        #         if tabla_val == tabla or tabla_val in tablas_no_validas: continue
        #         if tabla_val not in self.diccionario_permisos[permiso]:
        #             self.diccionario_permisos[permiso][tabla_val] = {}
        #         self.diccionario_permisos[permiso][tabla_val][columna] = obj.isChecked()
        #         if permiso == 'write':
        #             if tabla_val not in self.diccionario_permisos['read']:
        #                 self.diccionario_permisos['read'][tabla_val] = {}
        #             if columna not in self.diccionario_permisos['read'][tabla_val]:
        #                 self.diccionario_permisos['read'][tabla_val][columna] = self.diccionario_permisos['write'][tabla_val][columna]
        #             if self.diccionario_permisos['read'][tabla_val][columna] == False and self.diccionario_permisos['write'][tabla_val][columna]:
        #                 self.diccionario_permisos['read'][tabla_val][columna] = obj.isChecked()
        #             if self.diccionario_permisos['read'][tabla_val][columna] == False and self.diccionario_permisos['write'][tabla_val][columna] == False:
        #                 self.diccionario_permisos['read'][tabla_val][columna] = obj.isChecked()
        #         try:
        #             # aqui se agregan los permisos de las llaves foraneas
        #             lista_foreignkey = self.foreign_keys[tabla_val]
        #             lista_tabla_col = lista_foreignkey[0]
        #             columna_p = lista_tabla_col[0]
        #             tabla_secundaria = lista_tabla_col[1]
        #             columna_secundaria = lista_tabla_col[2]
        #             if tabla_val not in self.diccionario_permisos[permiso]:
        #                 self.diccionario_permisos[permiso][tabla_val] = {}
        #             self.diccionario_permisos[permiso][tabla_val][columna_p] = obj.isChecked()
                    
        #             if columna == columna_p:
        #                 if tabla_secundaria not in self.diccionario_permisos[permiso]:
        #                     self.diccionario_permisos[permiso][tabla_secundaria] = {}
        #                 self.diccionario_permisos[permiso][tabla_secundaria][columna_secundaria] = obj.isChecked()
        #         except KeyError as error:
        #             #print("La tabla no tiene llaves foraneas")
        #             return
        
        # este metodo verifica que al deseleccionar todos los elementos de una subtabla que esta subtabla se le quiten los permisos en la tabla final
        # en caso de que no todas las columnas se deseleccionaron, la casilla de la subtabla se queda en true
        for key in subtablas:
            subtabla = subtablas[key][0]
            columna_subtabla = subtablas[key][1].split(',')
            if subtabla == tabla:
                cols = getPermisos(relacionadas[subtabla])['read'].split(',')
                for col in columna_subtabla:
                    if col not in self.diccionario_permisos[permiso][subtabla]:
                        self.diccionario_permisos[permiso][subtabla][col] = obj.isChecked()
                    if 'tabla_final' not in  self.diccionario_permisos[permiso]: self.diccionario_permisos[permiso]['tabla_final'] = {}
                    if self.diccionario_permisos[permiso][subtabla][col] == False:
                        self.diccionario_permisos[permiso][relacionadas[subtabla]] = {cols[0]:False,cols[1]:False}
                        self.diccionario_permisos[permiso]['tabla_final'][key] = False
                    else:
                        self.diccionario_permisos[permiso][relacionadas[subtabla]] = {cols[0]:True,cols[1]:True}
                        self.diccionario_permisos[permiso]['tabla_final'][key] = True
                        break
        
        self.resetCheckboxes(self)
 

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

    def agregarLlavesForaneas(self,nombre_tabla,nombre_columna,nombre_usuario,cur):
        # subtablas = {'facturas':['no_facturas','no_factura'],'fechas_catastro_calif':['fechas_catastro_calif','cat_envio_calif,cat_regreso_calif,observaciones'],'fechas_catastro_td':['fechas_catastro_td','cat_envio_td,cat_regreso_td,observaciones'],'fechas_rpp':['fechas_rpp','envio_rpp,regreso_rpp,observaciones'],'desgloce_ppto':['desgloce_ppto','concepto,cantidad'],'pagos':['pagos','concepto,cantidad,autorizado_por,fecha,observaciones'],'depositos':['depositos','concepto,cantidad,tipo,banco,fecha,observaciones']}
        try:
            lista_tabla_col = self.foreign_keys[nombre_tabla]
            for item in lista_tabla_col:
                columna_principal = item[0]
                tabla_secundaria = item[1]
                columna_secundaria = item[2]
                # if nombre_columna in subtablas.keys():
                #      subtabla = subtablas[nombre_columna]
                #      query=f"GRANT SELECT ({subtabla[1]}) ON notarius.{subtabla[0]} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                #      cur.execute(query)
                if columna_principal == nombre_columna:
                     query=f"GRANT SELECT ({columna_secundaria}) ON notarius.{tabla_secundaria} TO '{nombre_usuario}'@'localhost' WITH GRANT OPTION;"
                     cur.execute(query)
        except KeyError as error:
            #print("La tabla no tiene llaves foraneas")
            return
        # for llave,accion in self.diccionario_permisos.copy().items():
        #     for tabla,columnas in accion.copy().items():
        #         for columna,checked in columnas.copy().items():
        #             print("AGREGANDO FK PARA",tabla,columna,checked)
        #             if checked:
        #                 for tabla_p, lista_foreignkey in self.foreign_keys.items():
        #                     lista_tabla_col = lista_foreignkey[0]
        #                     columna_p = lista_tabla_col[0]
        #                     tabla_secundaria = lista_tabla_col[1]
        #                     columna_secundaria = lista_tabla_col[2]
        #                     print(tabla_p)
        #                     if tabla == tabla_p:
        #                         if columna in ['facturas','fechas_catastro_calif','fechas_catastro_td','fechas_rpp,desgloce_ppto','pagos','depositos']: #lista de tablas que deben ser anidadas en los respectivos campos
        #                             subtabla = self.foreign_keys[tabla_secundaria]
        #                             tabla_secundaria_subtabla = subtabla[0][1]
        #                             col_secundaria_subtabla = subtabla[0][2]
        #                             print("AQUIIII",tabla_secundaria_subtabla,col_secundaria_subtabla)
        #                             if tabla_secundaria_subtabla not in self.diccionario_permisos['read']:
        #                                 self.diccionario_permisos['read'][tabla_secundaria_subtabla] = {}
        #                             self.diccionario_permisos['read'][tabla_secundaria_subtabla][col_secundaria_subtabla] = True
        #                         if columna == columna_p:
        #                             if tabla_secundaria not in self.diccionario_permisos['read']:
        #                                 self.diccionario_permisos['read'][tabla_secundaria] = {}
        #                             self.diccionario_permisos['read'][tabla_secundaria][columna_secundaria] = True
                    
    def generarGrants(self,nombre_usuario):
        #self.agregarLlavesForaneas()
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
                        #self.agregarLlavesForaneas(nombre_tabla,nombre_columna, nombre_usuario,cur)
                        if llave == 'read':
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
                        
        self.mensaje.setText("Usuario registrado exitosamente")
        self.checkThreadTimer = QtCore.QTimer(self)
        self.checkThreadTimer.setInterval(10000)
        self.checkThreadTimer.start()
        self.checkThreadTimer.timeout.connect(partial(self.mensaje.setText,''))
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
