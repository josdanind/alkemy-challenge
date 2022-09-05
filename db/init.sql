DROP TABLE IF EXISTS places;

CREATE TABLE places (
	id serial PRIMARY KEY,
	cod_localidad INT,
	id_provincia INT,
	id_departamento INT,
	categoria VARCHAR (100),
	provincia VARCHAR (80),
	localidad VARCHAR (50),
	nombre VARCHAR (200),
	domicilio VARCHAR (100),
	codigo_postal VARCHAR (50),
	numero_telefono VARCHAR(50),
	mail TEXT,
	web TEXT	
);

-- DROP TABLE IF EXISTS info;

-- CREATE TABLE info (
-- 	campo VARCHAR (50),
-- 	cantidad VARCHAR (50),
-- 	total_registros VARCHAR (50),
-- 	fuente VARCHAR (50)
-- );