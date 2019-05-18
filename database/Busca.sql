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
(select a.nome from autor a where a.id = livro.id_autor) as 'autor',
(select e.nome from editora e where e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE livro.titulo LIKE '%var_busca%';

-- pelo tombo

SELECT livro.*, 
(select a.nome from autor a where a.id = livro.id_autor) as 'autor',
(select e.nome from editora e where e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE livro.tombo LIKE '%var_busca%';

-- pelo nome da editora

SELECT livro.*, 
(select a.nome from autor a where a.id = livro.id_autor) as 'autor',
(select e.nome from editora e where e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE (select e.nome from editora e where e.id = livro.id_editora)
LIKE '%var_busca%';

-- pelo nome do autor

SELECT livro.*, 
(select a.nome from autor a where a.id = livro.id_autor) as 'autor',
(select e.nome from editora e where e.id = livro.id_editora) as 'editora'
 FROM livro
WHERE (select a.nome from autor a where a.id = livro.id_autor)
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


insert into emprestimo values(default, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 5 DAY), 1, 1);
select * from emprestimo;

