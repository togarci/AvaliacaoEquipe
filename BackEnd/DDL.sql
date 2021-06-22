-- TABELA TypeSkill
INSERT INTO type_skill (type_skill) VALUES ('Entrega de Resultados');
INSERT INTO type_skill (type_skill) VALUES ('Autonomia');
INSERT INTO type_skill (type_skill) VALUES ('Proatividade');
INSERT INTO type_skill (type_skill) VALUES ('Colaboração');

-- TABELA Question
-- Perguntas Entrega de resultado
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Conseguiu realizar as tasks da melhor maneira visando a entrega da atividade ?', 1);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Buscou garantir uma boa qualidade de entregas sem erros e bem documentadas ?', 1);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Na ultima sprint, manteve uma boa frequência nas entregas de suas atividades ?', 1);

-- Perguntas Autonomia
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Conseguiu realizar as atividades propostas sem ajuda de outros membros da equipe ?', 2);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Preparou-se rapidamente para se adequar as suas atividades da sprint ?', 2);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Se você encontra um problema no projeto, você o corrige imediatamente e manteve os membros informados ?', 2);

-- Perguntas Proatividade
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Com base nas atividades da sprint, tomou iniciativa para realizar alguma atividade sem esperar por seus companheiros de equipe ?', 3);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Após realizar suas atividades, buscou novas atividades para realizar antes do final da sprint ?', 3);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Realizou tarefas que não faziam parte das suas funções ?', 3);

-- Perguntas Colaboração
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Ajudou os membros da equipe sempre que surgiram duvidas ou empecilhos para o andamento do projeto ?', 4);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Compartilhou ou buscou experiências para contribuir com o amadurecimento do projeto e dos integrantes da equipe ?', 4);
INSERT INTO question (question, fk_id_type_skill)
VALUES ('Manteve a equipe informada das suas atividades na sprint ?', 4);

-- TABELA user_groups
INSERT INTO user_groups (group_name) VALUES ('Master');
INSERT INTO user_groups (group_name) VALUES ('Time');
INSERT INTO user_groups (group_name) VALUES ('Admin');