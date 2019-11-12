-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: Prison
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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
-- Current Database: `Prison`
--

USE `Prison`;

--
-- Table structure for table `Appeals`
--

DROP TABLE IF EXISTS `Appeals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Appeals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filing_date` date NOT NULL,
  `hearing_date` date DEFAULT NULL,
  `status` enum('FILED','UNDER REVIEW','HEARING SCHEDULED','ACCEPTED','REJECTED') NOT NULL,
  `prisoner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `prisoner_id` (`prisoner_id`),
  CONSTRAINT `Appeals_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`),
  CONSTRAINT `Appeals_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Appeals`
--

LOCK TABLES `Appeals` WRITE;
/*!40000 ALTER TABLE `Appeals` DISABLE KEYS */;
INSERT INTO `Appeals` VALUES (1,'2019-11-12',NULL,'FILED',1),(2,'2019-11-12',NULL,'FILED',1),(3,'2019-11-12','2000-10-11','HEARING SCHEDULED',4);
/*!40000 ALTER TABLE `Appeals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Assignment_Guards`
--

DROP TABLE IF EXISTS `Assignment_Guards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assignment_Guards` (
  `job_id` int(11) NOT NULL,
  `guard_id` int(11) NOT NULL,
  PRIMARY KEY (`job_id`,`guard_id`),
  KEY `guard_id` (`guard_id`),
  CONSTRAINT `Assignment_Guards_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `Jobs` (`id`),
  CONSTRAINT `Assignment_Guards_ibfk_2` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`),
  CONSTRAINT `Assignment_Guards_ibfk_3` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Assignment_Guards_ibfk_4` FOREIGN KEY (`job_id`) REFERENCES `Jobs` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assignment_Guards`
--

LOCK TABLES `Assignment_Guards` WRITE;
/*!40000 ALTER TABLE `Assignment_Guards` DISABLE KEYS */;
INSERT INTO `Assignment_Guards` VALUES (4,2),(4,3);
/*!40000 ALTER TABLE `Assignment_Guards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Assignment_Prisoners`
--

DROP TABLE IF EXISTS `Assignment_Prisoners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assignment_Prisoners` (
  `job_id` int(11) NOT NULL,
  `prisoner_id` int(11) NOT NULL,
  PRIMARY KEY (`job_id`,`prisoner_id`),
  KEY `prisoner_id` (`prisoner_id`),
  CONSTRAINT `Assignment_Prisoners_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `Jobs` (`id`),
  CONSTRAINT `Assignment_Prisoners_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`),
  CONSTRAINT `Assignment_Prisoners_ibfk_3` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Assignment_Prisoners_ibfk_4` FOREIGN KEY (`job_id`) REFERENCES `Jobs` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assignment_Prisoners`
--

