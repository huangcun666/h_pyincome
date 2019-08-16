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
-- Dumping data for table `approval_apply_manage`
--

LOCK TABLES `approval_apply_manage` WRITE;
/*!40000 ALTER TABLE `approval_apply_manage` DISABLE KEYS */;
INSERT INTO `approval_apply_manage` VALUES (29,'92777a1b-dcc2-4a09-b2e9-bfbe8b25f006','会计部',11,'陈太智',116,'停账',340,0,'sss','','','',NULL,NULL,'',NULL,NULL,'',0,'陈太智','陈太智创建审批申请','2019-08-09 17:25:53','domizzi,','','2019-08-09 17:25:53'),(30,'7ddc3576-e87c-4ebf-8d01-a5cac0570dfc','会计部',11,'陈太智',116,'停账',340,0,'sss','','','',NULL,NULL,NULL,NULL,NULL,'',0,'陈太智','陈太智添加李江友为审批人','2019-08-09 17:26:51','domizzi,李江友,','','2019-08-09 17:25:57'),(31,'b3f4e9f3-f7f9-4fa4-84c3-e46bae6eab14','总经办',22,'陈太智',116,'停账',340,0,'','','','','2019-08-12 14:23:11',116,'陈太智',NULL,NULL,'',0,'陈太智','陈太智递交上级审批','2019-08-12 14:23:11','陈太智,','','2019-08-12 10:27:53'),(32,'9d587f51-df55-4a4f-8148-1a43ec1c83d0','总经办',22,'陈太智',116,'停账',340,0,'','','','',NULL,NULL,'',NULL,NULL,'',0,'陈太智','陈太智确认审批','2019-08-12 14:43:52','陈太智,','','2019-08-12 14:42:27');
/*!40000 ALTER TABLE `approval_apply_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-16 15:15:32
