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
materials_basepath  = os.path.abspath(materials_basepath + "/../materials/")

os.system("rsync -avrp --partial "+materials_basepath + " " + path+"/raw");
#rsync -avrp ./materials/ /tmp/2/raw

def mkdir(base,pathlist):
	path = base + "/"
	for i in pathlist:
		path = path + "/" + i
		try:
			os.mkdir(path)
		except:
			pass
def tostring(pathlist):
	path = "."
	for i in pathlist:
		path = path + "/" + i
	return path

def link(path1,path2):
	try:
		os.symlink(path1,path2)
	except:
		pass

conn = sqlite3.connect("/var/www/materials/materials.sqlite")
cursor = conn.cursor()
cursor.execute("select belongs.material_uuid,materials.name,study_form.study_form,speciality.code,speciality.name,belongs.student_year,discipline.name,discipline.semester from study_form, belongs, discipline, speciality,materials  where belongs.study_form_uuid == study_form.uuid and belongs.discipline_uuid == discipline.uuid and belongs.speciality_uuid == speciality.uuid and materials.uuid == belongs.material_uuid")
results = cursor.fetchall()
for i in results:
	(material_uuid, materials_name, study_form, speciality_code, speciality_name, student_year, discipline, semester) = i
	cursor.execute("select authors.fio from authors,authorship where authors.uuid == authorship.author_uuid and authorship.material_uuid == ?",(material_uuid,))
	for j in cursor.fetchall():
		mkdir(path, (study_form, speciality_code + "_" + speciality_name, u"Год обучения "+str(student_year), discipline, u"Семестр"+str(semester), j[0]))
		link(path + "/raw/" + strip_uuid(material_uuid), path + "/" + tostring((study_form, speciality_code + "_" + speciality_name, u"Год обучения "+str(student_year), discipline, u"Семестр"+str(semester), j[0], materials_name)))
		#Сделать здесь симлинк
conn.close()
