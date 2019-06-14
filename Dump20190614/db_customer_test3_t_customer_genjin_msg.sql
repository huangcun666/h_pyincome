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
-- Table structure for table `t_customer_genjin_msg`
--

DROP TABLE IF EXISTS `t_customer_genjin_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_genjin_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `msg` varchar(10000) DEFAULT NULL,
  `genjin_type` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_genjin_msg`
--

LOCK TABLES `t_customer_genjin_msg` WRITE;
/*!40000 ALTER TABLE `t_customer_genjin_msg` DISABLE KEYS */;
INSERT INTO `t_customer_genjin_msg` VALUES (1,4220,NULL,'2019-04-03 16:25:24','李江友',117,'这个客户是在黄晓晴名下，为什么显示是非记账',4),(2,2112,NULL,'2019-04-03 16:56:44','李江友',117,'该客户已显示收到解约违约金，应该是解约客户，已把逾期标签修改成解约',4),(3,2363,NULL,'2019-04-03 17:22:14','李江友',117,'逾期标签改成解约',4),(4,1410,NULL,'2019-04-03 17:26:27','李江友',117,'逾期改停账',4),(5,320,NULL,'2019-04-03 17:40:13','李江友',117,'逾期改解约',4),(6,299,NULL,'2019-04-03 17:45:10','李江友',117,'逾期改停账',4),(7,166,NULL,'2019-04-03 17:53:28','李江友',117,'逾期改解约',4),(8,962,NULL,'2019-04-04 13:55:34','李江友',117,'逾期改停账',4),(9,1314,NULL,'2019-04-04 13:56:26','李江友',117,'逾期改解约',4),(10,982,NULL,'2019-04-04 13:57:49','李江友',117,'逾期改停账，18年停账客户',4),(11,1311,NULL,'2019-04-04 13:59:13','李江友',117,'逾期改解约',4),(12,241,NULL,'2019-04-04 14:01:55','李江友',117,'逾期改解约',4),(13,1,NULL,'2019-04-04 14:11:11','李江友',117,'重复客户',4),(14,224,NULL,'2019-04-04 14:13:00','李江友',117,'逾期改解约',4),(15,283,NULL,'2019-04-04 14:15:29','李江友',117,'逾期改停账',4),(16,338,NULL,'2019-04-04 14:16:06','李江友',117,'逾期改停账',4),(17,2184,NULL,'2019-04-04 14:30:55','李江友',117,'逾期改解约',4),(18,1337,NULL,'2019-04-04 14:31:27','李江友',117,'逾期改解约',4),(19,1366,NULL,'2019-04-04 14:38:25','李江友',117,'逾期改解约',4),(20,2373,NULL,'2019-04-04 15:11:04','李江友',117,'文投有几家客户在我们这里，要注意不再服务的及时清理出去',1),(21,1457,NULL,'2019-04-04 15:38:07','李江友',117,'这个客户要问会计了解好客户的联系方式，要抢救下客户',4),(22,2045,NULL,'2019-04-04 16:06:05','李江友',117,'销售跟进这个客户获取客户在注销，已逾期很久，要做停账处理',4),(23,2235,NULL,'2019-04-04 16:27:56','李江友',117,'这个客户为注销客户，合理周转',4),(24,459,NULL,'2019-04-10 14:27:39','李江友',117,'应收信息显示17年已经停账，已把逾期标签改成停账',4),(25,676,NULL,'2019-04-10 14:30:20','李江友',117,'该客户不是在我们这里注销的，商事网显示已经注销了的',4),(26,1156,NULL,'2019-04-10 15:30:03','李江友',117,'销售反馈已经解约了，但是应收还是只是挂着已收款项',4),(27,5343,NULL,'2019-04-10 16:32:17','李江友',117,'这个客户还没有注册下来，所以还没有统一社会信用代码',4),(28,5142,NULL,'2019-04-10 18:15:23','李江友',117,'这个制造厂的账务如果有复杂的要向会计主管提出',4),(29,5004,NULL,'2019-04-10 18:48:24','李江友',117,'这个客户注册未完成',4),(30,4745,NULL,'2019-04-10 21:11:40','李江友',117,'最近的应收表的登记是把艾尔潮轩（广州）贸易有限公司改成广州脚丫子吧贸易有限公司，F699',4),(31,4718,NULL,'2019-04-10 21:20:58','李江友',117,'正确公司应为91440101MA5AW4J01D腾亿科技（广州）有限公司',4),(32,4700,NULL,'2019-04-10 21:25:05','李江友',117,'梁瑞莹登记：企业名称错误，系统已经有正确的企业，此记录可以删除',4),(33,4700,NULL,'2019-04-10 21:27:20','李江友',117,'正确名称为广州星贸科技有限公司，施亦丹，应收表登记客户编号F678，中铁环球中心客户',4),(34,4748,NULL,'2019-04-10 21:29:23','李江友',117,'与4700广州丹意科技有限公司重复',4),(35,4660,NULL,'2019-04-10 21:34:08','李江友',117,'与广州科鑫科技有限公司重复',4),(36,36,NULL,'2019-04-24 10:19:59','江嘉琳',153,'会计3月业绩表登记停账。',1),(37,220,NULL,'2019-04-24 10:23:06','江嘉琳',153,'会计3月业绩表标记停账。',1),(38,239,NULL,'2019-04-24 10:23:29','江嘉琳',153,'会计3月业绩表标记停账。',1),(39,254,NULL,'2019-04-24 10:23:53','江嘉琳',153,'会计3月业绩表标记停账。',1),(40,255,NULL,'2019-04-24 10:24:00','江嘉琳',153,'会计3月业绩表标记停账。',1),(41,283,NULL,'2019-04-24 10:25:41','江嘉琳',153,'会计3月业绩表标记停账。',1),(42,337,NULL,'2019-04-24 10:25:50','江嘉琳',153,'会计3月业绩表标记停账。',1),(43,839,NULL,'2019-04-24 10:26:59','江嘉琳',153,'会计3月业绩表标记停账。',1),(44,1319,NULL,'2019-04-24 10:27:44','江嘉琳',153,'会计3月业绩表标记停账。',1),(45,1320,NULL,'2019-04-24 10:28:11','江嘉琳',153,'会计3月业绩表标记停账。',1),(46,1765,NULL,'2019-04-24 10:33:10','江嘉琳',153,'会计3月业绩表标记停账。',1),(47,1899,NULL,'2019-04-24 10:33:44','江嘉琳',153,'会计3月业绩表标记停账。',1),(48,2026,NULL,'2019-04-24 10:33:50','江嘉琳',153,'会计3月业绩表标记停账。',1),(49,3766,NULL,'2019-04-24 11:12:22','江嘉琳',153,'系统上登记解约但是没有看到相关记录，会计3月业绩表还记录正常做账，而且款项是收齐到19.06月，请核实相关内容。',1),(50,704,NULL,'2019-04-24 11:48:30','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(51,789,NULL,'2019-04-24 11:51:07','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(52,1936,NULL,'2019-04-24 11:52:34','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(53,2046,NULL,'2019-04-24 13:38:31','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(54,2169,NULL,'2019-04-24 13:44:10','江嘉琳',153,'会计记录登记已停账。',1),(55,1848,NULL,'2019-04-24 14:33:03','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(56,136,NULL,'2019-04-24 17:15:09','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(57,209,NULL,'2019-04-24 17:15:29','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(58,308,NULL,'2019-04-24 17:16:45','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(59,731,NULL,'2019-04-24 17:17:56','江嘉琳',153,'会计3月业绩表标记的是停账。',1),(60,2709,NULL,'2019-04-25 09:18:18','江嘉琳',153,'会计3月业绩表登记停账。',1),(61,303,NULL,'2019-04-25 09:49:09','江嘉琳',153,'会计3月业绩表登记停账。',1),(62,970,NULL,'2019-04-25 10:13:03','江嘉琳',153,'会计3月业绩表登记停账。',1),(63,973,NULL,'2019-04-25 10:16:14','江嘉琳',153,'会计3月业绩表登记停账。',1),(64,976,NULL,'2019-04-25 10:17:22','江嘉琳',153,'会计3月业绩表登记停账。',1),(65,968,NULL,'2019-04-25 10:20:17','江嘉琳',153,'会计3月业绩表登记停账。',1),(66,1,NULL,'2019-04-29 11:37:37','李江友',117,'客户已修改，这个客户为正确客户',4),(67,2770,NULL,'2019-05-07 11:50:39','周萍',161,'2018年收入259934，利润13814.32，客户主要做服务，年底注意要跟客户核对一下往来，其中看到有申报工资，却申请免参保，要跟客户核对李俊丽是否在其它 地方也申报了工资，要跟客户说明清楚，如果在两家公司同时申报会带了什么样的影响',4),(68,874,NULL,'2019-05-07 17:14:47','周萍',161,'18年收入551164.34，利润92143.03，交了9081.3的所得税，应补272.7。客户开业到现在，去年亏损了1000元，其它年份都是盈利的，跟客户那边说一下尽量计提一下分红。还有其中应收款那里要跟客户核对清楚，有一些17年的科目余额到18年都没变动过的，是不是已经用现金收了款的呢？小规模公司应交税费不用涉及到进项税额和销项税额，还有社保申报的人数和工资申报的人数对不上，要跟客户说清楚两者不一致会带来的风险。',4),(69,874,NULL,'2019-05-07 17:25:09','周萍',161,'社保申报5个人，工资申报19个人',4),(70,385,NULL,'2019-05-07 17:33:13','周萍',161,'没有开发票，自主申报收入，18年收入35422.33，利润-201824.62，社保人员和工资人员相一致，银行流水购买社保的流水，没啥往来款，可以根据公司的情况与客户商量一下，适当调增一下收入。',4),(71,823,NULL,'2019-05-07 17:45:17','周萍',161,'收入30578，利润 -52539.68  社保 工资人员一致一个人，没有啥来往款，银行流水只有扣社保的流水。',4),(72,829,NULL,'2019-05-07 18:16:29','周萍',161,'收入35780，利润-80677.07，应收有一笔80000多的在贷方，要跟客户核对是不是已经确认为收入的了，应付有小余额，要跟客户核对 是不是已经付清的了。社保工资3人。',4),(73,829,NULL,'2019-05-07 18:17:49','周萍',161,'18年的本年利润没有结转',4),(74,211,NULL,'2019-05-07 18:28:58','周萍',161,'收入456014.56，利润为175157.24，可以弥补以前年度亏损，要交的所得税5331.28，跟客户核对清楚往来',4),(75,904,NULL,'2019-05-07 18:36:47','周萍',161,'收入58718.46，利润为-1161.32，还交了所得税1103.09，会涉及到退税，像这种企业  收入比较少，第一 二季度 的时候 ，就算是盈利一点的情况，先不要交企业所得税，可以暂估成本。因为到年末的时候很可能就会发生亏损的情况，那到做汇算 清缴 的时候 会涉及到退税了。',4),(76,1250,NULL,'2019-05-07 18:44:41','周萍',161,'客户已经解约，但是，有一点要核实清楚 的，就是客户之前 因为要摇号所以交了企业所得税，现在在年末发现公司亏损了，要申报退税了，对那车牌号那影响吗',4),(77,1379,NULL,'2019-05-07 18:51:18','周萍',161,'0申报的企业，有税种，但是，在接下来的月份，要跟客户商量一下，最好要申报一点收入，长期0申报很容易列为异常企业',4),(78,833,NULL,'2019-05-07 19:18:25','周萍',161,'18年收入445206.45，利润19192.88，所得税1919.29，看了客户累计利润44万，要注意一下股东分红的问题。工资 和社保的人员是相一致的',4),(79,831,NULL,'2019-05-07 19:23:53','周萍',161,'18年没有收入，利润为-126707.17，工资社保人员1人，每个月有支付房租水电费，银行流水就是付房租水电费和社保，建议客户可以适当申报一点收入，避免一直0申报列为税务异常',4),(80,3810,NULL,'2019-05-07 19:28:17','周萍',161,'18年刚成立的公司，暂没收入和成本，工资申报一个人，社保 人员为0，跟客户说清楚工资人员和社保 人员要一致，如果不一致会带来的风险',4),(81,3195,NULL,'2019-05-07 19:33:56','周萍',161,'18年收入为33611.65，利润16145.91  所得税  1614.59？客户愿意交那多的企业所得税？？如果是自主申报收入的，是不是可以适当的申报一点收入啦呢，因为刚成立几个月，企业所得税不用那么高的，差不多5个点的企业所得税税负率了。工资申报一个人，社保 人员为0，跟客户说清楚工资人员和社保 人员要一致，如果不一致会带来的风险',4),(82,1,NULL,'2019-05-09 14:13:13','李江友',117,'成立几年的公司了还没有税种，这个情况要提醒客户相关的税务风险',4),(83,131,NULL,'2019-05-09 15:09:09','李江友',117,'这个客户收了汇缴和年报的费用，欠款却差不多半年了，要让客户尽快付费',4),(84,158,NULL,'2019-05-09 15:33:20','刘婷',181,'18年账上暂估10万，有48419的税款未交，经联系客户交税无果，并理解合同到期（19.2）即服务结束，无需交接什么东西，给联系人发了解约书，再联系就不理我了',1),(85,365,NULL,'2019-05-09 15:37:43','李江友',117,'对于逾期的客户，会计要有意识的督促相应销售收款，并且对客户做相应的提醒协助销售收款',1),(86,158,NULL,'2019-05-09 15:39:12','刘婷',181,'记账凭证（18.1-19.2共14本）和税控盘都在我们这边，最后一次联系法人（19.4.8）说公司在注销中',1),(87,428,NULL,'2019-05-09 15:41:48','李江友',117,'对于逾期的客户，会计要有意识的督促相应销售收款，并且对客户做相应的提醒协助销售收款',1),(88,158,'/static/customer/genjin/158/3.png_158.png','2019-05-09 15:42:40','刘婷',181,'电子税务局被锁',1),(89,4359,NULL,'2019-05-09 16:17:25','周萍',161,'18年收入3970，利润-37282.71，累计亏损4.6万左右。自主申报收入，银行流水主要以扣社保为主，没啥往来，一个人的工资以及社保',4),(90,4359,NULL,'2019-05-09 17:46:33','周萍',161,'在网上查询 到申报的增值税申报表上收入为0，与账上和企业所得税的申报收入不一致，麻烦安排时间去前台改申报',4),(91,113,'/static/customer/genjin/113/2018.09减员.png_113.png','2019-05-10 09:08:36','周萍',161,'客户2018年9月减员，18年的收入1000元，利润为-33360.39，账上的收入、企业所得税申报的收入和增值税申报的收入不一致，账上的收入为1000，企业所得税申报的收入为1000，但是增值税申报的收入为0，麻烦会计尽早安排时间去前台改申报，上传结果，同时把去前台申报的正确报表放在共享上。',4),(92,3963,'/static/customer/genjin/3963/1557454915(1).png_3963.png','2019-05-10 10:21:43','张思',203,'2019.月扣税款2330.63元',1),(93,155,NULL,'2019-05-10 11:45:05','周萍',161,'18年收入49514.56 利润-99541.05，申报工资人员和社保2人。但是申报的工资金额与账上工资金额不一致，银行流水才入到18年5月份。麻烦会计尽快安排银行流水的录入，工资的改申报。',4),(94,810,NULL,'2019-05-10 15:01:59','唐海婷',187,'客户2017年之前是核定征收企业，服务费2000元/年，免账册费和工商年检汇算清缴。2018年该客户已变为查账征收，有税控盘开发票，每个季度客户都会控制开票金额在免增值税范围内，但是客户没有成本发票回来入账要交企业所得税，每次客户都不愿意交税，说我们不会做不帮她避税',1),(95,3808,'/static/customer/genjin/3808/ca0b41c7598c0a07bb9d1f5f23b8f4c.png_3808.png','2019-05-10 17:19:37','唐海婷',187,'客户18年8月成立的企业，无收入，现在客户说他自己去办理注销自己处理。',1),(96,3808,'/static/customer/genjin/3808/1557480034(1).jpg_3808.jpg','2019-05-10 17:21:57','唐海婷',187,'客户18年8月成立的企业，无收入，现在客户说他自己找人去办理注销自己处理',1),(97,4246,'/static/customer/genjin/4246/ca0b41c7598c0a07bb9d1f5f23b8f4c.png_4246.png','2019-05-10 17:22:56','唐海婷',187,'客户18年9月成立的企业，无收入，现在客户说他自己去办理注销自己处理',1),(98,217,NULL,'2019-05-10 18:57:46','周萍',161,'18年收入81167.64 利润是7239.82  可以弥补以前年度损益，申报两个人的社保和工资，汇算清缴成本没有填写，管理费金额填写错误，麻烦更改。',4),(99,217,NULL,'2019-05-10 19:02:38','周萍',161,'银行对账单的录入，看到只到18年3月份，麻烦尽快安排跟进',4),(100,218,NULL,'2019-05-10 19:17:10','周萍',161,'18年收入19310.68，利润为-100780.10，账务上发放工资上有一笔：其他应款-庄卫红，麻烦会计更正过来，18年的申报表没有及时下载，麻烦会计下载放共享上保存好。',4),(101,218,NULL,'2019-05-10 19:21:37','周萍',161,'增值税申报的收入为0，而账上的收入和企业所得税申报的收入为19310.68，三者收入不一致，麻烦会计尽快安排时间去更正',4),(102,247,NULL,'2019-05-10 19:39:40','周萍',161,'增值税申报的收入为98370.48  账上的收入为97358.22，企业所得税申报的收入为 97358.22，  而汇算清缴的收入为 97359.22，不一致，麻烦会计核实是什么原因。还有的汇算 清缴 的成本没有填写，而且要退税-3元？？',4),(103,5285,NULL,'2019-05-17 18:17:39','陈太智',116,'bvcvb',1),(104,5285,NULL,'2019-05-17 18:17:51','陈太智',116,'法的规定凤 梵蒂冈',1),(105,5063,NULL,'2019-05-20 09:44:16','陈太智',116,'到沙发到沙发到沙发发发凤\nfdfsdfsdfsdf',1),(110,2267,NULL,'2019-05-24 11:03:47','周萍',161,'fddfdg',1),(112,2267,NULL,'2019-05-24 11:24:56','陈太智',116,'88',1),(113,5285,NULL,'2019-05-28 13:52:18','陈太智',116,'sadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasd这个发大水sadasdsadasdsadasdsadasdsadasdsadasdsadasdsadasdsa是师德师风是dasdsadasdsadasdsadasdsadasdsadasdsadasd文字',2),(114,5285,NULL,'2019-05-28 13:53:11','陈太智',116,'电影《这个杀手不太冷》于1994年上映，由法国著名导演吕克 贝松执导，影星让·雷诺和娜塔莉波特曼主演，影片凭借出色的镜头掌控和对人心善恶的深层次挖掘成为了一部经典作品，该片先后获得日本电影学院奖最佳影片提名，和法国恺撒奖包括最佳导演、最佳男演员、最佳摄影、最佳剪辑等在内的七项重量级提名。',1),(115,5285,NULL,'2019-05-28 13:54:00','陈太智',116,'纽约贫民区住着一个意大利人，名叫莱昂（让·雷诺饰），他是一名职业杀手。一天，邻居家小姑娘玛蒂尔达（娜塔莉·波特曼饰）敲开了他的房门，要求在他这里暂避杀身之祸。原来，邻居家的主人是警察的眼线，因贪污了一小包毒品而遭到恶警史丹菲尔（加里·奥德曼饰）剿灭全家的惩罚。玛蒂尔达得到莱昂的救助，开始帮莱昂管理家务并教其识字，莱昂则教女孩用枪，两人相处融洽。并且在他们之间还产生了一种奇妙的化学反应：爱情。女孩跟踪史丹菲尔，贸然去报仇，不小心被抓。莱昂及时赶到，将女孩救回。他们再次搬家，但女孩还是落入史丹菲尔之手。莱昂撂倒一片警察，再次救出女孩并让她通过通风管道逃生，并嘱咐她去把他积攒的钱取出来。莱昂则化装成警察试图混出包围圈，但被狡猾的史丹菲尔识破，不得已引爆了身上的炸弹。',1),(116,5169,NULL,'2019-05-28 15:37:29','何燕平',290,'顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定三顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定三顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定123顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定三顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定三顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶定123',1),(117,5492,'','2019-05-30 11:05:28','陈太智',116,'得粉碎放斯蒂芬',1),(118,5492,'','2019-05-30 11:08:13','陈太智',116,'88888888888',1),(119,5492,'/static/customer/genjin/5492/da.png_5492.png|/static/customer/genjin/5492/违约金.png_5492.png|/static/customer/genjin/5492/违约金.png_5492.png|','2019-05-30 11:11:01','陈太智',116,'77777777',1),(120,5492,'','2019-05-30 11:36:00','陈太智',116,'23',1),(121,5492,'','2019-05-30 11:47:32','陈太智',116,'8888888888',1),(122,5492,'','2019-05-30 11:47:57','陈太智',116,'几句就坚决拒绝',1),(123,5492,'/static/customer/genjin/5492/banner.png_5492.png|/static/customer/genjin/5492/8.jpg_5492.jpg|','2019-05-31 15:20:01','吴蔚亮',98,'uu',1),(124,5102,'/static/customer/genjin/5102/2019-03-04 15-40-25屏幕截图.png_5102.png|','2019-06-05 14:36:34','张会会',164,'额外推翻为人服务而份额万人份第三方顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶当顶顶顶顶顶顶顶顶顶定额外推翻为人服务而份额万人份第三方顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶当顶顶顶顶顶顶顶顶顶定额外推翻为人服务而份额万人份第三方顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶当顶顶顶顶顶顶顶顶顶定额外推翻为人服务而份额万人份第三方顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶当顶顶顶顶顶顶顶顶顶定额外推翻为人服务而份额万人份第三方顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶当顶顶顶顶顶顶顶顶顶定额外推翻为人服务而份额万人份第三方顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶当顶顶顶顶顶顶顶顶顶定额外推翻为人服务而份额万人份第三方顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶当顶顶顶顶顶顶顶顶顶定',1),(125,5094,'','2019-06-05 16:00:51','张会会',164,'范德萨斯蒂芬斯蒂芬放第三方\ndsfsdfsdf',1),(126,5094,'','2019-06-05 16:09:26','陈太智',116,'iu和i',1),(127,5249,'','2019-06-05 16:09:47','陈太智',116,'fdsfsd',1),(128,5094,'','2019-06-05 16:10:45','陈太智',116,'范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=',1),(129,5094,'','2019-06-05 16:12:52','陈太智',116,'范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf范德萨斯蒂芬斯蒂芬放第三方 dsfsdfsdf=',1),(130,117,'','2019-06-05 16:22:12','陈太智',116,'纽约贫民区住着一个意大利人，名叫莱昂（让·雷诺饰），他是一名职业杀手。一天，邻居家小姑娘玛蒂尔达（娜塔莉·波特曼饰）敲开了他的房门，要求在他这里暂避杀身之祸。原来，邻居家的主人是警察的眼线，因贪污了一小包毒品而遭到恶警史丹菲尔（加里·奥德曼饰）剿灭全家的惩罚。玛蒂尔达得到莱昂的救助，开始帮莱昂管理家务并教其识字，莱昂则教女孩用枪，两人相处融洽。并且在他们之间还产生了一种奇妙的化学反应：爱情。女孩跟踪史丹菲尔，贸然去报仇，不小心被抓。莱昂及时赶到，将女孩救回。他们再次搬家，但女孩还是落入史丹菲尔之手。莱昂撂倒一片警察，再次救出女孩并让她通过通风管道逃生，并嘱咐她去把他积攒的钱取出来。莱昂则化装成警察试图混出包围圈，但被狡猾的史丹菲尔识破，不得已引爆了身上的炸弹。',1),(131,117,'','2019-06-05 16:22:40','陈太智',116,'约贫民区住着一个意大利人',1),(132,117,'','2019-06-05 16:25:50','陈太智',116,'纽约贫民区住着一个意大利人，名叫莱昂（让·雷诺饰），他是一名职业杀手。一天，邻居家小姑娘玛蒂尔达（娜塔莉·波特曼饰）敲开了他的房门，要求在他这里暂避杀身之祸。原来，邻居家的主人是警察的眼线，因贪污了一小包毒品而遭到恶警史丹菲尔（加里·奥德曼饰）剿灭全家的惩罚。玛蒂尔达得到莱昂的救助，开始帮莱昂管理家务并教其识字，莱昂则教女孩用枪，两人相处融洽。并且在他们之间还产生了一种奇妙的化学反应：爱情。女孩跟踪史丹菲尔，贸然去报仇，不小心被抓。莱昂及时赶到，将女孩救回。他们再次搬家，但女孩还是落入史丹菲尔之手。莱昂撂倒一片警察，再次救出女孩并让她通过通风管道逃生，并嘱咐她去把他积攒的钱取出来。莱昂则化装成警察试图混出包围圈，但被狡猾的史丹菲尔识破，不得已引爆了身上的炸弹。纽约贫民区住着一个意大利人，名叫莱昂（让·雷诺饰），他是一名职业杀手。一天，邻居家小姑娘玛蒂尔达（娜塔莉·波特曼饰）敲开了他的房门，要求在他这里暂避杀身之祸。原来，邻居家的主人是警察的眼线，因贪污了一小包毒品而遭到恶警史丹菲尔（加里·奥德曼饰）剿灭全家的惩罚。玛蒂尔达得到莱昂的救助，开始帮莱昂管理家务并教其识字，莱昂则教女孩用枪，两人相处融洽。并且在他们之间还产生了一种奇妙的化学反应：爱情。女孩跟踪史丹菲尔，贸然去报仇，不小心被抓。莱昂及时赶到，将女孩救回。他们再次搬家，但女孩还是落入史丹菲尔之手。莱昂撂倒一片警察，再次救出女孩并让她通过通风管道逃生，并嘱咐她去把他积攒的钱取出来。莱昂则化装成警察试图混出包围圈，但被狡猾的史丹菲尔识破，不得已引爆了身上的炸弹。纽约贫民区住着一个意大利人，名叫莱昂（让·雷诺饰），他是一名职业杀手。一天，邻居家小姑娘玛蒂尔达（娜塔莉·波特曼饰）敲开了他的房门，要求在他这里暂避杀身之祸。原来，邻居家的主人是警察的眼线，因贪污了一小包毒品而遭到恶警史丹菲尔（加里·奥德曼饰）剿灭全家的惩罚。玛蒂尔达得到莱昂的救助，开始帮莱昂管理家务并教其识字，莱昂则教女孩用枪，两人相处融洽。并且在他们之间还产生了一种奇妙的化学反应：爱情。女孩跟踪史丹菲尔，贸然去报仇，不小心被抓。莱昂及时赶到，将女孩救回。他们再次搬家，但女孩还是落入史丹菲尔之手。莱昂撂倒一片警察，再次救出女孩并让她通过通风管道逃生，并嘱咐她去把他积攒的钱取出来。莱昂则化装成警察试图混出包围圈，但被狡猾的史丹菲尔识破，不得已引爆了身上的炸弹。纽约贫民区住着一个意大利人，名叫莱昂（让·雷诺饰），他是一名职业杀手。一天，邻居家小姑娘玛蒂尔达（娜塔莉·波特曼饰）敲开了他的房门，要求在他这里暂避杀身之祸。原来，邻居家的主人是警察的眼线，因贪污了一小包毒品而遭到恶警史丹菲尔（加里·奥德曼饰）剿灭全家的惩罚。玛蒂尔达得到莱昂的救助，开始帮莱昂管理家务并教其识字，莱昂则教女孩用枪，两人相处融洽。并且在他们之间还产生了一种奇妙的化学反应：爱情。女孩跟踪史丹菲尔，贸然去报仇，不小心被抓。莱昂及时赶到，将女孩救回。他们再次搬家，但女孩还是落入史丹菲尔之手。莱昂撂倒一片警察，再次救出女孩并让她通过通风管道逃生，并嘱咐她去把他积攒的钱取出来。莱昂则化装成警察试图混出包围圈，但被狡猾的史丹菲尔识破，不得已引爆了身上的炸弹。',1),(135,5492,'','2019-06-06 09:13:17','陈太智',116,'房斯蒂芬',1);
/*!40000 ALTER TABLE `t_customer_genjin_msg` ENABLE KEYS */;
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
