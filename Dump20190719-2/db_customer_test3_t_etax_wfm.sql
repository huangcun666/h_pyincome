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
-- Table structure for table `t_etax_wfm`
--

DROP TABLE IF EXISTS `t_etax_wfm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_etax_wfm` (
  `customer_id` int(11) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `ctime` datetime DEFAULT NULL,
  `zsxmDm` varchar(255) DEFAULT NULL,
  `jkztDm` varchar(60) DEFAULT NULL,
  `gdslxDm` varchar(255) DEFAULT NULL,
  `sbztDm` varchar(255) DEFAULT NULL,
  `pzxh` varchar(255) DEFAULT NULL,
  `nsqxDm` varchar(255) DEFAULT NULL,
  `zsxmMc` varchar(255) DEFAULT NULL,
  `sbrq` varchar(255) DEFAULT NULL,
  `skssqQ` varchar(255) DEFAULT NULL,
  `yxcfsb` varchar(255) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `ysqxxId` varchar(255) DEFAULT NULL,
  `sbyfIn` varchar(255) DEFAULT NULL,
  `lastzs` varchar(255) DEFAULT NULL,
  `sbbcxx` varchar(255) DEFAULT NULL,
  `yzpzzlDm` varchar(255) DEFAULT NULL,
  `ybtse` varchar(255) DEFAULT NULL,
  `sbqx` varchar(255) DEFAULT NULL,
  `sbgcztDm` varchar(255) DEFAULT NULL,
  `skssqZ` varchar(255) DEFAULT NULL,
  `sbywbm` varchar(255) DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  `zspmMc` varchar(255) DEFAULT NULL,
  `zspmDm` varchar(255) DEFAULT NULL,
  `up_at` datetime DEFAULT NULL,
  `qdate` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_etax_wfm`
--

LOCK TABLES `t_etax_wfm` WRITE;
/*!40000 ALTER TABLE `t_etax_wfm` DISABLE KEYS */;
INSERT INTO `t_etax_wfm` VALUES (5410,'广州君达维修服务有限公司','2019-07-19 15:35:32','10101','','1','210','10014419000104924951','08','增值税(适用于小规模纳税人)','2019-07-01','2019-04-01','','sbywbm=XGMZZS&yzpzzldm=BDA0610611&gdslxDm=1&ssqq=2019-04-01&ssqz=2019-06-30&nsqxDm=08&zsxmDm=10101&zspmDm=101016201&sdhbz=N&ywjkbm=&sbqx=2019-07-15&tjNd=2019&tjYf=07','','','Y','','BDA0610611','0.0','2019-07-15','','2019-06-30','XGMZZS','8D22784DE53602D0E053560C4816A600',' ','101016201','2019-07-19 15:35:32','2019年07月'),(5410,'广州君达维修服务有限公司','2019-07-19 15:35:32','30216','','1','210','10014419000104924952','08','地方教育附加','2019-07-01','2019-04-01','','sbywbm=LHFJSSB&yzpzzldm=&gdslxDm=1&ssqq=2019-04-01&ssqz=2019-06-30&nsqxDm=08&zsxmDm=30216&zspmDm=302160100&sdhbz=N&ywjkbm=&sbqx=2019-07-15&tjNd=2019&tjYf=07','','','','','','0.0','2019-07-15','','2019-06-30','LHFJSSB','8D22784DE53702D0E053560C4816A600','增值税地方教育附加','302160100','2019-07-19 15:35:32','2019年07月'),(5410,'广州君达维修服务有限公司','2019-07-19 15:35:32','30203','','1','210','10014419000104924952','08','教育费附加','2019-07-01','2019-04-01','','sbywbm=LHFJSSB&yzpzzldm=&gdslxDm=1&ssqq=2019-04-01&ssqz=2019-06-30&nsqxDm=08&zsxmDm=30203&zspmDm=302030100&sdhbz=N&ywjkbm=&sbqx=2019-07-15&tjNd=2019&tjYf=07','','','','','','0.0','2019-07-15','','2019-06-30','LHFJSSB','8D22784DE53302D0E053560C4816A600','增值税教育费附加','302030100','2019-07-19 15:35:32','2019年07月'),(5410,'广州君达维修服务有限公司','2019-07-19 15:35:32','10109','','1','210','10014419000104924952','08','城市维护建设税','2019-07-01','2019-04-01','','sbywbm=LHFJSSB&yzpzzldm=&gdslxDm=1&ssqq=2019-04-01&ssqz=2019-06-30&nsqxDm=08&zsxmDm=10109&zspmDm=101090101&sdhbz=N&ywjkbm=&sbqx=2019-07-15&tjNd=2019&tjYf=07','','','','','','0.0','2019-07-15','','2019-06-30','LHFJSSB','8D22784DE53502D0E053560C4816A600','市区（增值税附征）','101090101','2019-07-19 15:35:32','2019年07月'),(5410,'广州君达维修服务有限公司','2019-07-19 15:35:32','10104','','1','210','10014419000117567743','08','企业所得税(月季报)','2019-07-09','2019-04-01','','sbywbm=QYSDS_A_18YJD&yzpzzldm=BDA0611033&gdslxDm=1&ssqq=2019-04-01&ssqz=2019-06-30&nsqxDm=08&zsxmDm=10104&zspmDm=101040001&sdhbz=N&ywjkbm=&sbqx=2019-07-15&tjNd=2019&tjYf=07','','','Y','','BDA0611033','0.0','2019-07-15','','2019-06-30','QYSDS_A_18YJD','8D22784DE53402D0E053560C4816A600','应纳税所得额','101040001','2019-07-19 15:35:32','2019年07月'),(5410,'广州君达维修服务有限公司','2019-07-19 15:35:32','10106','','1','210','10014419000105336220','06','个人所得税(代扣代缴)','2019-07-02','2019-06-01','','sbywbm=KJGRSDSSB&yzpzzldm=BDA0610135&gdslxDm=1&ssqq=2019-06-01&ssqz=2019-06-30&nsqxDm=06&zsxmDm=10106&zspmDm=101060100&sdhbz=N&ywjkbm=&sbqx=2019-07-15&tjNd=2019&tjYf=07','','','','','BDA0610135','0.0','2019-07-15','','2019-06-30','KJGRSDSSB','8D22784DE53802D0E053560C4816A600','工资薪金所得','101060100','2019-07-19 15:35:32','2019年07月');
/*!40000 ALTER TABLE `t_etax_wfm` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:50
