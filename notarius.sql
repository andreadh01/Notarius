-- MariaDB dump 10.19  Distrib 10.4.21-MariaDB, for osx10.10 (x86_64)
--
-- Host: localhost    Database: notarius
-- ------------------------------------------------------
-- Server version	10.4.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aviso_definitivo`
--

DROP TABLE IF EXISTS `aviso_definitivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aviso_definitivo` (
  `escritura_id` int(11) NOT NULL,
  `folio_rpp` int(11) DEFAULT NULL COMMENT 'Folio del pase a caja de Registro Público',
  `fecha_presentado` date DEFAULT NULL COMMENT 'Fecha de Ingreso en RPP',
  `fecha_salida` date DEFAULT NULL COMMENT 'Fecha de entregado por RPP',
  `fecha_vence` date DEFAULT NULL COMMENT 'Fecha de Vencimiento del aviso (90 dias naturales despues de fecha de presentacion en RPP)',
  PRIMARY KEY (`escritura_id`),
  KEY `fk_aviso_definitivo_rpp` (`folio_rpp`),
  CONSTRAINT `fk_aviso_definitivo_rpp` FOREIGN KEY (`folio_rpp`) REFERENCES `rpp` (`folio_rpp`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aviso_definitivo`
--

LOCK TABLES `aviso_definitivo` WRITE;
/*!40000 ALTER TABLE `aviso_definitivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `aviso_definitivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bitacora_depositos`
--

DROP TABLE IF EXISTS `bitacora_depositos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bitacora_depositos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `no_presupuesto` varchar(15) NOT NULL,
  `concepto` varchar(100) NOT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `observaciones` varchar(500) DEFAULT NULL,
  `banco` varchar(100) DEFAULT NULL,
  `tipo` enum('honorario','impuestos') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_bitacora_depositos` (`no_presupuesto`),
  CONSTRAINT `fk_bitacora_depositos` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Cada depósito que se haga en un número de presupuesto se va a agregar al campo ''cantidad'' en la tabla presupuesto de ese registro.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bitacora_depositos`
--

LOCK TABLES `bitacora_depositos` WRITE;
/*!40000 ALTER TABLE `bitacora_depositos` DISABLE KEYS */;
/*!40000 ALTER TABLE `bitacora_depositos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bitacora_pagos`
--

DROP TABLE IF EXISTS `bitacora_pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bitacora_pagos` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `no_presupuesto` varchar(15) NOT NULL,
  `concepto_id` int(11) NOT NULL COMMENT 'Se elegirá una opción del catalogo de conceptos de pago',
  `cantidad` decimal(10,2) NOT NULL,
  `autorizado_por` varchar(100) DEFAULT NULL,
  `observaciones` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_bitacora_pagos_presupuesto` (`no_presupuesto`),
  KEY `fk_bitacora_pagos` (`concepto_id`),
  CONSTRAINT `fk_bitacora_pagos` FOREIGN KEY (`concepto_id`) REFERENCES `cat_conceptos_pago` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_bitacora_pagos_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Cada pago que se agregue en un número de presupuesto va a descontar del campo ''cantidad'' en la tabla presupuesto de ese registro. En caso de que no se tenga dinero suficiente se debe autorizar el pago.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bitacora_pagos`
--

LOCK TABLES `bitacora_pagos` WRITE;
/*!40000 ALTER TABLE `bitacora_pagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `bitacora_pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cat_conceptos_pago`
--

DROP TABLE IF EXISTS `cat_conceptos_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cat_conceptos_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `concepto` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat_conceptos_pago`
--

LOCK TABLES `cat_conceptos_pago` WRITE;
/*!40000 ALTER TABLE `cat_conceptos_pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_conceptos_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catastro_calificacion`
--

DROP TABLE IF EXISTS `catastro_calificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catastro_calificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vencimiento_td` tinyint(1) DEFAULT NULL COMMENT 'Alerta del vencimiento del traslado de dominio',
  `no_presupuesto` varchar(15) NOT NULL,
  `escritura_id` int(11) DEFAULT NULL,
  `observaciones` varchar(500) DEFAULT NULL,
  `cat_rev` enum('si','en tramite','correccion') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_catastro_calificacion` (`escritura_id`),
  KEY `fk_catastro_calificacion_presupuesto` (`no_presupuesto`),
  CONSTRAINT `fk_catastro_calificacion` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_catastro_calificacion_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catastro_calificacion`
--

LOCK TABLES `catastro_calificacion` WRITE;
/*!40000 ALTER TABLE `catastro_calificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `catastro_calificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `catastro_td`
--

DROP TABLE IF EXISTS `catastro_td`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catastro_td` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `escritura_id` int(11) NOT NULL,
  `observaciones` varchar(500) DEFAULT NULL,
  `cat_terminado` enum('si','en tramite','correccion') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_catastro_td_escritura` (`escritura_id`),
  CONSTRAINT `fk_catastro_td_escritura` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catastro_td`
--

LOCK TABLES `catastro_td` WRITE;
/*!40000 ALTER TABLE `catastro_td` DISABLE KEYS */;
/*!40000 ALTER TABLE `catastro_td` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desgloce_ppto`
--

DROP TABLE IF EXISTS `desgloce_ppto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `desgloce_ppto` (
  `no_presupuesto` varchar(15) NOT NULL,
  `concepto` varchar(100) NOT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `pagado` tinyint(1) DEFAULT NULL,
  KEY `fk_desgloce_ppto_presupuesto` (`no_presupuesto`),
  CONSTRAINT `fk_desgloce_ppto_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='La sumatoria de todas las cantidades relacionadas a un número de presupuesto sera el monto total a pagar.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desgloce_ppto`
--

LOCK TABLES `desgloce_ppto` WRITE;
/*!40000 ALTER TABLE `desgloce_ppto` DISABLE KEYS */;
/*!40000 ALTER TABLE `desgloce_ppto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_notarias_seguimiento_juicios`
--

DROP TABLE IF EXISTS `direccion_notarias_seguimiento_juicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_notarias_seguimiento_juicios` (
  `escritura_id` int(11) NOT NULL,
  `no_oficio_escritura` int(11) DEFAULT NULL,
  `fecha_envio_escritura` date DEFAULT NULL,
  `fecha_solicitud_busqueda_testa_dircc` date DEFAULT NULL,
  `fecha_solicitud_busqueda_testa_rpp` date DEFAULT NULL,
  `fecha_publicacion_boletin` date DEFAULT NULL,
  `fecha_publicacion_periodico` date DEFAULT NULL,
  PRIMARY KEY (`escritura_id`),
  CONSTRAINT `fk_direccion_notarias_seguimiento_juicios` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_notarias_seguimiento_juicios`
--

LOCK TABLES `direccion_notarias_seguimiento_juicios` WRITE;
/*!40000 ALTER TABLE `direccion_notarias_seguimiento_juicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_notarias_seguimiento_juicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `escritura`
--

DROP TABLE IF EXISTS `escritura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `escritura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_escritura` int(10) unsigned NOT NULL,
  `bis` tinyint(1) DEFAULT 0,
  `no_presupuesto` varchar(15) DEFAULT NULL,
  `volumen` int(11) NOT NULL,
  `fecha` date NOT NULL COMMENT 'Fecha de Escritura',
  `no_expediente` int(11) NOT NULL COMMENT 'Numero de expediente del sistema de jurídico',
  `sr` tinyint(1) DEFAULT NULL COMMENT 'Indicador que significa si el tramite se ingresa en Registro Público, Sólo de control no es necesario mostrar en la consulta en solo lectura',
  `clave_catastral` int(11) NOT NULL,
  `infonavit` int(11) DEFAULT NULL COMMENT 'Numero de credito de infonavit',
  `entrega_testimonio` date DEFAULT NULL COMMENT 'Deben estar cubiertos todos los pagos para entregarlo, solo el admin puede autorizar con adeudo.',
  `observaciones` varchar(500) DEFAULT NULL,
  `fecha_vence` date DEFAULT NULL COMMENT '60 días hábiles después de la fecha de esccritura',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_escritura_no_escritura` (`no_escritura`),
  UNIQUE KEY `id` (`no_escritura`,`bis`),
  UNIQUE KEY `unq_escritura_bis` (`bis`),
  KEY `fk_escritura_presupuesto` (`no_presupuesto`),
  CONSTRAINT `fk_escritura_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Eva puede editar, agregar y consultar todos los datos de la tabla.\nMartin y Paulina pueden agregar y modificar campos hasta ''no_expediente'', puede visualizar el resto.\nLos demás pueden ver todos los campos, menos ''mes_de_pago'' y ''observaciones''.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `escritura`
--

LOCK TABLES `escritura` WRITE;
/*!40000 ALTER TABLE `escritura` DISABLE KEYS */;
/*!40000 ALTER TABLE `escritura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `facturas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_presupuesto` varchar(15) DEFAULT NULL,
  `no_factura` int(11) NOT NULL,
  `escritura_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_facturas_no_presupuesto` (`no_presupuesto`),
  KEY `fk_facturas_escritura` (`escritura_id`),
  CONSTRAINT `fk_facturas_escritura` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fechas_catastro_calif`
--

DROP TABLE IF EXISTS `fechas_catastro_calif`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fechas_catastro_calif` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cat_calif` int(11) NOT NULL,
  `cat_envio_calif` date DEFAULT NULL COMMENT 'Fecha de envio de Traslado de dominio a Catastro para informacion',
  `cat_regreso_calif` date DEFAULT NULL COMMENT 'Fecha de regreso de Traslado de dominio a Catastro para informacion',
  `observaciones` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_fechas_catastro_catastro_calificacion` (`id_cat_calif`),
  CONSTRAINT `fk_fechas_catastro_catastro_calificacion` FOREIGN KEY (`id_cat_calif`) REFERENCES `catastro_calificacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fechas_catastro_calif`
--

LOCK TABLES `fechas_catastro_calif` WRITE;
/*!40000 ALTER TABLE `fechas_catastro_calif` DISABLE KEYS */;
/*!40000 ALTER TABLE `fechas_catastro_calif` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fechas_catastro_td`
--

DROP TABLE IF EXISTS `fechas_catastro_td`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fechas_catastro_td` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cat_td` int(11) NOT NULL,
  `cat_envio_td` date DEFAULT NULL COMMENT 'Fecha de envio de Traslado de dominio a Catastro',
  `cat_regreso_td` date DEFAULT NULL COMMENT 'Nombre del regreso de Traslado de dominio (cuando esta terminado)',
  `observaciones` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_fechas_catastro_0_id_cat_td` (`id_cat_td`),
  CONSTRAINT `fk_fechas_catastro_0_catastro_td` FOREIGN KEY (`id_cat_td`) REFERENCES `catastro_td` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fechas_catastro_td`
--

LOCK TABLES `fechas_catastro_td` WRITE;
/*!40000 ALTER TABLE `fechas_catastro_td` DISABLE KEYS */;
/*!40000 ALTER TABLE `fechas_catastro_td` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fechas_catastro_td_0`
--

DROP TABLE IF EXISTS `fechas_catastro_td_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fechas_catastro_td_0` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_rpp` int(11) NOT NULL,
  `envio_rpp` date DEFAULT NULL COMMENT 'Fecha de Envio a Registro Público',
  `regreso_rpp` date DEFAULT NULL COMMENT 'Fecha de regreso de Registro Público',
  `observaciones` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_fechas_catastro_0_id_cat_td_0` (`id_rpp`),
  CONSTRAINT `fk_fechas_catastro_td_0_rpp` FOREIGN KEY (`id_rpp`) REFERENCES `rpp` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fechas_catastro_td_0`
--

LOCK TABLES `fechas_catastro_td_0` WRITE;
/*!40000 ALTER TABLE `fechas_catastro_td_0` DISABLE KEYS */;
/*!40000 ALTER TABLE `fechas_catastro_td_0` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `juridico`
--

DROP TABLE IF EXISTS `juridico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `juridico` (
  `escritura_id` int(11) NOT NULL,
  `contrato_en_extracto` tinyint(1) DEFAULT NULL,
  `firmas_en_extracto` tinyint(1) DEFAULT NULL,
  `pendientes` tinyint(1) DEFAULT NULL,
  `no_paso` tinyint(1) DEFAULT NULL,
  `otorgamiento` date DEFAULT NULL,
  `firma` date DEFAULT NULL,
  `autorizacion` date DEFAULT NULL,
  `fecha_aviso_renap` date DEFAULT NULL,
  `fecha_envio_dircc` date DEFAULT NULL,
  `uif_poder_irrevocable` date DEFAULT NULL,
  `fecha_aviso_reloat` date DEFAULT NULL,
  `fecha_aviso_dir_not_tpa` date DEFAULT NULL,
  `folios` int(11) DEFAULT NULL,
  `numeracion_folios` varchar(100) DEFAULT NULL,
  `folio_cancelado` int(11) DEFAULT NULL,
  `fecha_minuta` date DEFAULT NULL,
  `fecha_apendice` date DEFAULT NULL,
  `minuta` tinyint(1) DEFAULT NULL,
  `apendice` tinyint(1) DEFAULT NULL,
  `fecha_entrega_juridico` date DEFAULT NULL,
  `fecha_aviso_portal` date DEFAULT NULL,
  `fecha_cierre_antilavado` date DEFAULT NULL,
  `isr_enajenacion` tinyint(1) DEFAULT NULL,
  `isr_adquisicion` tinyint(1) DEFAULT NULL,
  `iva` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`escritura_id`),
  CONSTRAINT `fk_juridico_escritura` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `juridico`
--

LOCK TABLES `juridico` WRITE;
/*!40000 ALTER TABLE `juridico` DISABLE KEYS */;
/*!40000 ALTER TABLE `juridico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presupuesto`
--

DROP TABLE IF EXISTS `presupuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presupuesto` (
  `no_presupuesto` varchar(15) NOT NULL,
  `proyectista` varchar(100) NOT NULL COMMENT 'Abogado responsable',
  `proyecto` varchar(200) NOT NULL COMMENT 'DESCRIPCION DEL TRAMITE',
  `gestor` varchar(100) DEFAULT NULL COMMENT 'Nombre del gestor encargado del asunto (persona externa de la notaria)',
  `enajentante` varchar(100) DEFAULT NULL COMMENT 'PERSONA QUE VENDE, PUEDE QUEDAR EN BLANCO',
  `adquiriente` varchar(100) NOT NULL COMMENT 'PERSONA QUE ADQUIERE O CONTRATA EL SERVICIO',
  `valor_operacion` decimal(10,2) NOT NULL,
  `monto_honorarios` decimal(10,2) DEFAULT NULL,
  `fecha_honorarios` date DEFAULT NULL,
  `cantidad` decimal(10,2) DEFAULT NULL,
  `mes_de_pago` date DEFAULT NULL COMMENT 'Mes y año en la que se pago la comisión al proyectista',
  UNIQUE KEY `unq_presupuesto_no_presupuesto` (`no_presupuesto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presupuesto`
--

LOCK TABLES `presupuesto` WRITE;
/*!40000 ALTER TABLE `presupuesto` DISABLE KEYS */;
/*!40000 ALTER TABLE `presupuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rpp`
--

DROP TABLE IF EXISTS `rpp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rpp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_presupuesto` varchar(15) NOT NULL,
  `escritura_id` int(11) DEFAULT NULL,
  `folio_rpp` int(11) DEFAULT NULL COMMENT 'Folio del pase a caja de Registro Público',
  `observaciones` varchar(500) DEFAULT NULL,
  `registrada` enum('en tramite','si','rechazado','reingreso','saldo insuficiente') DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_rpp_folio_rpp` (`folio_rpp`),
  KEY `fk_rpp_presupuesto` (`no_presupuesto`),
  KEY `fk_rpp_escritura` (`escritura_id`),
  CONSTRAINT `fk_rpp_escritura` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_rpp_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rpp`
--

LOCK TABLES `rpp` WRITE;
/*!40000 ALTER TABLE `rpp` DISABLE KEYS */;
/*!40000 ALTER TABLE `rpp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(100) DEFAULT NULL,
  `contrasena` varchar(300) DEFAULT NULL,
  `rol` enum('admin','empleado','proyectista','armadores','otro') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Empleados: Martin, Eva y Paulina\nProyectistas:\n Alicia Felix\nMartha Soto\nAbraham Castro\nYesenia\nAna Luisa Rodriguez\nJuan Martin Ruiz\nRene Luna Araiza\nRene Luna Sugich\nGloria';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-21 23:52:33
