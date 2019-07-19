-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_his
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
-- Table structure for table `business_develop_manage_msg`
--

DROP TABLE IF EXISTS `business_develop_manage_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_develop_manage_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  `tag_type` varchar(255) DEFAULT NULL,
  `btype_id` int(11) NOT NULL DEFAULT '1',
  `company_name` varchar(255) DEFAULT NULL,
  `company_regid` varchar(255) DEFAULT NULL,
  `rel_id` int(11) NOT NULL DEFAULT '0',
  `ext_id` int(11) NOT NULL DEFAULT '0',
  `file_list` varchar(4000) DEFAULT NULL,
  `project_id` int(11) NOT NULL DEFAULT '0',
  `file_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3740 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_manage_msg`
--

LOCK TABLES `business_develop_manage_msg` WRITE;
/*!40000 ALTER TABLE `business_develop_manage_msg` DISABLE KEYS */;
INSERT INTO `business_develop_manage_msg` VALUES (3708,145,'陈小奋','设置跟进人为冉小凤','2019-03-04 16:01:18',NULL,11,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3709,145,'陈小奋','设置跟进人为冉小凤','2019-03-05 11:07:44',NULL,12,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3710,107,'冉小凤','冉小凤已接单','2019-03-05 11:08:45',NULL,12,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3711,107,'冉小凤','冉小凤确认办结','2019-03-05 11:23:14',NULL,12,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3712,116,'陈太智','陈太智审核不通过','2019-03-05 11:23:49',NULL,12,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3713,116,'陈太智','36_咨询注册_咨询（前端）','2019-04-07 15:32:19',NULL,12,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3714,116,'陈太智','37_咨询记账_咨询（前端）','2019-04-07 15:33:10',NULL,12,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3715,116,'陈太智','36_咨询注册_咨询（前端）','2019-04-08 09:51:10',NULL,12,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3716,145,'陈小奋','设置跟进人为陈太智','2019-04-16 13:57:07',NULL,13,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3717,145,'陈小奋','设置跟进人为冉小凤','2019-04-16 14:06:44',NULL,14,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3718,116,'陈太智','陈太智已接单','2019-04-16 14:26:45',NULL,13,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3719,116,'陈太智','37_咨询记账_咨询（前端）,38_咨询变更_咨询（前端）','2019-04-16 14:27:01',NULL,13,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3720,116,'陈太智','sefs','2019-04-19 13:37:21',NULL,13,'跟进记录',3,NULL,NULL,0,0,NULL,0,NULL),(3721,116,'陈太智','37_咨询记账_咨询（前端）,38_咨询变更_咨询（前端）,39_咨询注销_咨询（前端）','2019-04-20 10:53:14',NULL,13,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3722,116,'陈太智','38_咨询变更_咨询（前端）,39_咨询注销_咨询（前端）,44_公司起名_咨询（前端）','2019-04-20 10:53:27',NULL,13,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3723,116,'陈太智','38_咨询变更_咨询（前端）,39_咨询注销_咨询（前端）','2019-04-27 10:18:15',NULL,14,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3724,116,'陈太智','38_咨询变更_咨询（前端）,39_咨询注销_咨询（前端）,44_公司起名_咨询（前端）,64_意向变弱_跟进（业务）','2019-04-28 14:08:36',NULL,13,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3725,116,'陈太智','23131','2019-04-28 14:08:43',NULL,13,'跟进记录',3,NULL,NULL,0,0,NULL,0,NULL),(3726,116,'陈太智','1','2019-04-28 14:09:23',NULL,13,'跟进记录',3,NULL,NULL,0,0,NULL,0,'/static/business_manage/13/903182339617634059.jpg'),(3727,116,'陈太智','38_咨询变更_咨询（前端）,39_咨询注销_咨询（前端）,44_公司起名_咨询（前端）,87_中质量B2类_质量（业务）,88_低质量C1类_质量（业务）,90_同行_质量（业务）,91_无效业务咨询_质量（业务）,92_没咨询过我司_质量（业务）,58_方案未确定_跟进（业务）,64_意向变弱_跟进（业务）,74_需求商标_需求（业务）,75_需求个体户_需求（业务）,76_需求买卖公司_需求（业务）,77_需求香港公司_需求（业务）,83_需求入户_需求（业务）,84_需求装修_需求（业务）','2019-04-28 14:17:16',NULL,13,'操作标签',1,NULL,NULL,0,0,NULL,0,NULL),(3728,116,'陈太智','jkldasjdka','2019-04-30 14:50:53',NULL,13,'跟进记录',3,NULL,NULL,0,0,NULL,0,NULL),(3729,116,'陈太智','跟进人设置为陈太智','2019-04-30 14:54:32',NULL,15,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3730,116,'陈太智','陈太智已接单','2019-04-30 14:54:49',NULL,15,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3731,116,'陈太智','跟进人设置为仝春梅','2019-05-06 11:14:10',NULL,16,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3732,116,'陈太智','跟进人设置为梁羽祺','2019-05-06 11:16:48',NULL,17,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3733,435,'梁羽祺','梁羽祺已接单','2019-05-06 11:17:15',NULL,17,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3734,435,'梁羽祺','123123','2019-05-06 11:18:31',NULL,17,'跟进记录',3,NULL,NULL,0,0,NULL,0,NULL),(3735,143,'仝春梅','仝春梅已接单','2019-05-06 11:24:42',NULL,16,'操作记录',2,NULL,NULL,0,0,NULL,0,NULL),(3737,116,'陈太智','1_电话__2019-05-06 18:20:00','2019-05-06 18:26:17',NULL,13,'销售计划',4,NULL,NULL,0,0,NULL,0,NULL),(3738,116,'陈太智','1_电话_fgdds_2019-05-06 18:25:00','2019-05-06 18:26:31',NULL,13,'销售计划',4,NULL,NULL,0,0,NULL,0,NULL),(3739,116,'陈太智','1_电话_dasdsafsdfsdf_2019-05-06 05:25:00','2019-05-06 18:27:10',NULL,13,'销售计划',4,NULL,NULL,0,0,NULL,0,NULL);
/*!40000 ALTER TABLE `business_develop_manage_msg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:35
