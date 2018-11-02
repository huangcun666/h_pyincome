-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income1
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
-- Table structure for table `t_projects_income_title_print`
--

DROP TABLE IF EXISTS `t_projects_income_title_print`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_income_title_print` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL DEFAULT '0',
  `title_id` int(11) NOT NULL DEFAULT '0',
  `all_income` decimal(18,2) NOT NULL DEFAULT '0.00',
  `wait_income` decimal(18,2) NOT NULL DEFAULT '0.00',
  `all_income_cn` varchar(255) DEFAULT NULL,
  `wait_income_cn` varchar(255) DEFAULT NULL,
  `project_name` varchar(255) DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `end_date1` datetime DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `uid_name` varchar(255) DEFAULT NULL,
  `uid` int(11) NOT NULL,
  `end_date2` datetime DEFAULT NULL,
  `customer_name` varchar(255) DEFAULT NULL,
  `ys_remark` varchar(4000) DEFAULT NULL,
  `remark` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=202 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_income_title_print`
--

LOCK TABLES `t_projects_income_title_print` WRITE;
/*!40000 ALTER TABLE `t_projects_income_title_print` DISABLE KEYS */;
INSERT INTO `t_projects_income_title_print` VALUES (191,418,171,800.00,0.00,'捌佰圆',NULL,'申请商标800','2018-05-02 00:00:00','2018-05-01 00:00:00','2018-05-02 07:45:46','2018-05-02 07:45:46','吴蔚亮',98,'2018-05-02 00:00:00','邓玥莹','xxx',NULL),(192,418,191,800.00,0.00,'捌佰圆',NULL,'申请商标800','2018-05-02 00:00:00','2018-05-01 00:00:00','2018-05-02 07:49:25','2018-05-02 07:49:25','吴蔚亮',98,'2018-05-02 00:00:00','邓玥莹','ddddd',NULL),(193,418,192,8000000.00,0.00,'捌佰万元整',NULL,'申请商标800','2018-05-02 00:00:00','2018-05-09 00:00:00','2018-05-02 07:51:08','2018-05-02 07:51:08','吴蔚亮',98,'2018-05-01 00:00:00','邓玥莹','bbbb',NULL),(194,415,168,1200.00,0.00,'壹仟贰佰圆',NULL,'自有地址注册1200','2018-05-01 00:00:00','2018-05-02 00:00:00','2018-05-02 08:11:10','2018-05-02 08:11:10','吴蔚亮',98,'2018-05-02 00:00:00','陈瑾','',NULL),(195,386,40,3060.00,0.00,'叁仟零陆拾圆',NULL,'代理记账18年4月-18年3月2760+账册300','2018-05-03 00:00:00','2018-05-03 00:00:00','2018-05-03 01:26:10','2018-05-03 01:26:10','庄培润',97,'2018-04-23 00:00:00','陈非夷 -广州乐猫网络科技有限公司','的撒的',NULL),(196,409,126,4280.00,0.00,'肆仟贰佰捌拾圆',NULL,'天河长期虚拟地址注册2600+记账1380半年付+账册300/年','2018-05-01 00:00:00','2018-05-01 00:00:00','2018-05-03 01:47:54','2018-05-03 01:47:54','庄培润',97,'2018-04-24 00:00:00','李影林','',''),(197,267,135,2500.00,0.00,'贰仟伍佰圆',NULL,'南沙地址续期2500（含天河备案证明）','2018-05-09 00:00:00','2018-05-09 00:00:00','2018-05-09 05:57:43','2018-05-09 05:57:43','吴蔚亮',98,'2018-04-24 00:00:00','林良杰 -广州瑞貔贸易有限公司','',NULL),(198,408,109,4800.00,0.00,'肆仟捌佰圆',NULL,'挂靠南沙地址跨区变更地址+变更公司名称+经营范围4800(含天河备案证明以及刻公章+财务章并备案','2018-05-10 00:00:00','2018-05-01 00:00:00','2018-05-10 01:34:40','2018-05-10 01:34:40','庄培润',97,'2018-04-03 00:00:00','陈晓明','舅舅家',NULL),(199,412,130,4200.00,0.00,'肆仟贰佰圆',NULL,'自有地址改用天河开票地址注册追加4200','2018-05-11 00:00:00','2018-05-22 00:00:00','2018-05-10 02:32:11','2018-05-10 02:32:11','庄培润',97,'2018-04-24 00:00:00','王威','外婆家','ni爷爷是大多数代收'),(200,394,46,1000.00,0.00,'壹仟圆',NULL,'自有地址注册1000','2018-05-03 00:00:00','2018-05-10 00:00:00','2018-05-10 06:20:20','2018-05-10 06:20:20','庄培润',97,'2018-04-23 00:00:00','周英杰','大赛的','sasa'),(201,411,128,4000.00,0.00,'肆仟圆',NULL,'总服务费开票税点4000','2018-05-10 00:00:00','2018-05-03 00:00:00','2018-05-10 06:22:33','2018-05-10 06:22:33','庄培润',97,'2018-04-24 00:00:00','谢祎 -广州东方新能源有限公司','你奶奶','你爷爷');
/*!40000 ALTER TABLE `t_projects_income_title_print` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:31
