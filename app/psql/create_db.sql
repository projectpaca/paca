-- \i C:/Users/victor.dahl/Documents/GitHub/paca/app/psql/create_db.sql
\set ON_ERROR_STOP ON
\c ah8723
drop database if exists paca_database;
create database paca_database;
\c paca_database;


CREATE TABLE person(
	-- Anställda
	anstid			INT UNIQUE primary key
	,name			VARCHAR(30) NOT NULL
	,email			text
	,supervisor		BOOLEAN
);

CREATE TABLE phone (
	--Telefonnummer till anställd
	anstid_f		INT PRIMARY KEY	--FRÄMMANDE
	,phone_nr	INT NOT NULL

	,foreign key (anstid_f) references person(anstid)
);

CREATE TABLE pass(
	-- Info om ett pass
	pass_id		SERIAL UNIQUE PRIMARY KEY
	,name		VARCHAR(30) NOT NULL
	,behov		INT --Antal anställda som behövs på passet
	,date		DATE
	,time		TIME
	,break		TIME
);

CREATE TABLE shift_demand(
	pass_id_f		INT
	,pid_f		INT
	
	,foreign key (pass_id_f) references pass(pass_id)
	,foreign key (pid_f) references person(anstid)
);
	
CREATE TABLE availability(
	-- Anställdas tillgänglighet
	anstid_f		INT  PRIMARY KEY
	,date		DATE
	,time		TIME
	,comment	CHAR(144)
	
	,foreign key (anstid_f) references person(anstid)
);

CREATE TABLE department(
	-- Förteckning av befintliga avdelningar
	depid		SERIAL UNIQUE PRIMARY KEY
	,name		CHAR(144)
	,boss		int
	
	,foreign key (boss) references person(anstid)
);

CREATE TABLE avd_anstid(
	-- Vilken anställd som jobbar i vilken avdelning
	anstid_f 		INT PRIMARY KEY
	,depid_f	INT

	,foreign key (anstid_f) references person(anstid)
	,foreign key (depid_f) references department(depid)
);

/*CREATE TABLE images(
	anstid_f			int
	,imgname		CHAR(30)
	,img 			bytes
	,foreign key (anstid_f) references person(anstid)
);*/
	
/* REVOKE ALL PRIVILEGES ON DATABASE paca_database FROM public;
CREATE ROLE paca_admin LOGIN; 
GRANT paca_admin TO ah8723;
GRANT paca_admin TO ah8078; */