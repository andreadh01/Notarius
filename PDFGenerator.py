import os
from jinja2 import Template
from PyQt5.QtWidgets import QFileDialog
import pdfkit

from usuarios import getNombreCompleto, getNombreCompletoSubtabla

facturas_nombres = ["Número de factura"]

pagos_nombres = ["Fecha","Concepto","Cantidad","Autorizado por","Observaciones"]

depositos_nombres = ["Fecha","Concepto","Cantidad","Banco","Tipo","Observaciones"]

desglose_nombres = ["Concepto","Cantidad"]

fechas_nombres = ["Fecha de envío","Fecha de regreso",	"Observaciones"]

general_nombres = [
    "Proyectista"			,
	"Proyecto"				,
	"Gestor"				,
	"Enajenante"			,
	"Adquiriente"			,
	"Volumen"				,
	"Número de expediente"	,
	"Fecha de escritura"	,
	"Fecha vence TD"		,
	"SR"					,
	"Clave catastral"		,
	"Número de Infonavit"	,
	"Entrega de testimonio"	,
	"Observaciones escritura"]
juridico_nombres = [
    "Acto jurídico o contrato en extracto"	,
	"Firmas de las partes en extracto"		,
	"Pendientes"							,
	"No paso"								,
	"Otorgamiento"							,
	"Firma"									,
	"Autorización"							,
	"Fecha de aviso al RENAP"				,
	"Fecha envío a la DIRCC"				,
	"UIF poder irrevocable"					,
	"Fecha de aviso al RELOAT"				,
	"Fecha aviso DIR NOT TPA"				,
	"Folios"								,
	"Numeración de folios"					,
	"Folio cancelado"						,
	"Minuta"								,
	"Fecha recibido minuta"					,
	"Apéndice"								,
	"Fecha recibido apéndice"				,
	"Fecha entrega por jurídico"			,
	"Fecha de aviso al portal"				,
	"Fecha de cierre de antilavado"			,
	"ISR de enajenación"					,
	"ISR de adquisición"					,
	"IVA"									]
tramites_nombres = [
    "Número de oficio",
	"Fecha de envío a Dirección de Notarias",
	"Fecha de solicitud de búsqueda de testamento en Dirección de Notaria",
	"Fecha de solicitud de búsqueda de testamento en RPP",
	"Fecha de Publicación en Boletín Oficial",
	"Fecha de Publicación en Periódico de los Avisos"]
cc_nombres = [
		"Catastro calificación terminado",
	"Observaciones catastro calificación"]
ctd_nombres = [
		"Catastro TD terminado",
	"Observaciones catastro TD"
]
rpp_nombres = [
		"Folio RPP"												,
	"Registrada"												,
	"Observaciones RPP"											,
	"Fecha de presentado de Aviso Definitivo (ingreso a RPP)"	,
	"Fecha salida de Aviso Definitivo (entregado por RPP)"		,
	"Fecha vence de Aviso Definitivo"							
]
presupuesto_nombres = [
 	"Valor de operación"	,
	"Fecha de honorarios"	,
	"Monto de honorarios"	,
	"Monto de impuestos"	,
	"Pago de comisión"		,
	"Saldo"					
]
def generarPDF(self):
	file_path = os.path.abspath("style.css")
	logo = os.path.abspath("logo.png")
	registro = self.listaregistros_editarregistros
	print(registro)
	subtablas = self.diccionarioregistros_editarregistros_subtablas
	print('subtablasssss',subtablas)
	outfile, _ = QFileDialog.getSaveFileName(filter='PDF Files (*.pdf)')
	if outfile != '':
		with open("reporte.html", encoding='utf8') as f:
			template_content = f.read()

		template = Template(template_content)
		dicc_general, dicc_juridico, dicc_tramites,dicc_presupuesto,dicc_cc,dicc_ctd,dicc_rpp,dicc_facturas,dicc_fechascc,dicc_fechasctd,dicc_fechasrpp,dicc_desglose,dicc_pagos,dicc_depositos = generarDicts(registro, subtablas)
		# Render the template with the content
		html_content = template.render(file_path=file_path, img_path=logo, no_presupuesto=registro['no_presupuesto'], no_escritura=registro['no_escritura'], bis=registro['bis'], 
dicc_general = dicc_general,
dicc_juridico = dicc_juridico,
dicc_tramites = dicc_tramites,
dicc_presupuesto = dicc_presupuesto,
dicc_cc = dicc_cc,
dicc_ctd = dicc_ctd,
dicc_rpp = dicc_rpp,
dicc_facturas = dicc_facturas,
dicc_fechascc = dicc_fechascc,
dicc_fechasctd = dicc_fechasctd,
dicc_fechasrpp = dicc_fechasrpp,
dicc_desglose = dicc_desglose,
dicc_pagos = dicc_pagos,
dicc_depositos = dicc_depositos,
depositos_nombres = depositos_nombres,
pagos_nombres = pagos_nombres,desglose_nombres=desglose_nombres,fechas_nombres=fechas_nombres,facturas_nombres=facturas_nombres)	
    	# dict general, dict juridico, dict tramites -> dict cc -> dict fechas_cc, dict presupuesto -> desgloce -> pagos ->depositos

		# Create the file
		pdfkit.from_string(html_content, outfile,options={"enable-local-file-access": "",'encoding': "UTF-8"})

