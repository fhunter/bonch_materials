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

#Форма обучения -> специальность -> год -> дисциплина -> преподаватель -> материал
#CREATE TABLE belongs (id integer primary key asc autoincrement, material_uuid text references materials (uuid) on update restrict on delete restrict, speciality_uuid text references speciality (uuid) on update restrict on delete restrict, student_year numeric not null default 1, study_form_uuid text references study_form (uuid) on update restrict on delete restrict, discipline_uuid text references discipline (uuid) on update restrict on delete restrict);

conn = sqlite3.connect("/var/www/materials/materials.sqlite")
cursor = conn.cursor()
cursor.execute("select study_form.study_form,study_form.uuid from study_form, belongs where belongs.study_form_uuid == study_form.uuid group by study_form.uuid")
study_forms = cursor.fetchall()
#Here goes addition of first directory level
for (k,l) in study_forms:
	cursor.execute("select speciality.code,speciality.name,speciality.uuid,belongs.student_year,belongs.material_uuid from belongs,speciality where belongs.speciality_uuid == speciality.uuid and belongs.study_form_uuid == ? group by belongs.student_year", (l,))
	speciality = cursor.fetchall()
	for (m,n,o,p,p1) in speciality:
		cursor.execute("select discipline.name, discipline.semester from discipline,belongs where belongs.discipline_uuid == discipline.uuid")
		discipline = cursor.fetchall()
		for (q,r) in discipline:
			cursor.execute("select authors.fio from authorship, authors where authors.uuid == authorship.author_uuid and authorship.material_uuid == ?", (p1,))
			authors = cursor.fetchall()
			for t in authors:
				print u"%s/%s-%s/%s/%s семестр %s/%s/%s"%(k,m,n,p,q,r,t[0],p1)
conn.close()

#def makesetofdirs(basepath,dirset):
#	for i in dirset:
#		try:
#			os.mkdir(basepath + "/" + i)
#		except:
#			pass
#
#makesetofdirs(path,["raw","by_author","by_speciality","by_year", "by_discipline", "by_studyform"])
#os.system("rsync -arcp --delete %s %s" % (materials_basepath + "/", path + "/raw/"))
#
#makesetofdirs(path + "/by_studyform",list1)
