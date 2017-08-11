/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50628
 Source Host           : localhost
 Source Database       : emysite

 Target Server Type    : MySQL
 Target Server Version : 50628
 File Encoding         : utf-8

 Date: 08/11/2017 13:07:12 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_7352dbe385444ef1_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_7352dbe385444ef1_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_91bcb7f89f25c6e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_60c1622e7d366e73_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can add permission', '2', 'add_permission'), ('5', 'Can change permission', '2', 'change_permission'), ('6', 'Can delete permission', '2', 'delete_permission'), ('7', 'Can add group', '3', 'add_group'), ('8', 'Can change group', '3', 'change_group'), ('9', 'Can delete group', '3', 'delete_group'), ('10', 'Can add user', '4', 'add_user'), ('11', 'Can change user', '4', 'change_user'), ('12', 'Can delete user', '4', 'delete_user'), ('13', 'Can add content type', '5', 'add_contenttype'), ('14', 'Can change content type', '5', 'change_contenttype'), ('15', 'Can delete content type', '5', 'delete_contenttype'), ('16', 'Can add session', '6', 'add_session'), ('17', 'Can change session', '6', 'change_session'), ('18', 'Can delete session', '6', 'delete_session'), ('19', 'Can add 文章', '7', 'add_post'), ('20', 'Can change 文章', '7', 'change_post'), ('21', 'Can delete 文章', '7', 'delete_post'), ('22', 'Can add 评论', '8', 'add_comment'), ('23', 'Can change 评论', '8', 'change_comment'), ('24', 'Can delete 评论', '8', 'delete_comment'), ('25', 'Can add Tag', '9', 'add_tag'), ('26', 'Can change Tag', '9', 'change_tag'), ('27', 'Can delete Tag', '9', 'delete_tag'), ('28', 'Can add Tagged Item', '10', 'add_taggeditem'), ('29', 'Can change Tagged Item', '10', 'change_taggeditem'), ('30', 'Can delete Tagged Item', '10', 'delete_taggeditem');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `auth_user`
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$20000$uN2fNXaGOuNq$9pCJM8/+IdQ6zLVpXpfsBtFHWXZuMef1yk58cdW0p0M=', '2017-07-31 10:48:32.375123', '1', 'jimmy', '', '', 'jim@jim.com', '1', '1', '2017-07-31 10:04:07.736487');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_65912f3b2183a4a1_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_65912f3b2183a4a1_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_5d50410bff156d79_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_us_permission_id_deb38ce2e6d8add_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_us_permission_id_deb38ce2e6d8add_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_2a668f2b7599a0fa_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `blog_comment`
-- ----------------------------
DROP TABLE IF EXISTS `blog_comment`;
CREATE TABLE `blog_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `body` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_comment_post_id_2b0fafa5dc122745_fk_blog_post_id` (`post_id`),
  CONSTRAINT `blog_comment_post_id_2b0fafa5dc122745_fk_blog_post_id` FOREIGN KEY (`post_id`) REFERENCES `blog_post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `blog_comment`
-- ----------------------------
BEGIN;
INSERT INTO `blog_comment` VALUES ('1', 'Jimmy', 'jimmy@jimmy.com', '中新经纬客户端8月1日电(董湘依) 从年初持续至今的楼市调控风暴仍在继续，不管房价是涨是跌，对于在一二线城市里的奋斗打拼的普通人来说，他们的梦想之一或许就是拥有自己的住房！如果买房之路上还能“摊上”一位给力的好老板，那人生应该算是相当圆满了！', '2017-08-02 13:52:45.518202', '2017-08-02 13:52:45.518266', '1', '2'), ('2', 'Jimmy', 'jimmy@jimmy.com', '中新经纬客户端8月1日电(董湘依) 从年初持续至今的楼市调控风暴仍在继续，不管房价是涨是跌，对于在一二线城市里的奋斗打拼的普通人来说，他们的梦想之一或许就是拥有自己的住房！如果买房之路上还能“摊上”一位给力的好老板，那人生应该算是相当圆满了！', '2017-08-02 13:53:05.075205', '2017-08-02 13:53:05.075301', '1', '2'), ('3', 'tommy', 'tommy@tommy.com', '中新经纬客户端8月1日电(董湘依) 从年初持续至今的楼市调控风暴仍在继续，不管房价是涨是跌，对于在一二线城市里的奋斗打拼的普通人来说，他们的梦想之一或许就是拥有自己的住房！如果买房之路上还能“摊上”一位给力的好老板，那人生应该算是相当圆满了！', '2017-08-02 13:53:19.177488', '2017-08-02 13:53:19.177529', '1', '2'), ('4', '中国', 'tom@tom.com', '中新经纬客户端8月1日电(董湘依) 从年初持续至今的楼市调控风暴仍在继续，不管房价是涨是跌，对于在一二线城市里的奋斗打拼的普通人来说，他们的梦想之一或许就是拥有自己的住房！如果买房之路上还能“摊上”一位给力的好老板，那人生应该算是相当圆满了！', '2017-08-02 13:54:02.537993', '2017-08-02 13:54:02.538043', '1', '2'), ('5', '中国', 'tom@tom.com', '中新经纬客户端8月1日电(董湘依) 从年初持续至今的楼市调控风暴仍在继续，不管房价是涨是跌，对于在一二线城市里的奋斗打拼的普通人来说，他们的梦想之一或许就是拥有自己的住房！如果买房之路上还能“摊上”一位给力的好老板，那人生应该算是相当圆满了！', '2017-08-02 13:54:22.775108', '2017-08-02 13:54:22.775164', '1', '2'), ('6', 'Andklo', 'andli@tom.com', 'It\'s very interesting.\r\ni like it', '2017-08-02 13:55:36.448487', '2017-08-02 13:57:35.441438', '0', '2'), ('7', 'M4 AK47', 'M4AK47@aliyun.com', 'This is very interesting ', '2017-08-02 14:02:39.461751', '2017-08-02 14:02:39.461810', '1', '2'), ('8', 'LeftLeft', 'Left@left.com', 'please shooting', '2017-08-02 14:05:01.261888', '2017-08-02 14:05:01.262141', '1', '2'), ('9', 'LeftLeft', 'Left@left.com', 'please shooting', '2017-08-02 14:05:54.185100', '2017-08-02 14:05:54.185189', '1', '2'), ('10', '这是一个评论', 'pinglun@pinglun.com', '发来得及案例集\r\n', '2017-08-10 15:41:01.773311', '2017-08-10 15:41:01.773341', '1', '1');
COMMIT;

-- ----------------------------
--  Table structure for `blog_post`
-- ----------------------------
DROP TABLE IF EXISTS `blog_post`;
CREATE TABLE `blog_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `body` longtext NOT NULL,
  `publish` datetime(6) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `status` varchar(10) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_post_author_id_7de2c580f74e2bb_fk_auth_user_id` (`author_id`),
  KEY `blog_post_2dbcba41` (`slug`),
  CONSTRAINT `blog_post_author_id_7de2c580f74e2bb_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `blog_post`
