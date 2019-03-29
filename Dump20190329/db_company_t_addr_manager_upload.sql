-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_company
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
-- Table structure for table `t_addr_manager_upload`
--

DROP TABLE IF EXISTS `t_addr_manager_upload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_addr_manager_upload` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `file_name` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(45) DEFAULT NULL,
  `addr_id` int(11) NOT NULL DEFAULT '0',
  `req_id` int(11) NOT NULL DEFAULT '0',
  `remark` varchar(45) DEFAULT NULL,
  `up_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_manager_upload`
--

LOCK TABLES `t_addr_manager_upload` WRITE;
/*!40000 ALTER TABLE `t_addr_manager_upload` DISABLE KEYS */;
INSERT INTO `t_addr_manager_upload` VALUES (1,'/static/addr/679/9030627e-c9ca-41fc-9205-f9ff6e7dccd4_679.tif','2018-12-26 10:18:23',116,'陈太智',679,29,'',NULL),(2,'/static/addr/679/e462df62-0c81-48fc-93fd-2d5633a9df94_679.tif','2018-12-26 10:19:44',116,'陈太智',679,29,'',NULL),(3,'/static/addr/679/6c175402-295a-49fc-b8a4-a7755762af9e_679.tif','2018-12-26 10:19:44',116,'陈太智',679,29,'',NULL),(4,'/static/addr/679/3b7c46ea-70c3-41ae-a430-49f4c1b3701b_679.gif','2018-12-26 10:20:07',116,'陈太智',679,29,'',NULL),(5,'/static/addr/679/c9a2b294-e4d5-4558-8e54-bce6bf3818d3_679.gif','2018-12-26 10:20:07',116,'陈太智',679,29,'',NULL),(6,'/static/addr/679/f3eeb0c0-25b9-4e05-90a8-cb5b56b2e481_679.gif','2018-12-26 10:20:07',116,'陈太智',679,29,'',NULL),(7,'/static/addr/679/1f81fc0b-f766-4a16-ae12-de624ed00e46_679.tif','2018-12-26 10:20:44',116,'陈太智',679,29,'',NULL),(8,'/static/addr/679/0bd985cc-e1cf-4c67-b3d9-bcfdafabc76e_679.tif','2018-12-26 10:20:44',116,'陈太智',679,29,'',NULL),(9,'/static/addr/679/48b57ddf-b9e7-420c-b301-3213bc07ca92_679.tif','2018-12-26 10:20:46',116,'陈太智',679,29,'',NULL),(10,'/static/addr/679/b16044dc-0231-449b-b319-2c312b3e85f5_679.tif','2018-12-26 10:20:46',116,'陈太智',679,29,'',NULL),(11,'/static/addr/679/1307a576-a8cb-4d52-86da-2380fd2f62a5_679.tif','2018-12-26 10:21:24',116,'陈太智',679,29,'',NULL),(12,'/static/addr/679/1c441e97-24e1-42a4-9363-35d9d39a8432_679.tif','2018-12-26 10:21:24',116,'陈太智',679,29,'',NULL),(13,'/static/addr/679/62959b32-0a9d-4efd-bfe7-7012aad3b294_679.tif','2018-12-26 10:21:42',116,'陈太智',679,29,'',NULL),(14,'/static/addr/679/6f5e62aa-3728-4a99-824b-fc9e4447d949_679.tif','2018-12-26 10:21:42',116,'陈太智',679,29,'',NULL),(15,'/static/addr/679/c08af965-9c2d-4426-a1a8-21eefc0b3ad3_679.gif','2018-12-26 10:21:42',116,'陈太智',679,29,'',NULL),(16,'/static/addr/679/665cce68-6196-4494-a4f4-b11cf72ddbc2_679.tif','2018-12-26 10:28:50',116,'陈太智',679,29,'','跟进人反馈'),(17,'/static/addr/679/b078df88-38e7-4ebb-9c2f-a80190d96c53_679.gif','2018-12-26 10:28:50',116,'陈太智',679,29,'','跟进人反馈'),(18,'/static/addr/679/406d1b7e-474c-46d0-a0a6-d5aa5730f9b2_679.tif','2018-12-26 10:28:52',116,'陈太智',679,29,'','跟进人反馈'),(19,'/static/addr/679/5d990387-66cc-4d61-9b81-df72d8acce9e_679.gif','2018-12-26 10:28:52',116,'陈太智',679,29,'','跟进人反馈'),(20,'/static/addr/679/aed9dd6b-d4d4-4c0e-b4d7-ae8f1167c243_679.gif','2018-12-26 10:32:15',116,'陈太智',679,29,'','跟进人反馈'),(21,'/static/addr/679/2988399b-e40f-47c1-a077-0f36ee102d1f_679.gif','2018-12-26 10:32:16',116,'陈太智',679,29,'','跟进人反馈'),(22,'/static/addr/679/281bd60d-9484-42bf-8364-7ad4ebf17118_679.txt','2018-12-26 10:42:07',116,'陈太智',679,29,'','跟进人反馈'),(23,'/static/addr/679/cd3bbf6e-22c0-458a-bb7a-aee2a02b5930_679.tif','2018-12-26 10:42:07',116,'陈太智',679,29,'','跟进人反馈'),(24,'/static/addr/679/b78cd559-dd47-4ade-b091-c4f75b71fae6_679.txt','2018-12-26 10:42:07',116,'陈太智',679,29,'','跟进人反馈'),(25,'/static/addr/679/f6df478f-b02b-4460-86bc-073d92055c85_679.txt','2018-12-26 10:42:15',116,'陈太智',679,29,'','跟进人反馈'),(26,'/static/addr/679/15a8dca1-8570-4596-b575-06d230a8bf73_679.tif','2018-12-26 10:42:15',116,'陈太智',679,29,'','跟进人反馈'),(27,'/static/addr/679/9b35c867-80b3-4917-b06b-e5ab3363ab7a_679.txt','2018-12-26 10:42:15',116,'陈太智',679,29,'','跟进人反馈'),(28,'/static/addr/679/49728e81-4154-4804-8780-dbf3be7894e3_679.txt','2018-12-26 10:42:39',116,'陈太智',679,29,'','跟进人反馈'),(29,'/static/addr/679/ca24751e-aff7-4b14-b51a-cd9f04604cbf_679.tif','2018-12-26 10:42:39',116,'陈太智',679,29,'','跟进人反馈'),(30,'/static/addr/679/efaa4652-b497-4305-9bb7-ea0a23075962_679.txt','2018-12-26 10:42:39',116,'陈太智',679,29,'','跟进人反馈'),(31,'/static/addr/679/9e4daaf1-95a6-4704-8ba9-a2244e6c23e1_679.txt','2018-12-26 10:43:02',116,'陈太智',679,29,'','跟进人反馈'),(32,'/static/addr/679/adc0394d-55ac-4c05-8ec3-c01aab16aa09_679.tif','2018-12-26 10:43:02',116,'陈太智',679,29,'','跟进人反馈'),(33,'/static/addr/679/590b62b3-c7e6-4337-bc18-f17e7747b5fe_679.txt','2018-12-26 10:43:02',116,'陈太智',679,29,'','跟进人反馈'),(34,'/static/addr/679/d33409de-2bd2-4773-8a35-93d66e081e20_679.txt','2018-12-26 10:43:30',116,'陈太智',679,29,'','跟进人反馈'),(35,'/static/addr/679/ac59fe86-8bd1-4638-801d-5da7c329ce9f_679.tif','2018-12-26 10:43:30',116,'陈太智',679,29,'','跟进人反馈'),(36,'/static/addr/679/ddc377fc-247a-42d9-b63c-1f7b5c321ee5_679.txt','2018-12-26 10:43:30',116,'陈太智',679,29,'','跟进人反馈'),(37,'/static/addr/679/9a503ca1-2b3b-4b77-bb6a-054b42accaa4_679.txt','2018-12-26 10:44:02',116,'陈太智',679,29,'','跟进人反馈'),(38,'/static/addr/679/1b2b782e-9388-473e-85f3-962425680742_679.tif','2018-12-26 10:44:02',116,'陈太智',679,29,'','跟进人反馈'),(39,'/static/addr/679/b5868340-ab00-441f-9b5b-8b56d3c2c2b6_679.txt','2018-12-26 10:44:02',116,'陈太智',679,29,'','跟进人反馈'),(40,'/static/addr/679/fbaf70bb-f939-4ef4-ba1e-f677b960e62c_679.txt','2018-12-26 10:44:22',116,'陈太智',679,29,'','跟进人反馈'),(41,'/static/addr/679/e3b2ed34-a6bb-490a-acc9-c0cc1697fcf2_679.tif','2018-12-26 10:44:22',116,'陈太智',679,29,'','跟进人反馈'),(42,'/static/addr/679/e355a71e-7a7a-45a9-a7ae-4981358e5879_679.txt','2018-12-26 10:44:22',116,'陈太智',679,29,'','跟进人反馈'),(43,'/static/addr/870/6849b392-7fc6-4662-9a2f-1087c735eed1_870.jpg','2019-01-15 11:57:22',93,'domizzi',870,38,'','跟进人反馈');
/*!40000 ALTER TABLE `t_addr_manager_upload` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:03
