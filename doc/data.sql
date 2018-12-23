create database `shenshuo` default character set utf8mb4 collate utf8mb4_unicode_ci;

 CREATE TABLE `cron_log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` varchar(30) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `task_cmd` varchar(120) DEFAULT NULL,
  `task_log` text,
  `exec_time` datetime DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8085 DEFAULT CHARSET=utf8;