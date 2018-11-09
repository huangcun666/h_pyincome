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
-- Table structure for table `t_projects_income_count`
--

DROP TABLE IF EXISTS `t_projects_income_count`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_income_count` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ca` datetime DEFAULT NULL COMMENT '时间\n',
  `ssim` decimal(18,2) NOT NULL DEFAULT '0.00' COMMENT '每行总数\n',
  `us` varchar(2500) DEFAULT '' COMMENT '每天人跟到款金额\n',
  `team_name` varchar(45) DEFAULT NULL,
  `type_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=269 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_income_count`
--

LOCK TABLES `t_projects_income_count` WRITE;
/*!40000 ALTER TABLE `t_projects_income_count` DISABLE KEYS */;
INSERT INTO `t_projects_income_count` VALUES (1,'2018-04-20 00:00:00',92910.00,'赵松筑|15660.00,何健锋|3900.00,何家辉|30860.00,冉小凤|150.00,庄培润|42340.00','销售顾问',NULL),(2,'2018-04-21 00:00:00',34680.00,'何家辉|5000.00,庄培润|23880.00,赵松筑|5800.00','销售顾问',NULL),(3,'2018-04-22 00:00:00',5000.00,'何家辉|5000.00','销售顾问',NULL),(4,'2018-04-23 00:00:00',297483.00,'李晓琴|7000.00,何健锋|35960.00,赵松筑|61600.00,何家辉|91228.00,孙泽阳|400.00,庄培润|101295.00','销售顾问',NULL),(5,'2018-04-24 00:00:00',233800.00,'赵松筑|56660.00,何健锋|59660.00,何家辉|72560.00,庄培润|44920.00','销售顾问',NULL),(6,'2018-04-25 00:00:00',164760.00,'庄培润|58360.00,李晓琴|9800.00,何健锋|8300.00,李静|12450.00,何家辉|19960.00,罗文波|5500.00,冯恒冠|2000.00,赵松筑|48390.00','销售顾问',NULL),(7,'2018-04-26 00:00:00',72540.00,'何家辉|26500.00,庄培润|31740.00,李静|12000.00,罗文波|1500.00,赵松筑|800.00','销售顾问',NULL),(8,'2018-04-27 00:00:00',70570.00,'李晓琴|13120.00,何健锋|12380.00,李静|8200.00,何家辉|4060.00,赵松筑|17010.00,冯恒冠|300.00,庄培润|15500.00','销售顾问',NULL),(9,'2018-04-28 00:00:00',22700.00,'廖小捷|2500.00,赵松筑|13260.00,何家辉|800.00,庄培润|6140.00','销售顾问',NULL),(10,'2018-04-29 00:00:00',10960.00,'李晓琴|4360.00,赵松筑|6600.00','销售顾问',NULL),(11,'2018-05-02 00:00:00',74520.00,'何健锋|7000.00,何家辉|6000.00,庄培润|30460.00,赵松筑|31060.00','销售顾问',NULL),(12,'2018-05-03 00:00:00',66800.00,'李静|16700.00,何家辉|6600.00,赵松筑|11760.00,冉小凤|1000.00,庄培润|13320.00,李晓琴|9060.00,何健锋|8360.00','销售顾问',NULL),(13,'2018-05-04 00:00:00',69530.00,'李晓琴|200.00,李静|32860.00,何健锋|2970.00,赵松筑|4500.00,何家辉|15500.00,庄培润|13500.00','销售顾问',NULL),(14,'2018-05-07 00:00:00',147560.00,'庄培润|18040.00,李晓琴|30220.00,李静|38980.00,何健锋|26700.00,赵松筑|25660.00,何家辉|7960.00','销售顾问',NULL),(15,'2018-05-08 00:00:00',73690.00,'何健锋|11210.00,罗文波|3800.00,何家辉|7600.00,赵松筑|1900.00,庄培润|8300.00,李晓琴|20300.00,李静|20580.00','销售顾问',NULL),(16,'2018-05-09 00:00:00',42080.00,'李晓琴|7560.00,李静|7560.00,罗文波|300.00,何健锋|11800.00,庄培润|14860.00','销售顾问',NULL),(17,'2018-05-10 00:00:00',65946.00,'何家辉|9700.00,庄培润|500.00,李晓琴|14120.00,李静|9026.00,何健锋|3800.00,赵松筑|28800.00','销售顾问',NULL),(18,'2018-05-11 00:00:00',40360.00,'赵松筑|24700.00,何健锋|7900.00,庄培润|4000.00,李晓琴|2260.00,李静|1500.00','销售顾问',NULL),(19,'2018-05-12 00:00:00',2500.00,'李晓琴|2500.00','销售顾问',NULL),(20,'2018-05-14 00:00:00',84320.00,'朱伟峰|11600.00,李晓琴|13000.00,何健锋|8300.00,李静|21360.00,何家辉|9560.00,赵松筑|15000.00,庄培润|5500.00','销售顾问',NULL),(21,'2018-05-15 00:00:00',135878.00,'何健锋|14300.00,赵松筑|6000.00,何家辉|27450.00,庄培润|29588.00,李晓琴|37060.00,李静|21480.00','销售顾问',NULL),(22,'2018-05-16 00:00:00',38980.00,'李静|5810.00,罗文波|3480.00,何家辉|10800.00,李晓琴|18590.00,李江友|300.00','销售顾问',NULL),(23,'2018-05-17 00:00:00',104294.18,'李江友|7074.18,李静|4700.00,何健锋|43100.00,赵松筑|2200.00,庄培润|39160.00,李晓琴|8060.00','销售顾问',NULL),(24,'2018-05-18 00:00:00',122465.00,'李静|33180.00,庄培润|28385.00,赵松筑|22200.00,庞陈雪|800.00,朱伟峰|23700.00,何健锋|6600.00,李晓琴|5600.00,何家辉|2000.00','销售顾问',NULL),(25,'2018-05-19 00:00:00',33200.00,'庄培润|15800.00,赵松筑|17400.00','销售顾问',NULL),(26,'2018-05-20 00:00:00',12200.00,'李静|10700.00,李晓琴|1500.00','销售顾问',NULL),(27,'2018-05-21 00:00:00',64260.00,'朱伟峰|11600.00,李晓琴|16100.00,何健锋|1500.00,李静|7400.00,何家辉|10400.00,赵松筑|4460.00,庄培润|12800.00','销售顾问',NULL),(28,'2018-05-22 00:00:00',52860.00,'李静|17000.00,何家辉|1300.00,庄培润|26760.00,朱伟峰|1000.00,李晓琴|2000.00,何健锋|4800.00','销售顾问',NULL),(29,'2018-05-23 00:00:00',67660.00,'罗文波|3000.00,何健锋|13100.00,赵松筑|15000.00,庄培润|14680.00,李晓琴|6200.00,李静|15680.00','销售顾问',NULL),(30,'2018-05-24 00:00:00',72840.00,'李晓琴|24690.00,李静|19460.00,何健锋|12030.00,罗文波|4800.00,冯恒冠|200.00,赵松筑|2000.00,庄培润|9660.00','销售顾问',NULL),(31,'2018-05-25 00:00:00',60900.00,'何家辉|13600.00,庄培润|22960.00,李晓琴|3500.00,李静|20840.00','销售顾问',NULL),(32,'2018-05-26 00:00:00',164500.00,'赵松筑|68600.00,何家辉|58000.00,庄培润|8400.00,李静|500.00,何健锋|29000.00','销售顾问',NULL),(33,'2018-05-27 00:00:00',112000.00,'李静|24000.00,何健锋|23200.00,赵松筑|23200.00,何家辉|17400.00,朱伟峰|12600.00,李晓琴|11600.00','销售顾问',NULL),(34,'2018-05-28 00:00:00',176107.00,'廖小捷|3500.00,李晓琴|15190.00,何健锋|20900.00,李静|24020.00,何家辉|500.00,赵松筑|100597.00,庄培润|11400.00','销售顾问',NULL),(35,'2018-05-29 00:00:00',197577.00,'何健锋|15540.00,杨辉|68500.00,何家辉|28900.00,赵松筑|23200.00,庄培润|32197.00,李晓琴|13520.00,李静|15720.00','销售顾问',NULL),(36,'2018-05-30 00:00:00',122870.00,'朱伟峰|34800.00,李晓琴|7560.00,李静|5960.00,何家辉|30200.00,杨辉|5800.00,庄培润|9850.00,赵松筑|28700.00','销售顾问',NULL),(37,'2018-05-31 00:00:00',74248.00,'杨辉|6600.00,何家辉|40600.00,赵松筑|6200.00,庄培润|13800.00,李晓琴|1560.00,李静|5488.00','销售顾问',NULL),(38,'2018-06-01 00:00:00',71310.00,'李晓琴|4200.00,杨辉|3200.00,何健锋|12850.00,赵松筑|23200.00,庄培润|16760.00,朱伟峰|11100.00','销售顾问',NULL),(39,'2018-06-02 00:00:00',25900.00,'李晓琴|1500.00,杨辉|11600.00,何家辉|7000.00,朱伟峰|5800.00','销售顾问',NULL),(40,'2018-06-03 00:00:00',45360.00,'朱伟峰|11600.00,李晓琴|1500.00,杨辉|5800.00,何家辉|5800.00,赵松筑|11600.00,庄培润|9060.00','销售顾问',NULL),(41,'2018-06-04 00:00:00',93180.00,'李静|24420.00,何家辉|1300.00,杨辉|5800.00,庄培润|12140.00,赵松筑|6000.00,朱伟峰|11600.00,李晓琴|26120.00,何健锋|5800.00','销售顾问',NULL),(42,'2018-06-05 00:00:00',107920.00,'赵松筑|3500.00,朱伟峰|4800.00,李晓琴|14360.00,李静|4260.00,何家辉|49800.00,杨辉|11600.00,庄培润|19600.00','销售顾问',NULL),(43,'2018-06-06 00:00:00',71080.00,'李静|15650.00,何家辉|5800.00,赵松筑|6000.00,庄培润|27950.00,朱伟峰|5800.00,李晓琴|9880.00','销售顾问',NULL),(44,'2018-06-07 00:00:00',29420.00,'李静|12360.00,杨辉|5800.00,何家辉|3000.00,庄培润|3900.00,李晓琴|4360.00','销售顾问',NULL),(45,'2018-06-08 00:00:00',37480.00,'李晓琴|4000.00,李静|23280.00,何健锋|4800.00,庄培润|5400.00','销售顾问',NULL),(46,'2018-06-09 00:00:00',26600.00,'何健锋|10300.00,庄培润|16300.00','销售顾问',NULL),(47,'2018-06-10 00:00:00',38060.00,'赵松筑|11600.00,何健锋|5800.00,朱伟峰|11600.00,李晓琴|3000.00,李静|6060.00','销售顾问',NULL),(48,'2018-06-11 00:00:00',105128.00,'李静|21200.00,何健锋|17400.00,杨辉|4800.00,何家辉|20200.00,赵松筑|5100.00,庄培润|25180.00,李晓琴|11248.00','销售顾问',NULL),(49,'2018-06-12 00:00:00',72440.00,'朱伟峰|5800.00,李晓琴|12760.00,李静|15580.00,何家辉|5800.00,杨辉|10600.00,庄培润|21900.00','销售顾问',NULL),(50,'2018-06-13 00:00:00',57780.00,'何家辉|17400.00,杨辉|5800.00,冯恒冠|300.00,庄培润|11200.00,李晓琴|7160.00,李静|15920.00','销售顾问',NULL),(51,'2018-06-14 00:00:00',42480.00,'赵松筑|17600.00,何家辉|8700.00,庄培润|11620.00,李晓琴|4560.00','销售顾问',NULL),(52,'2018-06-15 00:00:00',93500.00,'何健锋|12400.00,庄培润|38540.00,李晓琴|29360.00,李静|13200.00','销售顾问',NULL),(53,'2018-06-16 00:00:00',7300.00,'李静|7300.00','销售顾问',NULL),(54,'2018-06-17 00:00:00',21200.00,'何家辉|5800.00,杨辉|15400.00','销售顾问',NULL),(55,'2018-06-18 00:00:00',5800.00,'杨辉|5800.00','销售顾问',NULL),(56,'2018-06-19 00:00:00',75798.00,'何健锋|11600.00,庄培润|28598.00,朱伟峰|15800.00,李静|13200.00,赵松筑|6600.00','销售顾问',NULL),(57,'2018-06-20 00:00:00',86468.00,'何健锋|5800.00,赵松筑|5800.00,庄培润|17048.00,朱伟峰|11600.00,李静|23020.00,杨辉|23200.00','销售顾问',NULL),(58,'2018-06-21 00:00:00',85798.00,'赵松筑|22160.00,庄培润|20690.00,李静|39348.00,杨辉|3600.00','销售顾问',NULL),(59,'2018-06-22 00:00:00',35000.00,'庄培润|18700.00,李静|16300.00','销售顾问',NULL),(60,'2018-06-23 00:00:00',19155.00,'何家辉|11600.00,庄培润|7555.00','销售顾问',NULL),(61,'2018-06-24 00:00:00',5360.00,'李晓琴|4060.00,李静|1300.00','销售顾问',NULL),(62,'2018-06-25 00:00:00',95560.00,'庄培润|10460.00,李晓琴|40040.00,李静|14860.00,何健锋|11600.00,杨辉|5800.00,何家辉|7000.00,赵松筑|5800.00','销售顾问',NULL),(63,'2018-06-26 00:00:00',64175.00,'李静|10620.00,何家辉|9800.00,杨辉|4800.00,庄培润|24355.00,赵松筑|5800.00,朱伟峰|2000.00,李晓琴|6800.00','销售顾问',NULL),(64,'2018-06-27 00:00:00',76010.00,'朱伟峰|5800.00,苏济泓|4800.00,李晓琴|11960.00,赵松筑|4800.00,李静|9660.00,何健锋|12530.00,庄培润|14860.00,杨辉|11600.00','销售顾问',NULL),(65,'2018-06-28 00:00:00',35760.00,'李静|12500.00,庄培润|17260.00,李晓琴|6000.00','销售顾问',NULL),(66,'2018-06-29 00:00:00',70252.00,'杨辉|5800.00,庄培润|17910.00,朱伟峰|5800.00,李晓琴|6760.00,李静|33982.00','销售顾问',NULL),(67,'2018-06-30 00:00:00',140200.00,'杨辉|36600.00,苏济泓|5800.00,朱伟峰|46100.00,赵松筑|11600.00,李晓琴|24480.00,李静|15620.00','销售顾问',NULL),(68,'2018-07-01 00:00:00',73260.00,'朱伟峰|17400.00,杨辉|5800.00,苏济泓|10600.00,何健锋|22900.00,赵松筑|5800.00,庄培润|10760.00','销售顾问',NULL),(69,'2018-07-02 00:00:00',82500.00,'杨辉|11600.00,庄培润|17560.00,苏济泓|16400.00,朱伟峰|11600.00,李晓琴|12760.00,李静|6780.00,何健锋|5800.00','销售顾问',NULL),(70,'2018-07-03 00:00:00',68600.00,'李晓琴|13960.00,李静|25120.00,何家辉|4560.00,庄培润|19160.00,朱伟峰|5800.00','销售顾问',NULL),(71,'2018-07-04 00:00:00',69860.00,'庄培润|4960.00,李晓琴|3000.00,李静|11500.00,何健锋|36800.00,杨辉|5800.00,何家辉|2000.00,苏济泓|5800.00','销售顾问',NULL),(72,'2018-07-05 00:00:00',98280.00,'李静|14660.00,何健锋|4600.00,杨辉|12600.00,何家辉|700.00,赵松筑|5800.00,庄培润|42000.00,李晓琴|17920.00','销售顾问',NULL),(73,'2018-07-06 00:00:00',59700.00,'李晓琴|5800.00,杨辉|5800.00,庄培润|42300.00,朱伟峰|5800.00','销售顾问',NULL),(74,'2018-07-07 00:00:00',17400.00,'朱伟峰|11600.00,杨辉|5800.00','销售顾问',NULL),(75,'2018-07-08 00:00:00',11600.00,'苏济泓|5800.00,杨辉|5800.00','销售顾问',NULL),(76,'2018-07-09 00:00:00',99060.00,'庄培润|55000.00,李晓琴|31800.00,李静|12260.00','销售顾问',NULL),(77,'2018-07-10 00:00:00',43020.00,'庄培润|19060.00,李晓琴|1000.00,李静|17160.00,杨辉|5800.00','销售顾问',NULL),(78,'2018-07-11 00:00:00',61210.00,'朱伟峰|5800.00,李静|17360.00,杨辉|5800.00,赵松筑|10990.00,庄培润|21260.00','销售顾问',NULL),(79,'2018-07-12 00:00:00',48460.00,'何健锋|4800.00,赵松筑|1300.00,庄培润|6900.00,朱伟峰|5800.00,李晓琴|19560.00,李静|10100.00','销售顾问',NULL),(80,'2018-07-13 00:00:00',41460.00,'庄培润|14800.00,李晓琴|-1800.00,李静|28460.00','销售顾问',NULL),(81,'2018-07-14 00:00:00',10100.00,'何健锋|4800.00,李静|2300.00,赵松筑|3000.00','销售顾问',NULL),(82,'2018-07-15 00:00:00',52260.00,'庄培润|29860.00,朱伟峰|5800.00,杨辉|11600.00,何健锋|5000.00','销售顾问',NULL),(83,'2018-07-16 00:00:00',88798.00,'罗文波|50.00,庄培润|36978.00,赵松筑|10500.00,朱伟峰|5800.00,李晓琴|24080.00,何健锋|1000.00,李静|11590.00,何家辉|-1200.00','销售顾问',NULL),(84,'2018-07-17 00:00:00',38920.00,'赵松筑|12300.00,庄培润|10060.00,李晓琴|8760.00,李静|7800.00','销售顾问',NULL),(85,'2018-07-18 00:00:00',80890.00,'杨辉|5800.00,赵松筑|5800.00,庄培润|41680.00,李晓琴|15860.00,李静|11750.00','销售顾问',NULL),(86,'2018-07-19 00:00:00',72930.00,'杨辉|5800.00,赵松筑|11300.00,庄培润|16260.00,李晓琴|7210.00,李静|32360.00','销售顾问',NULL),(87,'2018-07-20 00:00:00',65820.00,'李静|17900.00,赵松筑|5200.00,何健锋|13200.00,庄培润|28720.00,朱伟峰|800.00','销售顾问',NULL),(88,'2018-07-21 00:00:00',17460.00,'庄培润|17460.00','销售顾问',NULL),(89,'2018-07-22 00:00:00',7300.00,'李静|500.00,赵松筑|1000.00,朱伟峰|5800.00','销售顾问',NULL),(90,'2018-07-23 00:00:00',102600.00,'李晓琴|4900.00,李静|1500.00,何健锋|4000.00,杨辉|9440.00,庄培润|59160.00,赵松筑|12300.00,朱伟峰|11300.00','销售顾问',NULL),(91,'2018-07-24 00:00:00',80815.00,'何健锋|13500.00,李静|5400.00,何家辉|6020.00,赵松筑|34900.00,庄培润|23155.00,朱伟峰|5200.00,李晓琴|-7360.00','销售顾问',NULL),(92,'2018-07-25 00:00:00',102506.00,'朱伟峰|5800.00,李晓琴|3186.00,李静|-3000.00,何健锋|10300.00,杨辉|1000.00,庄培润|51160.00,赵松筑|34060.00','销售顾问',NULL),(93,'2018-07-26 00:00:00',103040.00,'何健锋|18560.00,赵松筑|28800.00,庄培润|48530.00,朱伟峰|50.00,李晓琴|1300.00,杨辉|5800.00','销售顾问',NULL),(94,'2018-07-27 00:00:00',35060.00,'赵松筑|27500.00,何健锋|4000.00,庄培润|4060.00,李晓琴|-500.00','销售顾问',NULL),(95,'2018-07-28 00:00:00',8800.00,'杨辉|5800.00,赵松筑|3000.00','销售顾问',NULL),(96,'2018-07-29 00:00:00',56986.00,'杨辉|11600.00,何健锋|22186.00,朱伟峰|23200.00','销售顾问',NULL),(97,'2018-07-30 00:00:00',101185.00,'李晓琴|3460.00,李静|0.00,何健锋|32165.00,赵松筑|14700.00,庄培润|46060.00,朱伟峰|4800.00','销售顾问',NULL),(98,'2018-07-31 00:00:00',75770.00,'李静|0.00,王秋剑|5800.00,庄培润|35920.00,赵松筑|26250.00,朱伟峰|7800.00','销售顾问',NULL),(99,'2018-08-01 00:00:00',54185.00,'冯恒冠|1700.00,庄培润|24500.00,李静|-4740.00,赵松筑|18300.00,何健锋|14425.00','销售顾问',NULL),(100,'2018-08-02 00:00:00',57992.00,'何健锋|19150.00,李静|-2000.00,杨辉|5800.00,赵松筑|35042.00','销售顾问',NULL),(101,'2018-08-03 00:00:00',25000.00,'赵松筑|15900.00,何健锋|9100.00','销售顾问',NULL),(102,'2018-08-04 00:00:00',27700.00,'何健锋|16100.00,朱伟峰|5800.00,王秋剑|5800.00','销售顾问',NULL),(103,'2018-08-05 00:00:00',8800.00,'赵松筑|8800.00','销售顾问',NULL),(104,'2018-08-06 00:00:00',89660.00,'赵松筑|27260.00,何健锋|24120.00,何家辉|0.00,庄培润|32480.00,杨辉|5800.00','销售顾问',NULL),(105,'2018-08-07 00:00:00',92120.00,'朱伟峰|9400.00,李静|1200.00,何健锋|18680.00,王秋剑|5800.00,何家辉|0.00,赵松筑|43860.00,庄培润|13180.00','销售顾问',NULL),(106,'2018-08-08 00:00:00',39650.00,'何健锋|13000.00,赵松筑|6700.00,何家辉|600.00,庄培润|11050.00,李晓琴|600.00,仝春梅|7500.00,李静|200.00','销售顾问',NULL),(107,'2018-08-09 00:00:00',77258.00,'庄培润|27060.00,杨辉|5800.00,仝春梅|1000.00,赵松筑|16080.00,何健锋|26918.00,何家辉|400.00','销售顾问',NULL),(108,'2018-08-10 00:00:00',34640.00,'李晓琴|4100.00,李静|400.00,赵松筑|14800.00,何健锋|4200.00,庄培润|11140.00','销售顾问',NULL),(109,'2018-08-11 00:00:00',17800.00,'赵松筑|12000.00,王秋剑|5800.00','销售顾问',NULL),(110,'2018-08-12 00:00:00',12300.00,'何健锋|6500.00,王秋剑|5800.00','销售顾问',NULL),(111,'2018-08-13 00:00:00',38100.00,'朱伟峰|11600.00,赵松筑|14400.00,何健锋|6100.00,庄培润|6000.00','销售顾问',NULL),(112,'2018-08-14 00:00:00',86940.00,'廖小捷|3500.00,朱伟峰|7800.00,李晓琴|0.00,何健锋|26660.00,李静|500.00,庄培润|12420.00,赵松筑|36060.00','销售顾问',NULL),(113,'2018-08-15 00:00:00',77280.00,'何健锋|14100.00,庄培润|41320.00,李晓琴|1000.00,赵松筑|20860.00','销售顾问',NULL),(114,'2018-08-16 00:00:00',70610.00,'庄培润|35950.00,朱伟峰|5800.00,杨辉|5800.00,赵松筑|13560.00,何健锋|9500.00','销售顾问',NULL),(115,'2018-08-17 00:00:00',50720.00,'何健锋|15920.00,庄培润|8340.00,杨辉|5800.00,王秋剑|11600.00,赵松筑|9060.00','销售顾问',NULL),(116,'2018-08-18 00:00:00',29700.00,'庄培润|6500.00,杨辉|17400.00,王秋剑|5800.00','销售顾问',NULL),(117,'2018-08-19 00:00:00',11600.00,'朱伟峰|11600.00','销售顾问',NULL),(118,'2018-08-20 00:00:00',51840.00,'杨辉|0.00,何健锋|9360.00,王秋剑|5800.00,庄培润|28820.00,朱伟峰|5800.00,李静|2060.00','销售顾问',NULL),(119,'2018-08-21 00:00:00',44030.00,'赵松筑|8000.00,何健锋|13558.00,庄培润|16672.00,朱伟峰|5800.00','销售顾问',NULL),(120,'2018-08-22 00:00:00',162610.00,'李静|0.00,杨辉|46400.00,何健锋|25150.00,王秋剑|17400.00,庄培润|22760.00,赵松筑|10300.00,朱伟峰|40600.00','销售顾问',NULL),(121,'2018-08-23 00:00:00',76010.00,'朱伟峰|2000.00,何家辉|0.00,李静|-1700.00,冯恒冠|800.00,王秋剑|28700.00,庄培润|4840.00,赵松筑|21000.00,廖小捷|2000.00,何健锋|18370.00','销售顾问',NULL),(122,'2018-08-24 00:00:00',110070.00,'庄培润|74130.00,朱伟峰|5800.00,李静|0.00,赵松筑|20260.00,何健锋|9880.00','销售顾问',NULL),(123,'2018-08-25 00:00:00',27820.00,'冉小凤|2800.00,杨辉|11600.00,赵松筑|13420.00','销售顾问',NULL),(124,'2018-08-26 00:00:00',35800.00,'朱伟峰|17400.00,杨辉|18400.00','销售顾问',NULL),(125,'2018-08-27 00:00:00',55970.00,'何健锋|9550.00,李静|-4600.00,何家辉|0.00,杨辉|17400.00,冉小凤|1500.00,赵松筑|12500.00,庄培润|2220.00,朱伟峰|17400.00','销售顾问',NULL),(126,'2018-08-28 00:00:00',6800.00,'庄培润|6800.00','销售顾问',NULL),(127,'2018-09-12 00:00:00',23.00,'庄培润|23.00','销售顾问',NULL),(128,'2018-09-18 00:00:00',1.00,'冯恒冠|1.00','销售顾问',NULL),(129,'2018-09-25 00:00:00',16720.00,'庄培润|16720.00','销售顾问',NULL),(130,'2018-09-27 00:00:00',4000.00,'庄培润|4000.00','销售顾问',NULL),(131,'2018-09-29 00:00:00',598.00,'庄培润|598.00','销售顾问',NULL),(132,'2018-10-08 00:00:00',1100.00,'李静|1100.00','销售顾问',NULL),(133,'2018-10-20 00:00:00',1800.00,'庄培润|1800.00','销售顾问',NULL),(134,'2018-10-22 00:00:00',300.00,'庄培润|300.00','销售顾问',NULL),(135,'2018-11-01 00:00:00',11211.00,'庄培润|11211.00','销售顾问',NULL),(136,'2018-11-05 00:00:00',227.00,'庄培润|227.00','销售顾问',NULL),(137,'2018-11-06 00:00:00',1.00,'庄培润|1.00','销售顾问',NULL),(256,'2018-05-03 00:00:00',1000.00,'冉小凤|1000.00','客服顾问',NULL),(257,'2018-11-05 00:00:00',123.00,'冉小凤|123.00','客服顾问',NULL),(259,'2018-10-20 00:00:00',2100.00,'马嘉欣|2100.00','客服会计',NULL),(260,'2018-10-22 00:00:00',500.00,'马嘉欣|200.00,黄柳如|300.00','客服会计',NULL),(261,'2018-10-29 00:00:00',2760.00,'黄柳如|2760.00','客服会计',NULL),(262,'2018-10-30 00:00:00',7836.00,'黄柳如|7836.00','客服会计',NULL),(266,NULL,0.00,'|7500.00,仝春梅|8500.00,何健锋|1017142.00,何家辉|732118.00,冉小凤|5450.00,冯恒冠|5301.00,孙泽阳|400.00,庄培润|2228966.00,庞陈雪|800.00,廖小捷|11500.00,朱伟峰|537450.00,李晓琴|710934.00,李江友|7374.18,李静|986714.00,杨辉|520340.00,王秋剑|98300.00,罗文波|22430.00,苏济泓|49200.00,赵松筑|1468739.00','销售顾问','个人总额'),(267,NULL,0.00,'冉小凤|1123.00','客服顾问','个人总额'),(268,NULL,0.00,'马嘉欣|2300.00,黄柳如|10896.00','客服会计','个人总额');
/*!40000 ALTER TABLE `t_projects_income_count` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:47