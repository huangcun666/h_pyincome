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
-- Table structure for table `t_projects_income_old`
--

DROP TABLE IF EXISTS `t_projects_income_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_income_old` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL DEFAULT '0',
  `income_name` varchar(255) DEFAULT NULL,
  `income_money` decimal(18,2) NOT NULL DEFAULT '0.00',
  `is_lock` tinyint(1) NOT NULL DEFAULT '0',
  `uid` int(11) DEFAULT '0',
  `guid` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `remark` varchar(2000) DEFAULT NULL,
  `income_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `pay_type_name` varchar(255) DEFAULT NULL,
  `pay_type_id` int(11) DEFAULT NULL,
  `income_at` datetime DEFAULT NULL,
  `is_other` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=465 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_income_old`
--

LOCK TABLES `t_projects_income_old` WRITE;
/*!40000 ALTER TABLE `t_projects_income_old` DISABLE KEYS */;
INSERT INTO `t_projects_income_old` VALUES (198,181,'合同定金',1000.00,0,97,'33a03c75-87b7-4b06-bd17-c816af918730','2018-04-02 09:43:54','2018-04-02 09:43:54','',40,15,'发业','微信',21,'2018-04-02 17:43:00',0),(200,182,'合同定金',1300.00,0,97,'5f6473fd-16e5-4927-af3f-f71c4ba9ae3f','2018-04-02 09:49:50','2018-04-02 09:49:50','',40,15,'发业','微信',21,'2018-04-02 17:49:00',0),(202,184,'合同定金',1500.00,0,97,'16aa8a83-904a-4af9-adaf-d28be11d4074','2018-04-02 09:52:16','2018-04-02 09:52:16','',40,15,'发业','微信',21,'2018-04-02 17:52:00',0),(203,185,'合同定金',9000.00,0,97,'cd35ff6e-4463-481e-ad4e-5fc9850d62a9','2018-04-02 09:54:15','2018-04-02 09:54:15','',40,15,'发业','微信',21,'2018-04-02 17:54:00',0),(205,187,'合同定金',800.00,0,122,'5775f133-1db4-446b-8470-ac08bb403531','2018-04-02 10:10:53','2018-04-02 10:10:53','已交全款',40,15,'发业','支付宝',20,'2018-04-02 18:10:00',0),(207,183,'合同定金',2300.00,0,122,'bb0263d1-424e-40bc-b8a0-bda06604fb6d','2018-04-03 03:07:13','2018-04-03 03:07:13','已交全款',40,16,'商脉','微信',21,'2018-04-03 11:05:00',0),(229,186,'合同定金',3000.00,0,97,'b6728191-31bb-4169-a54c-c2974ea9aa27','2018-04-03 03:15:40','2018-04-03 03:15:40','',40,15,'发业','微信',21,'2018-04-03 11:15:00',0),(238,189,'二期定金',1000.00,0,132,'cf013bc9-36c9-4e6a-b29b-e6448a08e03d','2018-04-03 04:23:50','2018-04-03 04:23:50','测试',41,15,'发业','刷卡机',17,'2018-04-03 12:18:00',0),(243,190,'办结尾款',1060.00,0,122,'35b55ca2-db39-44d2-aa9f-2674452d0f9e','2018-04-03 06:13:31','2018-04-03 06:13:31','记帐及账册尾款',43,15,'发业','刷卡机',17,'2018-04-03 14:12:00',0),(245,190,'办结尾款',1200.00,0,122,'52e66c85-98db-4309-a62f-46adc7df6e2f','2018-04-03 06:14:10','2018-04-03 06:14:10','注册尾款',43,15,'发业','刷卡机',17,'2018-04-03 14:13:00',0),(246,190,'代收款项',200.00,0,122,'e739126f-dff2-44a8-bc6a-2fddc4721d56','2018-04-03 06:20:50','2018-04-03 06:20:50','代买国税CA',48,15,'发业','刷卡机',17,'2018-04-03 14:20:00',1),(248,199,'退款',1500.00,0,124,'faeef186-28b3-40ef-ab54-47e72a21fd33','2018-04-03 06:58:53','2018-04-03 06:58:53','由于联系不上客户，客户资料也未提供，现变更定金1500元不退，取消变更',91,15,'发业','基本户',19,'2018-04-03 14:57:00',0),(249,201,'合同定金',1300.00,0,123,'88f641cb-796b-4e57-9727-8ce37825cb51','2018-04-03 07:02:25','2018-04-03 07:02:25','',40,15,'发业','刷卡机',17,'2018-04-03 15:02:00',0),(251,203,'合同定金',1500.00,0,132,'1c6e70e8-010c-4986-9382-5cda25fc7aae','2018-04-03 08:06:51','2018-04-03 08:06:51','',40,15,'发业','现金',18,'2018-04-03 16:06:00',0),(254,207,'合同定金',111.00,0,132,'6b96b798-52b7-44b4-8c78-146d57dd04f0','2018-04-03 09:16:44','2018-04-03 09:16:44','dasda',40,15,'发业','刷卡机',17,'2018-04-03 17:16:00',0),(255,207,'合同定金',1.00,0,132,'ca2b2c45-628c-4d8c-a21e-5b5c436d2f18','2018-04-03 09:16:57','2018-04-03 09:16:57','test',40,15,'发业','刷卡机',17,'2018-04-03 17:16:00',1),(256,206,'合同定金',7800.00,0,123,'91b0431f-57f2-4ba0-86d4-2e8209bf6229','2018-04-03 09:32:19','2018-04-03 09:32:19','',40,15,'发业','现金',18,'2018-04-03 17:32:00',0),(257,206,'合同定金',7800.00,0,123,'74d8833c-93c1-4f08-b7ca-c10d9361612a','2018-04-03 09:32:34','2018-04-03 09:32:34','',40,15,'发业','现金',18,'2018-04-03 17:32:00',1),(260,205,'合同定金',6060.00,0,123,'5b2b5b1e-43a9-4243-a06f-73f161c45626','2018-04-03 09:33:53','2018-04-03 09:33:53','',40,15,'发业','刷卡机',17,'2018-04-03 17:33:00',0),(262,210,'办结尾款',1000.00,0,124,'de85827f-1eb3-4e0c-9284-829f4be9d99f','2018-04-03 09:39:38','2018-04-03 09:39:38','已结办业务，尾款已结清。',43,15,'发业','支付宝',20,'2018-04-03 17:38:00',1),(264,180,'合同定金',800.00,0,122,'04f314f8-3031-43d4-ba4d-74127a4ad432','2018-04-03 09:40:59','2018-04-03 09:40:59','已交全款',40,15,'发业','支付宝',20,'2018-04-03 17:40:00',0),(265,211,'办结尾款',1000.00,0,97,'679b5782-37eb-4c4c-a997-2c8d40fc37b5','2018-04-03 09:50:10','2018-04-03 09:50:10','',43,15,'发业','现金',18,'2018-04-03 17:49:00',0),(268,213,'合同定金',3000.00,0,121,'b3f78740-3011-4d0d-8d79-ba8567703135','2018-04-03 10:08:12','2018-04-03 10:08:12','',40,15,'发业','建行',23,'2018-04-03 18:07:00',0),(270,214,'合同定金',700.00,0,121,'49d005e6-02fe-472f-82a2-681d7e4ced74','2018-04-03 10:20:01','2018-04-03 10:20:01','',40,15,'发业','中国银行',25,'2018-04-03 18:19:00',0),(271,215,'合同定金',8260.00,0,97,'0821fb70-57eb-4b24-915b-dba0fe0f8634','2018-04-03 10:33:18','2018-04-03 10:33:18','',40,15,'发业','微信',21,'2018-04-03 18:32:00',0),(272,216,'合同定金',5000.00,0,122,'39b91294-f01d-462e-8e73-7e9d3aca6b4b','2018-04-04 01:58:17','2018-04-04 01:58:17','已交全款',40,15,'发业','微信',21,'2018-04-04 09:57:00',0),(273,202,'合同定金',2500.00,0,123,'406baf9e-55d0-440d-99ac-35ce380d0b77','2018-04-04 03:29:52','2018-04-04 03:29:52','',40,16,'商脉','微信',21,'2018-04-04 11:29:00',0),(277,218,'合同定金',3000.00,0,122,'1dde4fea-fe6c-4f12-a428-da3c55303285','2018-04-04 08:03:37','2018-04-04 08:03:37','定金',40,15,'发业','微信',21,'2018-04-04 16:03:00',0),(278,219,'合同定金',400.00,0,122,'748df31b-fb39-4616-9af7-cdb4ff4347c5','2018-04-04 09:01:36','2018-04-04 09:01:36','还有二次款项客户晚上转',40,15,'发业','微信',21,'2018-04-04 17:00:00',0),(280,221,'合同定金',6060.00,0,97,'b18184b2-42a8-400c-a010-88ca6ff4aa88','2018-04-07 05:35:37','2018-04-07 05:35:37','',40,15,'发业','支付宝',20,'2018-04-07 13:35:00',0),(281,222,'合同定金',3000.00,0,97,'c9dd651f-9f3f-41e1-888c-341dcb39349f','2018-04-07 06:26:02','2018-04-07 06:26:02','',40,15,'发业','微信',21,'2018-04-07 14:25:00',0),(282,223,'合同定金',2700.00,0,97,'84c9c9a4-0d8e-4c5f-9b59-932f5041fca4','2018-04-07 08:47:10','2018-04-07 08:47:10','自有地址注册1300+食品证1400',40,15,'发业','微信',21,'2018-04-07 16:46:00',0),(283,224,'合同定金',5760.00,0,97,'c1526566-8578-435c-96f6-a443115419b4','2018-04-07 08:59:55','2018-04-07 08:59:55','',40,15,'发业','刷卡机',17,'2018-04-07 16:59:00',0),(284,220,'合同定金',2200.00,0,122,'e68ce0b9-5519-43ca-8362-49337d1418a0','2018-04-08 01:47:48','2018-04-08 01:47:48','注册定金',40,15,'发业','基本户',19,'2018-04-08 09:46:00',0),(285,220,'合同定金',2200.00,0,122,'f3404f36-8fd6-42c7-bf88-44307c53f0d9','2018-04-08 01:47:56','2018-04-08 01:47:56','注册定金',40,15,'发业','基本户',19,'2018-04-08 09:47:00',0),(286,219,'二期定金',900.00,0,122,'286a2ac6-aeb3-40cf-8440-291f1b592945','2018-04-08 01:49:37','2018-04-08 01:49:37','',41,15,'发业','微信',21,'2018-04-08 09:49:00',0),(289,226,'合同定金',1000.00,0,123,'1085475d-9dcf-4dac-b640-c03258f6b5f4','2018-04-08 02:38:19','2018-04-13 08:41:44','反馈人，郑颖芝',40,16,'商脉','微信',21,'2018-04-13 16:41:00',0),(291,227,'合同定金',7000.00,0,123,'7014efdb-1e44-4692-b2a7-e276caa0fa85','2018-04-08 03:43:12','2018-04-08 03:43:12','',40,15,'发业','现金',18,'2018-04-08 11:42:00',0),(293,217,'代收款项',200.00,0,123,'da4eb3d4-3e40-4ee2-9ac3-097f19cbd01d','2018-04-08 04:03:08','2018-04-08 04:03:08','CA款项已付',48,15,'发业','刷卡机',17,'2018-04-08 12:02:00',1),(294,217,'合同定金',6060.00,0,123,'4bef214c-673c-4dd8-9d0f-09b290a61e31','2018-04-08 05:50:50','2018-04-08 05:50:50','实收款项6260.其中200为CA款项',40,15,'发业','刷卡机',17,'2018-04-08 13:49:00',0),(295,228,'合同定金',3000.00,0,123,'7135ad37-8440-4749-ade7-d01b2a23071c','2018-04-08 06:15:37','2018-04-08 06:15:37','',40,15,'发业','刷卡机',17,'2018-04-08 14:15:00',0),(296,208,'CA费用',200.00,0,123,'61968d62-cd8a-4b49-b8b4-a759952e0658','2018-04-08 06:20:50','2018-04-11 08:26:35','',93,15,'发业','支付宝',20,'2018-04-11 16:24:00',1),(297,209,'合同定金',1600.00,0,121,'a76e24c4-704b-4283-8d60-6b7d9f15fde7','2018-04-08 06:33:41','2018-04-08 06:33:41','',40,15,'发业','微信',21,'2018-04-03 17:35:00',0),(298,212,'合同定金',800.00,0,121,'8b2116c3-e43b-49e9-8a79-e8737c52681b','2018-04-08 06:34:16','2018-04-08 06:34:16','',40,15,'发业','微信',21,'2018-04-03 17:50:00',0),(301,229,'全款',3060.00,0,122,'e87810a9-5efc-4762-a062-0f0ebd138e9d','2018-04-08 06:37:26','2018-04-08 06:37:26','',92,15,'发业','刷卡机',17,'2018-04-08 14:37:00',0),(302,229,'全款',200.00,0,122,'6d067703-e9a7-4089-8773-bfaebde99cde','2018-04-08 06:37:44','2018-04-08 06:37:44','代买国税CA',92,15,'发业','刷卡机',17,'2018-04-08 14:37:00',1),(303,231,'全款',900.00,0,122,'ebccc16e-01a8-4dfa-9bb2-dc2c39510376','2018-04-08 06:50:00','2018-04-08 06:50:00','',92,15,'发业','刷卡机',17,'2018-04-08 14:49:00',0),(304,230,'合同定金',500.00,0,123,'5aa53c48-69ed-49f3-af38-c77ffbacff2a','2018-04-08 07:04:04','2018-04-08 07:04:04','剩余尾款100变更好再付',40,15,'发业','微信',21,'2018-04-08 15:03:00',0),(306,232,'全款',1600.00,0,122,'98414f89-dabe-4f08-b69c-29398c1e2680','2018-04-09 02:31:45','2018-04-09 02:31:45','',92,15,'发业','微信',21,'2018-04-09 10:31:00',0),(307,233,'合同定金',6060.00,0,97,'04e9d8d6-bd62-4d5a-8714-058b6a44ca44','2018-04-09 04:08:44','2018-04-09 04:08:44','',40,15,'发业','刷卡机',17,'2018-04-09 12:08:00',0),(308,234,'办结尾款',400.00,0,122,'784449b2-8e61-4039-b70f-49234d6d61a9','2018-04-09 05:55:06','2018-04-09 05:55:06','',43,15,'发业','刷卡机',17,'2018-04-09 13:54:00',0),(309,235,'合同定金',3500.00,0,123,'71fe3118-6033-4a85-bbdd-af071ed7bc1a','2018-04-09 05:57:16','2018-04-09 05:57:16','反馈人何家辉',40,15,'发业','支付宝',20,'2018-04-09 13:56:00',0),(310,225,'全款',1300.00,0,121,'51c4d4df-74f0-4f8f-b101-7bb252ddfece','2018-04-09 06:05:18','2018-04-09 06:05:18','',92,15,'发业','微信',21,'2018-04-09 14:04:00',0),(313,237,'合同定金',5548.00,0,123,'38d3a597-5a52-402e-83d4-882e07d13053','2018-04-09 06:32:30','2018-04-09 06:32:30','',40,15,'发业','微信',21,'2018-04-09 14:32:00',0),(314,238,'合同定金',1500.00,0,97,'eef268c7-ea74-4335-834e-4ba51ca80685','2018-04-09 07:12:16','2018-04-09 07:12:16','',40,15,'发业','工行',22,'2018-04-09 15:10:00',0),(315,239,'全款',4800.00,0,121,'3141e6cc-f173-4c52-a83b-138475596951','2018-04-09 08:02:51','2018-04-09 08:02:51','',92,15,'发业','工行',22,'2018-04-09 16:02:00',0),(316,240,'合同定金',4500.00,0,123,'cb390e62-783c-44e4-bcfc-7b87a0c5fbd4','2018-04-09 08:27:49','2018-04-09 08:27:49','',40,15,'发业','微信',21,'2018-04-09 16:27:00',0),(317,236,'办结尾款',2700.00,0,122,'a5030d3c-bd37-4ed8-bbe4-220b1d94e179','2018-04-09 09:07:08','2018-04-09 09:07:08','',43,15,'发业','刷卡机',17,'2018-04-09 17:06:00',0),(318,236,'CA费用',200.00,0,122,'0fd8e314-2ab2-435b-9ce6-46ac463f2026','2018-04-09 09:10:59','2018-04-09 09:10:59','',93,15,'发业','刷卡机',17,'2018-04-09 17:10:00',1),(319,241,'全款',1200.00,0,121,'22dd398f-fe80-4639-9441-70cff780a9f8','2018-04-09 09:38:23','2018-04-09 09:38:23','',92,15,'发业','微信',21,'2018-04-09 17:37:00',0),(320,242,'全款',2000.00,0,121,'635e80da-38a6-414b-9e34-be1afe47d191','2018-04-09 09:42:24','2018-04-09 09:42:24','',92,15,'发业','微信',21,'2018-04-09 17:41:00',0),(321,243,'办结尾款',2000.00,0,121,'80499d67-ed5b-4b26-adfd-b0f14eb88119','2018-04-09 10:05:32','2018-04-09 10:05:32','',43,15,'发业','支付宝',20,'2018-04-09 18:05:00',0),(323,244,'合同定金',1500.00,0,97,'2124c375-d394-4ee4-94bd-f45fadddd6b1','2018-04-09 10:09:09','2018-04-09 10:09:09','记账日期（17年11月-18年10月）',40,15,'发业','支付宝',20,'2018-04-09 18:06:00',0),(324,245,'全款',9330.00,0,97,'915210f8-bf0f-4f43-bc26-3daa74c2765c','2018-04-10 02:45:56','2018-04-10 02:45:56','',92,15,'发业','支付宝',20,'2018-04-10 10:45:00',0),(325,246,'全款',3000.00,0,97,'553ad4cf-bd75-4662-98dc-6511a468b408','2018-04-10 03:02:18','2018-04-10 03:02:18','',92,15,'发业','微信',21,'2018-04-10 11:01:00',0),(326,247,'全款',3000.00,0,123,'7b94c7b4-01a9-4dd2-b470-526cd8645dbe','2018-04-10 03:04:24','2018-04-10 03:04:24','',92,15,'发业','工行',22,'2018-04-10 11:03:00',0),(327,248,'全款',900.00,0,123,'dcc1facb-c63a-4c22-b28a-3eba7829f6e6','2018-04-10 03:09:54','2018-04-10 03:09:54','',92,15,'发业','微信',21,'2018-04-10 11:09:00',0),(328,249,'全款',3000.00,0,97,'829cd7b4-75cf-49f5-b26a-21204f0946dc','2018-04-10 03:26:28','2018-04-10 03:26:28','4-3号微信付500元。4-10号刷卡付2500元',92,15,'发业','刷卡机',17,'2018-04-10 11:25:00',0),(329,250,'全款',3800.00,0,97,'36c2c2a0-ba9a-42a2-94d6-6ec27858f387','2018-04-10 05:41:26','2018-04-10 05:41:26','',92,15,'发业','基本户',19,'2018-04-10 13:41:00',0),(330,251,'全款',3500.00,0,123,'ef13c050-4b48-4308-8f51-9b5ac018cd8e','2018-04-10 05:57:25','2018-04-10 05:57:25','',92,15,'发业','微信',21,'2018-04-10 13:57:00',0),(331,252,'办结尾款',3060.00,0,123,'68c68016-884e-4ab3-b26d-178b889e223b','2018-04-10 06:38:27','2018-04-11 08:33:33','',43,15,'发业','支付宝',20,'2018-04-11 16:33:00',0),(332,252,'CA费用',200.00,0,123,'427af241-a98f-423b-a5f2-2f9e311f166b','2018-04-10 06:38:45','2018-04-11 08:33:54','',93,15,'发业','支付宝',20,'2018-04-11 16:33:00',1),(333,253,'全款',2400.00,0,97,'f87b2806-444c-479e-a4b4-8a31605aaf6a','2018-04-10 07:11:40','2018-04-10 07:11:40','',92,15,'发业','微信',21,'2018-04-10 15:11:00',0),(334,254,'全款',3000.00,0,122,'9ea11927-d94b-4ce4-9f64-8e3d099d6771','2018-04-10 08:30:56','2018-04-10 08:30:56','',92,15,'发业','支付宝',20,'2018-04-10 16:30:00',0),(335,255,'合同定金',500.00,0,123,'d7c24a22-1e97-478c-b993-442595787ac8','2018-04-10 08:35:34','2018-04-11 08:29:07','尾款跟客户月底好周末过来付清',40,16,'商脉','微信',21,'2018-04-11 16:28:00',0),(336,256,'合同定金',15000.00,0,123,'f8336e68-1673-45f4-9f5b-211cf88fe457','2018-04-10 09:27:07','2018-04-10 09:27:07','',40,15,'发业','刷卡机',17,'2018-04-10 17:26:00',0),(337,257,'合同定金',3000.00,0,97,'06e3a03e-36dc-410c-bc90-5ed9a4e403fe','2018-04-10 10:11:05','2018-04-10 10:11:05','出地址受理执照的时候收齐尾款',40,15,'发业','基本户',19,'2018-04-10 18:10:00',0),(338,258,'全款',5800.00,0,121,'9749d5ce-41c3-491d-9c06-b7c5f74ed240','2018-04-10 10:25:15','2018-04-10 10:25:15','',92,15,'发业','刷卡机',17,'2018-04-10 18:24:00',0),(339,260,'合同定金',2000.00,0,122,'4bef1a66-efb4-4a78-b019-291e699185e2','2018-04-11 06:18:18','2018-04-11 06:18:18','',40,15,'发业','刷卡机',17,'2018-04-11 14:18:00',0),(340,261,'全款',1300.00,0,122,'249bef55-60bf-410b-82bb-866aacb0fe60','2018-04-11 06:24:55','2018-04-11 06:58:31','',92,15,'发业','刷卡机',17,'2018-04-11 14:58:00',0),(341,262,'全款',5800.00,0,121,'2ca1416c-a676-457b-98ad-f7ddc77890be','2018-04-11 07:39:21','2018-04-11 07:39:21','万科云米酷客户加急办理',92,15,'发业','刷卡机',17,'2018-04-11 15:38:00',0),(342,263,'全款',5500.00,0,121,'d8c70cc3-ab2b-4165-a7ef-41d1db067325','2018-04-11 08:07:06','2018-04-11 08:07:06','',92,15,'发业','刷卡机',17,'2018-04-11 16:06:00',0),(343,264,'合同定金',2300.00,0,97,'fe3add1d-f261-4000-ae84-5a631d1441b5','2018-04-11 08:43:59','2018-04-11 08:43:59','',40,15,'发业','微信',21,'2018-04-11 16:43:00',0),(344,265,'全款',1500.00,0,97,'28faf68d-4dbd-44ab-80b5-6cde3790c00b','2018-04-11 09:11:00','2018-04-12 01:47:03','',92,16,'商脉','微信',21,'2018-04-12 09:46:00',0),(346,266,'合同定金',2565.00,0,97,'6192bd95-958d-45fe-b007-3b85332a1cb8','2018-04-11 09:42:29','2018-04-11 09:42:29','18年6月-19年5月一般纳税人记账费用6000+账册费申请好一般纳税人资格领取到发票的时候和客户收齐',40,15,'发业','刷卡机',17,'2018-04-11 17:39:00',0),(347,267,'全款',2500.00,0,97,'978238cd-631e-4889-b092-db2d7c4dd47d','2018-04-11 09:53:39','2018-04-11 09:53:39','',92,15,'发业','支付宝',20,'2018-04-11 17:53:00',0),(348,268,'全款',2500.00,0,121,'af9ea8ff-6baa-4e52-8231-263ada493c2b','2018-04-11 09:59:26','2018-04-11 09:59:26','撤销注销服务费2500',92,15,'发业','微信',21,'2018-04-11 17:58:00',0),(349,213,'办结尾款',2500.00,0,121,'dcac214a-9558-428b-8b36-2b0709797b47','2018-04-11 10:01:44','2018-04-17 03:17:56','客户转了3400，（开户2500，注册尾款900）',43,15,'发业','中国银行',25,'2018-04-17 11:08:00',0),(350,269,'全款',3000.00,0,97,'aebc535e-5ccc-49f6-b5a4-caec1b8cc4d7','2018-04-11 10:03:54','2018-04-11 10:03:54','',92,15,'发业','建行',23,'2018-04-11 18:03:00',0),(351,270,'全款',900.00,0,121,'1e9fd9f0-fa90-4a22-8147-4755c4c8f8e2','2018-04-11 10:15:39','2018-04-11 10:15:39','',92,15,'发业','建行',23,'2018-04-11 18:14:00',0),(352,271,'全款',1500.00,0,97,'0930abf0-9a12-4fd9-a8d2-8988916d6d33','2018-04-12 01:18:21','2018-04-12 01:18:21','',92,15,'发业','微信',21,'2018-04-12 09:17:00',0),(353,272,'合同定金',2300.00,0,122,'f2bde820-e1d1-4097-a03d-88758f97af55','2018-04-12 01:21:28','2018-04-12 01:21:28','',40,15,'发业','刷卡机',17,'2018-04-12 09:21:00',0),(354,273,'全款',1800.00,0,123,'3a3cfa4b-82cc-412c-b0e1-3cbe03a5ccfa','2018-04-12 01:51:21','2018-04-12 03:38:12','',92,15,'发业','支付宝',20,'2018-04-12 11:37:00',0),(355,273,'CA费用',200.00,0,123,'21bcbc1b-b79b-44d1-a1da-be910f0c381d','2018-04-12 01:51:50','2018-04-12 03:38:18','',93,15,'发业','支付宝',20,'2018-04-12 11:38:00',1),(356,274,'CA费用',200.00,0,123,'cc3ebd19-4f52-4f12-b0f5-08634e6d2532','2018-04-12 01:56:20','2018-04-12 03:48:50','',93,15,'发业','支付宝',20,'2018-04-12 11:43:00',1),(357,274,'全款',900.00,0,123,'fa5f44fd-9a40-4c09-97e7-c5f5e0847340','2018-04-12 03:13:55','2018-04-12 03:13:55','',92,15,'发业','微信',21,'2018-04-12 11:13:00',0),(358,276,'全款',900.00,0,122,'b7940bf7-f34f-4393-a99b-84820de85abf','2018-04-12 03:22:21','2018-04-12 03:22:21','',92,15,'发业','刷卡机',17,'2018-04-12 11:22:00',0),(359,277,'合同定金',7000.00,0,122,'daafd98d-c301-496d-a365-fded9002b50f','2018-04-12 05:56:23','2018-04-12 05:56:23','',40,15,'发业','支付宝',20,'2018-04-12 13:56:00',0),(360,278,'余款',300.00,0,123,'bd53f307-1f10-4d23-9e63-8719dec581d9','2018-04-12 06:08:31','2018-04-12 06:08:31','',42,15,'发业','微信',21,'2018-04-12 14:08:00',0),(361,279,'全款',3000.00,0,97,'34d2e492-ef9f-4129-8314-e22733419698','2018-04-12 08:17:23','2018-04-12 08:17:23','',92,15,'发业','微信',21,'2018-04-12 16:17:00',0),(362,280,'合同定金',5000.00,0,123,'5ad55e34-3a0f-4bd3-970c-2a3815a785e3','2018-04-12 09:07:48','2018-04-12 09:07:48','',40,15,'发业','微信',21,'2018-04-12 17:06:00',0),(363,281,'全款',1000.00,0,123,'0d369f80-72df-42f6-bbbe-d75459c35189','2018-04-12 09:10:35','2018-04-12 09:10:35','',92,15,'发业','刷卡机',17,'2018-04-12 17:10:00',0),(364,282,'合同定金',1000.00,0,97,'4ae61946-2208-47d8-a7b4-e39cca7d9e84','2018-04-12 09:29:54','2018-04-13 01:26:49','',40,15,'发业','支付宝',20,'2018-04-13 09:24:00',0),(365,283,'全款',7000.00,0,123,'b490e3e8-eb19-4e67-a942-73f8f527432a','2018-04-12 09:40:13','2018-04-12 09:40:13','',92,15,'发业','刷卡机',17,'2018-04-12 17:40:00',0),(366,284,'全款',3500.00,0,123,'8c65a48d-dc90-4d91-bc73-d8ce32b065b0','2018-04-12 09:55:02','2018-04-12 09:55:02','',92,15,'发业','农行',24,'2018-04-12 17:54:00',0),(367,288,'合同定金',1300.00,0,121,'91609501-7a93-4a7d-90ad-191c742d3ff7','2018-04-12 10:37:15','2018-04-12 10:37:15','自有地址定金800，记账半年一付定金500',40,15,'发业','微信',21,'2018-04-12 18:36:00',0),(368,287,'合同定金',1300.00,0,121,'13f3be8e-6656-4dc0-bc65-8d56523a67ba','2018-04-12 10:39:49','2018-04-12 10:39:49','自有注册定金800+记账半年一付定金500',40,15,'发业','微信',21,'2018-04-12 18:39:00',0),(369,286,'合同定金',1300.00,0,121,'e6d01f61-854f-4c73-aead-416b2f9c8ae5','2018-04-12 10:41:05','2018-04-12 10:41:05','自有地址注册800+记账半年一付定金500',40,15,'发业','微信',21,'2018-04-12 18:40:00',0),(370,285,'合同定金',1300.00,0,121,'633ab066-7793-4b5b-acbd-1d185f4d0a7b','2018-04-12 10:42:10','2018-04-12 10:42:10','自有地址注册800+记账半年一付定金500',40,15,'发业','微信',21,'2018-04-12 18:41:00',0),(371,289,'全款',4800.00,0,121,'fbc937b9-c9db-4623-bcbb-1f598c948c05','2018-04-12 10:46:33','2018-04-12 10:46:33','',92,15,'发业','支付宝',20,'2018-04-12 18:46:00',0),(372,290,'全款',3000.00,0,121,'92af5581-abe3-491f-92c2-173dad224848','2018-04-12 10:49:38','2018-04-12 10:49:38','',92,15,'发业','支付宝',20,'2018-04-12 18:49:00',0),(373,291,'合同定金',7000.00,0,122,'28f76e67-d9a1-4058-9deb-7207b280078f','2018-04-13 01:22:43','2018-04-13 01:22:43','',40,15,'发业','微信',21,'2018-04-13 09:22:00',0),(374,292,'全款',2500.00,0,122,'7e32181c-c6e3-4d11-a18f-9a5518173c2f','2018-04-13 01:25:41','2018-04-13 01:25:41','',92,15,'发业','刷卡机',17,'2018-04-13 09:25:00',0),(375,293,'全款',5300.00,0,122,'193c6e03-5f60-4fce-a645-24d49c4273fc','2018-04-13 01:28:05','2018-04-13 01:28:05','',92,15,'发业','微信',21,'2018-04-13 09:27:00',0),(376,294,'全款',1300.00,0,97,'7c5133ec-b402-4476-9980-5399465c9b7a','2018-04-13 01:28:54','2018-04-13 01:28:54','',92,15,'发业','微信',21,'2018-04-13 09:28:00',0),(377,295,'全款',3200.00,0,97,'6875d278-8696-4ea3-bf7c-39f77063b7b9','2018-04-13 01:45:49','2018-04-13 02:04:35','',92,15,'发业','支付宝',20,'2018-04-13 10:03:00',0),(378,296,'全款',10000.00,0,97,'0899c655-494e-4218-8736-6ca2557683f8','2018-04-13 01:52:10','2018-04-13 01:52:10','',92,15,'发业','中国银行',25,'2018-04-13 09:51:00',0),(379,297,'全款',2700.00,0,123,'3abeba2f-1a13-42ac-a9a1-e504ecd2f18b','2018-04-13 03:02:40','2018-04-13 03:02:40','',92,15,'发业','支付宝',20,'2018-04-13 11:02:00',0),(380,298,'全款',3060.00,0,122,'0c3e0a48-9d94-4c19-862c-adfd627f73af','2018-04-13 04:33:26','2018-04-13 04:33:26','',92,15,'发业','基本户',19,'2018-04-13 12:33:00',0),(381,298,'CA费用',200.00,0,122,'6200e3a7-a2e6-46c6-8479-927e60e2b543','2018-04-13 04:33:38','2018-04-13 04:33:38','',93,15,'发业','基本户',19,'2018-04-13 12:33:00',1),(382,299,'全款',4400.00,0,122,'021c850d-6274-4d50-8321-ab85a927ea99','2018-04-13 04:45:36','2018-04-13 04:46:04','',92,15,'发业','支付宝',20,'2018-04-13 12:45:00',0),(383,300,'合同定金',4500.00,0,122,'f6489441-437d-4326-9e41-49d29c8eb55a','2018-04-13 04:53:38','2018-04-13 04:53:38','',40,15,'发业','微信',21,'2018-04-13 12:53:00',0),(384,301,'全款',5500.00,0,97,'cc6ce8c1-fedf-41e6-ac36-3d8a06189b40','2018-04-13 05:12:14','2018-04-13 05:12:14','',92,15,'发业','刷卡机',17,'2018-04-13 13:12:00',0),(385,302,'全款',3000.00,0,97,'0d438ebd-f2f2-4936-8d62-730356723e3d','2018-04-13 05:26:08','2018-04-13 05:26:08','',92,15,'发业','微信',21,'2018-04-13 13:25:00',0),(386,303,'全款',800.00,0,123,'6e428ed6-1265-4a51-b25c-bd06646ed2c7','2018-04-13 07:46:23','2018-04-13 07:46:23','',92,15,'发业','微信',21,'2018-04-13 15:46:00',0),(387,304,'全款',800.00,0,97,'887d1c3c-f43a-47ea-8add-4511adf2426d','2018-04-13 08:10:02','2018-04-13 08:10:02','',92,15,'发业','微信',21,'2018-04-13 16:09:00',0),(388,305,'全款',1300.00,0,97,'e0ceb9b4-29a6-4012-927f-c7cc54ca0031','2018-04-13 09:30:35','2018-04-13 09:30:35','',92,15,'发业','刷卡机',17,'2018-04-13 17:30:00',0),(389,306,'全款',1800.00,0,123,'5451626f-0145-4138-8b7c-a8e2748921f2','2018-04-13 10:17:51','2018-04-16 02:08:32','',92,16,'商脉','微信',21,'2018-04-16 10:07:00',0),(390,307,'全款',5800.00,0,121,'93a2fa40-7243-45b6-956c-c22e04f7165b','2018-04-13 10:20:25','2018-04-13 10:20:25','',92,15,'发业','刷卡机',17,'2018-04-13 18:20:00',0),(391,308,'全款',6500.00,0,121,'7eb198b2-51db-42f6-87cf-ed06ea864d60','2018-04-13 10:24:27','2018-04-13 10:24:27','',92,15,'发业','微信',21,'2018-04-13 18:24:00',0),(392,309,'合同定金',5000.00,0,123,'a47d6d71-d1d9-44c7-a1ae-2ba79bbe5f45','2018-04-14 09:07:09','2018-04-16 02:17:29','',40,15,'发业','支付宝',20,'2018-04-16 10:13:00',0),(393,310,'全款',4360.00,0,97,'8eae0c2f-59ce-4265-9cc8-b25931433f4b','2018-04-15 07:21:54','2018-04-15 07:21:54','',92,15,'发业','支付宝',20,'2018-04-15 15:21:00',0),(394,311,'全款',5800.00,0,122,'b4fa6ead-27c5-4429-8236-16b11f590bf3','2018-04-15 09:32:34','2018-04-15 09:32:34','',92,15,'发业','刷卡机',17,'2018-04-15 17:32:00',0),(395,312,'全款',5800.00,0,122,'f1eeded3-d353-4eaf-9fe1-9d2c81fa51fb','2018-04-15 09:35:59','2018-04-15 09:35:59','',92,15,'发业','刷卡机',17,'2018-04-15 17:35:00',0),(396,313,'合同定金',9500.00,0,123,'bea66ad1-46cd-4f2c-873c-1731f5e6ce7f','2018-04-16 01:57:18','2018-04-16 02:01:36','注册定金7500+食品证定金1000+记账定金1000',40,15,'发业','刷卡机',17,'2018-04-16 10:00:00',0),(397,314,'全款',5800.00,0,121,'9e67f424-b2e1-43cf-8f89-14d562d68e62','2018-04-16 02:19:08','2018-04-16 02:19:08','',92,15,'发业','刷卡机',17,'2018-04-14 13:15:00',0),(398,315,'全款',5800.00,0,121,'9e22b488-706a-4f03-8a95-65c96c9a09a3','2018-04-16 02:27:19','2018-04-16 02:27:19','',92,15,'发业','微信',21,'2018-04-15 14:20:00',0),(399,316,'全款',5800.00,0,121,'2ba629ac-1578-4fcb-ba05-c4cfaf7f0db5','2018-04-16 02:30:23','2018-04-16 02:30:23','',92,15,'发业','刷卡机',17,'2018-04-15 14:40:00',0),(400,317,'全款',1600.00,0,121,'63b7ed54-ac14-4831-9d0e-972e99f1e6f8','2018-04-16 02:39:03','2018-04-16 02:39:03','',92,15,'发业','支付宝',20,'2018-04-13 20:20:00',0),(401,318,'全款',3060.00,0,121,'7244d409-a82e-4c48-8849-821e09ce5d1c','2018-04-16 04:03:49','2018-04-16 04:03:49','',92,15,'发业','支付宝',20,'2018-04-16 12:03:00',0),(402,319,'全款',4000.00,0,123,'1c921faf-536c-4b3d-8ea7-0ecdf3795b7d','2018-04-16 06:13:40','2018-04-16 08:56:11','',92,16,'商脉','微信',21,'2018-04-16 16:55:00',0),(403,320,'全款',3500.00,0,123,'95d2f1e5-e5a9-4296-b620-339d0bd4e1e1','2018-04-16 06:50:07','2018-04-16 06:50:07','',92,15,'发业','支付宝',20,'2018-04-16 14:49:00',0),(404,321,'全款',1300.00,0,122,'e5a6e27a-2042-4e7b-8a2b-10eda42804db','2018-04-16 08:17:44','2018-04-16 08:17:44','',92,15,'发业','微信',21,'2018-04-16 16:17:00',0),(405,322,'全款',2700.00,0,122,'7f8b704a-5a74-48b6-b527-eacb67136019','2018-04-16 08:25:19','2018-04-16 08:59:05','',92,15,'发业','中国银行',25,'2018-04-16 16:58:00',0),(407,324,'全款',900.00,0,123,'ce27d0f8-4a93-4b37-972a-e40b8e0f9c75','2018-04-16 09:34:17','2018-04-16 09:37:15','',92,16,'商脉','微信',21,'2018-04-16 17:37:00',0),(408,325,'全款',1500.00,0,123,'05456b21-07af-4f68-adac-4b68b8f46053','2018-04-16 09:42:19','2018-04-16 09:42:19','',92,15,'发业','中国银行',25,'2018-04-16 17:41:00',0),(409,326,'全款',800.00,0,97,'02f415b7-c0d7-49a3-b2dc-ea7f9a7c9e50','2018-04-16 09:45:41','2018-04-16 09:45:41','',92,15,'发业','微信',21,'2018-04-16 17:45:00',0),(410,327,'全款',3000.00,0,121,'f568acb0-ab43-413f-a059-176eabc8bc20','2018-04-16 10:21:43','2018-04-17 02:50:00','',92,15,'发业','刷卡机',17,'2018-04-17 10:36:00',0),(411,329,'全款',1300.00,0,121,'6354836d-8c08-40ba-b6d5-955e0db207ba','2018-04-17 01:13:40','2018-04-17 01:13:40','',92,15,'发业','微信',21,'2018-04-16 17:45:00',0),(412,330,'全款',700.00,0,122,'797fdc03-8bf0-4894-a26f-cf7280dc43a4','2018-04-17 02:49:39','2018-04-17 02:49:39','',92,15,'发业','刷卡机',17,'2018-04-17 10:49:00',0),(413,328,'全款',5500.00,0,119,'e5a34398-c90e-453d-8246-b77fd047a8ea','2018-04-17 03:08:58','2018-04-17 03:08:58','外资 王楠楠-艾达旗  返佣金5500',92,15,'发业','工行',22,'2018-04-15 11:05:00',0),(414,331,'全款',2000.00,0,123,'e7537ec5-d120-4c69-a9b6-1fd090174e23','2018-04-17 03:43:53','2018-04-17 03:43:53','',92,15,'发业','刷卡机',17,'2018-04-17 11:43:00',0),(415,332,'全款',3500.00,0,123,'7cc79c22-02e9-4671-a90f-2d782202bccb','2018-04-17 06:05:27','2018-04-17 07:27:40','',92,16,'商脉','微信',21,'2018-04-17 15:26:00',0),(416,230,'办结尾款',100.00,0,123,'7f292d3f-c079-4ee9-be85-9b888f4aaee7','2018-04-17 07:20:59','2018-04-18 01:16:49','客户钱已经转给陈总了',43,15,'发业','微信',21,'2018-04-18 09:15:00',0),(417,333,'全款',2200.00,0,123,'3a844df9-df25-461a-8add-78b18027f6ae','2018-04-17 08:15:16','2018-04-17 08:15:16','客户一笔800款项转个了曹艳，一笔1400面对面转的',92,15,'发业','微信',21,'2018-04-17 16:14:00',0),(418,334,'全款',4800.00,0,122,'12c0c175-7815-452b-957f-0ac79ed95ad3','2018-04-17 08:55:42','2018-04-17 08:55:42','',92,15,'发业','刷卡机',17,'2018-04-17 16:55:00',0),(419,335,'全款',3000.00,0,123,'4bc0df34-e4d8-4af3-b239-5c5048a0d02f','2018-04-17 09:00:51','2018-04-17 09:00:51','',92,15,'发业','微信',21,'2018-04-17 17:00:00',0),(420,336,'全款',850.00,0,122,'73e71e50-eb1a-449f-b1dc-ab9790c99a08','2018-04-17 09:23:24','2018-04-17 09:23:24','',92,15,'发业','微信',21,'2018-04-17 17:22:00',0),(421,337,'全款',4500.00,0,97,'dda16d0e-9a28-4fbc-a532-5a0402df2fa2','2018-04-18 01:34:42','2018-04-18 01:34:42','',92,15,'发业','微信',21,'2018-04-18 09:34:00',0),(422,323,'全款',5000.00,0,97,'8c9d2590-101c-42e9-b869-76a6ab01a08c','2018-04-18 01:47:22','2018-04-18 01:47:22','实际录业绩金额为5000元，到时候需要返点1000元给客户',92,15,'发业','基本户',19,'2018-04-17 10:45:00',0),(423,323,'其他',1000.00,0,97,'55fae1e2-f139-42d8-96c2-8d08ec18db57','2018-04-18 01:47:54','2018-04-18 01:47:54','实际录业绩金额为5000元，到时候需要返点1000元给客户',97,15,'发业','基本户',19,'2018-04-17 13:50:00',1),(424,338,'全款',5000.00,0,121,'4a63c256-df9c-42a1-bbb0-a74ca502e6c6','2018-04-18 02:17:48','2018-04-18 02:17:48','',92,15,'发业','农行',24,'2018-04-18 10:17:00',0),(425,255,'余款',2500.00,0,123,'95fdc97d-06d5-4c66-85eb-487ca927be73','2018-04-18 03:18:39','2018-04-18 03:18:39','补交二次代理记账服务费2500.2018.2.5-2019.1.',42,15,'发业','支付宝',20,'2018-04-18 11:17:00',0),(426,255,'CA费用',500.00,0,123,'b689cb07-e0a0-495e-a8d8-59dbdbe5d90c','2018-04-18 03:19:16','2018-04-18 03:19:16','代买CA200.首次申请发票300.共计3000',93,15,'发业','支付宝',20,'2018-04-18 11:18:00',1),(427,339,'全款',6060.00,0,97,'bb9a409e-e089-43af-93bc-36d028b257a5','2018-04-18 03:21:57','2018-04-18 03:44:26','',92,15,'发业','刷卡机',17,'2018-04-18 11:43:00',0),(429,340,'全款',1500.00,0,123,'7a80fa6b-cb32-4bcc-8b58-99bb9eef84ec','2018-04-18 03:53:09','2018-04-18 03:53:09','',92,15,'发业','微信',21,'2018-04-18 11:52:00',0),(430,339,'CA费用',200.00,0,97,'c60e8d26-4d89-4fbe-bf39-27cb0eb6b970','2018-04-18 05:41:35','2018-04-18 05:41:35','',93,15,'发业','刷卡机',17,'2018-04-18 13:41:00',1),(431,341,'合同定金',3300.00,0,97,'91aee254-ae41-4f51-bb0d-7c969b1b38eb','2018-04-18 05:50:07','2018-04-18 05:50:07','',40,15,'发业','微信',21,'2018-04-18 13:49:00',0),(432,343,'全款',800.00,0,123,'96bff743-3f13-4578-9c29-540d0a6e9658','2018-04-18 07:18:28','2018-04-18 07:18:28','',92,15,'发业','现金',18,'2018-04-18 15:18:00',0),(433,344,'全款',3000.00,0,122,'4373d437-6017-4df6-9ca0-eb8a54688aaf','2018-04-18 07:50:48','2018-04-18 07:50:48','',92,15,'发业','刷卡机',17,'2018-04-18 15:50:00',0),(434,345,'全款',5560.00,0,97,'f80c4311-d8cf-431c-aba1-7d4ff4f4ade3','2018-04-18 08:12:09','2018-04-18 08:12:09','',92,15,'发业','刷卡机',17,'2018-04-18 16:11:00',0),(435,346,'全款',6500.00,0,97,'073b28fb-83d8-42d2-949f-f273fb524a79','2018-04-18 08:23:32','2018-04-18 08:23:32','',92,15,'发业','微信',21,'2018-04-18 16:23:00',0),(436,347,'全款',900.00,0,123,'84d844fe-3a7e-416f-9925-80c9a2ecdbf6','2018-04-18 08:36:58','2018-04-18 08:38:56','',92,16,'商脉','微信',21,'2018-04-18 16:38:00',0),(437,348,'全款',7000.00,0,97,'b64d5737-e3e5-459a-97f5-8361de5804f2','2018-04-18 08:42:47','2018-04-18 08:42:47','',92,15,'发业','微信',21,'2018-04-18 16:42:00',0),(438,349,'合同定金',3800.00,0,122,'0c62368b-2502-4763-b384-f0849bbfa53e','2018-04-18 08:52:35','2018-04-18 08:52:35','',40,15,'发业','基本户',19,'2018-04-18 16:52:00',0),(439,342,'全款',1500.00,0,97,'0e78bead-a5a6-4993-a2c5-a6fac3a6b75e','2018-04-18 08:53:30','2018-04-18 08:53:30','',92,15,'发业','微信',21,'2018-04-18 16:50:00',0),(440,350,'全款',1800.00,0,123,'6abf80ac-7174-4714-ac93-32727dd70cfb','2018-04-18 09:17:09','2018-04-18 09:17:09','',92,15,'发业','支付宝',20,'2018-04-18 17:16:00',0),(441,351,'合同定金',1500.00,0,123,'73523903-d9b9-4d5d-b22d-0abbc62bbfdf','2018-04-18 09:45:26','2018-04-18 09:45:26','',40,15,'发业','基本户',19,'2018-04-18 17:45:00',0),(442,352,'全款',900.00,0,121,'aece33cd-ec1d-4f00-acc0-391f267e9314','2018-04-18 10:01:47','2018-04-18 10:01:47','',92,15,'发业','微信',21,'2018-04-18 18:01:00',0),(443,353,'全款',2700.00,0,121,'fac63b4c-e03b-4871-97bb-6df6398a0d5b','2018-04-18 10:14:07','2018-04-18 10:14:07','',92,15,'发业','微信',21,'2018-04-18 18:13:00',0),(444,354,'全款',3000.00,0,121,'f328d9a8-c38f-4af4-8caf-7299343c3b26','2018-04-18 10:17:53','2018-04-19 01:09:31','',92,16,'商脉','微信',21,'2018-04-19 09:08:00',0),(445,355,'全款',5800.00,0,121,'d71bbbac-6d2c-4639-8ccd-2ee58610bb8f','2018-04-18 10:21:19','2018-04-18 10:21:19','',92,15,'发业','刷卡机',17,'2018-04-18 18:21:00',0),(446,356,'全款',5800.00,0,121,'74e09585-61c6-4ff9-810e-312a2efbdf7c','2018-04-18 10:23:22','2018-04-18 10:23:22','',92,15,'发业','刷卡机',17,'2018-04-18 18:23:00',0),(447,357,'全款',5800.00,0,121,'d5c0ef2c-f417-43c3-9c30-00b304358b33','2018-04-18 10:25:46','2018-04-18 10:25:46','',92,15,'发业','刷卡机',17,'2018-04-18 18:25:00',0),(448,358,'全款',5800.00,0,121,'d60aa168-820e-479e-a80a-01415c984547','2018-04-18 10:27:23','2018-04-18 10:27:23','',92,15,'发业','微信',21,'2018-04-18 18:27:00',0),(449,359,'全款',2000.00,0,94,'783f3ec8-aefc-4e2b-bd81-ad12d605cd22','2018-04-19 01:17:54','2018-04-19 01:17:54','客户分两次给钱',92,15,'发业','微信',21,'2018-04-19 09:17:00',0),(450,360,'全款',800.00,0,123,'e318f055-9bd5-408d-b44c-5f961dc296ba','2018-04-19 01:46:45','2018-04-19 03:48:35','',92,16,'商脉','微信',21,'2018-04-19 11:48:00',0),(451,361,'全款',9430.00,0,121,'b701a718-c00f-40d9-b9cb-3dbe06f7574c','2018-04-19 04:41:50','2018-04-19 04:41:50','内部客户杨俊—广州新台旺生物科技有限公司     800变更增资+230元（2018.4月份记账）+一般纳税人资格认定1200+一般纳税人记账7200元免账册，一起共9430   记账一般纳税人是7200一年免账册（2018.5月份开始）业绩实为6440',92,15,'发业','中国银行',25,'2018-04-19 12:40:00',0),(452,362,'全款',3060.00,0,121,'a46b5e75-0ebd-4979-8363-127de3ea7195','2018-04-19 04:51:51','2018-04-19 04:51:51','代收ca200',92,15,'发业','微信',21,'2018-04-19 12:51:00',0),(453,362,'CA费用',200.00,0,121,'470f4b72-fd95-4a67-b225-042fa7f8939e','2018-04-19 04:53:07','2018-04-19 04:53:07','',93,15,'发业','微信',21,'2018-04-19 12:51:00',1),(454,363,'全款',3800.00,0,121,'c79a5556-ec10-4e68-be16-e67c6c7374fc','2018-04-19 04:59:21','2018-04-19 06:19:20','客户补账2017.11-2018.3月份800元+一年记账2700+账册300/年，一起3800（含税），额外代收ca200元，2017年工商年检费用100，一起4100元',92,15,'发业','刷卡机',17,'2018-04-19 14:19:00',0),(455,364,'全款',3000.00,0,123,'3a2e16a1-a194-4890-b97d-1885499e4109','2018-04-19 05:59:25','2018-04-19 05:59:25','之前微信给了200，今天基本户转了2800.',92,15,'发业','基本户',19,'2018-04-19 13:57:00',0),(456,363,'CA费用',200.00,0,121,'003eda9a-9db5-4d31-91e0-92b3b58f07c8','2018-04-19 06:19:03','2018-04-19 06:19:03','客户补账2017.11-2018.3月份800元+一年记账2700+账册300/年，一起3800（含税），额外代收ca200元，2017年工商年检费用100，一起4100元',93,15,'发业','刷卡机',17,'2018-04-19 14:18:00',1),(457,365,'全款',200.00,0,121,'d48527e0-0b3d-4bce-b42f-4ea6e9d99896','2018-04-19 06:39:05','2018-04-19 06:39:05','',92,15,'发业','微信',21,'2018-04-19 14:38:00',0),(458,366,'全款',1500.00,0,97,'395c1aae-5f05-46ea-99c2-bb6db333ed4e','2018-04-19 06:41:51','2018-04-19 06:51:44','',92,16,'商脉','微信',21,'2018-04-19 14:51:00',0),(459,367,'全款',600.00,0,97,'cb13b27b-15fa-4bda-b4e0-280c96f36aa7','2018-04-19 07:18:41','2018-04-19 09:10:46','',92,16,'商脉','微信',21,'2018-04-19 16:55:00',0),(460,368,'全款',2700.00,0,123,'9611a181-6bf1-4007-84d4-8c6a3f7fb3e9','2018-04-19 07:44:46','2018-04-19 07:44:46','',92,15,'发业','中国银行',25,'2018-04-19 15:44:00',0),(461,368,'CA费用',200.00,0,123,'b179edef-5ecb-4e62-97b9-10b0a5ce207d','2018-04-19 07:46:16','2018-04-19 07:46:16','',93,15,'发业','中国银行',25,'2018-04-19 15:44:00',1),(462,369,'全款',2500.00,0,123,'52f69249-8e8c-4c37-be20-44ea362ecbfb','2018-04-19 09:39:34','2018-04-19 09:39:34','',92,15,'发业','微信',21,'2018-04-19 17:39:00',0),(463,370,'全款',1300.00,0,121,'a388e551-35bc-43b0-925a-ed60ea613b86','2018-04-19 10:04:35','2018-04-19 10:04:35','',92,15,'发业','刷卡机',17,'2018-04-19 18:04:00',0),(464,371,'全款',7260.00,0,121,'8838f17f-ef60-45c2-9d59-05b816b101e2','2018-04-19 10:20:38','2018-04-19 10:20:38','远程客户',92,15,'发业','工行',22,'2018-04-19 18:20:00',0);
/*!40000 ALTER TABLE `t_projects_income_old` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:53
