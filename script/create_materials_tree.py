#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
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
def makesetofdirs(basepath,dirset):
	for i in dirset:
		try:
			os.mkdir(basepath + "/" + i)
		except:
			pass

makesetofdirs(path,["raw","by_author","by_speciality","by_year", "by_discipline", "by_studyform"])
os.system("rsync -arcp --delete %s %s" % (materials_basepath + "/", path + "/raw/"))

#По автору
list1=[]
for i in belongs:
	for j in authorship:
		if j[2] == i[1]:
			for k in authors:
				if k[1]==j[1]:
					list1.append(k[2])
makesetofdirs(path + "/by_author",list1)

#by_speciality
list1=[]
for i in belongs:
	for j in speciality:
		if i[2] == j[1]:
			list1.append(j[2]+"-"+j[3])
makesetofdirs(path + "/by_speciality",list1)

#by_year
list1=[]
for i in belongs:
	list1.append(str(i[3]))
makesetofdirs(path + "/by_year/",list1)

#by_discipline
list1=[]
for i in discipline:
	try:
		os.mkdir(path + "/by_discipline/" + i[2]+"-"+str(i[4]))
	except:
		pass
#by_studyform
list1=[]
for i in belongs:
	for j in study_form:
		if i[4]==j[1]:
			list1.append(j[2])
makesetofdirs(path + "/by_studyform",list1)