-- ----------------------------
BEGIN;
INSERT INTO `blog_post` VALUES ('1', '0731早报｜反制措施升级！普京：美国外交人员必须离境', 'zaobao-0730', '反制措施升级！普京：美国外交人员必须离境\r\n\r\n据法新社消息，俄罗斯总统普京宣布755名美国外交官必须离开俄罗斯。\r\n\r\n另据俄罗斯RT新闻网消息，俄罗斯总统弗拉基米尔·普京在接受Rossiya 1电视频道专访时表示，755名美国外交官将不得不离开俄罗斯，因为华盛顿对俄的不友好政策。\r\n\r\n“美方在毫无缘由的情形下采取了一项措施，但重要的是要注意，这使俄美关系恶化了。他们非法限制，企图影响世界其他国家，包括那些有兴趣发展和保持与俄罗斯的关系的国家，甚至我们的盟友，”普京在星期天对频道主持人弗拉基米尔·索洛维诺夫说。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n美军小动作不停 萨德系统连续两次测试成功\r\n\r\n据美国全国广播公司（NBC）消息，美国军方已经成功测试了太平洋高空区域防卫系统，即“萨德（THAAD）”反导防御系统。\r\n\r\n美国导弹防御局（MDA）负责人在当地媒体引用的声明中证实了这一消息。\r\n\r\n声明中还表示，中程目标弹道导弹（MRBM）先由美国空军C-17在太平洋上空发射，随后位于阿拉斯加州科迪亚克的太平洋太空港复合体阿拉斯加州的“萨德（THAAD）”武器系统检测到导弹后，立即启动跟踪和拦截目标。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n索马里恐怖组织袭击下沙巴 至少致8名非盟军死亡\r\n\r\n据福克斯新闻网（Fox News）消息，索马里反政府武装“沙巴布”（Al-Shabab，又称索马里青年党）的战斗人员30日袭击了索马里南部，造成至少8名非洲联盟军死亡。\r\n\r\n据路透消息，当地的一名高级地区官员说，星期天在青年党战斗人员和索马里政府和非洲联盟维和部队之间的战斗死亡人数为24人。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n巴勒斯坦将把犹太人定居点问题交海牙裁决\r\n\r\n据联合早报消息，巴勒斯坦外长马勒基30日对外表示，巴勒斯坦领导层决定近期向荷兰海牙国际刑事法院（ICC）提交申请，将以色列在巴勒斯坦土地上建设犹太人定居点的问题交由国际刑事法院裁决。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n白宫新通讯主任妻子提出离婚 或因不喜欢特朗普\r\n\r\n据美国《纽约每日新闻》30日报道，就在斯卡拉穆奇入职白宫前几周，他的第二任妻子狄德利·鲍尔毅然提出离婚，而她当时还怀着9个月的身孕，即将临盆。二人婚姻危机的源头似乎正是鲍尔对斯卡拉穆奇的新上司，以及整个华盛顿政治圈发自内心的“嫌恶”。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n安倍又想拉女右翼分子入阁 该女曾否认日本侵华历史\r\n\r\n由于前防卫大臣稻田朋美等“女将”丑闻不断，导致内阁支持率大跌。日本首相安倍晋三有意于8月3日改组内阁时邀自己的女性朋友、右翼分子樱井良子进入内阁，出任文部科学大臣，以改善“安倍娘子军”形象，提高支持率。\r\n\r\n日本《产经新闻》29日称，1945年出生的樱井良子是日本右翼论坛活跃分子。她否认日本侵华历史、南京大屠杀和“慰安妇”问题，曾参与编写《最新日本史》一书，将“七七事变”以及中日全面战争爆发的责任推到中国身上。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n特朗普鼓励警员“动粗”遭猛批 纽约警局局长：外行\r\n\r\n美国总统鼓励警察“动粗”？据美国有线电视新闻网(CNN)30日报道，特朗普当地时间28日在纽约州萨福克县会晤当地执法人员，并就黑帮暴力问题发表演讲。特朗普表示，警员对于被抓获的嫌疑人可以“强硬”一些、“对于刚刚杀过人的嫌犯不用太客气”“尽管把他们狠狠地丢上囚车”。演讲时气氛十分热烈，在特朗普讲到上述语句时，现场甚至爆发出阵阵掌声和喝彩声。然而，这番讲话迅速被各界解读为“总统鼓励警员滥用暴力”，引发广泛争议并遭到全美多间警局驳斥。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n日本火箭发射失败 民间企业独立开发火箭进程受阻\r\n\r\n据联合时报消息，日本民间企业独立开发的火箭首次抵达高度超过100公里的太空的壮举未能实现，发射以失败告终。\r\n\r\n日本北海道大树町的航天创新企业“星际科技”（Interstellar Technologies）在当地时间30日下午4时半左右，从该町的试验场发射了自主开发的小型火箭。不过，由于来自火箭的通信在约80秒后中断而紧急停止了发动机。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n脱欧不忘卖酒 苏格兰要求英保护威士忌出口\r\n\r\n据英国星期日快报（Sunday Express）消息，苏格兰政府要求英国当局制定法律框架，在英国脱欧后保护苏格兰威士忌出口。\r\n\r\n据BBC报道，苏格兰经济部长布朗提出了相关建议。他说，出口威士忌每年给苏格兰创造40亿美元英镑 (约合353.87亿人民币)的收入，还能提供2万个就业岗位。\r\n\r\n0731早报｜反制措施升级！普京：美国外交人员必须离境\r\n\r\n美国牛肉真来了：已进入超市 每公斤100-300元\r\n\r\n距离我国解禁美国牛肉，已经有1个多月的时间了，1个多月以来，美国牛肉已经进入国内各大电商平台和零售商超。\r\n\r\n各大主要生鲜电商平台也已经开售进口美国牛肉。目前北京市场销售的国产牛肉，大多来自内蒙古、河北等地区，以冷鲜肉为主，价格普遍是每公斤70-90元。进口牛肉主要是冷冻产品，其中澳大利亚牛肉每公斤55-70元，巴西等南美牛肉每公斤在40-55元。而目前开卖的进口美国牛肉，主打中高端市场，通过空运过来，价格每公斤100元到300元不等', '2017-07-31 10:55:00.000000', '2017-07-31 10:57:13.409115', '2017-08-02 21:56:11.744368', 'published', '1'), ('2', '杨焕宁“消失”90天后，中纪委给出了答案', 'yanghuanning-0730', '7月31日，中纪委通报：日前，经中共中央批准，中共中央纪委对第十八届中央委员，国家安全生产监督管理总局原党组书记、局长杨焕宁严重违纪问题进行了立案审查。\r\n\r\n经查，杨焕宁同志身为中央委员，严重违反政治纪律和政治规矩，在大是大非问题上背离党性原则；违反廉洁纪律，利用职权谋取私利。依据《中国共产党纪律处分条例》等有关规定，经中央纪委常委会会议研究并报中央政治局会议审议，决定给予杨焕宁同志留党察看二年处分，由监察部报国务院批准给予其行政撤职处分，降为副局级非领导职务；终止其党的十八大代表资格；收缴其违纪所得。给予其留党察看二年的处分，待召开中央委员会全体会议时予以追认。\r\n\r\n此前，杨焕宁已经“消失”了90天。\r\n\r\n杨焕宁“消失”90天后，中纪委给出了答案\r\n\r\n据安监总局官网显示，5月2日14时50分左右，贵州省毕节市大方县境内，成贵快铁在建工程七扇岩隧道发生瓦斯爆炸事故。接到事故报告后，安监总局党组书记、局长杨焕宁立即做出部署，即派工作组立即赶赴现场。\r\n\r\n上述消息，是杨焕宁最近一次公开亮相。\r\n\r\n从5月2日至7月31日，杨焕宁缺席了安监系统的一系列重要会议，例如5月5日的全国安全生产应急救援队伍做好2017年汛期事故灾害救援工作视频会议，5月15日的推进“两学一做”学习教育常态化制度化动员部署会议等等。\r\n\r\n7月26-27日两天，省部级主要领导干部“学习习近平总书记重要讲话精神，迎接党的十九大”专题研讨班在京举行。\r\n\r\n据27日晚央视《新闻联播》视频画面显示，各部委及总局一把手均出席了这个会议，但是画面中没有杨焕宁。\r\n\r\n就在27日当晚，安监总局官网“领导信息”板块，杨焕宁的简历被撤下。官网显示，目前，安监总局领导班子由5名副局长、一名纪检组长、一名总工程师担任，而安监总局局长岗位暂缺。\r\n\r\n生于1957年3月的杨焕宁，现年60岁。“政事儿”（微信ID：gcxxjgzh）注意到，此前，媒体报道杨焕宁的仕途履历时，常采用两个标签“老公安”、“反恐专家”。\r\n\r\n杨焕宁“消失”90天后，中纪委给出了答案\r\n\r\n跟许多“50后”相同，杨焕宁插过队，当过工人。1979年考入西南政法学院刑侦专业，1983年毕业后成为公安部刑事侦察局办公室干部。据《人民日报》时政公号报道，杨焕宁的父亲也是公安，曾任职济南铁路公安局。\r\n\r\n从1983年参加工作，至2015年10月调任安监总局局长，这长达32年间，杨焕宁只于2005年至2008年这三年，任黑龙江省委政法委书记，其余年份一直在公安系统任职，从警年限前后共计达29年。\r\n\r\n其间，周永康于2002年至2003年，出任中央政治局委员、中央书记处书记，国务委员、国务院党组成员；杨焕宁时任公安部副部长、党委委员。\r\n\r\n2003年至2013年，周先后担任中央政治局委员、中央政法委员会副书记、公安部部长；中央政治局常委、中央政法委员会书记。杨焕宁则经历了从公安部副部长，到黑龙江省委政法委书记（2005年），再到正部级公安部常务副部长的仕途调整。\r\n\r\n杨焕宁由黑龙江省委政法委书记，调任正部级公安部常务副部长时，正值2008年5月，距离2008北京奥运只余三个月。\r\n', '2017-07-31 11:03:00.000000', '2017-07-31 11:04:21.063215', '2017-08-02 21:55:57.202473', 'published', '1'), ('3', 'One more post', 'one-more-post', 'Post Body.', '2017-07-31 11:23:00.000000', '2017-07-31 11:23:35.228845', '2017-08-02 15:01:28.762014', 'published', '1'), ('4', 'New title', 'Another-post', 'Post Body.', '2017-07-31 11:29:00.000000', '2017-07-31 11:29:11.066078', '2017-08-02 15:01:38.585353', 'published', '1');
COMMIT;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_4ecf8f95afd686f9_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_3ac078208108e130_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_4ecf8f95afd686f9_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_3ac078208108e130_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_admin_log`
-- ----------------------------
BEGIN;
INSERT INTO `django_admin_log` VALUES ('1', '2017-07-31 10:57:13.410611', '1', '0731早报｜反制措施升级！普京：美国外交人员必须离境', '1', '', '7', '1'), ('2', '2017-07-31 11:04:21.064424', '2', '杨焕宁“消失”90天后，中纪委给出了答案', '1', '', '7', '1'), ('3', '2017-08-02 13:57:35.444764', '6', 'Comment by Andklo on 杨焕宁“消失”90天后，中纪委给出了答案', '2', '已修改 active 。', '8', '1'), ('4', '2017-08-02 15:01:18.420806', '1', '0731早报｜反制措施升级！普京：美国外交人员必须离境', '2', '已修改 tags 。', '7', '1'), ('5', '2017-08-02 15:01:28.784220', '3', 'One more post', '2', '已修改 tags 。', '7', '1'), ('6', '2017-08-02 15:01:38.609799', '4', 'New title', '2', '已修改 tags 。', '7', '1'), ('7', '2017-08-02 15:01:55.893395', '2', '杨焕宁“消失”90天后，中纪委给出了答案', '2', '已修改 tags 。', '7', '1'), ('8', '2017-08-02 21:55:57.233519', '2', '杨焕宁“消失”90天后，中纪委给出了答案', '2', '已修改 tags 。', '7', '1'), ('9', '2017-08-02 21:56:11.774821', '1', '0731早报｜反制措施升级！普京：美国外交人员必须离境', '2', '已修改 tags 。', '7', '1');
COMMIT;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_2bfcf3218182610d_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry'), ('3', 'auth', 'group'), ('2', 'auth', 'permission'), ('4', 'auth', 'user'), ('8', 'blog', 'comment'), ('7', 'blog', 'post'), ('5', 'contenttypes', 'contenttype'), ('6', 'sessions', 'session'), ('9', 'taggit', 'tag'), ('10', 'taggit', 'taggeditem');
COMMIT;

-- ----------------------------
--  Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_migrations`
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2017-07-31 10:03:35.542489'), ('2', 'auth', '0001_initial', '2017-07-31 10:03:35.730014'), ('3', 'admin', '0001_initial', '2017-07-31 10:03:35.785882'), ('4', 'contenttypes', '0002_remove_content_type_name', '2017-07-31 10:03:35.870212'), ('5', 'auth', '0002_alter_permission_name_max_length', '2017-07-31 10:03:35.898090'), ('6', 'auth', '0003_alter_user_email_max_length', '2017-07-31 10:03:35.923663'), ('7', 'auth', '0004_alter_user_username_opts', '2017-07-31 10:03:35.933776'), ('8', 'auth', '0005_alter_user_last_login_null', '2017-07-31 10:03:35.962241'), ('9', 'auth', '0006_require_contenttypes_0002', '2017-07-31 10:03:35.964230'), ('10', 'sessions', '0001_initial', '2017-07-31 10:03:35.999938'), ('11', 'blog', '0001_initial', '2017-07-31 10:40:41.878233'), ('12', 'blog', '0002_comment', '2017-08-02 12:58:17.998915'), ('13', 'taggit', '0001_initial', '2017-08-02 14:54:25.286389'), ('14', 'taggit', '0002_auto_20150616_2121', '2017-08-02 14:54:25.319503'), ('15', 'blog', '0003_auto_20170802_1454', '2017-08-02 14:54:25.351769');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_session`
-- ----------------------------
BEGIN;
INSERT INTO `django_session` VALUES ('43ul7yf011vv72sgv7dm5bmd8cgtkkkh', 'OGZhYjQyYjI3ZDUyMjJhMzZiMDljMTAwYWM1NmM3OWExOTRlNTVhZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY4ZWY0MzBkNzkyMmVjN2NkOTEzZGQ1ZTBlZjYzNTcyZDZjMzMzNzAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-08-14 10:48:32.376786');
COMMIT;

