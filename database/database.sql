-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: TCC
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

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
-- Table structure for table `autor`
--

DROP TABLE IF EXISTS `autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autor`
--

LOCK TABLES `autor` WRITE;
/*!40000 ALTER TABLE `autor` DISABLE KEYS */;
INSERT INTO `autor` VALUES (1,'João Angela'),(2,'Bruno Perri'),(3,'João Coimbra'),(4,'Stephen Hawking'),(5,'Markus Zusak'),(7,'John Boyne'),(8,'Julio Verne'),(9,'R.J.Palacio'),(10,'George R. R. Martin'),(11,'Machado de Assis'),(12,'Ray Kroc'),(13,'Gill VIcente'),(14,'Tomás Antônio Gonzaga'),(15,'Luiz Vaz de Cameos'),(16,'J. K. Rowling');
/*!40000 ALTER TABLE `autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editora`
--

DROP TABLE IF EXISTS `editora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `editora` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editora`
--

LOCK TABLES `editora` WRITE;
/*!40000 ALTER TABLE `editora` DISABLE KEYS */;
INSERT INTO `editora` VALUES (1,'Panini'),(4,'JBC'),(5,'Intrínseca'),(6,'Seguinte'),(7,'Moderna'),(8,'LeYa'),(9,'Antofagica Editora'),(10,'Figurati'),(11,'L&PM'),(12,'Martin Claret'),(13,'BestBolso'),(14,'Rocco');
/*!40000 ALTER TABLE `editora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emprestimo`
--

DROP TABLE IF EXISTS `emprestimo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emprestimo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `retirada` date NOT NULL,
  `devolucao` date NOT NULL,
  `tombo` int(11) NOT NULL,
  `id_socio` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_socio` (`id_socio`),
  KEY `tombo` (`tombo`),
  CONSTRAINT `emprestimo_ibfk_1` FOREIGN KEY (`id_socio`) REFERENCES `socio` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emprestimo_ibfk_2` FOREIGN KEY (`tombo`) REFERENCES `livro` (`tombo`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emprestimo`
--

LOCK TABLES `emprestimo` WRITE;
/*!40000 ALTER TABLE `emprestimo` DISABLE KEYS */;
/*!40000 ALTER TABLE `emprestimo` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER emprestimo_after_delete
AFTER DELETE
   ON emprestimo FOR EACH ROW

BEGIN
   INSERT INTO emprestimo_morto
   ( id,
     retirada,
     devolucao,
     data_retorno,
     tombo,
     id_socio)
   VALUES
   ( OLD.id,
 OLD.retirada,
     OLD.devolucao,
     default,
     OLD.tombo,
     OLD.id_socio);

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `emprestimo_morto`
--

DROP TABLE IF EXISTS `emprestimo_morto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emprestimo_morto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `retirada` date NOT NULL,
  `devolucao` date NOT NULL,
  `data_retorno` datetime DEFAULT CURRENT_TIMESTAMP,
  `tombo` int(11) NOT NULL,
  `id_socio` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_socio` (`id_socio`),
  KEY `tombo` (`tombo`),
  CONSTRAINT `emprestimo_morto_ibfk_1` FOREIGN KEY (`id_socio`) REFERENCES `socio` (`id`) ON DELETE CASCADE,
  CONSTRAINT `emprestimo_morto_ibfk_2` FOREIGN KEY (`tombo`) REFERENCES `livro` (`tombo`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emprestimo_morto`
--

LOCK TABLES `emprestimo_morto` WRITE;
/*!40000 ALTER TABLE `emprestimo_morto` DISABLE KEYS */;
INSERT INTO `emprestimo_morto` VALUES (4,'2019-05-20','2019-05-25','2019-05-20 20:10:43',21,1);
/*!40000 ALTER TABLE `emprestimo_morto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionario`
--

DROP TABLE IF EXISTS `funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funcionario` (
  `matricula` int(11) NOT NULL,
  `nome` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `cargo` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `caminho_imagem` varchar(500) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`matricula`),
  UNIQUE KEY `matricula` (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionario`
--

LOCK TABLES `funcionario` WRITE;
/*!40000 ALTER TABLE `funcionario` DISABLE KEYS */;
INSERT INTO `funcionario` VALUES (123456,'admin','admin','null');
/*!40000 ALTER TABLE `funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `livro`
--

DROP TABLE IF EXISTS `livro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `livro` (
  `tombo` int(11) NOT NULL,
  `titulo` varchar(50) CHARACTER SET utf8 NOT NULL,
  `entrada` date NOT NULL,
  `etq` varchar(10) CHARACTER SET utf8 NOT NULL,
  `ano` int(11) NOT NULL,
  `v` int(11) NOT NULL,
  `ex` int(11) NOT NULL,
  `id_editora` int(11) NOT NULL,
  `id_autor` int(11) NOT NULL,
  `status` enum('EMPRESTADO','ESTANTE','EXTRAVIADO','RESERVADO','PERDIDO') DEFAULT 'ESTANTE',
  `caminho_imagem` varchar(500) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`tombo`),
  KEY `id_editora` (`id_editora`),
  KEY `id_autor` (`id_autor`),
  CONSTRAINT `livro_ibfk_1` FOREIGN KEY (`id_editora`) REFERENCES `editora` (`id`) ON DELETE CASCADE,
  CONSTRAINT `livro_ibfk_2` FOREIGN KEY (`id_autor`) REFERENCES `autor` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livro`
--

LOCK TABLES `livro` WRITE;
/*!40000 ALTER TABLE `livro` DISABLE KEYS */;
INSERT INTO `livro` VALUES (1,'A Menina que Roubava Livros','2019-06-17','LIN',2010,2,1,5,5,'ESTANTE','A_menina_Que_Roubava_Livros.jpg'),(2,'O menino do pijama listrado','2019-06-17','LIN',2002,1,4,6,7,'ESTANTE','O_menino_do_pijama_listrado.jpg'),(3,'Extraordinário','2019-06-17','Bolso',2003,2,5,5,9,'ESTANTE','Extraordinario.jpg'),(4,'Auggie & Eu','2019-04-12','LIN',2002,1,4,5,9,'ESTANTE','Auggie_E_Eu.jpg'),(5,'365 Dias Extraordinários','2019-06-17','Bolso',2009,3,2,5,9,'ESTANTE','365_Dias_Extraordina'),(6,'Somos Todos Extraordinarios','2019-06-17','LIN',2008,3,2,5,9,'ESTANTE','Somos_Todos_Extraordinarios.jpg'),(7,'A Volta Ao Mundo Em 80 Dias','2018-04-15','LIN',2000,2,6,5,8,'ESTANTE','A_Volta.jpg'),(8,'O Mundo de Gelo e Fogo','2018-04-15','LIN',2004,2,4,8,10,'ESTANTE','O_Mundo_de_Gelo_e_fogo.jpg'),(9,'O Cavaleiro dos Sete Reinos','2018-04-15','Bolso',2003,1,3,8,10,'ESTANTE','O_Cavaleiro_dos_Sete_Reinos.jpg'),(10,'Fogo & Sangue','2017-07-17','LIN',2013,3,4,8,10,'ESTANTE','Fogo_E_Sangue.jpg'),(11,'A Tormenta de Espadas','2015-04-17','LIN',2000,4,7,8,10,'ESTANTE','A_Tormenta_de_Espadas.jpg'),(12,'Memórias Póstumas De Brás Cubas','2018-04-17','Bolso',2000,1,3,9,11,'PERDIDO','Memrias_Pstumas_De_Brs_Cubas.jpg'),(13,'Fome de Poder','2019-06-17','Bolso',2000,2,4,11,12,'ESTANTE','Fome_De_Poder.jpg'),(14,'Auto da barca do inferno','2017-04-15','LIN',2000,3,2,11,13,'RESERVADO','Auto_Da_Barca_Do_Inferno.jpg'),(15,'Cartas Chilenas','2018-06-17','Bolso',2000,1,2,12,14,'ESTANTE','Cartas_Chilenas.jpg'),(16,'Os Lusíadas','2017-06-17','Bolso',2000,2,5,13,15,'ESTANTE','Os_Lusiadas.jpg'),(17,'Harry Potter E A Pedra Filosofal','2017-06-17','LIN',2000,1,2,14,16,'ESTANTE','Harry_Potter_E_A_Pedra_Filosofal.jpg'),(18,'Harry Potter E O Cálice De Fogo','2017-04-17','Bolso',2000,2,5,14,16,'ESTANTE','HarryPotter_E_O_Calice_De_Fogo.jpg'),(19,'Harry Potter e o Prisioneiro de Azkaban','2018-04-17','LIN',2000,3,4,14,16,'ESTANTE','Harry_Potter_e_o_Prisioneiro_de_Azkaban.jpg'),(20,'Harry Potter E A Câmara Secreta','2017-04-17','Bolso',2000,2,4,14,16,'ESTANTE','Harry_Potter_E_A_Cmara_Secreta.jpg'),(21,'Harry Potter e o Enigma Do Príncipe','2018-06-18','LIN',2014,5,4,14,16,'ESTANTE','Harry_Potter_e_o_Enigma_Do_Principe.jpg'),(22,'Harry Potter E As Relíquias Da Morte','2019-06-18','Bolso',2015,6,3,14,16,'ESTANTE','Harry_Potter_E_As_Relquias_Da_Morte.jpg'),(23,'História Concisa da Literatura Brasileira','2017-06-18','LIN',2000,1,2,1,1,'ESTANTE','Histria_Concisa_da_Literatura_Brasileira.jpg'),(24,'40 contos escolhidos','2018-06-18','Bolso',2000,2,1,1,1,'ESTANTE','40_contos_escolhidos.jpg'),(25,'Triste Fim de Policarpo Quaresma','2017-03-16','LIN',2004,2,4,1,1,'ESTANTE','Triste_Fim_de_Policarpo_Quaresma.jpg'),(26,'Buracos Negros','2019-06-18','Bolso',2003,2,3,5,4,'ESTANTE','Buracos_Negros.jpg');
/*!40000 ALTER TABLE `livro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserva`
--

DROP TABLE IF EXISTS `reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reserva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `tombo` int(11) NOT NULL,
  `id_socio` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_socio` (`id_socio`),
  KEY `tombo` (`tombo`),
  CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`id_socio`) REFERENCES `socio` (`id`) ON DELETE CASCADE,
  CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`tombo`) REFERENCES `livro` (`tombo`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva`
--

LOCK TABLES `reserva` WRITE;
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
INSERT INTO `reserva` VALUES (1,'2019-05-17 21:37:07',14,1);
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER reserva_after_delete
AFTER DELETE
   ON reserva FOR EACH ROW

BEGIN
   INSERT INTO reserva_morta
   ( id,
     create_date,
     delete_date,
     tombo,
     id_socio)
   VALUES
   ( OLD.id,
 OLD.created_at,
     default,
     OLD.tombo,
     OLD.id_socio);

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `reserva_morta`
--

DROP TABLE IF EXISTS `reserva_morta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reserva_morta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` date DEFAULT NULL,
  `delete_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `tombo` int(11) NOT NULL,
  `id_socio` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_socio` (`id_socio`),
  KEY `tombo` (`tombo`),
  CONSTRAINT `reserva_morta_ibfk_1` FOREIGN KEY (`id_socio`) REFERENCES `socio` (`id`) ON DELETE CASCADE,
  CONSTRAINT `reserva_morta_ibfk_2` FOREIGN KEY (`tombo`) REFERENCES `livro` (`tombo`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva_morta`
--

LOCK TABLES `reserva_morta` WRITE;
/*!40000 ALTER TABLE `reserva_morta` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva_morta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socio`
--

DROP TABLE IF EXISTS `socio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `socio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) CHARACTER SET utf8 NOT NULL,
  `rg` char(12) NOT NULL,
  `nasc` date NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 NOT NULL,
  `associacao` datetime DEFAULT CURRENT_TIMESTAMP,
  `nome_pai` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `nome_mae` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `cidade` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `bairro` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `logradouro` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `num` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `tel_res` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `cel_1` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  `cel_2` varchar(20) CHARACTER SET utf8 DEFAULT NULL,
  caminho_imagem NVARCHAR(500),    
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socio`
--

LOCK TABLES `socio` WRITE;
/*!40000 ALTER TABLE `socio` DISABLE KEYS */;
INSERT INTO `socio` VALUES (1,'Eduardo de Andrade Palhares Jr','12345978','1997-07-16','xeduardopalhares@gmail.com','2019-05-15 04:37:04','Eduardo de Andrade Palhares','Adriana Cristina Silvestre da Silva','Cotia','Jd. Rio das Pedras','Rua Potengi','609','1156894478','1159897944','1148978965');
/*!40000 ALTER TABLE `socio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-20 20:13:46
