-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tkinter
-- ------------------------------------------------------
-- Server version	8.0.20


--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;

CREATE TABLE `student_info` (
  `Name` varchar(50) DEFAULT NULL,
  `Branch` varchar(50) DEFAULT NULL,
  `Reg_ID` varchar(50) DEFAULT NULL,
  `Subject_Marks` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES ('Shubhanshu','IT','1701106375','Physics : 96'),('Sunit','IT','1701106422','Maths : 89'),('Aditya','IT','1701106539','Chemistry : 92'),('Subhashree','IT','1701106427','Physics : 88'),('Siddhartha','IT','1701106275','Chemistry : 89'),('Arpita','CSE','1701106678','Maths : 93'),('Anurag','IEE','1701106478','Chemistry : 86'),('Smruti','IEE','1701106389','Physics : 76'),('Amrit','EE','1701106567','Physics : 89'),('Nikita','CSE','1701106789','Chemistry : 95');
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;


-- Dump completed on 2020-05-26 18:00:59
