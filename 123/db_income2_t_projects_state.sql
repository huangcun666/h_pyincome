-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income2
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
-- Table structure for table `t_projects_state`
--

DROP TABLE IF EXISTS `t_projects_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_state` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `msg_txt` varchar(1000) DEFAULT NULL,
  `order_int` int(11) NOT NULL DEFAULT '0',
  `parent` int(11) NOT NULL DEFAULT '0',
  `is_hide` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_state`
--

LOCK TABLES `t_projects_state` WRITE;
/*!40000 ALTER TABLE `t_projects_state` DISABLE KEYS */;
INSERT INTO `t_projects_state` VALUES (1,'预计核名',2,11,0),(2,'领取核名',4,11,0),(3,'勾选经营范围',5,11,0),(4,'地址安排',6,11,0),(5,'执照受理',7,11,0),(6,'领取执照',8,11,0),(7,'刻章备案',9,11,0),(8,'银行开户',10,11,0),(9,'核名中',3,11,0),(10,'资料审查',1,11,0),(11,'资料审查',0,11,1),(12,'已与客户建立联系',0,11,1),(13,'受阻',0,11,1),(14,'预计核名',0,11,1),(15,'核名中',0,11,1),(16,'领取核名',0,11,1),(17,'勾选经营范围',0,11,1),(18,'地址安排',0,11,1),(19,'加急办理',0,11,1),(20,'约号中',0,11,1),(21,'执照受理',0,11,1),(22,'领取执照',0,11,1),(23,'刻章备案',0,11,1),(24,'银行开户',0,11,1),(25,'税务环节',0,11,1),(26,'其他',0,11,1),(27,'资料审查',0,11,2),(28,'已与客户建立联系',0,11,2),(29,'受阻',0,11,2),(30,'变更信息已确认',0,11,2),(31,'迁移档案中',0,11,2),(32,'约号中',0,11,2),(33,'执照受理',0,11,2),(34,'领取执照',0,11,2),(36,'刻章备案',0,11,2),(37,'银行变更中',0,11,2),(38,'税务变更中',0,11,2),(39,'解除工商异常中',0,11,2),(40,'解除税务异常中',0,11,2),(41,'其他',0,11,2),(42,'已与客户建立联系',0,11,3),(43,'已收取资料',0,11,3),(44,'已做税务报道',0,11,3),(45,'已下载国税APP并实名',0,11,3),(46,'三员已绑定',0,11,3),(47,'受阻',0,11,3),(48,'记账报税中',0,11,3),(49,'正常',0,11,3),(50,'非正常',0,11,3),(51,'其他',0,11,3),(52,'资料审查',0,11,4),(53,'已与客户建立联系',0,11,4),(54,'登报纸',0,11,4),(55,'清算备案中',0,11,4),(56,'移交会计注销国地税中',0,11,4),(57,'受阻',0,11,4),(58,'注销执照',0,11,4),(59,'注销银行',0,11,4),(60,'其他',0,11,4),(61,'资料审查',0,11,5),(62,'已与客户建立联系',0,11,5),(63,'食品证办理',0,11,5),(64,'进出口权办理',0,11,5),(65,'领取证件',0,11,5),(66,'受阻',0,11,5),(67,'其他',0,11,5),(68,'资料审查',0,11,6),(69,'递交报件',0,11,6),(70,'受阻',0,11,6),(71,'电子申请号',0,11,6),(72,'电子受理回执',0,11,6),(73,'纸质受理回执',0,11,6),(74,'初审',0,11,6),(75,'商标证书',0,11,6),(76,'其他',0,11,6),(77,'资料审查无误',0,11,7),(79,'资料送出',0,11,7),(80,'受阻',0,11,7),(81,'加急执照',0,11,7),(82,'特殊地址备案',0,11,7),(83,'解除工商异常',0,11,7),(84,'解除税务',0,11,7),(85,'异常',0,11,7),(86,'其他',0,11,7),(87,'资料审查',0,11,8),(88,'已与客户建立联系',0,11,8),(89,'受阻',0,11,8),(90,'刻章',0,11,8),(91,'章备案',0,11,8),(92,'登报纸',0,11,8),(93,'跑腿',0,11,8),(94,'工商年检',0,11,8),(95,'汇算清缴',0,11,8),(96,'香港公司',0,11,8),(98,'条形码',0,11,8),(99,'网站建设',0,11,8),(100,'三证合一',0,11,8),(101,'垫资',0,11,8),(102,'银行代开户',0,11,8),(103,'代缴罚款',0,11,8),(104,'其他',0,11,8);
/*!40000 ALTER TABLE `t_projects_state` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:08
