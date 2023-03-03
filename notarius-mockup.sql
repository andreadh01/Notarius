CREATE DATABASE notarius;

USE notarius;

DROP TABLE IF EXISTS `presupuesto`;

CREATE TABLE `presupuesto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `proyectista` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Abogado responsable',
  `proyecto` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'DESCRIPCION DEL TRAMITE',
  `gestor` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Nombre del gestor encargado del asunto (persona externa de la notaria)',
  `enajentante` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'PERSONA QUE VENDE, PUEDE QUEDAR EN BLANCO',
  `adquiriente` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'PERSONA QUE ADQUIERE O CONTRATA EL SERVICIO',
  `valor_operacion` decimal(10,2) NOT NULL,
  `monto_honorarios` decimal(10,2) DEFAULT NULL,
  `fecha_honorarios` date DEFAULT NULL,
  `cantidad` decimal(10,2) DEFAULT NULL,
  `mes_de_pago` date DEFAULT NULL COMMENT 'Mes y año en la que se pago la comisión al proyectista',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_presupuesto_no_presupuesto` (`no_presupuesto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('156', 'Miss Jordane Kub', 'Gulgowski and Sons', 'Ms. Elena Jacobs', 'Trent Russel', 'Dr. Reinhold Olson PhD', '18078818.92', '347359.40', '2010-06-22', '9.00', '1982-03-23');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('164', 'Kali Lindgren', 'Lowe, Fahey and Bergnaum', 'Alexane Crist', 'River Armstrong', 'Viola Runolfsdottir', '55.94', '2.43', '1983-09-19', '76216753.00', '1999-09-02');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('174', 'Arnold Jerde', 'Kerluke-Zulauf', 'Sigurd Erdman', 'Tremaine Hoppe Sr.', 'Davon Breitenberg', '539.70', '660363.13', '2007-03-16', '9394655.00', '2006-01-17');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('235', 'Wilma Thiel', 'Herman-Runolfsdottir', 'Ariel Friesen', 'Antonia Wiegand', 'Vida Moen PhD', '0.00', '15200.70', '2019-12-05', '99999999.99', '1992-11-10');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('243', 'Maximo Predovic', 'Goodwin-Turner', 'Lexie Dach', 'Katheryn Fisher', 'Lawson Towne', '422562.91', '1421502.70', '1994-10-02', '327.00', '2016-02-29');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('283', 'Randal Hilpert', 'Kuhic and Sons', 'Marion Kozey', 'Zoie Schmeler', 'Ethelyn Sauer', '0.00', '0.00', '2015-10-09', '6483920.00', '2001-10-28');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('430', 'Hollie Kemmer', 'Yost-Sporer', 'Jess Tillman', 'Lonie Homenick', 'Kip Balistreri Sr.', '5.47', '4525035.92', '1994-01-11', '83993138.00', '2021-05-07');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('437', 'Prof. Michelle Prosacco III', 'Lockman-Leannon', 'Devyn Beier Jr.', 'Manuel Heller MD', 'Ms. Martine Brakus MD', '9702.83', '597.10', '1982-11-07', '58838.00', '1981-07-09');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('510', 'Ozella Dibbert IV', 'Pollich Inc', 'Dr. Samara Haag', 'Mara Hessel V', 'Porter Veum', '999123.71', '6094.90', '1996-05-20', '99999999.99', '1976-04-21');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('636', 'Vernie Ziemann', 'Ullrich and Sons', 'Andres Grady', 'Gaylord Champlin', 'Abbigail Kozey', '471.00', '99999999.99', '1985-04-24', '40599.00', '1972-09-14');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('662', 'Miss Grace Volkman DDS', 'Spinka Inc', 'Ricky Ryan', 'Gayle Beer', 'Prof. Kaitlin Schumm', '606114.28', '1.86', '1972-07-15', '55053.00', '1986-11-11');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('673', 'Jerry Mueller', 'Harber-Reichert', 'Reva Gislason', 'Johanna Sawayn PhD', 'Randi Parisian', '0.00', '8.82', '2020-01-12', '81602.00', '1977-09-11');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('700', 'Mckayla Powlowski', 'Rosenbaum, Beer and Murphy', 'Prof. Porter Larson', 'Samir Schimmel', 'Dr. Janie Leannon', '1535961.35', '2846189.39', '1977-06-01', '569.00', '1990-05-31');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('761', 'Wilhelm Crooks', 'Gleason-Ward', 'Dr. Angela Rath I', 'Schuyler Wiza', 'Terrance Osinski MD', '3.00', '145853.48', '1977-02-03', '22203.00', '1997-09-29');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('775', 'Roman Williamson', 'Jacobs Inc', 'Favian Nitzsche', 'Bradly Gibson', 'Dr. Charlotte Reichert', '99999999.99', '466.91', '2020-01-16', '0.00', '2011-01-25');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('776', 'Regan Schamberger DVM', 'Abbott-Homenick', 'Hollie Rogahn', 'Maurine Kunde', 'Sonya Gerlach', '70095604.46', '4932291.39', '1988-03-17', '41108.00', '1984-01-19');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('844', 'Daniella Gislason', 'Hilpert-Goyette', 'Ms. Jaunita Leuschke III', 'Dr. Chesley Crona I', 'Miss Hallie Reichert', '0.00', '212.52', '1977-01-23', '89180929.00', '1991-11-06');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('877', 'Jane Upton', 'Waters Inc', 'Alexie Feil', 'Ali Schuppe', 'Minnie Yost', '171810.09', '1.48', '1986-09-19', '99999999.99', '1980-03-02');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('910', 'Prof. Maryjane Prosacco', 'Hermann and Sons', 'Ivory Krajcik', 'Ms. Piper Champlin', 'Shanelle Wilderman', '4633.88', '0.00', '2009-08-18', '951886.00', '1995-07-24');
INSERT INTO `presupuesto` (`no_presupuesto`, `proyectista`, `proyecto`, `gestor`, `enajentante`, `adquiriente`, `valor_operacion`, `monto_honorarios`, `fecha_honorarios`, `cantidad`, `mes_de_pago`) VALUES ('998', 'Ms. Grace Sawayn V', 'Nicolas Group', 'Malinda Gutmann', 'Dr. Lue Beatty', 'Mrs. Aaliyah Von', '299410.00', '492472.00', '2005-03-29', '52.00', '1993-10-06');

DROP TABLE IF EXISTS `bitacora_depositos`;

CREATE TABLE `bitacora_depositos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `concepto` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `banco` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo` enum('honorario','impuestos') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_bitacora_depositos` (`no_presupuesto`),
  CONSTRAINT `fk_bitacora_depositos` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Cada depósito que se haga en un número de presupuesto se va a agregar al campo ''cantidad'' en la tabla presupuesto de ese registro.';

INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (1, '1976-05-04 18:01:28', '156', 'culpa', '47285406.70', 'Exercitationem tempora quos dolorem quo. Consequatur accusamus cum explicabo neque sequi enim et est. Et illum dolores voluptatum aspernatur. Nam nostrum magnam minus in qui enim.', 'Fay-Langworth', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (2, '2008-07-07 13:16:10', '164', 'delectus', '937.20', 'Amet voluptatem qui saepe. Quibusdam architecto ullam autem vero amet quia. Sit aut aut cupiditate eum voluptas voluptatem.', 'Hudson-Muller', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (3, '2020-11-29 13:17:36', '174', 'ipsam', '77876056.67', 'Voluptatem id dolorum qui consequatur natus. In blanditiis deleniti dolorem dicta. Maxime omnis amet soluta blanditiis sit nobis itaque. Molestiae voluptatem est ut reprehenderit ut.', 'Gottlieb, Padberg and Rutherford', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (4, '1979-03-31 22:24:49', '235', 'doloremque', '3996041.00', 'Sed modi enim totam deleniti illo. Voluptatem eligendi cupiditate voluptas et natus impedit asperiores asperiores. Commodi quae illum ducimus iure.', 'Considine LLC', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (5, '1982-05-27 19:11:06', '243', 'quas', '3.83', 'Itaque ipsum accusamus ipsum occaecati sit. Voluptas doloremque magnam esse odio. Officiis ullam asperiores optio velit vitae corrupti quisquam. Exercitationem tempora sapiente asperiores ut tempore.', 'Hickle LLC', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (6, '1994-03-13 23:21:51', '283', 'ullam', '307.34', 'Rem eius aut est excepturi. Ut est suscipit maiores consequuntur numquam dignissimos voluptatem distinctio. Eum recusandae et dolores quam ut aliquam. Nesciunt quisquam amet repellendus modi autem.', 'Torp-Hayes', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (7, '1982-05-02 12:16:32', '430', 'cupiditate', '44112789.43', 'Architecto quas officiis nobis. Dolores corrupti alias neque facilis repellendus. Ipsum non facere voluptatem ullam laudantium in accusantium.', 'Windler-Ebert', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (8, '1978-01-29 03:18:54', '437', 'facilis', '99999999.99', 'Dolore quas repellat nihil velit perferendis aut est. Illum reiciendis consequatur non. Dolores autem nam ut repellat. Magnam aut quaerat blanditiis nostrum quae.', 'Borer, Homenick and Glover', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (9, '1975-03-09 09:53:22', '510', 'laboriosam', '26.70', 'Exercitationem in vero sit pariatur veritatis ea. Est sit incidunt sed atque. Dolor modi similique aut ipsa consequatur. Incidunt vitae inventore omnis.', 'Steuber, Rau and Ernser', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (10, '2021-12-30 04:03:37', '636', 'repellat', '50.00', 'Exercitationem deleniti enim perspiciatis. Fuga veniam id illum velit. Voluptatibus harum porro quo error aperiam asperiores.', 'Moore Inc', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (11, '2018-06-13 05:34:13', '662', 'ut', '1428.99', 'Ducimus vero eligendi harum rerum. Consequatur iure soluta vitae iure delectus. Eligendi possimus et nobis excepturi illo fuga corrupti.', 'Borer, Windler and Adams', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (12, '2003-12-18 04:52:55', '673', 'fugiat', '51856459.44', 'Est expedita dignissimos et eum temporibus quis enim animi. Dolore atque est accusantium fugiat est aut. Nihil non hic omnis optio.', 'Gusikowski-Hirthe', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (13, '2012-02-22 14:24:20', '700', 'ad', '116110.40', 'Voluptate ut quia porro enim adipisci libero. Sequi molestiae tempore possimus non et quae officiis. Repudiandae deleniti et ducimus in quis.', 'Okuneva-Pacocha', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (14, '1996-08-18 01:04:44', '761', 'voluptatibus', '0.00', 'Deserunt impedit animi quae assumenda. Consequatur blanditiis reiciendis sed officiis est. Adipisci tempore quia voluptas molestias expedita voluptatum hic molestiae.', 'Heidenreich-Konopelski', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (15, '1970-07-29 05:30:19', '775', 'harum', '825092.00', 'Occaecati tempore commodi aut qui aperiam dignissimos odit placeat. Quo ea ullam facere quae incidunt ut qui.', 'Ortiz-Ratke', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (16, '1973-03-23 17:54:29', '776', 'inventore', '0.00', 'Consequatur voluptatem id dolorem dolor error quo. Quia ipsum iure autem et fuga reiciendis saepe et. Mollitia quia rem reiciendis. Et facere nemo repudiandae molestias vel laborum qui accusamus.', 'Reichert, Kautzer and Beahan', 'impuestos');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (17, '2016-03-15 09:29:13', '844', 'ducimus', '16.30', 'Illo quia totam nihil nisi. In occaecati recusandae laborum ut sunt veritatis soluta. Totam modi est sit sunt et.', 'Kuhlman Inc', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (18, '1974-07-21 19:42:14', '877', 'incidunt', '905097.20', 'Vero qui adipisci rerum non enim quam. Enim est repellendus laudantium voluptas. Sint consequatur maxime quis ipsum. Occaecati minus et soluta corrupti sunt minus. Tempora maiores qui vero nam.', 'Sipes Group', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (19, '1991-07-25 07:08:31', '910', 'quia', '1179.81', 'Dolorem odio modi sint omnis optio. Ut natus voluptate beatae voluptates labore veniam incidunt. Officiis sunt vitae recusandae asperiores quos in et.', 'Huels, Stoltenberg and Ernser', 'honorario');
INSERT INTO `bitacora_depositos` (`id`, `fecha`, `no_presupuesto`, `concepto`, `cantidad`, `observaciones`, `banco`, `tipo`) VALUES (20, '1988-12-05 20:16:25', '998', 'unde', '0.00', 'Molestiae aspernatur earum porro aut officia amet expedita. Perspiciatis cum id culpa beatae. Ea explicabo illum quaerat consequuntur deserunt.', 'Hayes-Hilll', 'honorario');


DROP TABLE IF EXISTS `cat_conceptos_pago`;

CREATE TABLE `cat_conceptos_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `concepto` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (1, 'soluta');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (2, 'sunt');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (3, 'eius');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (4, 'in');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (5, 'earum');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (6, 'qui');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (7, 'debitis');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (8, 'totam');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (9, 'quos');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (10, 'consequatur');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (11, 'accusamus');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (12, 'eius');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (13, 'quo');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (14, 'et');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (15, 'est');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (16, 'aut');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (17, 'ut');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (18, 'voluptas');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (19, 'voluptates');
INSERT INTO `cat_conceptos_pago` (`id`, `concepto`) VALUES (20, 'eos');

DROP TABLE IF EXISTS `bitacora_pagos`;

CREATE TABLE `bitacora_pagos` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `concepto_id` int(11) NOT NULL COMMENT 'Se elegirá una opción del catalogo de conceptos de pago',
  `cantidad` decimal(10,2) NOT NULL,
  `autorizado_por` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_bitacora_pagos_presupuesto` (`no_presupuesto`),
  KEY `fk_bitacora_pagos` (`concepto_id`),
  CONSTRAINT `fk_bitacora_pagos` FOREIGN KEY (`concepto_id`) REFERENCES `cat_conceptos_pago` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_bitacora_pagos_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Cada pago que se agregue en un número de presupuesto va a descontar del campo ''cantidad'' en la tabla presupuesto de ese registro. En caso de que no se tenga dinero suficiente se debe autorizar el pago.';

INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (81, '1976-10-10 03:03:11', '156', 1, '0.00', 'Kattie Stiedemann', 'Sunt occaecati debitis repudiandae facere dolore id repellat repudiandae. Omnis dolores alias fugiat reprehenderit facere. Eos modi harum optio.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (82, '2008-06-19 18:54:00', '164', 2, '30268303.17', 'Dr. Norris Gusikowski II', 'Pariatur ipsam saepe nemo officia nostrum nostrum. Facere temporibus ea dolorem consequatur possimus aut fugiat. Quia vitae aspernatur assumenda beatae et.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (83, '1986-06-24 09:47:28', '174', 3, '122.43', 'Mikel Kling PhD', 'Esse sequi corporis aliquam nulla provident vel. Dicta in sed soluta similique expedita. Velit eaque rerum qui voluptatem et odio soluta. Ipsum rem voluptatem reprehenderit sequi nobis ut itaque.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (84, '1979-02-07 04:12:02', '235', 4, '572.34', 'Rosalind Blanda', 'Id eligendi necessitatibus quia neque consequatur non. Optio quia quia rerum ut culpa voluptate. Ducimus dolore atque et perspiciatis minima eligendi rerum.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (85, '1986-10-24 11:47:08', '243', 5, '296625.71', 'Ms. Georgette Cummerata DVM', 'Libero incidunt delectus illo qui dolor et enim voluptatum. Et et reiciendis non qui tempora. Ut ut voluptatem accusantium fugit consequuntur et.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (86, '2014-12-05 10:33:02', '283', 6, '353.34', 'Kurt O Reilly', 'Quae vero voluptas similique rerum atque consequatur et. Omnis repellat adipisci nobis quis maxime commodi harum. Et delectus qui impedit expedita.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (87, '1989-04-23 21:12:00', '430', 7, '33.35', 'Esperanza Sipes', 'Perferendis eligendi voluptate aut quos labore. Deserunt est ut dolor deserunt ad velit eveniet. Repellat est aliquid illo amet. Amet ut nostrum quaerat quia eius.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (88, '2018-07-27 00:04:35', '437', 8, '95692.81', 'Miss Desiree Sauer I', 'Veniam porro id corrupti iste. Aut nihil adipisci est et. Veritatis natus in modi ab sit reiciendis. Quis necessitatibus quos itaque sint fuga alias fugit.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (89, '2002-02-26 07:28:33', '510', 9, '0.00', 'Laverna Braun', 'Ratione voluptate dolorem sint sit. Quaerat non perferendis facilis odit. Animi quasi esse facilis nihil tenetur ab fugiat.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (90, '2005-03-12 07:14:22', '636', 10, '1245170.51', 'Santino Turcotte', 'Esse et ducimus et repellendus sit a qui. Quos quam sed at non repellendus qui dolor. Ad qui dicta beatae similique facere.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (91, '2022-09-22 22:04:30', '662', 11, '2150.83', 'Prof. Johnny Eichmann V', 'Non aperiam qui molestiae. Et odit et fugit. Recusandae libero et distinctio et.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (92, '1999-09-04 04:07:07', '673', 12, '58559.70', 'Miss Annabelle Stroman IV', 'Tempora quia id eos ut enim nesciunt ratione. Minima ex eum quia. Sequi rerum et sunt hic quaerat asperiores optio. Ea et quia quia repudiandae repudiandae repellat ut.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (93, '1992-10-25 21:11:17', '700', 13, '1253.26', 'Wiley Altenwerth', 'Numquam dolorem quidem deserunt quis quisquam est. Dolor modi consequatur id ad rerum alias. Doloremque quia officia voluptatem est odio.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (94, '2016-08-19 10:33:07', '761', 14, '85705.91', 'Dr. Buck Mayert', 'Est quo dolorem animi aut dolorem animi hic expedita. Doloribus vero aperiam consequuntur. Aut ad qui et.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (95, '1989-12-14 16:04:03', '775', 15, '0.02', 'Godfrey Jakubowski', 'Voluptates consectetur neque quas est sit doloribus consequatur. Explicabo ducimus est quos consequatur repudiandae officia. Magni odio qui et et.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (96, '1999-12-10 13:31:52', '776', 16, '34.59', 'Dr. Johathan Reichel PhD', 'Voluptatem nihil saepe qui tempore quasi qui. Nulla in ratione vel dolorem ea.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (97, '2019-01-18 19:03:50', '844', 17, '2655488.12', 'Jarred Rice', 'Perspiciatis rerum excepturi molestiae. Dolore inventore in totam est porro dolorem in deleniti. Non molestias eveniet non sit.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (98, '2021-06-30 11:19:35', '877', 18, '99999999.99', 'Dr. Max Gulgowski', 'Quos quas dolores qui. Voluptatem quos reprehenderit aut quis. Exercitationem tenetur eum soluta aut nobis. Voluptas nulla est amet saepe itaque architecto voluptates.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (99, '2017-02-06 14:05:47', '910', 19, '2391.88', 'Ms. Meredith Gaylord IV', 'Ut ipsam et consequuntur aspernatur sapiente quia autem natus. Omnis sapiente et neque. Beatae omnis reprehenderit totam quaerat qui iste. Ut ex eius distinctio maiores.');
INSERT INTO `bitacora_pagos` (`id`, `fecha`, `no_presupuesto`, `concepto_id`, `cantidad`, `autorizado_por`, `observaciones`) VALUES (100, '1985-06-19 19:17:57', '998', 20, '453812.42', 'Yadira Powlowski MD', 'Impedit quia voluptatem consectetur eum deserunt. Nihil fuga molestiae accusantium deleniti eos. Soluta id expedita ab et. Quidem quas saepe qui quia.');


DROP TABLE IF EXISTS `desgloce_ppto`;

CREATE TABLE `desgloce_ppto` (
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `concepto` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `pagado` tinyint(1) DEFAULT NULL,
  KEY `fk_desgloce_ppto_presupuesto` (`no_presupuesto`),
  CONSTRAINT `fk_desgloce_ppto_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='La sumatoria de todas las cantidades relacionadas a un número de presupuesto sera el monto total a pagar.';

INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('156', 'in', '131528.29', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('164', 'perferendis', '3588.61', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('174', 'adipisci', '157552.75', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('235', 'sed', '57726.08', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('243', 'odit', '0.63', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('283', 'consequatur', '251.18', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('430', 'inventore', '772.38', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('437', 'facilis', '0.00', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('510', 'a', '31.72', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('636', 'et', '2405344.20', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('662', 'aliquid', '2.04', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('673', 'dolorum', '3.17', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('700', 'iusto', '630000.00', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('761', 'porro', '19062892.40', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('775', 'atque', '0.61', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('776', 'non', '559690.20', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('844', 'odit', '50701.52', 1);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('877', 'architecto', '39376.17', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('910', 'et', '219271.17', 0);
INSERT INTO `desgloce_ppto` (`no_presupuesto`, `concepto`, `cantidad`, `pagado`) VALUES ('998', 'ullam', '1.37', 1);

DROP TABLE IF EXISTS `escritura`;

CREATE TABLE `escritura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_escritura` int(10) unsigned NOT NULL,
  `bis` tinyint(1) DEFAULT 0,
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `volumen` int(11) NOT NULL,
  `fecha` date NOT NULL COMMENT 'Fecha de Escritura',
  `no_expediente` int(11) NOT NULL COMMENT 'Numero de expediente del sistema de jurídico',
  `sr` tinyint(1) DEFAULT NULL COMMENT 'Indicador que significa si el tramite se ingresa en Registro Público, Sólo de control no es necesario mostrar en la consulta en solo lectura',
  `clave_catastral` int(11) NOT NULL,
  `infonavit` int(11) DEFAULT NULL COMMENT 'Numero de credito de infonavit',
  `entrega_testimonio` date DEFAULT NULL COMMENT 'Deben estar cubiertos todos los pagos para entregarlo, solo el admin puede autorizar con adeudo.',
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha_vence` date DEFAULT NULL COMMENT '60 días hábiles después de la fecha de esccritura',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_escritura_no_escritura` (`no_escritura`),
  UNIQUE KEY `id` (`no_escritura`,`bis`),
  UNIQUE KEY `unq_escritura_bis` (`bis`),
  KEY `fk_escritura_presupuesto` (`no_presupuesto`),
  CONSTRAINT `fk_escritura_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Eva puede editar, agregar y consultar todos los datos de la tabla.\nMartin y Paulina pueden agregar y modificar campos hasta ''no_expediente'', puede visualizar el resto.\nLos demás pueden ver todos los campos, menos ''mes_de_pago'' y ''observaciones''.';

INSERT INTO `escritura` (`id`, `no_escritura`, `bis`, `no_presupuesto`, `volumen`, `fecha`, `no_expediente`, `sr`, `clave_catastral`, `infonavit`, `entrega_testimonio`, `observaciones`, `fecha_vence`) VALUES (21, 152942070, 0, '156', 17, '1979-11-28', 609, 4, 702, 765, '1991-03-28', 'Est distinctio nisi nam eum. Quaerat officiis error aut quidem aut rem.\nPerferendis qui saepe sed voluptas similique sint. Sed itaque debitis aliquam et. Aut quibusdam consectetur aperiam sed.', '1998-12-31');
INSERT INTO `escritura` (`id`, `no_escritura`, `bis`, `no_presupuesto`, `volumen`, `fecha`, `no_expediente`, `sr`, `clave_catastral`, `infonavit`, `entrega_testimonio`, `observaciones`, `fecha_vence`) VALUES (25, 46096, 1, '243', 45, '1971-11-03', 361, 0, 597, 923, '2020-05-08', 'Minus omnis perspiciatis minima ut qui. Totam assumenda voluptatem accusantium. Inventore reiciendis ipsam deserunt voluptatibus ea. Possimus qui quod sapiente et laudantium corporis.', '2000-11-12');

DROP TABLE IF EXISTS `catastro_calificacion`;

CREATE TABLE `catastro_calificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vencimiento_td` tinyint(1) DEFAULT NULL COMMENT 'Alerta del vencimiento del traslado de dominio',
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `escritura_id` int(11) DEFAULT NULL,
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cat_rev` enum('si','en tramite','correccion') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_catastro_calificacion` (`escritura_id`),
  KEY `fk_catastro_calificacion_presupuesto` (`no_presupuesto`),
  CONSTRAINT `fk_catastro_calificacion` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_catastro_calificacion_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `catastro_calificacion` (`id`, `vencimiento_td`, `no_presupuesto`, `escritura_id`, `observaciones`, `cat_rev`) VALUES (1, 9, '156', 21, 'Odit aut nihil qui quas qui reprehenderit. Vitae delectus iure sint sint quae repellat. Eum recusandae odio magnam est iure. Nostrum asperiores quisquam voluptas repudiandae magni qui atque sed.', 'si');
INSERT INTO `catastro_calificacion` (`id`, `vencimiento_td`, `no_presupuesto`, `escritura_id`, `observaciones`, `cat_rev`) VALUES (2, 6, '164', 25, 'Aut sed aut rerum tempora quia earum. Exercitationem dolor accusantium distinctio commodi. Ut est saepe sequi sit dolores.', 'si');

DROP TABLE IF EXISTS `catastro_td`;

CREATE TABLE `catastro_td` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `escritura_id` int(11) NOT NULL,
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cat_terminado` enum('si','en tramite','correccion') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_catastro_td_escritura` (`escritura_id`),
  CONSTRAINT `fk_catastro_td_escritura` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `catastro_td` (`id`, `escritura_id`, `observaciones`, `cat_terminado`) VALUES (1, 21, 'Assumenda illo nobis commodi cum. Ut consequatur nobis quia a facere nisi perferendis. Consectetur minus illo maiores ullam molestiae repudiandae repellendus.', 'si');
INSERT INTO `catastro_td` (`id`, `escritura_id`, `observaciones`, `cat_terminado`) VALUES (2, 25, 'Velit consectetur molestias voluptatem. Earum hic velit inventore aliquam. Vitae asperiores consequatur qui odio.', 'correccion');

DROP TABLE IF EXISTS `direccion_notarias_seguimiento_juicios`;

CREATE TABLE `direccion_notarias_seguimiento_juicios` (
  `id` int(11) NOT NULL,
  `no_oficio_escritura` int(11) DEFAULT NULL,
  `fecha_envio_escritura` date DEFAULT NULL,
  `fecha_solicitud_busqueda_testa_dircc` date DEFAULT NULL,
  `fecha_solicitud_busqueda_testa_rpp` date DEFAULT NULL,
  `fecha_publicacion_boletin` date DEFAULT NULL,
  `fecha_publicacion_periodico` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_direccion_notarias_seguimiento_juicios` FOREIGN KEY (`id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `direccion_notarias_seguimiento_juicios` (`id`, `no_oficio_escritura`, `fecha_envio_escritura`, `fecha_solicitud_busqueda_testa_dircc`, `fecha_solicitud_busqueda_testa_rpp`, `fecha_publicacion_boletin`, `fecha_publicacion_periodico`) VALUES (21, 38459576, '1995-11-26', '2007-08-06', '1987-03-11', '1981-08-01', '2000-12-29');
INSERT INTO `direccion_notarias_seguimiento_juicios` (`id`, `no_oficio_escritura`, `fecha_envio_escritura`, `fecha_solicitud_busqueda_testa_dircc`, `fecha_solicitud_busqueda_testa_rpp`, `fecha_publicacion_boletin`, `fecha_publicacion_periodico`) VALUES (25, 633786591, '2004-03-09', '1989-08-10', '2016-06-11', '2006-07-09', '1984-05-08');

DROP TABLE IF EXISTS `facturas`;

CREATE TABLE `facturas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `no_factura` int(11) NOT NULL,
  `escritura_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_facturas_no_presupuesto` (`no_presupuesto`),
  KEY `fk_facturas_escritura` (`escritura_id`),
  CONSTRAINT `fk_facturas_escritura` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (1, '156', 7475, 21);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (2, '164', 978713, 25);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (3, '174', 7, 21);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (4, '235', 33, 25);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (5, '243', 52, 21);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (6, '283', 965, 25);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (7, '430', 9372938, 21);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (8, '437', 625739, 25);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (9, '510', 67284265, 21);
INSERT INTO `facturas` (`id`, `no_presupuesto`, `no_factura`, `escritura_id`) VALUES (10, '636', 91, 25);

DROP TABLE IF EXISTS `juridico`;

CREATE TABLE `juridico` (
  `id` int(11) NOT NULL,
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
  `numeracion_folios` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
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
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_juridico_escritura` FOREIGN KEY (`id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `juridico` (`id`, `contrato_en_extracto`, `firmas_en_extracto`, `pendientes`, `no_paso`, `otorgamiento`, `firma`, `autorizacion`, `fecha_aviso_renap`, `fecha_envio_dircc`, `uif_poder_irrevocable`, `fecha_aviso_reloat`, `fecha_aviso_dir_not_tpa`, `folios`, `numeracion_folios`, `folio_cancelado`, `fecha_minuta`, `fecha_apendice`, `minuta`, `apendice`, `fecha_entrega_juridico`, `fecha_aviso_portal`, `fecha_cierre_antilavado`, `isr_enajenacion`, `isr_adquisicion`, `iva`) VALUES (21, 9, 5, 1, 9, '1994-05-07', '1983-08-04', '1973-12-04', '1994-06-05', '1972-03-04', '1977-05-21', '1978-07-11', '2006-06-01', 324, '4', 8, '1999-07-06', '1998-02-02', 3, 3, '1988-01-01', '2017-11-30', '1996-06-03', 1, 3, 0);
INSERT INTO `juridico` (`id`, `contrato_en_extracto`, `firmas_en_extracto`, `pendientes`, `no_paso`, `otorgamiento`, `firma`, `autorizacion`, `fecha_aviso_renap`, `fecha_envio_dircc`, `uif_poder_irrevocable`, `fecha_aviso_reloat`, `fecha_aviso_dir_not_tpa`, `folios`, `numeracion_folios`, `folio_cancelado`, `fecha_minuta`, `fecha_apendice`, `minuta`, `apendice`, `fecha_entrega_juridico`, `fecha_aviso_portal`, `fecha_cierre_antilavado`, `isr_enajenacion`, `isr_adquisicion`, `iva`) VALUES (25, 9, 1, 5, 0, '1987-10-16', '1995-08-18', '1988-02-08', '2015-07-02', '1971-01-22', '2018-06-01', '1975-02-18', '2013-10-18', 23897038, '4', 1, '1999-11-12', '2015-08-27', 7, 7, '2004-07-28', '2001-08-20', '1980-11-03', 9, 5, 8);

DROP TABLE IF EXISTS `usuario`;

CREATE TABLE `usuario` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `contrasena` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rol` enum('admin','empleado','proyectista','armadores','otro') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Empleados: Martin, Eva y Paulina\nProyectistas:\n Alicia Felix\nMartha Soto\nAbraham Castro\nYesenia\nAna Luisa Rodriguez\nJuan Martin Ruiz\nRene Luna Araiza\nRene Luna Sugich\nGloria';

DROP TABLE IF EXISTS `rpp`;

CREATE TABLE `rpp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_presupuesto` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `escritura_id` int(11) DEFAULT NULL,
  `folio_rpp` int(11) DEFAULT NULL COMMENT 'Folio del pase a caja de Registro Público',
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `registrada` enum('en tramite','si','rechazado','reingreso','saldo insuficiente') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_rpp_folio_rpp` (`folio_rpp`),
  KEY `fk_rpp_presupuesto` (`no_presupuesto`),
  KEY `fk_rpp_escritura` (`escritura_id`),
  CONSTRAINT `fk_rpp_escritura` FOREIGN KEY (`escritura_id`) REFERENCES `escritura` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_rpp_presupuesto` FOREIGN KEY (`no_presupuesto`) REFERENCES `presupuesto` (`no_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `rpp` (`id`, `no_presupuesto`, `escritura_id`, `folio_rpp`, `observaciones`, `registrada`) VALUES (1, '156', 21, 0, 'Natus aut quis quaerat sed corporis. Quis est laboriosam excepturi incidunt vitae veniam et. Quam dicta libero placeat voluptas.', 'en tramite');
INSERT INTO `rpp` (`id`, `no_presupuesto`, `escritura_id`, `folio_rpp`, `observaciones`, `registrada`) VALUES (2, '164', 25, 662362675, 'Explicabo consectetur perferendis debitis est. Et aut a laudantium dolore praesentium voluptatem voluptas quis. Facilis nostrum vel suscipit dolorum fuga nihil porro qui.', 'rechazado');


DROP TABLE IF EXISTS `fechas_rpp`;

CREATE TABLE `fechas_rpp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_rpp` int(11) NOT NULL,
  `envio_rpp` date DEFAULT NULL COMMENT 'Fecha de Envio a Registro Público',
  `regreso_rpp` date DEFAULT NULL COMMENT 'Fecha de regreso de Registro Público',
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_fechas_catastro_0_id_cat_td_0` (`id_rpp`),
  CONSTRAINT `fk_fechas_catastro_td_0_rpp` FOREIGN KEY (`id_rpp`) REFERENCES `rpp` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `fechas_rpp` (`id`, `id_rpp`, `envio_rpp`, `regreso_rpp`, `observaciones`) VALUES (4, 1, '2011-05-04', '2011-10-13', 'Aut omnis aspernatur labore est corrupti atque. Dolorum ut occaecati consequatur repellat non. Nesciunt repellat aut odio magnam animi vitae.');
INSERT INTO `fechas_rpp` (`id`, `id_rpp`, `envio_rpp`, `regreso_rpp`, `observaciones`) VALUES (5, 2, '2008-09-15', '2011-12-04', 'Neque illum quisquam accusamus nisi molestias. Enim natus soluta est sed qui sequi soluta.');


DROP TABLE IF EXISTS `fechas_catastro_td`;

CREATE TABLE `fechas_catastro_td` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cat_td` int(11) NOT NULL,
  `cat_envio_td` date DEFAULT NULL COMMENT 'Fecha de envio de Traslado de dominio a Catastro',
  `cat_regreso_td` date DEFAULT NULL COMMENT 'Nombre del regreso de Traslado de dominio (cuando esta terminado)',
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unq_fechas_catastro_0_id_cat_td` (`id_cat_td`),
  CONSTRAINT `fk_fechas_catastro_0_catastro_td` FOREIGN KEY (`id_cat_td`) REFERENCES `catastro_td` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `fechas_catastro_td` (`id`, `id_cat_td`, `cat_envio_td`, `cat_regreso_td`, `observaciones`) VALUES (4, 1, '1993-03-22', '1991-01-29', 'Totam quasi suscipit mollitia necessitatibus. Cumque quo sit voluptates sint dolore aut. Consequatur eos illum ut aliquid eligendi voluptate. Iure repellat ut libero fugit qui.');
INSERT INTO `fechas_catastro_td` (`id`, `id_cat_td`, `cat_envio_td`, `cat_regreso_td`, `observaciones`) VALUES (5, 2, '1975-06-25', '1997-07-25', 'Velit temporibus dolores veritatis nobis. Qui qui est voluptas incidunt sed perspiciatis. Facilis iure nisi itaque repudiandae animi omnis nostrum deleniti.');

DROP TABLE IF EXISTS `aviso_definitivo`;

CREATE TABLE `aviso_definitivo` (
  `id` int(11) NOT NULL,
  `folio_rpp` int(11) DEFAULT NULL COMMENT 'Folio del pase a caja de Registro Público',
  `fecha_presentado` date DEFAULT NULL COMMENT 'Fecha de Ingreso en RPP',
  `fecha_salida` date DEFAULT NULL COMMENT 'Fecha de entregado por RPP',
  `fecha_vence` date DEFAULT NULL COMMENT 'Fecha de Vencimiento del aviso (90 dias naturales despues de fecha de presentacion en RPP)',
  PRIMARY KEY (`id`),
  KEY `fk_aviso_definitivo_rpp` (`folio_rpp`),
  CONSTRAINT `fk_aviso_definitivo_rpp` FOREIGN KEY (`folio_rpp`) REFERENCES `rpp` (`folio_rpp`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `aviso_definitivo` (`id`, `folio_rpp`, `fecha_presentado`, `fecha_salida`, `fecha_vence`) VALUES (21, 0, '1996-07-08', '1977-05-03', '2000-10-30');
INSERT INTO `aviso_definitivo` (`id`, `folio_rpp`, `fecha_presentado`, `fecha_salida`, `fecha_vence`) VALUES (25, 662362675, '1978-10-22', '1973-12-26', '1970-06-20');

DROP TABLE IF EXISTS `fechas_catastro_calif`;

CREATE TABLE `fechas_catastro_calif` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cat_calif` int(11) NOT NULL,
  `cat_envio_calif` date DEFAULT NULL COMMENT 'Fecha de envio de Traslado de dominio a Catastro para informacion',
  `cat_regreso_calif` date DEFAULT NULL COMMENT 'Fecha de regreso de Traslado de dominio a Catastro para informacion',
  `observaciones` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_fechas_catastro_catastro_calificacion` (`id_cat_calif`),
  CONSTRAINT `fk_fechas_catastro_catastro_calificacion` FOREIGN KEY (`id_cat_calif`) REFERENCES `catastro_calificacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `fechas_catastro_calif` (`id`, `id_cat_calif`, `cat_envio_calif`, `cat_regreso_calif`, `observaciones`) VALUES (1, 1, '1998-05-06', '1986-12-14', 'Dolore soluta id alias possimus itaque sint iusto. Quasi doloribus beatae molestiae mollitia accusamus reprehenderit. Voluptatem blanditiis et omnis rerum tempore voluptatem.');
INSERT INTO `fechas_catastro_calif` (`id`, `id_cat_calif`, `cat_envio_calif`, `cat_regreso_calif`, `observaciones`) VALUES (2, 2, '1970-06-26', '1972-04-22', 'Accusamus molestiae ea dolorem eum eos consequuntur sed. Repudiandae in beatae assumenda. Quia dolorum fugit occaecati et. Quasi possimus voluptates dicta adipisci qui cupiditate.');
INSERT INTO `fechas_catastro_calif` (`id`, `id_cat_calif`, `cat_envio_calif`, `cat_regreso_calif`, `observaciones`) VALUES (3, 1, '1998-09-18', '2005-10-13', 'Assumenda tempora necessitatibus voluptas pariatur. Excepturi dolorem porro accusamus illum quas aut quis sit. Voluptatem consequatur sapiente fuga beatae commodi.');
