


CREATE DATABASE IF NOT EXISTS `baza`;
use `baza`;


CREATE TABLE IF NOT EXISTS `tabela`(
`id` int NOT NULL AUTO_INCREMENT,
`temperature` DECIMAL(15,2),
`date_with_time` TIMESTAMP,
PRIMARY KEY (`id`)

);
