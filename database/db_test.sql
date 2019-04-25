DROP DATABASE tcc_tests;

CREATE DATABASE tcc_tests;
USE tcc_tests;

CREATE TABLE autor (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome NVARCHAR(50) NOT NULL
);

CREATE TABLE funcionario(
	matricula INT NOT NULL UNIQUE PRIMARY KEY,
    nome NVARCHAR(255),
    cargo NVARCHAR(50)
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
    id_edtora INT NOT NULL,
    id_autor INT NOT NULL,
    status ENUM('EMPRESTADO', 'ESTANTE', 'EXTRAVIADO', 'RESERVADO', 'PERDIDO') default 'ESTANTE',
    nomenclatura ENUM ('LIN', 'LBR', 'POE', 'LES'),
    FOREIGN KEY (id_edtora) REFERENCES editora (id),
    FOREIGN KEY (id_autor) REFERENCES autor (id)
);

CREATE TABLE socio (
    id INT NOT NULL AUTO_INCREMENT,
    nome NVARCHAR(255) NOT NULL,
    rg CHAR(12) NOT NULL,
    nasc DATE NOT NULL,
    email NVARCHAR(255) NOT NULL,
    associacao DATETIME DEFAULT NOW(),
    nome_pai NVARCHAR(255),
    nome_mae NVARCHAR(255),
    cidade NVARCHAR(255),
    bairro NVARCHAR(255),
    logradouro NVARCHAR(255),
    num NVARCHAR(20),
    tel_res NVARCHAR(20),
    cel_1 NVARCHAR(20),
    cel_2 NVARCHAR(20),
    CONSTRAINT id_socio PRIMARY KEY (id)
);

CREATE TABLE emprestimo(
	retirada DATE NOT NULL,
    devolucao DATE NOT NULL,
    tombo INT NOT NULL,
    id_socio INT NOT NULL,
    FOREIGN KEY (id_socio) REFERENCES socio (id),
    FOREIGN KEY (tombo) REFERENCES livro (tombo)
);

INSERT INTO funcionario values (123456, "teste", "teste");