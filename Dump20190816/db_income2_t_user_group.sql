-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: 192.168.2.168    Database: db_income2
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.26-MariaDB-0+deb9u1

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
-- Dumping data for table `t_user_group`
--

LOCK TABLES `t_user_group` WRITE;
/*!40000 ALTER TABLE `t_user_group` DISABLE KEYS */;
INSERT INTO `t_user_group` VALUES (1,'销售顾问',0,'/project?tag=my',1),(2,'出纳',0,'/project?tag=list_finance&show=1&state=2',0),(3,'财务',0,'/project?tag=list_finance&show=1&state=3',0),(5,'合同确认',0,'/project?tag=list_finance&show=1&state=5',0),(6,'在线客服',0,'/project?tag=my',0),(7,'跟单分配员',0,'/project?tag=projects_state',0),(8,'管理员',0,'/project?tag=allview',0),(9,'工商专员',0,'/project?tag=projects_qc',1),(10,'会计',0,'/customer?my=1',1),(11,'仓管',0,'/project?tag=projects_cg',0),(12,'外勤',0,'/project?tag=projects_transition',1),(13,'客服顾问',0,'/project?tag=relation_projects',1),(14,'人事行政',0,'/project?tag=express_list',1),(15,'外联部',0,'/project?tag=bj_manage_yw',1),(16,'市场技术部',0,'/project?tag=express_list',1);
/*!40000 ALTER TABLE `t_user_group` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-16 15:15:37
