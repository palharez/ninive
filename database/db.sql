-- drop database tcc;

CREATE DATABASE TCC;
USE TCC;

CREATE TABLE autor (
    id INT NOT NULL AUTO_INCREMENT,
    nome NVARCHAR(50) NOT NULL,
    CONSTRAINT id_autor_pk PRIMARY KEY (id)
);

CREATE TABLE funcionario(
	matricula INT NOT NULL UNIQUE,
    nome NVARCHAR(255),
    cargo NVARCHAR(50),
    CONSTRAINT matricula_pk PRIMARY KEY (MATRICULA)
);



CREATE TABLE editora (
    id INT NOT NULL AUTO_INCREMENT,
    nome NVARCHAR(50) NOT NULL,
    CONSTRAINT id_editora_pk PRIMARY KEY (id)
);

CREATE TABLE livro (
    tombo INT NOT NULL AUTO_INCREMENT,
    titulo NVARCHAR(50) NOT NULL,
    entrada DATE NOT NULL,
    etq NVARCHAR(10) NOT NULL,
    ano INT NOT NULL,
    v INT NOT NULL,
    ex INT NOT NULL,
    id_edtora INT NOT NULL,
    id_autor INT NOT NULL,
    status ENUM('EMPRESTADO', 'ESTANTE', 'EXTRAVIADO', 'RESERVADO', 'PERDIDO'),
    nomenclatura ENUM ('LIN', 'LBR', 'POE', 'LES'),
    CONSTRAINT tombo_pk PRIMARY KEY (TOMBO),
    CONSTRAINT id_edtora_fk FOREIGN KEY (id_edtora)
        REFERENCES editora (id),
    CONSTRAINT id_autor_fk FOREIGN KEY (id_autor)
        REFERENCES autor (id)
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
    CONSTRAINT id_socio_fk FOREIGN KEY (id_socio)
        REFERENCES socio (id),
    CONSTRAINT tombo_fk FOREIGN KEY (tombo)
        REFERENCES livro (tombo)
);


SELECT 
    *
FROM
    socio;