LOCK TABLES `Assignment_Prisoners` WRITE;
/*!40000 ALTER TABLE `Assignment_Prisoners` DISABLE KEYS */;
INSERT INTO `Assignment_Prisoners` VALUES (3,1),(4,1),(3,3),(4,3);
/*!40000 ALTER TABLE `Assignment_Prisoners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Crimes`
--

DROP TABLE IF EXISTS `Crimes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Crimes` (
  `prisoner_id` int(11) NOT NULL,
  `crime` varchar(2047) NOT NULL,
  PRIMARY KEY (`prisoner_id`,`crime`),
  CONSTRAINT `Crimes_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`),
  CONSTRAINT `Crimes_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Crimes`
--

LOCK TABLES `Crimes` WRITE;
/*!40000 ALTER TABLE `Crimes` DISABLE KEYS */;
INSERT INTO `Crimes` VALUES (3,'arson'),(3,'murder'),(4,'Assault'),(4,'Murder'),(4,'Violations'),(5,'Murder'),(5,'Smuggling');
/*!40000 ALTER TABLE `Crimes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Emergency_Contacts`
--

DROP TABLE IF EXISTS `Emergency_Contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Emergency_Contacts` (
  `prisoner_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `relationship` varchar(255) DEFAULT NULL,
  `address` varchar(2047) NOT NULL,
  `phone` char(10) NOT NULL,
  PRIMARY KEY (`prisoner_id`,`first_name`,`middle_name`,`last_name`),
  CONSTRAINT `Emergency_Contacts_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`),
  CONSTRAINT `Emergency_Contacts_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Emergency_Contacts`
--

LOCK TABLES `Emergency_Contacts` WRITE;
/*!40000 ALTER TABLE `Emergency_Contacts` DISABLE KEYS */;
INSERT INTO `Emergency_Contacts` VALUES (1,'Naman','','','Brother','X199 Road','8877551100');
/*!40000 ALTER TABLE `Emergency_Contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Guards`
--

DROP TABLE IF EXISTS `Guards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Guards` (
  `id` int(11) NOT NULL,
  `shift` enum('DAY','NIGHT') DEFAULT NULL,
  `wing` char(1) DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `supervisor_id` (`supervisor_id`),
  KEY `id` (`id`),
  CONSTRAINT `Guards_ibfk_1` FOREIGN KEY (`supervisor_id`) REFERENCES `Prison_Staff` (`id`),
  CONSTRAINT `Guards_ibfk_2` FOREIGN KEY (`id`) REFERENCES `Prison_Staff` (`id`),
  CONSTRAINT `Guards_ibfk_3` FOREIGN KEY (`id`) REFERENCES `Prison_Staff` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Guards_ibfk_4` FOREIGN KEY (`supervisor_id`) REFERENCES `Prison_Staff` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Guards`
--

LOCK TABLES `Guards` WRITE;
/*!40000 ALTER TABLE `Guards` DISABLE KEYS */;
INSERT INTO `Guards` VALUES (2,'NIGHT','Q',NULL),(3,'DAY','W',NULL);
/*!40000 ALTER TABLE `Guards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Incident_Guards`
--

DROP TABLE IF EXISTS `Incident_Guards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Incident_Guards` (
  `offence_id` int(11) NOT NULL,
  `guard_id` int(11) NOT NULL,
  PRIMARY KEY (`offence_id`,`guard_id`),
  KEY `guard_id` (`guard_id`),
  CONSTRAINT `Incident_Guards_ibfk_1` FOREIGN KEY (`offence_id`) REFERENCES `Offences` (`id`),
  CONSTRAINT `Incident_Guards_ibfk_2` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`),
  CONSTRAINT `Incident_Guards_ibfk_3` FOREIGN KEY (`offence_id`) REFERENCES `Offences` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Incident_Guards_ibfk_4` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Incident_Guards`
--

LOCK TABLES `Incident_Guards` WRITE;
/*!40000 ALTER TABLE `Incident_Guards` DISABLE KEYS */;
INSERT INTO `Incident_Guards` VALUES (7,2);
/*!40000 ALTER TABLE `Incident_Guards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Incident_Prisoners`
--

DROP TABLE IF EXISTS `Incident_Prisoners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Incident_Prisoners` (
  `offence_id` int(11) NOT NULL,
  `prisoner_id` int(11) NOT NULL,
  PRIMARY KEY (`offence_id`,`prisoner_id`),
  KEY `prisoner_id` (`prisoner_id`),
  CONSTRAINT `Incident_Prisoners_ibfk_1` FOREIGN KEY (`offence_id`) REFERENCES `Offences` (`id`),
  CONSTRAINT `Incident_Prisoners_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`),
  CONSTRAINT `Incident_Prisoners_ibfk_3` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Incident_Prisoners_ibfk_4` FOREIGN KEY (`offence_id`) REFERENCES `Offences` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Incident_Prisoners`
--

LOCK TABLES `Incident_Prisoners` WRITE;
/*!40000 ALTER TABLE `Incident_Prisoners` DISABLE KEYS */;
INSERT INTO `Incident_Prisoners` VALUES (6,1),(7,1),(6,3),(7,3),(7,4);
/*!40000 ALTER TABLE `Incident_Prisoners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jobs`
--

DROP TABLE IF EXISTS `Jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Jobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(255) NOT NULL,
  `working_hours_begin` time DEFAULT NULL,
  `working_hours_end` time DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `supervisor_id` (`supervisor_id`),
  CONSTRAINT `Jobs_ibfk_1` FOREIGN KEY (`supervisor_id`) REFERENCES `Prison_Staff` (`id`),
  CONSTRAINT `Jobs_ibfk_2` FOREIGN KEY (`supervisor_id`) REFERENCES `Prison_Staff` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jobs`
--

LOCK TABLES `Jobs` WRITE;
/*!40000 ALTER TABLE `Jobs` DISABLE KEYS */;
INSERT INTO `Jobs` VALUES (3,'fijg','23:55:00','23:45:00',NULL),(4,'Laundry','09:00:00','11:00:00',5);
/*!40000 ALTER TABLE `Jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Offence_Type`
--

DROP TABLE IF EXISTS `Offence_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Offence_Type` (
  `offence_id` int(11) NOT NULL,
  `type` enum('ASSAULT','ATTEMPTED ESCAPE','FELONY','RIOTS','CONTRABAND','DESTRUCTION OF PROPERTY','INSUBORDINATION','MISCELLANEOUS') NOT NULL,
  PRIMARY KEY (`offence_id`,`type`),
  CONSTRAINT `Offence_Type_ibfk_1` FOREIGN KEY (`offence_id`) REFERENCES `Offences` (`id`),
  CONSTRAINT `Offence_Type_ibfk_2` FOREIGN KEY (`offence_id`) REFERENCES `Offences` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Offence_Type`
--

LOCK TABLES `Offence_Type` WRITE;
/*!40000 ALTER TABLE `Offence_Type` DISABLE KEYS */;
INSERT INTO `Offence_Type` VALUES (6,'ATTEMPTED ESCAPE'),(6,'INSUBORDINATION'),(7,'ASSAULT'),(7,'INSUBORDINATION');
/*!40000 ALTER TABLE `Offence_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Offences`
--

DROP TABLE IF EXISTS `Offences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Offences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(2047) NOT NULL,
  `date_time` datetime NOT NULL,
  `location` varchar(255) NOT NULL,
  `severity` enum('LOW','MEDIUM','HIGH') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Offences`
--

LOCK TABLES `Offences` WRITE;
/*!40000 ALTER TABLE `Offences` DISABLE KEYS */;
INSERT INTO `Offences` VALUES (6,'20 people escaped','2019-11-12 12:44:00','Hall','LOW'),(7,'Fight between inmates','2019-11-12 19:30:00','Prison Grounds','MEDIUM');
/*!40000 ALTER TABLE `Offences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prison_Staff`
--

DROP TABLE IF EXISTS `Prison_Staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Prison_Staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `dob` date DEFAULT NULL,
  `sex` enum('M','F','OTHER') NOT NULL,
  `address` varchar(2047) DEFAULT NULL,
  `phone` char(10) DEFAULT NULL,
  `post` enum('WARDEN','ADMINISTRATIVE STAFF','PRISON OFFICER','PROBATION OFFICER','PSYCHOLOGIST','EDUCATION STAFF','HEALTHCARE STAFF','KITCHEN STAFF','HOUSEKEEPING STAFF','MAINTENANCE STAFF','GUARD') NOT NULL,
  `salary` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prison_Staff`
--

LOCK TABLES `Prison_Staff` WRITE;
/*!40000 ALTER TABLE `Prison_Staff` DISABLE KEYS */;
INSERT INTO `Prison_Staff` VALUES (2,'Pranav','','Pramod',NULL,'M',NULL,NULL,'GUARD',20000),(3,'Oorja','b','naman','2000-11-11','F','dg','9899891123','GUARD',8000),(4,'Mallika','S','Subramanian','2000-01-20','F','B83 enclave','9899810000','HEALTHCARE STAFF',9000),(5,'Lola','','','1999-10-10','F','Marg Enclave','8010099876','HOUSEKEEPING STAFF',10000);
/*!40000 ALTER TABLE `Prison_Staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prisoners`
--

DROP TABLE IF EXISTS `Prisoners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Prisoners` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `sex` enum('M','F','OTHER') NOT NULL,
  `dob` date DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `height` float DEFAULT NULL,
  `blood_group` enum('A+','A-','B+','B-','O+','O-','AB+','AB-') DEFAULT NULL,
  `medical_history` varchar(2047) DEFAULT NULL,
  `arrival_date` date NOT NULL,
  `sentence` varchar(2047) NOT NULL,
  `cell` int(3) NOT NULL,
  `security_level` enum('LOW','MEDIUM','HIGH') NOT NULL,
  `wing` char(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prisoners`
--

LOCK TABLES `Prisoners` WRITE;
/*!40000 ALTER TABLE `Prisoners` DISABLE KEYS */;
INSERT INTO `Prisoners` VALUES (1,'Shradha','','Sehgal','F','2001-10-21',40,5.5,'O+','','2019-11-11','20 Years without Payrole',20,'LOW','Q'),(3,'james','','','M','2000-11-11',22,132,'B-','ssaffs','2019-11-12','3 years',132,'LOW','A'),(4,'Max','','','M','1987-03-04',70,5.4,'O+','None','2019-11-12','10 years',199,'LOW','A'),(5,'Arindam','Shiva','Tripathi','M','2001-01-01',60,5.8,'O+',NULL,'2019-11-12','20 Years without payrole',200,'MEDIUM','Q');
/*!40000 ALTER TABLE `Prisoners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Visitors`
--

DROP TABLE IF EXISTS `Visitors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Visitors` (
  `prisoner_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `relationship` varchar(255) DEFAULT NULL,
  `address` varchar(2047) DEFAULT NULL,
  `phone` char(10) DEFAULT NULL,
  PRIMARY KEY (`prisoner_id`,`first_name`,`middle_name`,`last_name`),
  CONSTRAINT `Visitors_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`),
  CONSTRAINT `Visitors_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Visitors`
--

LOCK TABLES `Visitors` WRITE;
/*!40000 ALTER TABLE `Visitors` DISABLE KEYS */;
INSERT INTO `Visitors` VALUES (1,'Jivitesh','','Jain','Friend','139 Bakul Nivas, IIIT Hyderabad','9711267621'),(1,'Naman','','','Brother','X199 Road','8811997755'),(4,'Priya','','','Mother','66 Enclave',NULL);
/*!40000 ALTER TABLE `Visitors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Visits`
--

DROP TABLE IF EXISTS `Visits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Visits` (
  `prisoner_id` int(11) NOT NULL,
  `date_time` datetime NOT NULL,
  `visitor_first_name` varchar(255) NOT NULL,
  `visitor_middle_name` varchar(255) NOT NULL,
  `visitor_last_name` varchar(255) NOT NULL,
  `guard_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`prisoner_id`,`date_time`),
  KEY `prisoner_id` (`prisoner_id`,`visitor_first_name`,`visitor_middle_name`,`visitor_last_name`),
  KEY `guard_id` (`guard_id`),
  CONSTRAINT `Visits_ibfk_1` FOREIGN KEY (`prisoner_id`, `visitor_first_name`, `visitor_middle_name`, `visitor_last_name`) REFERENCES `Visitors` (`prisoner_id`, `first_name`, `middle_name`, `last_name`),
  CONSTRAINT `Visits_ibfk_2` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`),
  CONSTRAINT `Visits_ibfk_3` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Visits_ibfk_4` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Visits`
--

LOCK TABLES `Visits` WRITE;
/*!40000 ALTER TABLE `Visits` DISABLE KEYS */;
INSERT INTO `Visits` VALUES (1,'2019-11-12 13:04:00','Jivitesh','','Jain',NULL),(1,'2019-11-12 13:05:00','Jivitesh','','Jain',2),(1,'2019-11-12 13:07:00','Jivitesh','','jain',2),(1,'2019-11-12 19:35:00','Naman','','',3),(4,'2019-11-12 19:33:00','Priya','','',3);
/*!40000 ALTER TABLE `Visits` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-13  0:37:33
