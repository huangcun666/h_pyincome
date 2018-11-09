-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: datadb
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
-- Table structure for table `t_receipt`
--

DROP TABLE IF EXISTS `t_receipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_receipt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sale_name` varchar(20) DEFAULT NULL,
  `craeted_at` datetime DEFAULT NULL,
  `project_name` varchar(100) DEFAULT NULL,
  `all_income` decimal(10,2) DEFAULT NULL,
  `kf_name` varchar(20) DEFAULT NULL,
  `customer_company` varchar(20) DEFAULT NULL,
  `cus_id` int(11) DEFAULT NULL,
  `customer_name` varchar(20) DEFAULT NULL,
  `income_type` varchar(20) DEFAULT NULL,
  `income_name` varchar(20) DEFAULT NULL,
  `customer_guid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_receipt`
--

LOCK TABLES `t_receipt` WRITE;
/*!40000 ALTER TABLE `t_receipt` DISABLE KEYS */;
INSERT INTO `t_receipt` VALUES (5,'何健锋','2018-04-12 01:20:30','自有荔湾地址注册公司1300+半年记账1680+账册300',3280.00,'陈泠宇','',272,'陈泠宇','支付宝','谢妙欣',NULL),(7,'庄培润','2018-04-12 01:17:37','自有地址注册1500',1500.00,'朱振','',271,'朱振','支付宝','谢妙欣',NULL),(8,'何家辉','2018-04-12 01:25:06','申请两类商标1800+代买国税CA200',2000.00,'包春燕','璐菲服饰（广州）有限公司',273,'包春燕','支付宝','谢妙欣',NULL),(9,'何家辉','2018-04-12 01:55:30','代买国税CA200+申请商标900元',1100.00,'包群雁','广州爱衣库服饰有限公司',274,'包群雁','支付宝','谢妙欣',NULL),(10,'何家辉','2018-04-12 03:00:54','登报费用0',0.00,'高恒在','广州瑾卓科技有限公司',275,'高恒在','支付宝','谢妙欣',NULL),(11,'何健锋','2018-04-12 03:21:29','注册一个商标900',900.00,'刘拥军','广州市有山有海商贸有限公司',276,'刘拥军','支付宝','谢妙欣',NULL),(12,'何健锋','2018-04-12 05:55:42','挂靠天河开票地址注册公司6000+记帐2760+账册300',9060.00,'黄勋宝','',277,'黄勋宝','支付宝','谢妙欣',NULL),(13,'赵松筑','2018-04-11 10:13:51','公司名义注册第41类商标，一标一类900元',900.00,'赵菊平','广州爱知树教育咨询有限公司',268,'赵菊平','支付宝','谢妙欣',NULL),(14,'庄培润','2018-04-11 10:03:16','补签17年1月到18年的1月份的账3000',3000.00,'杨思远','广州日灿电子科技有限公司',267,'杨思远','支付宝','谢妙欣',NULL),(15,'赵松筑','2018-04-11 09:57:57','撤销注销服务费2500',NULL,'李峦峰','广州市蔻缦纶电子商务有限公司',270,'李峦峰','支付宝','谢妙欣',NULL),(16,'庄培润','2018-04-11 09:52:16','南沙地址续期2500（含天河备案证明）',2500.00,'林良杰','广州瑞貔贸易有限公司',269,'林良杰','支付宝','谢妙欣',NULL),(20,'何家辉','2018-04-12 01:25:06','申请两类商标1800+代买国税CA200',2000.00,'包春燕','璐菲服饰（广州）有限公司',273,'包春燕','支付宝','谢妙欣',NULL);
/*!40000 ALTER TABLE `t_receipt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:44