def generarDicts(registro,subtablas):
    dicc_general, dicc_juridico, dicc_tramites, dicc_presupuesto, dicc_cc, dicc_ctd, dicc_rpp, dicc_facturas, dicc_fechascc, dicc_fechasctd, dicc_fechasrpp, dicc_desglose, dicc_pagos,dicc_depositos = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},{}
    for col, val in registro.items():
        col = getNombreCompleto(col)
        print(col)
        if col in general_nombres:
            dicc_general[col] = val
        if col in juridico_nombres:
            dicc_juridico[col] = val
        if col in tramites_nombres:
            dicc_tramites[col] = val
        if col in presupuesto_nombres:
            dicc_presupuesto[col] = val
        if col in cc_nombres:
            dicc_cc[col] = val
        if col in ctd_nombres:
            dicc_ctd[col] = val
        if col in rpp_nombres:
            dicc_rpp[col] = val
    
    for key, registros in subtablas.items():
        for index, reg in registros.items():
            print('key',index, 'resgistrooo',reg)
            for col, val in reg.items():
                col = getNombreCompletoSubtabla(key,col)
                if col in facturas_nombres:
                    if index not in dicc_facturas:
                        dicc_facturas[index] = {}
                    dicc_facturas[index][col] = val
                if col in pagos_nombres:
                    if key == 'pagos':
                        if index not in dicc_pagos:
                            dicc_pagos[index] = {}
                        dicc_pagos[index][col] = val
                if col in desglose_nombres:
                    if key == 'desgloce_ppto':
                        if index not in dicc_desglose:
                            dicc_desglose[index] = {}
                        dicc_desglose[index][col] = val
                if col in depositos_nombres:
                    if key == 'depositos':
                        if index not in dicc_depositos:
                            dicc_depositos[index] = {}
                        dicc_depositos[index][col] = val
                if col in fechas_nombres:
                    if key == 'fechas_catastro_calif':
                        if index not in dicc_fechascc:
                            dicc_fechascc[index] = {}
                        dicc_fechascc[index][col] = val
                    if key == 'fechas_catastro_td':
                        if index not in dicc_fechasctd:
                            dicc_fechasctd[index] = {}
                        dicc_fechasctd[index][col] = val
                    if key == 'fechas_rpp':
                        if index not in dicc_fechasrpp:
                            dicc_fechasrpp[index] = {}
                        dicc_fechasrpp[index][col] = val

                
            

    return dicc_general, dicc_juridico, dicc_tramites,dicc_presupuesto,dicc_cc,dicc_ctd,dicc_rpp,dicc_facturas,dicc_fechascc,dicc_fechasctd,dicc_fechasrpp,dicc_desglose,dicc_pagos,dicc_depositos
