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