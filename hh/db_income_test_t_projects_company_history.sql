-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test
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
-- Table structure for table `t_projects_company_history`
--

DROP TABLE IF EXISTS `t_projects_company_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_company_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `company` varchar(45) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_company_history`
--

LOCK TABLES `t_projects_company_history` WRITE;
/*!40000 ALTER TABLE `t_projects_company_history` DISABLE KEYS */;
INSERT INTO `t_projects_company_history` VALUES (1,2179,'广州卡南贸易有限公司','李佳欣',268,'2018-08-08 02:32:29'),(2,1079,'广州比弗溪生态农业发展有限公司','钟东梅',136,'2018-08-08 02:53:34'),(3,1793,'广东晾伊佳智能家居科技有限公司','钟东梅',136,'2018-08-09 09:43:55'),(4,2236,'肤博士医疗科技（广州）有限公司','陈小银',106,'2018-08-10 08:04:27'),(5,2227,'广州耕田文化传播有限公司','陈勇极',139,'2018-08-14 08:04:24'),(6,2313,'寰东','吴蔚亮',98,'2018-08-16 01:02:23'),(7,2340,'广州嘉润丰贸易有限公司','陈小银',106,'2018-08-17 07:04:40'),(8,2353,'广州力天机械设备有限公司','庄培润',97,'2018-08-17 08:03:07'),(9,2238,'广东盈东动漫文化有限公司','吴凤',99,'2018-08-20 05:46:40'),(10,1522,'广州邻家商贸有限公司','吴凤',99,'2018-08-20 07:25:16'),(11,2401,'北京星吧客公寓管理有限公司第一分公司','梁倩',296,'2018-08-22 03:45:11'),(12,2402,'美联美家房地产经纪（北京）有限公司第一分公司','梁倩',296,'2018-08-22 03:45:44'),(13,2424,'广州嘉哲科技有限公司','陈小银',106,'2018-08-23 01:24:08'),(14,2363,'广州誉天科技有限公司','陈小银',106,'2018-08-23 01:52:14'),(15,2459,'广州爱上美科技有限公司','陶君怡',269,'2018-08-24 02:19:29'),(16,2406,'广州荣盛服装贸易有限公司','陈小银',106,'2018-08-24 07:16:50'),(17,2333,'暂无','钟明霞',137,'2018-08-27 00:38:23'),(18,2459,'广州爱上美贸易有限公司','陶君怡',269,'2018-08-27 09:19:59'),(19,2430,'广州科迪信息科技有限公司','陈小银',106,'2018-08-27 09:37:19'),(20,2510,'广州华铚贸易有限公司','陈小银',106,'2018-08-28 02:16:12'),(21,2516,'广州宇锐贸易有限公司','陶君怡',269,'2018-08-28 07:47:57'),(22,2514,'广州车尚劲汽车有限公司','梁倩',296,'2018-08-29 01:38:49'),(23,2521,'广州乐中投资有限公司','陈小银',106,'2018-08-29 08:49:41');
/*!40000 ALTER TABLE `t_projects_company_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:33:30
