-- TABELA Skill
INSERT INTO skill (name) VALUES ('Proatividade');
INSERT INTO skill (name) VALUES ('Autonomia');
INSERT INTO skill (name) VALUES ('Colaboração');
INSERT INTO skill (name) VALUES ('Entrega de Resultados');

-- TABELA Answer
-- Entrega de Resultados
INSERT INTO answer (id_skill, description) VALUES (1, 'Reativo');
INSERT INTO answer (id_skill, description) VALUES (1, 'Desfocado');
INSERT INTO answer (id_skill, description) VALUES (1, 'Ativo');
INSERT INTO answer (id_skill, description) VALUES (1, 'Proativo');

-- Autonomia
INSERT INTO answer (id_skill, description) VALUES (2, 'Dirigido');
INSERT INTO answer (id_skill, description) VALUES (2, 'Gerido');
INSERT INTO answer (id_skill, description) VALUES (2, 'Treinado');
INSERT INTO answer (id_skill, description) VALUES (2, 'Autogestão');

-- Colaboração
INSERT INTO answer (id_skill, description) VALUES (3, 'Ausente');
INSERT INTO answer (id_skill, description) VALUES (3, 'Cooperativo');
INSERT INTO answer (id_skill, description) VALUES (3, 'Coordenado');
INSERT INTO answer (id_skill, description) VALUES (3, 'Colaborativo');

-- Entregas de Resultados
INSERT INTO answer (id_skill, description) VALUES (4, 'Não há entregas');
INSERT INTO answer (id_skill, description) VALUES (4, 'Entregas duvidosas');
INSERT INTO answer (id_skill, description) VALUES (4, 'Entregas confiáveis');
INSERT INTO answer (id_skill, description) VALUES (4, 'Entregas perfeitas');
