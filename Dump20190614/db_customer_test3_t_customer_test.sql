-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_test3
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
-- Table structure for table `t_customer_test`
--

DROP TABLE IF EXISTS `t_customer_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(255) DEFAULT NULL,
  `reg_addr` varchar(1000) DEFAULT NULL,
  `reg_tel` varchar(200) DEFAULT NULL,
  `reg_number` varchar(100) DEFAULT NULL,
  `reg_person` varchar(100) DEFAULT NULL,
  `reg_bank` varchar(200) DEFAULT NULL,
  `reg_bank_account` varchar(200) DEFAULT NULL,
  `addr_type` varchar(200) DEFAULT NULL,
  `addr_expire` datetime DEFAULT NULL,
  `addr_cp` varchar(255) DEFAULT NULL,
  `acc_uid` int(11) DEFAULT NULL,
  `acc_uid_name` varchar(255) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `guid` varchar(45) DEFAULT NULL,
  `remark` varchar(3000) DEFAULT NULL,
  `reg_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `saic` varchar(450) DEFAULT NULL,
  `national_tax` varchar(450) DEFAULT NULL,
  `land_tax` varchar(450) DEFAULT NULL,
  `company_reguid` varchar(255) DEFAULT NULL,
  `industry_name` varchar(255) DEFAULT NULL,
  `is_general` tinyint(4) DEFAULT NULL,
  `credit_rating` int(11) DEFAULT NULL,
  `customer_rating` int(11) DEFAULT NULL,
  `credit_rating_name` varchar(255) DEFAULT NULL,
  `customer_rating_name` varchar(45) DEFAULT NULL,
  `updated_at_name` varchar(45) DEFAULT NULL,
  `customer_type` int(11) DEFAULT NULL,
  `customer_type_name` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(255) DEFAULT NULL,
  `acc_uid_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2400 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_test`
--

