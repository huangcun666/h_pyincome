-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test1
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_projects_member_other`
--

DROP TABLE IF EXISTS `t_projects_member_other`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_member_other` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `team_name` varchar(255) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `member_name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `remark` varchar(2550) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=448 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_member_other`
--

LOCK TABLES `t_projects_member_other` WRITE;
/*!40000 ALTER TABLE `t_projects_member_other` DISABLE KEYS */;
INSERT INTO `t_projects_member_other` VALUES (1,'外勤',204,'刘慧敏','2018-06-27 01:03:31',1181,NULL),(2,'外勤',204,'刘慧敏','2018-06-27 01:13:15',1188,NULL),(3,'外勤',204,'刘慧敏','2018-06-27 01:15:32',1161,NULL),(4,'外勤',204,'刘慧敏','2018-06-27 01:17:32',1193,NULL),(5,'外勤',204,'刘慧敏','2018-06-27 01:18:40',1172,NULL),(6,'外勤',204,'刘慧敏','2018-06-27 01:19:37',1202,NULL),(7,'外勤',204,'刘慧敏','2018-06-27 01:22:18',1183,NULL),(8,'外勤',204,'刘慧敏','2018-06-27 01:24:12',1211,NULL),(9,'外勤',204,'刘慧敏','2018-06-27 01:25:49',1182,NULL),(10,'外勤',204,'刘慧敏','2018-06-27 01:28:52',1196,NULL),(11,'外勤',206,'熊非儿','2018-06-27 01:29:56',1103,NULL),(12,'外勤',206,'熊非儿','2018-06-27 01:30:48',1105,NULL),(13,'外勤',206,'熊非儿','2018-06-27 01:31:44',1106,NULL),(14,'外勤',206,'熊非儿','2018-06-27 01:32:45',1107,NULL),(15,'外勤',206,'熊非儿','2018-06-27 01:33:43',1111,NULL),(16,'外勤',206,'熊非儿','2018-06-27 01:35:24',1110,NULL),(17,'外勤',204,'刘慧敏','2018-06-27 01:37:34',1162,NULL),(18,'外勤',204,'刘慧敏','2018-06-27 01:38:58',1164,NULL),(19,'外勤',206,'熊非儿','2018-06-27 01:41:57',1108,NULL),(20,'外勤',206,'熊非儿','2018-06-27 01:52:29',1109,NULL),(21,'外勤',204,'刘慧敏','2018-06-27 01:53:35',1201,NULL),(22,'外勤',107,'冉小凤','2018-06-27 03:43:24',492,NULL),(23,'外勤',204,'刘慧敏','2018-06-27 05:52:06',1166,NULL),(24,'外勤',204,'刘慧敏','2018-06-27 06:10:53',1165,NULL),(25,'外勤',256,'张美鹃','2018-06-27 07:49:20',894,NULL),(26,'外勤',256,'张美鹃','2018-06-27 07:50:43',1157,NULL),(27,'外勤',138,'王坚','2018-06-27 09:03:48',1353,NULL),(28,'外勤',151,'李静','2018-06-27 09:06:46',1374,NULL),(29,'外勤',106,'陈小银','2018-06-27 09:27:35',1187,NULL),(30,'外勤',138,'王坚','2018-06-27 09:31:38',1300,NULL),(31,'外勤',155,'岑美凤','2018-06-28 00:32:16',819,NULL),(32,'外勤',155,'岑美凤','2018-06-28 00:40:07',1094,NULL),(33,'外勤',155,'岑美凤','2018-06-28 00:52:16',341,NULL),(34,'外勤',155,'岑美凤','2018-06-28 00:55:31',486,NULL),(35,'外勤',155,'岑美凤','2018-06-28 01:03:49',450,NULL),(36,'外勤',155,'岑美凤','2018-06-28 09:30:07',1046,NULL),(37,'外勤',155,'岑美凤','2018-06-28 10:00:47',972,NULL),(38,'外勤',155,'岑美凤','2018-06-29 00:33:17',1125,NULL),(39,'外勤',155,'岑美凤','2018-06-29 00:46:34',271,NULL),(40,'外勤',155,'岑美凤','2018-06-29 00:48:34',522,NULL),(41,'外勤',116,'陈太智','2018-06-29 01:13:19',1286,NULL),(42,'外勤',155,'岑美凤','2018-06-29 01:37:55',1330,NULL),(43,'外勤',155,'岑美凤','2018-06-29 03:39:53',1299,NULL),(44,'外勤',155,'岑美凤','2018-06-29 05:54:01',832,NULL),(45,'外勤',155,'岑美凤','2018-06-29 06:28:12',1074,NULL),(46,'外勤',155,'岑美凤','2018-06-29 08:58:13',801,NULL),(47,'外勤',155,'岑美凤','2018-06-29 09:01:45',1266,NULL),(48,'外勤',155,'岑美凤','2018-06-29 09:08:58',1253,NULL),(49,'外勤',155,'岑美凤','2018-06-29 09:12:44',1257,NULL),(50,'外勤',155,'岑美凤','2018-06-29 09:15:46',1119,NULL),(51,'外勤',155,'岑美凤','2018-06-29 09:19:05',1265,NULL),(52,'外勤',155,'岑美凤','2018-06-29 09:21:20',1232,NULL),(53,'外勤',155,'岑美凤','2018-06-29 09:23:35',1175,NULL),(54,'外勤',155,'岑美凤','2018-06-29 09:24:15',1263,NULL),(55,'外勤',155,'岑美凤','2018-06-29 09:27:16',1256,NULL),(56,'外勤',155,'岑美凤','2018-06-29 09:32:59',1259,NULL),(57,'外勤',155,'岑美凤','2018-06-29 09:37:10',1261,NULL),(58,'外勤',155,'岑美凤','2018-06-29 09:48:48',839,NULL),(59,'外勤',123,'何家辉','2018-06-29 10:17:30',839,NULL),(60,'外勤',155,'岑美凤','2018-06-29 10:20:25',848,NULL),(61,'外勤',155,'岑美凤','2018-07-02 09:25:05',1138,NULL),(62,'外勤',155,'岑美凤','2018-07-03 01:30:21',1216,NULL),(63,'外勤',155,'岑美凤','2018-07-03 01:37:28',1283,NULL),(64,'外勤',155,'岑美凤','2018-07-03 09:17:42',1147,NULL),(65,'外勤',155,'岑美凤','2018-07-03 09:29:44',447,NULL),(66,'外勤',155,'岑美凤','2018-07-03 10:49:34',1229,NULL),(67,'外勤',139,'陈勇极','2018-07-04 01:51:44',1147,NULL),(68,'外勤',155,'岑美凤','2018-07-04 05:51:59',1254,NULL),(69,'外勤',155,'岑美凤','2018-07-04 05:52:00',678,NULL),(70,'外勤',155,'岑美凤','2018-07-04 05:53:53',1140,NULL),(71,'外勤',155,'岑美凤','2018-07-04 06:00:31',1255,NULL),(72,'外勤',155,'岑美凤','2018-07-04 06:04:56',1292,NULL),(73,'外勤',155,'岑美凤','2018-07-04 08:39:40',1327,NULL),(74,'外勤',155,'岑美凤','2018-07-04 08:47:46',1336,NULL),(75,'外勤',155,'岑美凤','2018-07-04 08:57:28',1314,NULL),(76,'外勤',155,'岑美凤','2018-07-04 08:59:16',1332,NULL),(77,'外勤',151,'李静','2018-07-05 02:17:34',819,NULL),(78,'外勤',155,'岑美凤','2018-07-05 02:17:39',965,NULL),(79,'外勤',155,'岑美凤','2018-07-05 03:37:29',1460,NULL),(80,'外勤',155,'岑美凤','2018-07-05 06:00:47',1355,NULL),(81,'外勤',155,'岑美凤','2018-07-05 06:10:34',1364,NULL),(82,'外勤',155,'岑美凤','2018-07-05 06:20:47',1323,NULL),(83,'外勤',155,'岑美凤','2018-07-05 06:27:54',1333,NULL),(84,'外勤',155,'岑美凤','2018-07-05 06:31:09',1258,NULL),(85,'外勤',155,'岑美凤','2018-07-05 06:40:27',1305,NULL),(86,'外勤',155,'岑美凤','2018-07-05 08:06:43',1245,NULL),(87,'外勤',155,'岑美凤','2018-07-06 04:06:44',643,NULL),(88,'外勤',155,'岑美凤','2018-07-06 04:08:58',1154,NULL),(89,'外勤',155,'岑美凤','2018-07-06 05:54:59',1295,NULL),(90,'外勤',155,'岑美凤','2018-07-06 05:59:54',1294,NULL),(91,'外勤',155,'岑美凤','2018-07-06 06:51:18',1308,NULL),(92,'外勤',155,'岑美凤','2018-07-06 06:53:12',1163,NULL),(93,'外勤',155,'岑美凤','2018-07-06 07:04:31',1130,NULL),(94,'外勤',94,'冯恒冠','2018-07-06 08:58:56',1130,NULL),(95,'外勤',155,'岑美凤','2018-07-06 09:03:21',1496,NULL),(96,'外勤',155,'岑美凤','2018-07-06 09:12:55',1497,NULL),(97,'外勤',155,'岑美凤','2018-07-06 09:17:43',1498,NULL),(98,'外勤',155,'岑美凤','2018-07-06 09:29:55',1375,NULL),(99,'外勤',155,'岑美凤','2018-07-06 09:38:20',1404,NULL),(100,'外勤',155,'岑美凤','2018-07-09 02:08:14',1096,NULL),(101,'外勤',155,'岑美凤','2018-07-09 03:43:52',1346,NULL),(102,'外勤',186,'梁家欣','2018-07-09 06:30:55',631,NULL),(103,'外勤',151,'李静','2018-07-09 08:18:42',965,NULL),(104,'外勤',151,'李静','2018-07-09 09:57:23',927,NULL),(105,'外勤',155,'岑美凤','2018-07-09 10:14:19',1372,NULL),(106,'外勤',155,'岑美凤','2018-07-10 09:23:06',1190,NULL),(107,'外勤',155,'岑美凤','2018-07-10 09:25:24',1099,NULL),(108,'外勤',155,'岑美凤','2018-07-11 02:18:36',1290,NULL),(109,'外勤',155,'岑美凤','2018-07-11 02:24:13',1291,NULL),(110,'外勤',155,'岑美凤','2018-07-11 03:04:35',1475,NULL),(111,'外勤',155,'岑美凤','2018-07-11 08:00:37',1361,NULL),(112,'外勤',155,'岑美凤','2018-07-11 09:01:34',1408,NULL),(113,'外勤',155,'岑美凤','2018-07-11 09:05:37',1461,NULL),(114,'外勤',155,'岑美凤','2018-07-11 09:08:07',1454,NULL),(115,'外勤',155,'岑美凤','2018-07-11 09:09:57',1433,NULL),(116,'外勤',155,'岑美凤','2018-07-11 09:10:07',1451,NULL),(117,'外勤',155,'岑美凤','2018-07-11 09:12:34',1420,NULL),(118,'外勤',155,'岑美凤','2018-07-11 09:22:34',1443,NULL),(119,'外勤',155,'岑美凤','2018-07-11 09:40:06',1442,NULL),(120,'外勤',155,'岑美凤','2018-07-11 09:54:05',1456,NULL),(121,'外勤',155,'岑美凤','2018-07-11 09:57:39',1376,NULL),(122,'外勤',155,'岑美凤','2018-07-12 01:27:11',1453,NULL),(123,'外勤',95,'何诗明','2018-07-12 01:57:07',447,NULL),(124,'外勤',155,'岑美凤','2018-07-12 05:46:42',1549,NULL),(125,'外勤',155,'岑美凤','2018-07-12 06:20:02',1159,NULL),(126,'外勤',155,'岑美凤','2018-07-12 06:26:29',1368,NULL),(127,'外勤',193,'陈转妹','2018-07-12 06:54:24',1315,NULL),(128,'外勤',155,'岑美凤','2018-07-12 10:20:03',1502,NULL),(129,'外勤',155,'岑美凤','2018-07-12 10:22:06',1505,NULL),(130,'外勤',155,'岑美凤','2018-07-12 10:23:22',1506,NULL),(131,'外勤',155,'岑美凤','2018-07-12 10:24:13',1507,NULL),(132,'外勤',155,'岑美凤','2018-07-13 01:16:54',1113,NULL),(133,'外勤',155,'岑美凤','2018-07-13 02:30:40',1331,NULL),(134,'外勤',194,'彭苏勉','2018-07-13 02:33:33',1464,NULL),(135,'外勤',175,'林艳容','2018-07-13 02:33:47',1331,NULL),(136,'外勤',155,'岑美凤','2018-07-13 04:05:34',1280,NULL),(137,'外勤',155,'岑美凤','2018-07-13 04:12:32',1560,NULL),(138,'外勤',155,'岑美凤','2018-07-13 05:36:16',1469,NULL),(139,'外勤',155,'岑美凤','2018-07-13 06:03:23',1340,NULL),(140,'外勤',155,'岑美凤','2018-07-13 06:16:18',1391,NULL),(141,'外勤',155,'岑美凤','2018-07-13 06:32:05',1279,NULL),(142,'外勤',155,'岑美凤','2018-07-13 06:55:18',1424,NULL),(143,'外勤',155,'岑美凤','2018-07-13 06:58:15',1474,NULL),(144,'外勤',191,'梁子幸','2018-07-13 07:18:31',1250,NULL),(145,'外勤',155,'岑美凤','2018-07-13 07:21:43',1269,NULL),(146,'外勤',155,'岑美凤','2018-07-13 07:32:14',1150,NULL),(147,'外勤',155,'岑美凤','2018-07-13 07:37:31',1435,NULL),(148,'外勤',155,'岑美凤','2018-07-13 07:40:53',1434,NULL),(149,'外勤',155,'岑美凤','2018-07-13 08:05:58',1195,NULL),(150,'外勤',155,'岑美凤','2018-07-13 08:08:58',1176,NULL),(151,'外勤',155,'岑美凤','2018-07-13 08:23:08',1445,NULL),(152,'外勤',155,'岑美凤','2018-07-13 08:29:11',1421,NULL),(153,'外勤',155,'岑美凤','2018-07-13 08:34:18',1462,NULL),(154,'外勤',155,'岑美凤','2018-07-13 08:38:53',1425,NULL),(155,'外勤',155,'岑美凤','2018-07-13 08:42:53',1411,NULL),(156,'外勤',155,'岑美凤','2018-07-16 03:45:05',1458,NULL),(157,'外勤',139,'陈勇极','2018-07-16 07:17:56',0,NULL),(158,'外勤',155,'岑美凤','2018-07-16 07:43:04',1426,NULL),(159,'外勤',121,'赵松筑','2018-07-16 08:33:22',1195,NULL),(160,'外勤',155,'岑美凤','2018-07-16 08:43:57',1317,NULL),(161,'外勤',155,'岑美凤','2018-07-16 09:24:05',1459,NULL),(162,'外勤',155,'岑美凤','2018-07-16 09:28:05',1448,NULL),(163,'外勤',155,'岑美凤','2018-07-17 01:25:36',1428,NULL),(164,'外勤',155,'岑美凤','2018-07-17 02:44:05',992,NULL),(165,'外勤',155,'岑美凤','2018-07-17 08:07:26',1008,NULL),(166,'外勤',155,'岑美凤','2018-07-17 08:25:42',981,NULL),(167,'外勤',155,'岑美凤','2018-07-17 08:31:06',1423,NULL),(168,'外勤',155,'岑美凤','2018-07-17 08:33:51',1446,NULL),(169,'外勤',155,'岑美凤','2018-07-17 08:43:33',1422,NULL),(170,'外勤',155,'岑美凤','2018-07-17 08:56:37',555,NULL),(171,'外勤',155,'岑美凤','2018-07-17 09:06:23',1508,NULL),(172,'外勤',155,'岑美凤','2018-07-17 10:00:10',1592,NULL),(173,'外勤',155,'岑美凤','2018-07-17 10:02:36',564,NULL),(174,'外勤',151,'李静','2018-07-18 03:46:53',1075,NULL),(175,'外勤',155,'岑美凤','2018-07-18 07:41:55',1533,NULL),(176,'外勤',155,'岑美凤','2018-07-18 07:51:02',1555,NULL),(177,'外勤',155,'岑美凤','2018-07-18 07:56:35',1485,NULL),(178,'外勤',155,'岑美凤','2018-07-18 08:19:01',1546,NULL),(179,'外勤',155,'岑美凤','2018-07-18 08:21:50',1517,NULL),(180,'外勤',155,'岑美凤','2018-07-18 08:24:59',1540,NULL),(181,'外勤',155,'岑美凤','2018-07-18 08:28:14',1558,NULL),(182,'外勤',155,'岑美凤','2018-07-18 09:04:33',1381,NULL),(183,'外勤',155,'岑美凤','2018-07-18 09:07:54',1447,NULL),(184,'外勤',155,'岑美凤','2018-07-18 09:26:48',1002,NULL),(185,'外勤',155,'岑美凤','2018-07-18 10:19:56',1272,NULL),(186,'外勤',155,'岑美凤','2018-07-19 07:22:16',1521,NULL),(187,'外勤',155,'岑美凤','2018-07-19 07:33:59',1273,NULL),(188,'外勤',155,'岑美凤','2018-07-19 07:36:17',377,NULL),(189,'外勤',155,'岑美凤','2018-07-19 08:11:25',1548,NULL),(190,'外勤',155,'岑美凤','2018-07-19 09:24:44',1557,NULL),(191,'外勤',155,'岑美凤','2018-07-19 09:42:46',1556,NULL),(192,'外勤',155,'岑美凤','2018-07-19 10:44:28',1145,NULL),(193,'外勤',155,'岑美凤','2018-07-19 11:38:26',1302,NULL),(194,'外勤',155,'岑美凤','2018-07-20 02:12:18',1577,NULL),(195,'外勤',155,'岑美凤','2018-07-20 02:15:50',1377,NULL),(196,'外勤',141,'刘建光','2018-07-20 02:28:13',1049,NULL),(197,'外勤',155,'岑美凤','2018-07-20 03:14:21',1529,NULL),(198,'外勤',155,'岑美凤','2018-07-20 06:04:13',1667,NULL),(199,'外勤',155,'岑美凤','2018-07-20 06:15:58',1522,NULL),(200,'外勤',155,'岑美凤','2018-07-20 06:46:55',1578,NULL),(201,'外勤',155,'岑美凤','2018-07-20 07:11:33',1369,NULL),(202,'外勤',155,'岑美凤','2018-07-20 08:32:16',1429,NULL),(203,'外勤',155,'岑美凤','2018-07-20 08:55:24',477,NULL),(204,'外勤',155,'岑美凤','2018-07-20 09:07:29',1570,NULL),(205,'外勤',155,'岑美凤','2018-07-20 09:09:24',1576,NULL),(206,'外勤',155,'岑美凤','2018-07-20 09:14:51',1591,NULL),(207,'外勤',155,'岑美凤','2018-07-20 09:16:14',1286,NULL),(208,'外勤',155,'岑美凤','2018-07-20 09:29:41',1563,NULL),(209,'外勤',155,'岑美凤','2018-07-20 09:54:19',1565,NULL),(210,'外勤',107,'冉小凤','2018-07-23 01:36:28',0,NULL),(211,'外勤',155,'岑美凤','2018-07-23 02:29:51',1662,NULL),(212,'外勤',155,'岑美凤','2018-07-23 02:45:33',568,NULL),(213,'外勤',151,'李静','2018-07-23 05:41:37',1286,NULL),(214,'外勤',151,'李静','2018-07-23 05:49:50',1285,NULL),(215,'外勤',151,'李静','2018-07-23 06:08:34',555,NULL),(216,'外勤',151,'李静','2018-07-23 06:19:01',1145,NULL),(217,'外勤',141,'刘建光','2018-07-23 07:50:17',1520,NULL),(218,'外勤',155,'岑美凤','2018-07-23 09:03:47',1468,NULL),(219,'外勤',155,'岑美凤','2018-07-23 09:27:39',1567,NULL),(220,'外勤',107,'冉小凤','2018-07-24 01:36:46',1088,NULL),(221,'外勤',151,'李静','2018-07-24 01:50:32',477,NULL),(222,'外勤',155,'岑美凤','2018-07-24 02:57:26',1484,NULL),(223,'外勤',155,'岑美凤','2018-07-24 03:04:29',1574,NULL),(224,'外勤',155,'岑美凤','2018-07-24 03:09:18',1627,NULL),(225,'外勤',155,'岑美凤','2018-07-24 03:25:46',1598,NULL),(226,'外勤',193,'陈转妹','2018-07-24 03:58:05',1500,NULL),(227,'外勤',155,'岑美凤','2018-07-24 04:01:33',917,NULL),(228,'外勤',155,'岑美凤','2018-07-24 05:12:56',1635,NULL),(229,'外勤',155,'岑美凤','2018-07-24 05:17:40',1603,NULL),(230,'外勤',155,'岑美凤','2018-07-24 06:51:51',1612,NULL),(231,'外勤',155,'岑美凤','2018-07-24 07:49:16',1595,NULL),(232,'外勤',155,'岑美凤','2018-07-24 07:51:06',1470,NULL),(233,'外勤',155,'岑美凤','2018-07-24 08:15:54',1711,NULL),(234,'外勤',155,'岑美凤','2018-07-24 08:25:35',1482,NULL),(235,'外勤',155,'岑美凤','2018-07-24 08:29:19',980,NULL),(236,'外勤',155,'岑美凤','2018-07-25 01:22:26',547,NULL),(237,'外勤',155,'岑美凤','2018-07-25 02:35:54',1597,NULL),(238,'外勤',155,'岑美凤','2018-07-25 03:55:19',1636,NULL),(239,'外勤',155,'岑美凤','2018-07-25 04:03:02',1697,NULL),(240,'外勤',155,'岑美凤','2018-07-25 04:20:02',1686,NULL),(241,'外勤',155,'岑美凤','2018-07-25 06:07:15',1677,NULL),(242,'外勤',155,'岑美凤','2018-07-25 06:14:40',1698,NULL),(243,'外勤',155,'岑美凤','2018-07-25 07:18:02',1192,NULL),(244,'外勤',155,'岑美凤','2018-07-25 07:54:00',1081,NULL),(245,'外勤',155,'岑美凤','2018-07-25 08:09:31',1306,NULL),(246,'外勤',155,'岑美凤','2018-07-25 08:17:31',1189,NULL),(247,'外勤',155,'岑美凤','2018-07-25 08:27:16',1240,NULL),(248,'外勤',155,'岑美凤','2018-07-25 08:51:55',1734,NULL),(249,'外勤',155,'岑美凤','2018-07-26 02:12:38',1427,NULL),(250,'外勤',155,'岑美凤','2018-07-26 03:41:00',1665,NULL),(251,'外勤',155,'岑美凤','2018-07-26 03:42:52',1695,NULL),(252,'外勤',155,'岑美凤','2018-07-26 03:44:51',1625,NULL),(253,'外勤',155,'岑美凤','2018-07-26 03:47:27',1664,NULL),(254,'外勤',155,'岑美凤','2018-07-26 04:28:46',1631,NULL),(255,'外勤',155,'岑美凤','2018-07-26 05:44:12',1754,NULL),(256,'外勤',155,'岑美凤','2018-07-26 06:06:01',1738,NULL),(257,'外勤',155,'岑美凤','2018-07-26 06:14:16',201,NULL),(258,'外勤',97,'庄培润','2018-07-26 09:43:25',1400,NULL),(259,'外勤',155,'岑美凤','2018-07-26 09:46:05',1707,NULL),(260,'外勤',155,'岑美凤','2018-07-26 09:47:32',1252,NULL),(261,'外勤',155,'岑美凤','2018-07-27 01:10:16',1803,NULL),(262,'外勤',155,'岑美凤','2018-07-27 01:29:03',1407,NULL),(263,'外勤',155,'岑美凤','2018-07-27 01:59:53',1531,NULL),(264,'外勤',155,'岑美凤','2018-07-27 02:21:01',1213,NULL),(265,'外勤',155,'岑美凤','2018-07-27 03:03:19',1523,NULL),(266,'外勤',155,'岑美凤','2018-07-27 03:41:40',1354,NULL),(267,'外勤',140,'莫诗域','2018-07-27 06:29:23',1093,NULL),(268,'外勤',155,'岑美凤','2018-07-27 08:01:35',1535,NULL),(269,'外勤',155,'岑美凤','2018-07-27 09:02:45',1463,NULL),(270,'外勤',155,'岑美凤','2018-07-30 01:36:04',1800,NULL),(271,'外勤',155,'岑美凤','2018-07-30 02:47:18',1538,NULL),(272,'外勤',155,'岑美凤','2018-07-30 04:04:42',1171,NULL),(273,'外勤',155,'岑美凤','2018-07-30 06:31:51',1542,NULL),(274,'外勤',155,'岑美凤','2018-07-30 07:38:26',1717,NULL),(275,'外勤',155,'岑美凤','2018-07-30 08:58:38',1831,NULL),(276,'外勤',155,'岑美凤','2018-07-31 01:26:00',1393,NULL),(277,'外勤',155,'岑美凤','2018-07-31 03:56:35',1390,NULL),(278,'外勤',155,'岑美凤','2018-07-31 03:59:38',1680,NULL),(279,'外勤',155,'岑美凤','2018-07-31 04:14:39',1668,NULL),(280,'外勤',155,'岑美凤','2018-07-31 04:46:41',1692,NULL),(281,'外勤',97,'庄培润','2018-07-31 05:58:30',1675,NULL),(282,'外勤',155,'岑美凤','2018-07-31 06:12:14',1534,NULL),(283,'外勤',155,'岑美凤','2018-07-31 06:15:30',1712,NULL),(284,'外勤',155,'岑美凤','2018-07-31 06:17:43',1658,NULL),(285,'外勤',155,'岑美凤','2018-07-31 06:19:52',1620,NULL),(286,'外勤',155,'岑美凤','2018-07-31 06:21:45',1663,NULL),(287,'外勤',155,'岑美凤','2018-07-31 06:24:10',1660,NULL),(288,'外勤',155,'岑美凤','2018-07-31 07:08:03',1757,NULL),(289,'外勤',155,'岑美凤','2018-07-31 07:15:50',1726,NULL),(290,'外勤',155,'岑美凤','2018-07-31 07:43:15',1716,NULL),(291,'外勤',155,'岑美凤','2018-07-31 07:45:51',1243,NULL),(292,'外勤',155,'岑美凤','2018-07-31 07:50:19',1116,NULL),(293,'外勤',155,'岑美凤','2018-07-31 08:07:14',1688,NULL),(294,'外勤',155,'岑美凤','2018-07-31 09:28:31',1672,NULL),(295,'外勤',214,'杨树香','2018-08-01 01:20:28',1716,NULL),(296,'外勤',155,'岑美凤','2018-08-01 02:17:14',1562,NULL),(297,'外勤',155,'岑美凤','2018-08-01 06:01:01',1493,NULL),(298,'外勤',155,'岑美凤','2018-08-01 07:03:10',1139,NULL),(299,'外勤',155,'岑美凤','2018-08-01 07:26:30',1756,NULL),(300,'外勤',155,'岑美凤','2018-08-01 07:29:37',1731,NULL),(301,'外勤',155,'岑美凤','2018-08-01 08:17:06',1808,NULL),(302,'外勤',155,'岑美凤','2018-08-01 08:26:48',1821,NULL),(303,'外勤',155,'岑美凤','2018-08-02 02:10:14',1750,NULL),(304,'外勤',155,'岑美凤','2018-08-02 04:11:17',1596,NULL),(305,'外勤',155,'岑美凤','2018-08-02 05:47:47',1859,NULL),(306,'外勤',155,'岑美凤','2018-08-02 06:17:53',1087,NULL),(307,'外勤',155,'岑美凤','2018-08-02 06:31:08',1392,NULL),(308,'外勤',155,'岑美凤','2018-08-02 06:41:39',1399,NULL),(309,'外勤',155,'岑美凤','2018-08-02 06:44:58',1889,NULL),(310,'外勤',155,'岑美凤','2018-08-02 07:47:01',1851,NULL),(311,'外勤',155,'岑美凤','2018-08-02 08:05:07',1852,NULL),(312,'外勤',155,'岑美凤','2018-08-02 08:17:16',1849,NULL),(313,'外勤',155,'岑美凤','2018-08-02 08:58:51',1785,NULL),(314,'外勤',155,'岑美凤','2018-08-03 01:48:14',1492,NULL),(315,'外勤',155,'岑美凤','2018-08-03 02:19:41',1653,NULL),(316,'外勤',155,'岑美凤','2018-08-03 02:56:07',1922,NULL),(317,'外勤',155,'岑美凤','2018-08-03 07:00:51',1406,NULL),(318,'外勤',121,'赵松筑','2018-08-03 08:33:22',0,NULL),(319,'外勤',155,'岑美凤','2018-08-06 04:05:30',580,NULL),(320,'外勤',155,'岑美凤','2018-08-06 08:35:50',1735,NULL),(321,'外勤',155,'岑美凤','2018-08-06 08:39:33',1804,NULL),(322,'外勤',155,'岑美凤','2018-08-07 01:41:02',1780,NULL),(323,'外勤',155,'岑美凤','2018-08-07 01:45:17',1935,NULL),(324,'外勤',155,'岑美凤','2018-08-07 04:05:53',1858,NULL),(325,'外勤',155,'岑美凤','2018-08-07 04:13:48',1357,NULL),(326,'外勤',155,'岑美凤','2018-08-07 06:50:18',1788,NULL),(327,'外勤',155,'岑美凤','2018-08-07 06:56:57',1767,NULL),(328,'外勤',155,'岑美凤','2018-08-07 06:59:55',1787,NULL),(329,'外勤',155,'岑美凤','2018-08-07 07:11:44',1860,NULL),(330,'外勤',155,'岑美凤','2018-08-07 07:19:31',1890,NULL),(331,'外勤',155,'岑美凤','2018-08-07 07:30:43',1955,NULL),(332,'外勤',155,'岑美凤','2018-08-07 09:05:44',1613,NULL),(333,'外勤',155,'岑美凤','2018-08-07 09:11:03',1481,NULL),(334,'外勤',155,'岑美凤','2018-08-08 01:11:45',1891,NULL),(335,'外勤',155,'岑美凤','2018-08-08 01:54:00',1893,NULL),(336,'外勤',155,'岑美凤','2018-08-08 03:05:33',1880,NULL),(337,'外勤',155,'岑美凤','2018-08-08 03:28:14',1951,NULL),(338,'外勤',155,'岑美凤','2018-08-08 05:44:59',1952,NULL),(339,'外勤',155,'岑美凤','2018-08-08 08:39:05',397,NULL),(340,'外勤',155,'岑美凤','2018-08-09 01:28:31',1090,NULL),(341,'外勤',155,'岑美凤','2018-08-09 03:22:02',1903,NULL),(342,'外勤',155,'岑美凤','2018-08-09 03:55:47',1674,NULL),(343,'外勤',155,'岑美凤','2018-08-09 04:04:56',738,NULL),(344,'外勤',155,'岑美凤','2018-08-09 06:33:23',1554,NULL),(345,'外勤',155,'岑美凤','2018-08-09 06:48:52',1324,NULL),(346,'外勤',155,'岑美凤','2018-08-09 07:37:20',1604,NULL),(347,'外勤',155,'岑美凤','2018-08-09 07:48:20',1920,NULL),(348,'外勤',155,'岑美凤','2018-08-09 08:20:31',1907,NULL),(349,'外勤',155,'岑美凤','2018-08-09 08:33:44',1892,NULL),(350,'外勤',155,'岑美凤','2018-08-09 08:43:35',1779,NULL),(351,'外勤',155,'岑美凤','2018-08-09 08:51:18',1857,NULL),(352,'外勤',155,'岑美凤','2018-08-10 03:36:56',1473,NULL),(353,'外勤',155,'岑美凤','2018-08-10 03:47:44',1684,NULL),(354,'外勤',155,'岑美凤','2018-08-10 03:59:22',1994,NULL),(355,'外勤',155,'岑美凤','2018-08-10 04:23:12',1913,NULL),(356,'外勤',155,'岑美凤','2018-08-10 06:21:44',1932,NULL),(357,'外勤',155,'岑美凤','2018-08-10 06:28:31',1770,NULL),(358,'外勤',155,'岑美凤','2018-08-10 07:29:25',1908,NULL),(359,'外勤',155,'岑美凤','2018-08-10 07:59:45',2032,NULL),(360,'外勤',155,'岑美凤','2018-08-10 08:51:01',1666,NULL),(361,'外勤',155,'岑美凤','2018-08-10 08:56:59',1901,NULL),(362,'外勤',155,'岑美凤','2018-08-10 09:11:15',1875,NULL),(363,'外勤',155,'岑美凤','2018-08-13 03:52:08',1888,NULL),(364,'外勤',155,'岑美凤','2018-08-13 03:55:02',1902,NULL),(365,'外勤',107,'冉小凤','2018-08-13 05:58:28',1561,NULL),(366,'外勤',155,'岑美凤','2018-08-13 06:40:14',1397,NULL),(367,'外勤',155,'岑美凤','2018-08-13 07:26:07',2149,NULL),(368,'外勤',155,'岑美凤','2018-08-14 01:25:31',1571,NULL),(369,'外勤',155,'岑美凤','2018-08-14 02:34:15',2019,NULL),(370,'外勤',155,'岑美凤','2018-08-14 03:28:13',1805,NULL),(371,'外勤',155,'岑美凤','2018-08-14 03:41:53',2132,NULL),(372,'外勤',155,'岑美凤','2018-08-14 05:39:24',1745,NULL),(373,'外勤',155,'岑美凤','2018-08-14 05:53:27',2152,NULL),(374,'外勤',199,'杨辉','2018-08-14 05:55:34',1745,NULL),(375,'外勤',155,'岑美凤','2018-08-14 05:59:21',1235,NULL),(376,'外勤',155,'岑美凤','2018-08-14 06:09:06',1930,NULL),(377,'外勤',155,'岑美凤','2018-08-14 06:16:14',2045,NULL),(378,'外勤',155,'岑美凤','2018-08-14 06:21:05',1894,NULL),(379,'外勤',155,'岑美凤','2018-08-14 08:52:13',2150,NULL),(380,'外勤',155,'岑美凤','2018-08-14 09:07:50',2151,NULL),(381,'外勤',155,'岑美凤','2018-08-14 09:13:02',910,NULL),(382,'外勤',155,'岑美凤','2018-08-15 03:17:12',2191,NULL),(383,'外勤',155,'岑美凤','2018-08-15 04:00:24',2183,NULL),(384,'外勤',155,'岑美凤','2018-08-15 06:29:52',2040,NULL),(385,'外勤',155,'岑美凤','2018-08-16 03:32:38',1833,NULL),(386,'外勤',155,'岑美凤','2018-08-16 03:55:44',1933,NULL),(387,'外勤',155,'岑美凤','2018-08-16 05:51:46',1931,NULL),(388,'外勤',155,'岑美凤','2018-08-16 05:51:46',2194,NULL),(389,'外勤',155,'岑美凤','2018-08-16 05:56:01',1838,NULL),(390,'外勤',155,'岑美凤','2018-08-16 05:59:45',2201,NULL),(391,'外勤',155,'岑美凤','2018-08-16 09:21:44',1798,NULL),(392,'外勤',155,'岑美凤','2018-08-16 09:28:33',2210,NULL),(393,'外勤',155,'岑美凤','2018-08-16 09:33:32',1943,NULL),(394,'外勤',253,'陈静','2018-08-17 01:06:48',2201,NULL),(395,'外勤',155,'岑美凤','2018-08-17 01:17:20',2166,NULL),(396,'外勤',155,'岑美凤','2018-08-17 03:07:00',1941,NULL),(397,'外勤',155,'岑美凤','2018-08-17 03:16:19',2130,NULL),(398,'外勤',155,'岑美凤','2018-08-17 03:22:09',2014,NULL),(399,'外勤',155,'岑美凤','2018-08-17 05:40:50',2198,NULL),(400,'外勤',155,'岑美凤','2018-08-17 06:39:36',1678,NULL),(401,'外勤',155,'岑美凤','2018-08-17 07:25:16',1539,NULL),(402,'外勤',155,'岑美凤','2018-08-17 07:34:44',1758,NULL),(403,'外勤',139,'陈勇极','2018-08-17 07:43:48',1481,NULL),(404,'外勤',155,'岑美凤','2018-08-17 08:13:34',1856,NULL),(405,'外勤',155,'岑美凤','2018-08-17 08:18:05',2158,NULL),(406,'外勤',253,'陈静','2018-08-17 08:20:55',2158,NULL),(407,'外勤',155,'岑美凤','2018-08-20 04:01:50',2148,NULL),(408,'外勤',155,'岑美凤','2018-08-20 04:04:47',2187,NULL),(409,'外勤',139,'陈勇极','2018-08-20 05:46:43',2331,NULL),(410,'外勤',141,'刘建光','2018-08-20 06:06:56',1457,NULL),(411,'外勤',141,'刘建光','2018-08-20 06:07:32',1465,NULL),(412,'外勤',155,'岑美凤','2018-08-20 06:13:39',1921,NULL),(413,'外勤',155,'岑美凤','2018-08-20 06:15:12',2167,NULL),(414,'外勤',155,'岑美凤','2018-08-20 06:18:26',1847,NULL),(415,'外勤',122,'何健锋','2018-08-21 02:04:04',0,NULL),(416,'外勤',155,'岑美凤','2018-08-21 03:08:11',2179,NULL),(417,'外勤',155,'岑美凤','2018-08-21 05:49:37',294,NULL),(418,'外勤',155,'岑美凤','2018-08-21 06:14:50',1360,NULL),(419,'外勤',155,'岑美凤','2018-08-21 08:16:13',2337,NULL),(420,'外勤',155,'岑美凤','2018-08-21 08:21:41',1728,NULL),(421,'外勤',155,'岑美凤','2018-08-21 08:48:38',2078,NULL),(422,'外勤',155,'岑美凤','2018-08-21 09:20:17',1815,NULL),(423,'外勤',155,'岑美凤','2018-08-21 09:23:55',261,NULL),(424,'外勤',195,'杨婵','2018-08-22 01:44:57',2054,NULL),(425,'外勤',155,'岑美凤','2018-08-22 03:16:26',2195,NULL),(426,'外勤',155,'岑美凤','2018-08-22 04:00:08',2280,NULL),(427,'外勤',155,'岑美凤','2018-08-22 04:42:15',2236,NULL),(428,'外勤',155,'岑美凤','2018-08-22 06:10:58',1910,NULL),(429,'外勤',155,'岑美凤','2018-08-22 07:11:47',2267,NULL),(430,'外勤',155,'岑美凤','2018-08-22 09:23:12',2256,NULL),(431,'外勤',107,'冉小凤','2018-08-23 01:41:03',2273,NULL),(432,'外勤',155,'岑美凤','2018-08-23 02:12:18',1313,NULL),(433,'外勤',155,'岑美凤','2018-08-23 03:05:35',1027,NULL),(434,'外勤',155,'岑美凤','2018-08-23 03:14:54',1912,NULL),(435,'外勤',155,'岑美凤','2018-08-23 03:21:54',2350,NULL),(436,'外勤',155,'岑美凤','2018-08-24 03:00:51',2384,NULL),(437,'外勤',155,'岑美凤','2018-08-24 03:42:54',2223,NULL),(438,'外勤',155,'岑美凤','2018-08-24 03:55:22',2261,NULL),(439,'外勤',155,'岑美凤','2018-08-24 04:00:52',2249,NULL),(440,'外勤',155,'岑美凤','2018-08-24 04:04:06',2254,NULL),(441,'外勤',155,'岑美凤','2018-08-24 06:07:24',2346,NULL),(442,'外勤',155,'岑美凤','2018-08-24 06:35:59',1762,NULL),(443,'外勤',131,'朱伟峰','2018-08-27 01:13:25',2384,NULL),(444,'外勤',153,'江嘉琳','2018-08-27 03:00:59',2138,NULL),(445,'外勤',153,'江嘉琳','2018-08-27 03:12:59',2139,NULL),(446,'外勤',155,'岑美凤','2018-08-27 06:31:25',1956,NULL),(447,'外勤',155,'岑美凤','2018-08-27 07:37:52',1503,NULL);
/*!40000 ALTER TABLE `t_projects_member_other` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-14 11:34:26
