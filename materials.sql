PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE materials (id integer primary key asc autoincrement, uuid text unique not null, name text not null);
CREATE TABLE courses (id integer primary key asc autoincrement, uuid text unique not null, name text not null);
CREATE TABLE belongs (id integer primary key asc autoincrement, material_uuid text references materials (uuid) on update restrict on delete restrict, year integer, course_uuid text references courses (uuid) on update restrict on delete restrict);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('materials',1);
COMMIT;