LOCK TABLES `t_customer_test` WRITE;
/*!40000 ALTER TABLE `t_customer_test` DISABLE KEYS */;
INSERT INTO `t_customer_test` VALUES (2368,'广州市丽眼饰衣服饰有限公司','','','','','','','',NULL,'',161,'周萍','2018-05-16 06:18:31','2018-05-16 06:18:31','f46e5cf9-58d0-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2369,'广州马卡德贸易有限公司','','','','','','','',NULL,'',180,'黄晓晴','2018-05-16 06:18:31','2018-05-16 06:18:31','f46f69d1-58d0-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2370,'广州中西联健康网络科技有限公司','','','','','','','',NULL,'',161,'周萍','2018-05-16 06:18:31','2018-05-16 06:18:31','f47054de-58d0-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2371,'广州途裕捷投资咨询有限公司','','','','','','','',NULL,'',183,'孙甜甜','2018-05-16 06:38:32','2018-05-16 06:38:32','c064551d-58d3-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2372,'广州厨美酒店用品有限公司','','','','','','','',NULL,'',180,'黄晓晴','2018-05-16 06:38:32','2018-05-16 06:38:32','c067190e-58d3-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2373,'广东赢道投资管理有限公司','','','','','','','',NULL,'',161,'周萍','2018-05-16 06:38:32','2018-05-16 06:38:32','c0694374-58d3-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2374,'广州叮咖美服饰有限公司','','','','','','','',NULL,'',183,'孙甜甜','2018-05-16 06:38:32','2018-05-16 06:38:32','c06c28e9-58d3-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2375,'广州弥谱服饰有限公司','','','','','','','',NULL,'',165,'马洁纯','2018-05-16 06:38:32','2018-05-16 06:38:32','c06e4ce1-58d3-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2376,'广州左卫门信息科技有限公司','','','','','','','',NULL,'',161,'周萍','2018-05-16 07:07:07','2018-05-16 07:07:07','be8ca0db-58d7-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 07:07:07'),(2377,'广东慧爱文化发展有限公司','','','','','','','',NULL,'',180,'黄晓晴','2018-05-16 07:07:49','2018-05-16 07:07:49','d7ae0083-58d7-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 07:07:49'),(2378,'广东医萃堂医药科技有限公司','','','','','','','',NULL,'',165,'马洁纯','2018-05-16 07:07:49','2018-05-16 07:07:49','d7afd67d-58d7-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 07:07:49'),(2379,'广州岐峰网络科技有限公司','','','','','','','',NULL,'',165,'马洁纯','2018-05-16 07:10:33','2018-05-16 07:10:33','39be5455-58d8-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 07:10:33'),(2380,'广州青兰贸易有限公司','','','','','','','',NULL,'',165,'马洁纯','2018-05-16 07:10:33','2018-05-16 07:10:33','39c16eb2-58d8-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 07:10:33'),(2381,'广州京兆福圆源信息技术有限公司','','','','','','','',NULL,'',183,'孙甜甜','2018-05-16 07:10:34','2018-05-16 07:10:34','39c4d134-58d8-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 07:10:34'),(2382,'广东雅致多米诺骨牌运动俱乐部有限公司','','','','','','','',NULL,'',183,'孙甜甜','2018-05-16 07:10:34','2018-05-16 07:10:34','39c6de83-58d8-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 07:10:34'),(2383,'李培芳A公司','','','','','','','',NULL,'',183,'孙甜甜','2018-05-16 08:03:35','2018-05-16 08:03:35','a20ca9b4-58df-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:03:35'),(2384,'广州市升通贸易有限责任公司','','','','','','','',NULL,'',180,'黄晓晴','2018-05-16 08:09:53','2018-05-16 08:09:53','8385b5c3-58e0-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:09:53'),(2385,'广州立适康贸易有限公司','','','','','','','',NULL,'',172,'杨结英','2018-05-16 08:12:02','2018-05-16 08:12:02','d02682ed-58e0-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:12:02'),(2386,'广州马虎豆商贸有限公司','','','','','','','',NULL,'',172,'杨结英','2018-05-16 08:16:17','2018-05-16 08:16:17','683eebc7-58e1-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:16:17'),(2387,'广州苏羽服饰有限公司','','','','','','','',NULL,'',180,'黄晓晴','2018-05-16 08:39:06','2018-05-16 08:39:06','9802f6b6-58e4-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:39:06'),(2388,'广州服饰有限公司','','','','','','','',NULL,'',180,'黄晓晴','2018-05-16 08:41:16','2018-05-16 08:41:16','e5c8d51c-58e4-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:41:16'),(2389,'广州宫保鸡丁投资管理有限公司','','','','','','','',NULL,'',165,'马洁纯','2018-05-16 08:45:52','2018-05-16 08:45:52','8a0e596b-58e5-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:45:52'),(2390,'广州倍司科企业管理咨询有限公司','','','','','','','',NULL,'',166,'潘素婷','2018-05-16 08:50:43','2018-05-16 08:50:43','37735783-58e6-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:50:43'),(2391,'广州云祺垚贸易有限公司','','','','','','','',NULL,'',165,'马洁纯','2018-05-16 08:54:39','2018-05-16 08:54:39','c4704320-58e6-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:54:39'),(2392,'广州市时步网络通信设备安装有限公司','','','','','','','',NULL,'',166,'潘素婷','2018-05-16 08:58:45','2018-05-16 08:58:45','56c162b3-58e7-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 08:58:45'),(2393,'广州华而佳投资咨询有限公司','','','','','','','',NULL,'',173,'陈雨薇','2018-05-16 09:00:08','2018-05-16 09:00:08','88b24e87-58e7-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 09:00:08'),(2394,'广州华有限公司','','','','','','','',NULL,'',173,'陈雨薇','2018-05-16 09:01:09','2018-05-16 09:01:09','acd2824c-58e7-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 09:01:09'),(2395,'广州华公司','','','','','','','',NULL,'',173,'陈雨薇','2018-05-16 09:05:17','2018-05-16 09:05:17','40e5f378-58e8-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 09:05:17'),(2396,'广州公司','','','','','','','',NULL,'',173,'陈雨薇','2018-05-16 09:08:29','2018-05-16 09:08:29','b352730e-58e8-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 09:08:29'),(2397,'广公司','','','','','','','',NULL,'',173,'陈雨薇','2018-05-16 09:10:00','2018-05-16 09:10:00','e95e89c6-58e8-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 09:10:00'),(2398,'公司','','','','','','','',NULL,'',173,'陈雨薇','2018-05-16 09:15:55','2018-05-16 09:15:55','bcb32240-58e9-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 09:15:55'),(2399,'我的公司','','','','','','','',NULL,'',173,'陈雨薇','2018-05-16 09:24:34','2018-05-16 09:24:34','f22c1fe0-58ea-11e8-a20d-6045cb9a7117',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2018-05-16 09:24:34');
/*!40000 ALTER TABLE `t_customer_test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:07:10
