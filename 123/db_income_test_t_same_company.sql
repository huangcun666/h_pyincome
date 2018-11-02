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
-- Table structure for table `t_same_company`
--

DROP TABLE IF EXISTS `t_same_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_same_company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `customer_company` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_same_company`
--

LOCK TABLES `t_same_company` WRITE;
/*!40000 ALTER TABLE `t_same_company` DISABLE KEYS */;
INSERT INTO `t_same_company` VALUES (1,2266,1333,'广州极易懂企业信息咨询有限公司'),(2,1806,3407,'广州旭乐康科技有限公司'),(3,1915,3807,'小铭电子材料科技（广州）有限公司'),(4,2276,2959,'威宁物业投资（广州）有限公司'),(5,2275,2958,'威利控股(广州）有限公司'),(6,2274,2957,'澳中投资控股（广州）有限公司'),(7,1191,3348,'广州铭潮电子商务有限公司'),(8,2286,1940,'广州新迪网络科技有限公司'),(9,2192,3985,'广州市微琴湾服饰有限公司'),(10,2289,3421,'广州新希望信息咨询有限公司'),(11,2289,3421,'广州新希望信息咨询有限公司'),(12,2289,3421,'广州新希望信息咨询有限公司'),(13,2289,3421,'广州新希望信息咨询有限公司'),(14,2282,1881,'广东坤玛机电有限公司'),(15,2291,3537,'东方撒艺（广州）文化发展有限公司'),(16,1752,3684,'广州聚美传奇生物科技有限公司'),(17,2305,3185,'广州闪电健身体育有限公司'),(18,2306,858,'广州酷动体育发展有限公司'),(19,1912,4026,'上海励宏清洁服务有限公司广东分公司'),(20,2318,3961,'广州市力天机械设备有限公司'),(21,2311,2800,'广州汇锦能效科技有限公司'),(22,2322,3974,'广州昇达信息科技有限公司'),(23,2324,3974,'广州昇达信息科技有限公司'),(24,2329,1398,'广州霖智服饰有限公司'),(25,2338,3651,'广州朗晟实业投资有限公司'),(26,2344,1486,'共睹（广州）网络科技有限公司'),(27,2344,1486,'共睹（广州）网络科技有限公司'),(28,2353,3961,'广州市力天机械设备有限公司'),(29,2348,4041,'广州富利来科技有限公司'),(30,2349,4040,'广州广聚合科技有限公司'),(31,2372,1142,'广州万米投资咨询有限公司'),(32,2397,3040,'广州智聚众创空间有限公司'),(33,367,3468,'广州市曾城锦连居饮品店'),(34,1962,3442,'广州亚渼罗夕服饰有限公司'),(35,2403,3844,'广州常荣服饰有限公司'),(36,2408,3779,'广东旺程易购商贸有限公司'),(37,2413,4036,'广州金睿企业管理有限公司'),(38,2405,1974,'广州明心心理咨询有限责任公司'),(39,2429,1255,'广州真亦好服饰有限公司'),(40,2446,111,'广州凡几文化发展有限公司'),(41,2455,4097,'广州科迪信息科技有限公司'),(42,2444,3862,'广州云建影视科技有限公司'),(43,2453,4095,'广州淘米艺术有限公司'),(44,2451,4103,'广州福斯廷国际进出口有限公司'),(45,2463,4020,'广州米亚诺建筑装饰材料有限公司'),(46,2462,4107,'广东京卫人力资源有限公司'),(47,2464,4109,'广州微媒信息科技有限公司'),(48,2476,1315,'广州垦垦餐饮管理有限公司'),(49,2478,3135,'广州籁越服饰有限公司'),(50,2484,1553,'广州鑫达顺恒商务服务有限公司'),(51,2489,1774,'佰迪（广州）清洁服务有限公司'),(52,2490,1774,'佰迪（广州）清洁服务有限公司'),(53,2501,1553,'广州鑫达顺恒商务服务有限公司'),(54,2506,4027,'广州市南沙区我们家蛋糕烘焙店'),(55,2515,2277,'广州腾睿控股有限公司'),(56,2526,3942,'广州西汉传媒科技有限公司'),(57,2526,3942,'广州西汉传媒科技有限公司'),(58,2527,2770,'银信联（广州）科技有限公司'),(59,2540,3565,'广州市海珠区小家菜美食店'),(60,2542,1243,'广州布可说贸易有限公司'),(61,741,3326,'金狮保安服务（深圳）有限公司广州分公司'),(62,2541,1679,'广州德匠建筑有限公司');
/*!40000 ALTER TABLE `t_same_company` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:17
