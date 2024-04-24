create table bidan(
id serial primary key not null,
nip varchar(10) unique not null,
nama varchar(50) not null,
jk varchar(1) not null,
tempat_tugas varchar(10) not null);


