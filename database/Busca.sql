/* Busca na tabela autor */

SELECT * FROM autor
WHERE id LIKE '%var_busca%';

SELECT * FROM autor
WHERE nome LIKE '%var_busca%';

/* Busca na tabela editora */

SELECT * FROM editora
WHERE id LIKE '%var_busca%';

SELECT * FROM editora
WHERE nome LIKE '%var_busca%';


/* Busca na tabela livro */

-- pelo titulo

SELECT livro.*, 
(SELECT a.nome FROM autor a WHERE a.id = livro.id_autor) as 'autor',
(SELECT e.nome FROM editora e WHERE e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE livro.titulo LIKE '%var_busca%';

-- pelo tombo

SELECT livro.*, 
(SELECT a.nome FROM autor a WHERE a.id = livro.id_autor) as 'autor',
(SELECT e.nome FROM editora e WHERE e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE livro.tombo LIKE '%var_busca%';

-- pelo nome da editora

SELECT livro.*, 
(SELECT a.nome FROM autor a WHERE a.id = livro.id_autor) as 'autor',
(SELECT e.nome FROM editora e WHERE e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE (SELECT e.nome FROM editora e WHERE e.id = livro.id_editora)
LIKE '%var_busca%';

-- pelo nome do autor

SELECT livro.*, 
(SELECT a.nome FROM autor a WHERE a.id = livro.id_autor) as 'autor',
(SELECT e.nome FROM editora e WHERE e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE (SELECT a.nome FROM autor a WHERE a.id = livro.id_autor)
LIKE '%var_busca%';


/* Busca na tabela socio*/

-- pelo id

SELECT * FROM socio
WHERE id LIKE '%var_busca%';

-- pelo nome

SELECT * FROM socio
WHERE nome LIKE '%var_busca%';

-- pela idade

SELECT * FROM socio
WHERE TIMESTAMPDIFF(year, nasc,curdate()) = '%var_busca%';


/*Insert para a retirada*/


INSERT INTO emprestimo VALUES(default, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 5 DAY), 1, 1);
SELECT * FROM emprestimo;

SELECT count(tombo) FROM livro;

SELECT count(tombo) FROM livro
WHERE status = 'emprestado';

SELECT count(tombo) FROM livro
WHERE status = 'reservado';

SELECT count(tombo) FROM livro
WHERE status = 'estante';


/* reserva pelo socio */
SELECT reserva.*, 
(SELECT s.nome FROM socio s WHERE s.id = reserva.id_socio) as 'socio',
(SELECT l.titulo FROM livro l WHERE l.tombo = reserva.tombo) as 'livro'
 FROM reserva
WHERE (SELECT s.nome FROM socio s WHERE s.id = reserva.id_socio)
LIKE '%var_busca%';

/* reserva pelo livro */
SELECT reserva.*, 
(SELECT s.nome FROM socio s WHERE s.id = reserva.id_socio) as 'socio',
(SELECT l.titulo FROM livro l WHERE l.tombo = reserva.tombo) as 'livro'
 FROM reserva
WHERE (SELECT l.titulo FROM livro l WHERE l.tombo = reserva.tombo)
LIKE '%var_busca%';

/* reserva pelo id */
SELECT reserva.*, 
(SELECT s.nome FROM socio s WHERE s.id = reserva.id_socio) as 'socio',
(SELECT l.titulo FROM livro l WHERE l.tombo = reserva.tombo) as 'livro'
 FROM reserva
WHERE reserva.id
LIKE '%var_busca%';

/* emprestimo pelo socio */
SELECT emprestimo.*, 
(SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio) as 'socio',
(SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo) as 'livro'
 FROM emprestimo
WHERE (SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio)
LIKE '%var_busca%';

/* emprestimo pelo livro */
SELECT emprestimo.*, 
(SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio) as 'socio',
(SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo) as 'livro'
 FROM emprestimo
WHERE (SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo)
LIKE '%var_busca%';

/* emprestimo pelo id */
SELECT emprestimo.*, 
(SELECT s.nome FROM socio s WHERE s.id = emprestimo.id_socio) as 'socio',
(SELECT l.titulo FROM livro l WHERE l.tombo = emprestimo.tombo) as 'livro'
 FROM emprestimo
WHERE emprestimo.id
LIKE '%var_busca%';


/* */