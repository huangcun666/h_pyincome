-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_test
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
-- Table structure for table `t_customer_clearly_msg`
--

DROP TABLE IF EXISTS `t_customer_clearly_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_clearly_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(255) DEFAULT NULL,
  `uid_at` datetime DEFAULT NULL,
  `ass_msg` varchar(1000) DEFAULT NULL,
  `ctype` varchar(255) DEFAULT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  `clearly_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_clearly_msg`
--

LOCK TABLES `t_customer_clearly_msg` WRITE;
/*!40000 ALTER TABLE `t_customer_clearly_msg` DISABLE KEYS */;
INSERT INTO `t_customer_clearly_msg` VALUES (1,121,'赵松筑','2019-02-19 10:25:08','已转款','跟进记录','',2851),(2,97,'庄培润','2019-02-19 10:51:43','客户要先看看自己能不能做先','跟进记录','',30),(3,97,'庄培润','2019-02-19 10:57:03','年检200元，汇算不用做，客户还欠记账款没给，2月26号左右过来我们公司办理','跟进记录','',48),(4,107,'冉小凤','2019-02-19 13:42:15','客户说五月转款','跟进记录','',3010),(5,121,'赵松筑','2019-02-19 13:47:50','客户已把公司转让给新法人陈成就了，现在没有新的联系方式，在和客户、会计确认一下','跟进记录','',93),(6,121,'赵松筑','2019-02-19 13:56:59','客户说经济普查我们还没有做，晚点再转钱办理年检，不想那么快','跟进记录','',176),(7,107,'冉小凤','2019-02-19 15:16:40','不接电话','跟进记录','',3011),(8,107,'冉小凤','2019-02-19 15:17:53','客户要注销公司，不 年检','跟进记录','',2801),(9,107,'冉小凤','2019-02-20 15:25:06','客户因为地址被锁的事情，要先处理，找别的公司做的，如果可以就不会交给我们公司做，','跟进记录','',3011),(10,107,'冉小凤','2019-02-19 15:28:23','客户说晚点支付','跟进记录','',3001),(11,107,'冉小凤','2019-02-19 15:32:38','客户这家公司已经转让给别人了，记账和年检都不交给我们公司做','跟进记录','',2848),(12,107,'冉小凤','2019-02-19 15:38:41','客户想自己做工商年检，汇算清缴要等等','跟进记录','',2812),(13,126,'曹慧慧','2019-02-19 15:58:35','客户现在是要把账转走','跟进记录','',96),(14,130,'庞陈雪','2019-02-19 16:05:25','已经微信告知客户了','跟进记录','',1395),(15,97,'庄培润','2019-02-19 16:17:56','联系财务李小姐：18630374356','跟进记录','',2760),(16,97,'庄培润','2019-02-19 16:23:22','客户要等3月份再联系办理','跟进记录','',2748),(17,116,'陈太智','2019-02-20 09:12:52','ssss','跟进记录','',165),(18,97,'庄培润','2019-02-20 09:53:07','电话直接挂断，未接','跟进记录','',2839),(19,97,'庄培润','2019-02-20 10:03:25','广州美汇佳贸易有限公司 18年工商年检费用200元+汇算清缴费用800元 创业补贴法人除外有两人买社保可申请4000元补贴（服务费800元） 合计1800元，微信发给客户','跟进记录','',2722),(20,97,'庄培润','2019-02-20 10:13:11','18年工商年检200+汇算清缴800元，合计1000元  ，微信报价给客户','跟进记录','',2806),(21,97,'庄培润','2019-02-20 10:19:49','用户暂停服务，电话打不通','跟进记录','',2777),(22,97,'庄培润','2019-02-20 10:27:12','打了两次电话都未接','跟进记录','',2802),(23,97,'庄培润','2019-02-20 10:31:14','已通知客户，等客户晚点回复','跟进记录','',11),(24,97,'庄培润','2019-02-20 10:32:57','16年成立企业注销费用5000 1、含18年工商年检200元，18年汇算清缴800元，客户在考虑注销，还要和股东沟通一下先','跟进记录','',10),(25,97,'庄培润','2019-02-20 10:43:09','微信发给客户年检200.客户晚点回复','跟进记录','',3045),(26,97,'庄培润','2019-02-20 10:44:41','电话显示空号','跟进记录','',3007),(27,97,'庄培润','2019-02-20 11:01:07','加客户微信发给客户先','跟进记录','',2993),(28,97,'庄培润','2019-02-20 11:02:41','电话显示空号','跟进记录','',2983),(29,97,'庄培润','2019-02-20 11:11:16','微信通知胡斌先生，年检200+汇算清缴800','跟进记录','',2959),(30,97,'庄培润','2019-02-20 11:22:15','电话已通知年检200+汇算800.客户先了解先','跟进记录','',2946),(31,122,'何健锋','2019-02-20 11:22:47','客户在忙，晚点联系','跟进记录','',2717),(32,122,'何健锋','2019-02-20 11:23:23','未接电话','跟进记录','',2766),(33,122,'何健锋','2019-02-20 11:23:48','客户觉得汇算的价格（800）贵了，要考虑一下','跟进记录','',2890),(34,122,'何健锋','2019-02-20 11:24:20','客户要我联系另外一个负责人（尹维维）','跟进记录','',167),(35,97,'庄培润','2019-02-20 11:45:33','微信通知年检200元。客户电话么接，微信还没回复','跟进记录','',2921),(36,97,'庄培润','2019-02-20 11:49:52','客户在香港，+微信联系','跟进记录','',2918),(37,97,'庄培润','2019-02-20 13:30:03','微信先发给客户年检200元','跟进记录','',2892),(38,97,'庄培润','2019-02-20 13:39:37','18年工商年检费用200元+汇算清缴费用800元 创业补贴2人买社保，补贴金额4000元，服务费用800元 合计1800元 ，微信发给客户','跟进记录','',2778),(39,97,'庄培润','2019-02-20 13:42:39','1、工商年检费用200元，事务所出汇算清缴费用是1200元，合计1400元 2、工商年检费用200元，财务公司出汇算清缴费用是800元，合计1000元，微信发给客户，客户看做哪种先生','跟进记录','',156),(40,97,'庄培润','2019-02-20 13:51:15','加微信发给客户','跟进记录','',222),(41,97,'庄培润','2019-02-20 13:52:39','未接电话','跟进记录','',2711),(42,130,'庞陈雪','2019-02-20 14:39:20','已经跟客户说了要做汇算清缴了','跟进记录','',3012),(43,435,'梁羽祺','2019-02-20 14:51:23','客户说我们做账贵，所以做账也没给钱的，贵是因为他之前按季度付款250一个月，现在和他说清楚按年便宜点的，下午5点联系，在开车','跟进记录','',2979),(44,435,'梁羽祺','2019-02-20 14:52:44','客户说合伙人现在也不管了，他也不管了，也不注销，也不做账','跟进记录','',2833),(45,130,'庞陈雪','2019-02-20 15:17:31','不接电话','跟进记录','',2832),(46,130,'庞陈雪','2019-02-20 16:01:35','已经跟客户联系 明天给我答复','跟进记录','',21),(47,130,'庞陈雪','2019-02-20 16:02:18','客户没有接听电话','跟进记录','',23),(48,130,'庞陈雪','2019-02-20 16:03:12','客户不在我们这边做账了 准备自己去注销的 工商年检也不做了','跟进记录','',183),(49,435,'梁羽祺','2019-02-20 16:07:43','客户要看资料，给他看看上年做过的本子','跟进记录','',3003),(50,130,'庞陈雪','2019-02-20 16:08:44','客户的号码是空号','跟进记录','',2923),(51,130,'庞陈雪','2019-02-20 16:50:38','已经微信告知客户 了','跟进记录','',2855),(52,97,'庄培润','2019-02-20 17:00:15','微信发给客户','跟进记录','',2823);
/*!40000 ALTER TABLE `t_customer_clearly_msg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:05
