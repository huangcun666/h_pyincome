-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_test
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
-- Table structure for table `t_transition`
--

DROP TABLE IF EXISTS `t_transition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_transition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remark` varchar(2505) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `guid` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `tran_by` varchar(255) DEFAULT NULL,
  `rec_by` varchar(255) DEFAULT NULL,
  `tran_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(255) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_transition`
--

LOCK TABLES `t_transition` WRITE;
/*!40000 ALTER TABLE `t_transition` DISABLE KEYS */;
INSERT INTO `t_transition` VALUES (1,'fsdfdf',NULL,'a21b69d4-542f-11e8-a20d-6045cb9a7117','2018-05-10 08:53:39','fdsf','sfsfdsd','2018-05-16 00:00:00',116,'陈太智',NULL),(2,'fsdf',NULL,'050426d3-5430-11e8-a20d-6045cb9a7117','2018-05-10 08:56:25','dfsf','sfsdf','2018-05-10 00:00:00',116,'陈太智',NULL),(4,'fsdf',NULL,'2e1a28cc-54c0-11e8-a20d-6045cb9a7117','2018-05-11 02:08:21','fsd','fsdf','2018-05-15 00:00:00',116,'陈太智',25),(5,'fsdf',NULL,'2ec0671f-54c0-11e8-a20d-6045cb9a7117','2018-05-11 02:08:22','fsd','哦嗯大是凤','2018-05-15 00:00:00',116,'陈太智',25),(6,'aa','/static/customer/2524/3216b4d3-5b25-465a-93a5-e061b6081150_2524.jpg','d0d03179-5e52-11e8-8199-6045cb9a7117','2018-05-23 06:30:41','去','a','2018-05-23 00:00:00',161,'周萍',2524),(7,'f f f','/static/customer/tran_7/79700f31-e739-4fb3-9030-1b365e5a0156_7.png','fcd32cfd-5e52-11e8-8199-6045cb9a7117','2018-05-23 06:31:55','我','你','2018-05-23 00:00:00',161,'周萍',2524),(8,'132','/static/customer/tran_8/ab3adc01-920c-4542-b910-9c6cd920d99a_8.png','14d9d22a-5ef5-11e8-b807-6045cb9a7117','2018-05-24 01:52:14','w','n','2018-05-02 00:00:00',161,'周萍',2524),(9,'czxxc',NULL,'88e3c284-64b4-11e8-b807-6045cb9a7117','2018-05-31 09:25:18','czx','czxc','2018-04-30 00:00:00',161,'周萍',2533),(10,'czxxc','/static/customer/tran_10/2a0e3753-b355-46a7-ae04-03fdb2b9944c_10.jpeg','8969a71e-64b4-11e8-b807-6045cb9a7117','2018-05-31 09:25:19','czx','czxc','2018-04-30 00:00:00',161,'周萍',2533),(11,'','/static/customer/tran_11/a1858bd1-40ba-4a71-b312-e9c503cffd52_11.png','8ca8fe44-686c-11e8-b807-6045cb9a7117','2018-06-05 03:00:06','w','n','2018-06-06 00:00:00',161,'周萍',2515),(12,'','/static/customer/tran_12/825bc544-a715-4747-ab4a-4aea5693e5f8_12.jpg','8db5ee98-686c-11e8-b807-6045cb9a7117','2018-06-05 03:00:07','w','n','2018-06-06 00:00:00',161,'周萍',2515),(13,'',NULL,'adb2133e-6872-11e8-b807-6045cb9a7117','2018-06-05 03:43:58','w','n','2018-06-06 00:00:00',161,'周萍',1948),(14,'',NULL,'aeb026a7-6872-11e8-b807-6045cb9a7117','2018-06-05 03:44:00','w','n','2018-06-06 00:00:00',161,'周萍',1948),(15,'',NULL,'b7e5f711-6872-11e8-b807-6045cb9a7117','2018-06-05 03:44:15','12','23','2018-06-12 00:00:00',161,'周萍',1948),(16,'','/static/customer/tran_16/6a6447e4-05a0-434d-8816-7f4a5637c052_16.jpg','b8cb7a1f-6872-11e8-b807-6045cb9a7117','2018-06-05 03:44:17','12','23','2018-06-12 00:00:00',161,'周萍',1948),(17,'','/static/customer/tran_17/a9190887-b163-400d-9718-b5128da28ae0_17.jpg','e6bad0e4-693a-11e8-b807-6045cb9a7117','2018-06-06 03:37:13','12','123','2018-06-07 00:00:00',106,'陈小银',2517),(18,'','/static/customer/tran_18/1a3fc195-b962-4a41-a741-68c8c7dc90b2_18.jpg','e6d535ba-693a-11e8-b807-6045cb9a7117','2018-06-06 03:37:13','12','123','2018-06-07 00:00:00',106,'陈小银',2517),(25,'',NULL,'e161ea9b-69fa-11e8-b807-6045cb9a7117','2018-06-07 02:31:27','吴彦祖','彭宇彦','2018-06-06 00:00:00',161,'周萍',2534),(26,'新润香于2018.6.22解除记账合同','/static/customer/130/878ec589-286f-4f71-bec7-07a06be48ef0_130.jpg','cc769c56-75f0-11e8-af32-6045cb9a7117','2018-06-22 07:49:31','周萍','新润香胡芳','2018-06-22 00:00:00',161,'周萍',130),(27,'2018.6.22交接资料','/static/customer/130/2a87a05a-e897-4a72-a13f-dab3f14efc4c_130.jpg','e8e4b817-75f0-11e8-af32-6045cb9a7117','2018-06-22 07:50:19','周萍','新润香胡芳','2018-06-22 00:00:00',161,'周萍',130),(28,'2018.6月发票交接','/static/customer/130/247ccb4c-6011-4057-a97c-e0bd4e70337c_130.jpg','2bcf9476-75f1-11e8-af32-6045cb9a7117','2018-06-22 07:52:11','周萍','新润香胡芳','2018-06-22 00:00:00',161,'周萍',130),(29,'解约','/static/customer/2198/a6d46071-80e4-4039-a7d7-4f01c5005971_2198.jpg','589704da-75f5-11e8-af32-6045cb9a7117','2018-06-22 08:22:04','周萍','新润香分公司胡芳','2018-06-22 00:00:00',161,'周萍',2198),(30,'交接清单','/static/customer/2198/580ec36c-72d7-47d0-8401-d7ebaa5c1b85_2198.jpg','771ba50d-75f5-11e8-af32-6045cb9a7117','2018-06-22 08:22:56','周萍','新润香分公司胡芳','2018-06-22 00:00:00',161,'周萍',2198),(31,'交接发票清单','/static/customer/2198/1290494e-a4d1-4939-9778-46fd28c497ed_2198.jpg','8c6201c2-75f5-11e8-af32-6045cb9a7117','2018-06-22 08:23:31','周萍','新润香分公司胡芳','2018-06-22 00:00:00',161,'周萍',2198),(32,'解除代理记账合同','/static/customer/193/fe92557d-dbe1-441b-8234-406bd76fe0b8_193.jpg','a80916c7-75f5-11e8-af32-6045cb9a7117','2018-06-22 08:24:18','周萍','粤朗胡芳','2018-06-22 00:00:00',161,'周萍',193),(33,'交接清单','/static/customer/193/fb9124e1-d497-4802-9888-f3699230df5f_193.jpg','b4f2fc78-75f5-11e8-af32-6045cb9a7117','2018-06-22 08:24:39','周萍','粤朗胡芳','2018-06-22 00:00:00',161,'周萍',193),(34,'','/static/customer/1544/fb95a94c-637d-49ff-9908-99d56fec4dae_1544.jpg','388ebeef-8571-11e8-b047-6045cb9a7117','2018-07-12 01:16:36','梁家欣','何文瑞','2018-07-11 00:00:00',186,'梁家欣',1544);
/*!40000 ALTER TABLE `t_transition` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-14 11:34:41
