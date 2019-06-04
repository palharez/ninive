DROP DATABASE TCC;

CREATE DATABASE TCC;
USE TCC;

CREATE TABLE autor (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome NVARCHAR(50) NOT NULL
);

CREATE TABLE funcionario(
	matricula INT NOT NULL UNIQUE PRIMARY KEY,
    nome NVARCHAR(255),
    cargo NVARCHAR(50),
    caminho_imagem NVARCHAR(500)
);

CREATE TABLE editora (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome NVARCHAR(50) NOT NULL
);

CREATE TABLE livro (
    tombo INT NOT NULL PRIMARY KEY,
    titulo NVARCHAR(50) NOT NULL,
    entrada DATE NOT NULL,
    etq NVARCHAR(10) NOT NULL,
    ano INT NOT NULL,
    v INT NOT NULL,
    ex INT NOT NULL,
    id_editora INT NOT NULL,
    id_autor INT NOT NULL,
    status ENUM('EMPRESTADO', 'ESTANTE', 'EXTRAVIADO', 'RESERVADO', 'PERDIDO') default 'ESTANTE',
    caminho_imagem NVARCHAR(500),
    qtd INT NOT NULL DEFAULT 1,
    FOREIGN KEY (id_editora) REFERENCES editora (id) ON DELETE CASCADE,
    FOREIGN KEY (id_autor) REFERENCES autor (id) ON DELETE CASCADE
);

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
  `caminho_imagem` varchar(500) CHARACTER SET utf8 DEFAULT NULL,
  `status` enum('ATIVO','SUSPENSO') DEFAULT 'ATIVO',
  PRIMARY KEY (`id`)
);

CREATE TABLE emprestimo(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	retirada DATE NOT NULL,
    devolucao DATE NOT NULL,
    tombo INT NOT NULL,
    id_socio INT NOT NULL,
    FOREIGN KEY (id_socio) REFERENCES socio (id) ON DELETE CASCADE,
    FOREIGN KEY (tombo) REFERENCES livro (tombo) ON DELETE CASCADE
);

CREATE TABLE reserva(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    created_at DATETIME DEFAULT NOW(),
    tombo INT NOT NULL,
    id_socio INT NOT NULL,
    FOREIGN KEY (id_socio) REFERENCES socio (id) ON DELETE CASCADE,
    FOREIGN KEY (tombo) REFERENCES livro (tombo) ON DELETE CASCADE 
);

CREATE TABLE punicao(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_socio INT NOT NULL,
    data_punicao DATE NOT NULL,
    FOREIGN KEY (id_socio) REFERENCES socio (id) ON DELETE CASCADE
);

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
);

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
);

insert into funcionario values(123456, 'admin', 'admin', 'null');