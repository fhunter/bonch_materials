#!/usr/bin/env python
import os
import sqlite3
#import subprocess
import sys

if "REMOTE_ADDR" in os.environ:
	print "Content/type: text/html"
	print ""
	print "Wrong page"
	exit(0)

#This is not a CGI
try:
	path = sys.argv[1]
except:
	exit(1)

if not os.path.isdir(path):
	exit(2)

def strip_uuid(uuid):
	return uuid.replace('{','').replace('}','')

materials_basepath  = os.path.abspath(sys.argv[0])
materials_basepath  = os.path.dirname(materials_basepath)
materials_basepath  = os.path.abspath(materials_basepath + "/../materials")

conn = sqlite3.connect("/var/www/materials/materials.sqlite")
cursor = conn.cursor()
cursor.execute("select * from authors")
#CREATE TABLE authors ( id integer primary key asc autoincrement, uuid text unique not null, fio text not null);
authors = cursor.fetchall()
cursor.execute("select * from study_form")
#CREATE TABLE study_form ( id integer primary key asc autoincrement, uuid text unique not null, study_form text not null);
study_form = cursor.fetchall()
cursor.execute("select * from speciality")
#CREATE TABLE speciality ( id integer primary key asc autoincrement, uuid text unique not null, code text unique not null, name text not null, description text);
speciality = cursor.fetchall()
cursor.execute("select * from discipline")
#CREATE TABLE discipline ( id integer primary key asc autoincrement, uuid text unique not null, name text not null, description text, semester integer);
discipline = cursor.fetchall()
cursor.execute("select * from materials")
#CREATE TABLE materials ( id integer primary key asc autoincrement, uuid text unique not null, name text unique not null, description text, owner text not null, upload_date text not null default (datetime()),edit_date text);
materials = cursor.fetchall()
cursor.execute("select * from authorship")
#CREATE TABLE authorship (id integer primary key asc autoincrement, author_uuid text references authors ( uuid ) on delete restrict on update restrict, material_uuid text references materials ( uuid ) on delete restrict on update restrict);
authorship = cursor.fetchall()
cursor.execute("select * from belongs")
#CREATE TABLE belongs (id integer primary key asc autoincrement, material_uuid text references materials (uuid) on update restrict on delete restrict, speciality_uuid text references speciality (uuid) on update restrict on delete restrict, student_year numeric not null default 1, study_form_uuid text references study_form (uuid) on update restrict on delete restrict, discipline_uuid text references discipline (uuid) on update restrict on delete restrict);
belongs = cursor.fetchall()
conn.close()
#print authors
#print study_form
#print speciality
#print discipline
#print materials
#print authorship
#print belongs
#print materials_basepath
for i in ["/raw","/by_author","/by_speciality","/by_year"]:
	try:
		os.mkdir(path + i)
	except:
		pass
os.system("rsync -arcp --delete %s %s" % (materials_basepath + "/", path + "/raw/"))
