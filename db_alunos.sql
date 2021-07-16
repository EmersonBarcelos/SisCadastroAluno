CREATE DATABASE db_alunos;

USE db_alunos;

CREATE TABLE aluno_avaliacao (
  id INT (11) AUTO_INCREMENT,
  nome VARCHAR (50) NOT NULL,
  nota1 FLOAT (3,1),
  nota2 FLOAT (3,1),
  turma CHAR (1) NOT NULL,
  ano YEAR NOT NULL,
  PRIMARY KEY (id)
  );

/*Inserts para teste*/

INSERT INTO aluno_avaliacao VALUES (default,'Lucas Silva',9.0,7.0,'A',2020);
INSERT INTO aluno_avaliacao VALUES (default,'Marcelo Silva',7.0,4.0,'A',2019);
INSERT INTO aluno_avaliacao VALUES (default,'Leticia',8.0,8.1,'C',2019);
INSERT INTO aluno_avaliacao VALUES (default,'Miguel',5.0,7.2,'A',2020);
INSERT INTO aluno_avaliacao VALUES (default,'José',8.0,6.7,'C',2019);



