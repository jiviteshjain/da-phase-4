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
-- Table structure for table `Appeals`
--

DROP TABLE IF EXISTS `Appeals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Appeals` (
  `id` int(11) NOT NULL,
  `filing_date` date NOT NULL,
  `hearing_date` date DEFAULT NULL,
  `status` enum('FILED','UNDER REVIEW','HEARING SCHEDULED','ACCEPTED','REJECTED') NOT NULL,
  `prisoner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `prisoner_id` (`prisoner_id`),
  CONSTRAINT `Appeals_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Assignment_Guards_ibfk_2` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Assignment_Prisoners_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Crimes_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Emergency_Contacts_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `supervisor_id` (`supervisor_id`),
  KEY `id` (`id`),
  CONSTRAINT `Guards_ibfk_1` FOREIGN KEY (`supervisor_id`) REFERENCES `Prison_Staff` (`id`),
  CONSTRAINT `Guards_ibfk_2` FOREIGN KEY (`id`) REFERENCES `Prison_Staff` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Incident_Guards_ibfk_2` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Incident_Prisoners_ibfk_2` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Offence_Type_ibfk_1` FOREIGN KEY (`offence_id`) REFERENCES `Offences` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `post` varchar(255) NOT NULL,
  `salary` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `cell` char(3) NOT NULL,
  `security_level` enum('LOW','MEDIUM','HIGH') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `Visitors_ibfk_1` FOREIGN KEY (`prisoner_id`) REFERENCES `Prisoners` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `guard_id` int(11) NOT NULL,
  PRIMARY KEY (`prisoner_id`,`date_time`),
  KEY `prisoner_id` (`prisoner_id`,`visitor_first_name`,`visitor_middle_name`,`visitor_last_name`),
  KEY `guard_id` (`guard_id`),
  CONSTRAINT `Visits_ibfk_1` FOREIGN KEY (`prisoner_id`, `visitor_first_name`, `visitor_middle_name`, `visitor_last_name`) REFERENCES `Visitors` (`prisoner_id`, `first_name`, `middle_name`, `last_name`),
  CONSTRAINT `Visits_ibfk_2` FOREIGN KEY (`guard_id`) REFERENCES `Guards` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-10 23:01:21
