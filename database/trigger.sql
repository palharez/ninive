-- trigger e tabela morta da reserva

DELIMITER //

CREATE TRIGGER reserva_after_delete
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

END; //

DELIMITER ;


CREATE TABLE reserva_morta(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    create_date DATE,
    delete_date DATETIME DEFAULT NOW(),
    tombo INT NOT NULL,
    id_socio INT NOT NULL,
    FOREIGN KEY (id_socio) REFERENCES socio (id) ON DELETE CASCADE,
    FOREIGN KEY (tombo) REFERENCES livro (tombo) ON DELETE CASCADE 
);


-- trigger e tabela morta do emprestimo

DELIMITER //

CREATE TRIGGER emprestimo_after_delete
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

END; //

DELIMITER ;


CREATE TABLE emprestimo_morto(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	retirada DATE NOT NULL,
    devolucao DATE NOT NULL,
    data_retorno DATETIME DEFAULT NOW(),
    tombo INT NOT NULL,
    id_socio INT NOT NULL,
    FOREIGN KEY (id_socio) REFERENCES socio (id) ON DELETE CASCADE,
    FOREIGN KEY (tombo) REFERENCES livro (tombo) ON DELETE CASCADE
);