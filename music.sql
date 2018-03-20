-- schema.sql

drop database if exists music;

create database music;

use music;

grant select, insert, update, delete on music.* to 'www-data'@'localhost' identified by 'www-data';

create table songs (
	`title` varchar(500) not null,
	`path` varchar(500) not null,
	`size` varchar(500) not null,
	`date` varchar(500) not null,
	`id` Int not null auto_increment,
   	primary key (`id`)
) engine=innodb default charset=utf8;