-- ----------------------------
--  Table structure for `taggit_tag`
-- ----------------------------
DROP TABLE IF EXISTS `taggit_tag`;
CREATE TABLE `taggit_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `taggit_tag`
-- ----------------------------
BEGIN;
INSERT INTO `taggit_tag` VALUES ('1', 'china', 'china'), ('2', 'music', 'music'), ('3', 'jazz', 'jazz'), ('4', '音乐', ''), ('6', '自己', '_1'), ('8', '中国', '_2'), ('9', 'django', 'django'), ('10', 'code', 'code'), ('11', 'java', 'java'), ('12', 'python', 'python'), ('14', '杨焕宁', '_3'), ('16', '夏天', '_4'), ('17', 'summet', 'summet'), ('18', 'yanghuanyu', 'yanghuanyu'), ('19', 'myself', 'myself');
COMMIT;

-- ----------------------------
--  Table structure for `taggit_taggeditem`
-- ----------------------------
DROP TABLE IF EXISTS `taggit_taggeditem`;
CREATE TABLE `taggit_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `taggit_taggeditem_tag_id_707f74e17abc29b_fk_taggit_tag_id` (`tag_id`),
  KEY `taggit_taggeditem_af31437c` (`object_id`),
  KEY `taggit_taggeditem_content_type_id_69b9dd14c77d9aea_idx` (`content_type_id`,`object_id`),
  CONSTRAINT `taggi_content_type_id_76b17d7df869a72e_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `taggit_taggeditem_tag_id_707f74e17abc29b_fk_taggit_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `taggit_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `taggit_taggeditem`
-- ----------------------------
BEGIN;
INSERT INTO `taggit_taggeditem` VALUES ('7', '3', '7', '9'), ('8', '3', '7', '2'), ('9', '3', '7', '3'), ('10', '4', '7', '10'), ('11', '4', '7', '11'), ('12', '4', '7', '12'), ('16', '2', '7', '1'), ('17', '2', '7', '18'), ('18', '2', '7', '17'), ('19', '1', '7', '1'), ('20', '1', '7', '2'), ('21', '1', '7', '19');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
