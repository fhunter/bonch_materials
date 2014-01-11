PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE materials (id integer primary key asc autoincrement, uuid text unique not null, name text unique not null, description text);
CREATE TABLE courses (id integer primary key asc autoincrement, uuid text unique not null, name text unique not null, description text);
CREATE TABLE belongs (id integer primary key asc autoincrement, material_uuid text references materials (uuid) on update restrict on delete restrict, year integer, course_uuid text references courses (uuid) on update restrict on delete restrict);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('materials',1);
CREATE VIEW next_uuid as select '{' || hex( randomblob(4)) || '-' || hex( randomblob(2))  || '-' || '4' || substr( hex( randomblob(2)), 2) || '-' || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)) || '}';
COMMIT;
