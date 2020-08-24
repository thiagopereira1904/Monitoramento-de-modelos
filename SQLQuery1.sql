CREATE DATABASE db;

USE db;

DROP DATABASE db;

USE app;

/* TIPO MODELO */

CREATE TABLE tipo_modelo(
	id_tm INTEGER IDENTITY,
	nome_tm VARCHAR(30) NOT NULL,
	PRIMARY KEY(id_tm)
);

DROP TABLE tipo_modelo;

INSERT INTO tipo_modelo VALUES ('POC');
INSERT INTO tipo_modelo VALUES ('ESTUDO AVANÇADO');

SELECT * FROM tipo_modelo;


/* -------- */


/* AREA DEMANDANTE */


CREATE TABLE area_demandante(
	id_ad INTEGER IDENTITY,
	nome_ad VARCHAR(5) NOT NULL,
	PRIMARY KEY(id_ad)
	);

INSERT INTO area_demandante VALUES ('DCPS');
INSERT INTO area_demandante VALUES ('DGTI');
SELECT * FROM area_demandante;


/* -------- */


/* JORNADA */

CREATE TABLE jornada(
	id_jd INTEGER IDENTITY,
	nome_jd VARCHAR(30) NOT NULL,
	PRIMARY KEY(id_jd)
	);

DROP TABLE jornada;


SELECT * FROM jornada;

INSERT INTO jornada VALUES('CRÉDITO');
INSERT INTO jornada VALUES('DIGITAL');
INSERT INTO jornada VALUES('INVESTIMENTO');


/* -------- */

/* MODELOS */

CREATE TABLE modelo(
	id_md INTEGER IDENTITY,
	nome_md VARCHAR(30) NOT NULL,
	dataCad_md DATE NOT NULL,
	diaR_md INTEGER NOT NULL,
	obs_md VARCHAR(150),
	id_tm INTEGER NOT NULL,
	id_ad INTEGER NOT NULL,
	id_jd INTEGER NOT NULL,
	PRIMARY KEY(id_md),
	FOREIGN KEY(id_tm) REFERENCES tipo_modelo(id_tm),
	FOREIGN KEY(id_ad) REFERENCES area_demandante(id_ad),
	FOREIGN KEY(id_jd) REFERENCES jornada(id_jd)
	);

DROP TABLE modelo;

ALTER TABLE modelo ADD id_us INTEGER NOT NULL;

ALTER TABLE modelo ADD FOREIGN KEY(id_us) REFERENCES usuario(id_us);

INSERT INTO modelo (nome_md, dataCad_md, diaR_md, id_tm, id_ad, id_jd, id_us) VALUES ('CHURN DE PJ', '02-05-2020', 20, 1, 1, 1, 1);

SELECT * FROM modelo;
	
/* -------- */
/* BASES */

CREATE TABLE bases(
	id_bs INTEGER IDENTITY,
	path_bs VARCHAR(100) NOT NULL,
	safra_bs DATE NOT NULL,
	id_md INTEGER NOT NULL,
	PRIMARY KEY(id_bs),
	FOREIGN KEY(id_md) REFERENCES modelo(id_md)
	);

SELECT * FROM bases;

DROP TABLE bases;


/* -------- */

/* FUNCAO USUARIO */
CREATE TABLE funcao_usuario(
	id_fu INTEGER IDENTITY,
	nome_fu VARCHAR(15) NOT NULL,
	PRIMARY KEY(id_fu)
	);

DROP TABLE funcao_usuario;

INSERT INTO funcao_usuario VALUES ('FUNCIONÁRIO');
INSERT INTO funcao_usuario VALUES ('BOLSISTA');
INSERT INTO funcao_usuario VALUES ('ESTAGIÁRIO');

SELECT * FROM funcao_usuario;

/* USUÁRIO */
CREATE TABLE usuario(
	id_us INTEGER IDENTITY,
	numFunc_us VARCHAR(7) NOT NULL,
	email_us VARCHAR(50) NOT NULL,
	nome_us VARCHAR(50) NOT NULL,
	senha_us VARCHAR(18) DEFAULT 'admin',
	id_jd INTEGER,
	tipo_us BIT DEFAULT 0,
	sessao_us BIT DEFAULT 0,
	PRIMARY KEY(id_us),
	FOREIGN KEY(id_jd) REFERENCES jornada(id_jd)
	);

INSERT INTO usuario (numFunc_us, email_us, nome_us, id_jd, tipo_us)VALUES ('I376231', 'THIAGO.PEREIRA@BRADESCO.COM.BR', 'THIAGO PEREIRA DA SILVA', 1, 1);

SELECT * FROM usuario;
SELECT usuario.numFunc_us AS N_FUNC, usuario.email_us AS EMAIL, usuario.nome_us AS NOME, jornada.nome_jd as JORNADA FROM usuario INNER JOIN jornada ON usuario.id_jd = jornada.id_jd;
ALTER TABLE usuario DROP COLUMN tipo_us;

SELECT * FROM usuario WHERE numFunc_us = 'I376231' AND senha_us = 'admin';
DELETE FROM usuario WHERE id_us = 13;
DROP TABLE usuario;


UPDATE usuario SET numFunc_us = 'i376123' WHERE id_us = 1;

ALTER TABLE usuario ADD id_fu INTEGER;
ALTER TABLE usuario ADD FOREIGN KEY(id_fu) REFERENCES funcao_usuario(id_fu);

ALTER TABLE usuario ADD id_tu INTEGER;
ALTER TABLE usuario ADD FOREIGN KEY(id_tu) REFERENCES tipo_usuario(id_tu);

/* -------- */

/* TIPO_USUARIO */

CREATE TABLE tipo_usuario(
	id_tu INTEGER IDENTITY,
	nome_tu VARCHAR(20) NOT NULL,
	PRIMARY KEY(id_tu)
	);

INSERT INTO tipo_usuario VALUES ('COMUM'), ('ADMINISTRADOR');

SELECT * FROM tipo_usuario;

DELETE FROM tipo_usuario WHERE id_tu = 3;

