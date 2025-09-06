create table loja;
use loja;

create table clientes(
id int auto_increment primary key,
cpf varchar(12) unique,
nome varchar(100) not null,
email varchar(100) unique,
telefone varchar(15) unique,
data_cadastro datetime default (current_time())
);

-- CRUD

-- Criação 
insert into clientes (nome, cpf, email, telefone) values 
('João','32165498787','joao@email.com',85985858585),
('Maria','32165498781','maria@email.com',85985858584),
('Ana','32165498782','ana@email.com',85985858583),
('Pedro','32165498783','pedro@email.com',85985858582);

-- Leitura

select * from clientes;
select nome, email from clientes;
select * from clientes where nome = 'João';

-- Atualização

update clientes set telefone = '555555555',email = 'maria2@email.com' 
where id = 2;

-- DELETE

delete from clientes where id = 4;
