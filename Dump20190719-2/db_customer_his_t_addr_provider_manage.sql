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
-- Table structure for table `t_addr_provider_manage`
--

DROP TABLE IF EXISTS `t_addr_provider_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_addr_provider_manage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(45) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `remark` varchar(100) DEFAULT '',
  `updated_at` datetime DEFAULT NULL,
  `danbao_matter` varchar(500) DEFAULT '',
  `fp_limit` varchar(45) DEFAULT '',
  `type` varchar(45) DEFAULT NULL,
  `addr_nature` varchar(45) DEFAULT NULL,
  `cost_price` varchar(45) DEFAULT NULL,
  `register_price` varchar(45) DEFAULT NULL,
  `same_area_change_price` varchar(45) DEFAULT NULL,
  `dif_area_change_price` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `business_scope_limit` varchar(255) DEFAULT NULL,
  `accept_material` varchar(255) DEFAULT NULL,
  `addr_type` varchar(45) DEFAULT NULL,
  `proivde_end` varchar(45) DEFAULT NULL,
  `is_lock` tinyint(4) NOT NULL DEFAULT '0',
  `is_renew` tinyint(4) NOT NULL DEFAULT '0',
  `order_at` datetime DEFAULT NULL,
  `order_int` int(11) DEFAULT '100',
  `manage_type` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_provider_manage`
--

LOCK TABLES `t_addr_provider_manage` WRITE;
/*!40000 ALTER TABLE `t_addr_provider_manage` DISABLE KEYS */;
INSERT INTO `t_addr_provider_manage` VALUES (30,'天河','永盛众创','2018-11-06 14:10:42',118,'冯恒敏','',NULL,'付费期内保工商税务正常，如有异常免费处理正常或处理不了退回未使用月份费用','无限制，税局审批为准','预包装食品证地址','小规模','','8500（含预包装食品证）','8500','8500','天河区岑村沙浦大街','除生产加工、餐饮服务、娱乐行业、网吧、药品、医疗器械、危险化学品、民用爆品、烟花爆竹、放射性物品、旅行社等行业除外。','孵化器场地登记证明+租赁合同+出租方执照',NULL,NULL,1,1,'2018-11-06 14:06:14',100,0),(31,'天河','明驰','2018-11-06 14:14:15',118,'冯恒敏','',NULL,'付费期内保工商税务正常，如有异常免费处理正常或处理不了退回未使用月份费用','无限制，具体以税局审批为准','开票能解锁','小规模','','5800，签记账注册最低5300','5800（解锁异常需另加1000元）','6500（解锁异常需另加1000元）','荷光路、\"黄村路自编*号、中山大道*号、荔苑路*号，黄村北路*号A区、B区，黄村路*号、岑村元岗路*号 \"','可做厂房，除餐饮服务、娱乐行业、网吧、药品、医疗器械、危险化学品、民用爆品、烟花爆竹、放射性物品、旅行社等行业除外。','租赁合同+备案证明+街道非违建证明',NULL,NULL,1,1,'2018-11-06 14:17:26',100,0),(32,'天河','明驰','2018-11-06 14:17:26',118,'冯恒敏','',NULL,'付费期内保工商税务正常，如有异常免费处理正常或处理不了退回未使用月份费用','无，税局审批为准','开票能解锁','一般纳税人','','11000，签记账客户注册最低10000元','11000（解锁异常需另加1000元）','11500（解锁异常需另加1000元）','\"黄村路自编*号、中山大道*号、荔苑路*号，黄村北路*号A区、B区，黄村路*号、岑村元岗路*号 \"','除餐饮服务、娱乐行业、网吧、药品、医疗器械、危险化学品、民用爆品、烟花爆竹、放射性物品、旅行社等行业除外。','租赁合同+备案证明+街道非违建证明',NULL,NULL,1,1,'2018-11-06 14:14:15',100,0),(34,'越秀','文投','2018-11-06 14:30:30',118,'冯恒敏','',NULL,'付费期内保工商税务正常，如有异常免费处理正常或处理不了退回未使用月份费用','无，税局审批为准','众创','小规模/一般纳税人','','5500，签记账注册最低5000。一般纳税人11000','5500（解锁+1000）','6000（解锁+1000）','水荫路','除生产加工、餐饮服务、娱乐行业、网吧、药品、医疗器械、危险化学品、民用爆品、烟花爆竹、放射性物品、旅行社等行业除外。','合同+文投执照+科信局备案+科信局机构代码证',NULL,NULL,1,1,'2018-11-03 14:58:30',100,0),(38,'南沙','城投','2018-11-29 17:02:05',118,'冯恒敏','',NULL,'开票和一般纳税人资格认定可能会随政策变化而变化','税局审批为准','集群地址','小规模','','1800（股东或法人名下有房产），2800（无自己名下房产证提供）','1000','1500','丰泽东路106号','从事生产、加工、制造、施工、农副产品零售、种植、养殖、餐饮服务、旅业、娱乐服务、网吧、药品、医疗器械、小额贷款、证券服务、拍卖、典当、担保、小额贷款以及出口贸易业务等行业; 个体工商户不能使用本注册地址','房产证或备案证明+租赁合同',NULL,NULL,2,1,'2018-11-06 14:37:06',100,0),(41,'天河','好管家','2018-12-18 12:59:59',118,'冯恒敏','',NULL,'付费期保工商税务正常。注册资金超过500万不接','200万一年，具体以税局审批为准','开票可续期','小规模','','4500+记账3060','暂时不接','暂时不接','广州市天河区沙太南路','除生产加工、餐饮服务、建筑、娱乐行业、网吧、药品、医疗器械、危险化学品、民用爆品、烟花爆竹、放射性物品、旅行社等行业除外。','租赁合同+孵化器证明+入园协议',NULL,NULL,2,1,'2018-12-18 12:59:59',100,0),(42,'天河','好管家','2018-12-19 10:02:20',118,'冯恒敏','',NULL,'保工商一年正常。第二年续费2000元。注册资金超过500万不接','不能开票','孵化器j集群不开票地址可续期','小规模（集群注册）','','3000（第二年续费2000元）','不接','不接','天河区沙太南路','互联网商品销售（许可审批类商品除外），软件和信息技术服务业（需经许可审批事项除外），研究和试验发展，科技推广和应用服务业，文艺创作','租赁合同+孵化器证明+入园协议',NULL,NULL,2,1,'2018-12-19 10:02:20',100,0),(43,'天河','明德','2019-01-17 13:41:48',118,'冯恒敏','',NULL,'执照带“集群注册”或托管地址字样。保工商税务正常。因地址原因导致异常免费处理，处理不了退未使用月份费用。','200万以内，一个月不超20万','商务秘书集群地址','小规模','','3800（必须做账）（暂停销售，等第一批客户成功开票后再推）','不接','不接','天河区科韵北路','互联网商品销售、互联网商品零售、软件和信息技术服务业、研究和试验发展、文艺创作、其他商务服务业等非餐饮制造类，经营范围最终以工商局最终审判为准。该地址注册不下来的经营范围要删除或者加钱换其他地址注册。','托管协议',NULL,NULL,2,1,'2019-01-17 13:41:48',100,0);
/*!40000 ALTER TABLE `t_addr_provider_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:42
