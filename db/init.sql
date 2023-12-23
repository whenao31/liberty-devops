CREATE DATABASE my_test;
USE my_test;

CREATE OR REPLACE  TABLE usuarios (
  usuario varchar(20) NOT NULL,
  PRIMARY KEY (usuario)
);

CREATE OR REPLACE  TABLE `detalles` (
  usuario varchar(20) NOT NULL,
  nombre varchar(50) NOT NULL,
  edad int NOT NULL,
  pais varchar(50) NOT NULL,
  PRIMARY KEY (usuario),
  FOREIGN KEY (usuario) REFERENCES usuarios(usuario) ON DELETE CASCADE
);

INSERT INTO `usuarios` (`usuario`) VALUES
('jdoe'),
('alovelace');

INSERT INTO `detalles` (`usuario`, `nombre`, `edad`, `pais`) VALUES
('jdoe', '', 30, ''),
('alovelace', '', 0, '');
GRANT ALL PRIVILEGES ON my_test.* TO 'my_user'@'%';