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
-- Table structure for table `t_projects_type`
--

DROP TABLE IF EXISTS `t_projects_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_type` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `income_name` varchar(255) NOT NULL DEFAULT '',
  `income_category` varchar(255) NOT NULL DEFAULT '',
  `is_hide` tinyint(4) NOT NULL DEFAULT '0',
  `income_parentid` int(11) NOT NULL DEFAULT '0',
  `order_int` int(11) NOT NULL DEFAULT '0',
  `btag` varchar(255) DEFAULT NULL,
  `update_id` int(11) NOT NULL DEFAULT '0',
  `is_hide_first` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=211 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_type`
--

LOCK TABLES `t_projects_type` WRITE;
/*!40000 ALTER TABLE `t_projects_type` DISABLE KEYS */;
INSERT INTO `t_projects_type` VALUES (2,'推广','业务来源',0,0,101,NULL,0,0),(3,'客户推荐','业务来源',0,0,100,NULL,0,0),(4,'楼盘','业务来源',0,0,99,NULL,0,0),(5,'特殊核名','业务类型',0,0,106,NULL,0,0),(6,'加急','业务类型',0,0,107,NULL,0,0),(7,'注册','业务类型',0,0,101,NULL,0,0),(8,'变更','业务类型',0,0,104,NULL,0,0),(9,'注销','业务类型',0,0,108,NULL,0,0),(10,'记账','业务类型',0,0,98,NULL,0,0),(11,'进出口','业务类型',0,0,111,NULL,0,0),(12,'商标','业务类型',0,0,105,NULL,0,0),(13,'香港','业务类型',0,0,109,NULL,0,0),(14,'一般纳税人','业务类型',0,0,112,NULL,0,0),(15,'发业','收入公司',0,0,0,NULL,0,0),(16,'商脉','收入公司',0,0,0,NULL,0,0),(17,'刷卡机','支付方式',0,0,0,NULL,0,0),(18,'现金','支付方式',0,0,0,NULL,0,0),(19,'基本户','支付方式',0,0,0,NULL,0,0),(20,'支付宝','支付方式',0,0,0,NULL,0,0),(21,'微信','支付方式',0,0,0,NULL,0,0),(22,'工行','支付方式',0,0,0,NULL,0,0),(23,'建行','支付方式',0,0,0,NULL,0,0),(24,'农行','支付方式',0,0,0,NULL,0,0),(25,'中国银行','支付方式',0,0,0,NULL,0,0),(26,'身份证1','资料交接明细',0,0,100,NULL,0,0),(27,'营业执照','资料交接明细',0,0,101,NULL,0,0),(28,'租赁合同','资料交接明细',0,0,104,NULL,0,0),(29,'房屋租赁证明','资料交接明细',0,0,106,NULL,0,0),(30,'经营场所场地使用证明','资料交接明细',0,0,107,NULL,0,0),(31,'公章','资料交接明细',0,0,108,NULL,0,0),(32,'信息采集表','资料交接明细',0,0,109,NULL,0,0),(33,'身份证2','资料交接明细',0,0,102,NULL,0,0),(34,'销售顾问','项目角色',0,0,100,NULL,0,0),(36,'客服顾问','项目角色',0,0,101,NULL,0,0),(37,'组长','项目角色',0,0,102,NULL,0,0),(38,'工商专员','项目角色',0,0,105,NULL,0,1),(39,'在线客服','项目角色',0,0,103,NULL,0,0),(40,'合同定金','代收类型',0,0,0,NULL,0,0),(41,'二期定金','收入类型',0,0,0,NULL,0,0),(42,'余款','收入类型',0,0,0,NULL,0,0),(43,'尾款','代收类型',0,0,0,NULL,0,0),(44,'第一期付款','收入类型',0,0,0,NULL,0,0),(45,'第二期付款','收入类型',0,0,0,NULL,0,0),(46,'第三期付款','收入类型',0,0,0,NULL,0,0),(47,'第四期付款','收入类型',0,0,0,NULL,0,0),(49,'出纳','财务确认',0,0,0,NULL,0,0),(50,'已收合同','合同确认',0,0,102,NULL,0,0),(51,'财务','财务确认',0,0,0,NULL,0,0),(52,'复印件','资料类型',0,0,0,NULL,0,0),(53,'原件','资料类型',0,0,0,NULL,0,0),(55,'现场','签约方式',0,0,0,NULL,0,0),(56,'远程','签约方式',0,0,0,NULL,0,0),(57,'合同在途','合同确认',0,0,101,NULL,0,0),(59,'无合同','合同确认',0,0,103,NULL,0,0),(61,'在线咨询','沟通方式',0,0,0,NULL,0,0),(62,'电话直拨','沟通方式',0,0,0,NULL,0,0),(63,'来源关键词确认','来源关键词确认',0,0,0,NULL,0,0),(64,'百度','推广来源渠道',0,0,0,NULL,0,0),(65,'360','推广来源渠道',0,0,0,NULL,0,0),(66,'神马','推广来源渠道',0,0,0,NULL,0,0),(67,'搜狗','推广来源渠道',0,0,0,NULL,0,0),(69,'信息流','推广来源渠道',0,0,0,NULL,0,0),(71,'地址','业务类型',0,0,103,NULL,0,0),(72,'汇算','业务类型',0,0,110,NULL,0,0),(74,'入户','业务类型',0,0,104,NULL,0,0),(75,'房产证','资料交接明细',0,0,105,NULL,0,0),(76,'米酷','楼盘',0,0,105,NULL,0,0),(77,'天河北','楼盘',0,0,105,NULL,0,0),(78,'尚城','楼盘',0,0,105,NULL,0,0),(79,'百信广场','楼盘',0,0,105,NULL,0,0),(80,'城市之光','楼盘',0,0,105,NULL,0,0),(81,'内部推荐','业务来源',0,0,100,NULL,0,0),(82,'发票申请','业务类型',0,0,115,NULL,0,0),(83,'开票税点','业务类型',0,0,115,NULL,0,0),(84,'汇算清缴','业务类型',0,0,115,NULL,0,0),(85,'工商年检','业务类型',0,0,115,NULL,0,0),(86,'外资','业务类型',0,0,115,NULL,0,0),(87,'违约金','业务类型',0,0,115,NULL,0,0),(88,'社保','业务类型',0,0,115,NULL,0,0),(89,'网站','业务类型',0,0,115,NULL,0,0),(92,'全款','收入类型',0,0,0,NULL,0,0),(93,'CA费用','代收类型',0,0,0,NULL,0,0),(94,'税控盘','代收类型',0,0,0,NULL,0,0),(95,'印花税','代收类型',0,0,0,NULL,0,0),(96,'罚款','代收类型',0,0,0,NULL,0,0),(97,'其他','代收类型',0,0,0,NULL,0,0),(98,'天河长期虚拟地址','地址类型',0,0,0,NULL,0,0),(99,'天河开票地址','地址类型',0,0,0,NULL,0,0),(100,'天河一般私人地址','地址类型',0,0,0,NULL,0,0),(101,'天河自有地址','地址类型',0,0,0,NULL,0,0),(102,'越秀长期虚拟地址','地址类型',0,0,0,NULL,0,0),(103,'越秀开票地址','地址类型',0,0,0,NULL,0,0),(104,'越秀一般私人地址','地址类型',0,0,0,NULL,0,0),(105,'越秀自有地址','地址类型',0,0,0,NULL,0,0),(106,'海珠长期虚拟地址','地址类型',0,0,0,NULL,0,0),(107,'海珠开票地址','地址类型',0,0,0,NULL,0,0),(108,'海珠一般私人地址','地址类型',0,0,0,NULL,0,0),(109,'海珠自有地址','地址类型',0,0,0,NULL,0,0),(110,'白云长期虚拟地址','地址类型',0,0,0,NULL,0,0),(111,'白云开票地址','地址类型',0,0,0,NULL,0,0),(112,'白云一般私人地址','地址类型',0,0,0,NULL,0,0),(113,'白云自有地址','地址类型',0,0,0,NULL,0,0),(114,'花都长期虚拟地址','地址类型',0,0,0,NULL,0,0),(115,'花都开票地址','地址类型',0,0,0,NULL,0,0),(116,'花都一般私人地址','地址类型',0,0,0,NULL,0,0),(117,'花都自有地址','地址类型',0,0,0,NULL,0,0),(118,'黄埔长期虚拟地址','地址类型',0,0,0,NULL,0,0),(119,'黄埔开票地址','地址类型',0,0,0,NULL,0,0),(120,'黄埔一般私人地址','地址类型',0,0,0,NULL,0,0),(121,'黄埔自有地址','地址类型',0,0,0,NULL,0,0),(122,'增城长期虚拟地址','地址类型',0,0,0,NULL,0,0),(123,'增城开票地址','地址类型',0,0,0,NULL,0,0),(124,'增城一般私人地址','地址类型',0,0,0,NULL,0,0),(125,'增城自有地址','地址类型',0,0,0,NULL,0,0),(126,'长期虚拟地址','地址类型',0,0,0,NULL,0,0),(127,'开票地址','地址类型',0,0,0,NULL,0,0),(128,'一般私人地址','地址类型',0,0,0,NULL,0,0),(129,'自有地址','地址类型',0,0,0,NULL,0,0),(130,'无','地址类型',0,0,0,NULL,0,0),(131,'帐册费','业务类型',0,0,98,NULL,0,0),(132,'其他','业务类型',0,0,113,NULL,0,0),(133,'解除异常明细','业务类型',0,0,101,NULL,0,0),(134,'食品证','业务类型',0,0,113,NULL,0,0),(135,'世博汇','楼盘',0,0,105,NULL,0,0),(136,'刻章','业务类型',0,0,101,NULL,0,0),(137,'外出签单','签约方式',0,0,0,NULL,0,0),(138,'远洋天骄','楼盘',0,0,105,NULL,0,0),(139,'广州市','地市',0,0,0,NULL,0,0),(141,'天河','区域',0,0,0,NULL,0,0),(142,'越秀','区域',0,0,0,NULL,0,0),(143,'海珠','区域',0,0,0,NULL,0,0),(144,'荔湾','区域',0,0,0,NULL,0,0),(145,'番禺','区域',0,0,0,NULL,0,0),(146,'南沙','区域',0,0,0,NULL,0,0),(147,'增城','区域',0,0,0,NULL,0,0),(148,'黄埔','区域',0,0,0,NULL,0,0),(149,'白云','区域',0,0,0,NULL,0,0),(150,'萝岗','区域',0,0,0,NULL,0,0),(151,'办结','办结',0,0,3,'cq',0,0),(152,'仓管通知销售交接','办结',0,0,5,'cg',0,0),(153,'完成交接','办结',0,0,7,'cq',0,0),(154,'仓管确认交接完成','办结',0,0,8,'cg',0,0),(155,'公司注册','业务分类',0,0,105,NULL,0,0),(156,'公司变更','业务分类',0,0,105,NULL,0,0),(157,'解除异常','业务分类',0,0,105,NULL,0,0),(158,'公司注销','业务分类',0,0,105,NULL,0,0),(159,'商标','业务分类',0,0,105,NULL,0,0),(160,'特殊业务','业务分类',0,0,105,NULL,0,0),(161,'其他业务','业务分类',0,0,105,NULL,0,0),(162,'办理中','办结',0,0,2,'cq',0,0),(163,'销售顾问接受交接','办结',0,0,6,'sales',0,0),(164,'许可证','业务分类',0,0,105,NULL,0,0),(165,'填写办结信息','办结',0,0,4,'cq',0,0),(167,'待接单','办结',0,0,1,'cq',0,0),(168,'花都','区域',0,0,0,NULL,0,0),(169,'记账报税','业务分类',0,0,105,NULL,0,0),(170,'营业执照正本','移交资料',0,0,1,NULL,0,0),(171,'营业执照副本','移交资料',0,0,2,NULL,0,0),(172,'公司章程','移交资料',0,0,3,NULL,0,0),(173,'开业通知书','移交资料',0,0,4,NULL,0,0),(174,'租赁合同（原件、复件）','移交资料',0,0,5,NULL,0,0),(175,'公章','移交资料',0,0,6,NULL,0,0),(176,'国地税ETS','移交资料',0,0,9,NULL,0,0),(177,'刻章许可证','移交资料',0,0,9,NULL,0,0),(178,'银行开户许可证','移交资料',0,0,9,NULL,0,0),(179,'机构信用代码证','移交资料',0,0,10,NULL,0,0),(180,'结算账户申请书','移交资料',0,0,97,NULL,0,0),(181,'收费凭证','移交资料',0,0,97,NULL,0,0),(182,'业务凭证','移交资料',0,0,97,NULL,0,0),(183,'声明文件','移交资料',0,0,97,NULL,0,0),(184,'身份证原件','移交资料',0,0,97,NULL,0,0),(185,'支票业务服务协议','移交资料',0,0,97,NULL,0,0),(186,'公司电子银行服务申请表','移交资料',0,0,97,NULL,0,0),(187,'对账服务协议','移交资料',0,0,97,NULL,0,0),(188,'印鉴卡','移交资料',0,0,97,NULL,0,0),(189,'回单服务卡','移交资料',0,0,97,NULL,0,0),(190,'回单凭证','移交资料',0,0,97,NULL,0,0),(191,'财务章','移交资料',0,0,7,NULL,0,0),(192,'法人章','移交资料',0,0,7,NULL,0,0),(193,'黄埔万科中心','楼盘',0,0,105,NULL,0,0),(194,'万科山景城','楼盘',0,0,105,NULL,0,0),(195,'开发','区域',0,0,0,NULL,0,0),(196,'退款','代收类型',0,0,0,NULL,0,0),(197,'岭南V谷','楼盘',0,0,105,NULL,0,0),(198,'从化','区域',0,0,0,NULL,0,0),(199,'入户','业务分类',0,0,105,NULL,0,0),(200,'传统开发','业务来源',0,0,100,NULL,0,0),(201,'里享家','楼盘',0,0,105,NULL,0,0),(202,'会计','业务来源',0,0,90,NULL,0,0),(203,'续帐','业务来源',0,0,90,NULL,0,0),(204,'续帐费','业务类型',0,203,119,NULL,0,0),(205,'客服会计','项目角色',0,0,101,NULL,0,0),(206,'变更通知书','移交资料',0,0,0,NULL,0,0),(207,'股东会决议','移交资料',0,0,0,NULL,0,0),(208,'章程修正案','移交资料',0,0,0,NULL,0,0),(209,'出资转让合同书','移交资料',0,0,0,NULL,0,0),(210,'2222','111',0,0,105,NULL,0,0);
/*!40000 ALTER TABLE `t_projects_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:23
