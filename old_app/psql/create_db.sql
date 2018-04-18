-- \i C:/Users/victor.dahl/Documents/GitHub/paca/app/psql/create_db.sql
\set ON_ERROR_STOP ON
\c ah8723
drop database if exists paca_database;
create database paca_database;
\c paca_database;

CREATE TABLE person (
     	-- Information om en anställd
     empid					INT PRIMARY KEY
     ,pnr						INT UNIQUE NOT NULL
	,name						VARCHAR(30) NOT NULL
     ,email						TEXT
     ,employ_date		DATE
     ,emp_type			TEXT NOT NULL
     --,def_img
);
 
CREATE TABLE adress (
	-- Adressinfo för anställda
	empid_f					INT PRIMARY KEY
     ,street					VARCHAR
     ,postcode				INT
     ,city						TEXT
	 
	 ,foreign key (empid_f) references person(empid)
	);
 
CREATE TABLE admin_permission (
	-- Register över användare med förhöjda rättigheter. Booleskt värde (chef) för fulla rättigheter. 
	empid_f					INT PRIMARY KEY
	,chef						BOOLEAN
 
	,foreign key (empid_f) references person(empid)
);
 
CREATE TABLE phone (
     	--Telefonnummer till anställd
     	empid_f				INT PRIMARY KEY  	
     	,phone				INT NOT NULL
     	,type					CHAR(10)
 
     	,foreign key (empid_f) references person(empid)
);
 
 
CREATE TABLE next_of_kin (
	--En persons närmsta anhöriga
	empid_f				INT PRIMARY KEY
	,name					VARCHAR(30) NOT NULL
	,phone				INT NOT NULL
	,relationship		CHAR(10)
	,prio					INT                  	
 
	,foreign key (empid_f) references person(empid)
);
 
CREATE TABLE shift (
     	-- Info om ett pass
     	shift_id             	     	SERIAL UNIQUE PRIMARY KEY
     	,depid_f            	     	INT NOT NULL
     	,staffing						INT NOT NULL
     	,date       	     			DATE NOT NULL
     	,start_time       	     	TIME NOT NULL
     	,duration          	     	 TIME NOT NULL
     	,rest              	     		TIME
     	,available         	     	BOOLEAN
     	,description               TEXT
     	,comment        	     	TEXT
);
 
CREATE TABLE shift_staffing (
     	-- Bokade personer på ett pass
     	empid_f           	     	INT PRIMARY KEY
     	,shiftid_f						INT
     	,trainee            	     	BOOLEAN
     	
     	,foreign key (empid_f) references person(empid)
     	,foreign key (shiftid_f) references shift(shift_id)
);
     	
CREATE TABLE availability(
     	-- Anställdas tillgänglighet
     	empid_f           	    	INT PRIMARY KEY
     	,available         	    	BOOLEAN
     	,date       	     		DATE
     	,start_time       	    TIME
     	,duration				TIME
     	,comment				CHAR(144)
     	
     	,foreign key (empid_f) references person(empid)
);
 
CREATE TABLE department(
     	-- Förteckning över avdelningar
     	depid      	     		SERIAL UNIQUE PRIMARY KEY
     	,name						CHAR(144)
     	,description			CHAR(144)
     	,supervisor				INT
 
,foreign key (supervisor) references person(empid)
);
 
CREATE TABLE dep_empid(
     	-- Vilken anställd som jobbar i vilken avdelning (kan vara flera)
     	empid_f           	     	INT PRIMARY KEY
     	,depid_f  	               	INT
 
     	,foreign key (empid_f) references person(empid)
     	,foreign key (depid_f) references department(depid)
);
 
/* CREATE TABLE images(
     	-- Tabell för samtliga sparade profilbilder för en kund
     	empid_f                     	INT PRIMARY KEY
     	,imgname        	     	CHAR(30)
     	,img                 	bytes
 
     	,foreign key (empid_f) references person(empid)*/

	
/* REVOKE ALL PRIVILEGES ON DATABASE paca_database FROM public;
CREATE ROLE paca_admin LOGIN; 
GRANT paca_admin TO ah8723;
GRANT paca_admin TO ah8078; */