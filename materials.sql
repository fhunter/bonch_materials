PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE authors ( id integer primary key asc autoincrement, uuid text unique not null, fio text not null);
CREATE TABLE study_form ( id integer primary key asc autoincrement, uuid text unique not null, study_form text not null);
CREATE TABLE speciality ( id integer primary key asc autoincrement, uuid text unique not null, code text unique not null, name text not null, description text);
CREATE TABLE discipline ( id integer primary key asc autoincrement, uuid text unique not null, name text unique not null, description text, semester integer);
CREATE TABLE materials ( id integer primary key asc autoincrement, uuid text unique not null, name text unique not null, description text, owner text not null, upload_date text not null default (datetime()),edit_date text);
CREATE TABLE authorship (id integer primary key asc autoincrement, author_uuid text references authors ( uuid ) on delete restrict on update restrict, material_uuid text references materials ( uuid ) on delete restrict on update restrict);
CREATE TABLE belongs (id integer primary key asc autoincrement, material_uuid text references materials (uuid) on update restrict on delete restrict, speciality_uuid text references speciality (uuid) on update restrict on delete restrict, student_year numeric not null default 1, study_form_uuid text references study_form (uuid) on update restrict on delete restrict, discipline_uuid text references discipline (uuid) on update restrict on delete restrict);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('authorship',1);
CREATE VIEW next_uuid as select '{' || hex( randomblob(4)) || '-' || hex( randomblob(2))  || '-' || '4' || substr( hex( randomblob(2)), 2) || '-' || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)) || '}';
COMMIT;
