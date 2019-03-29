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
-- Table structure for table `t_user_teams`
--

DROP TABLE IF EXISTS `t_user_teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user_teams` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `team_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user_teams`
--

LOCK TABLES `t_user_teams` WRITE;
/*!40000 ALTER TABLE `t_user_teams` DISABLE KEYS */;
INSERT INTO `t_user_teams` VALUES (1,97,1),(2,121,1),(3,123,1),(4,131,1),(5,122,1),(6,151,1),(7,152,1),(8,119,1),(9,94,1),(10,149,1),(11,143,2),(12,107,2),(13,127,2),(14,150,2),(15,126,2),(16,130,2),(17,129,2),(18,144,2),(19,197,2),(20,94,3),(21,119,3),(22,100,4),(23,146,4),(24,145,4),(25,148,4),(26,149,4),(27,144,4),(28,200,2),(29,199,1),(30,95,5),(31,106,5),(32,119,5),(36,138,5),(37,139,5),(38,140,5),(39,141,5),(42,201,5),(46,154,5),(47,220,1),(48,287,2),(51,210,5),(52,239,5),(54,338,5),(55,335,1),(57,339,2),(58,143,1),(60,341,5),(61,342,5),(62,343,5),(63,154,1),(64,344,1),(65,345,1),(66,346,1),(67,347,1),(68,339,1),(69,296,5),(70,122,2),(71,107,1),(73,381,5),(74,127,1),(75,287,1),(76,94,2),(77,423,1),(78,389,1),(79,390,2),(80,131,2),(81,199,2),(82,335,2),(83,416,5),(84,417,5),(85,418,5),(86,419,5),(87,420,5),(88,380,5),(89,325,5),(90,291,5),(91,234,5),(92,324,5),(93,435,2);
/*!40000 ALTER TABLE `t_user_teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:27
