# vim: set fileencoding=utf-8 :
import os
from my_db import *
from my_speciality import get_speciality_by_uuid,get_speciality
from my_study_form import get_study_form_by_uuid,get_study_form
from my_discipline import get_discipline_by_uuid,get_discipline
from my_author import get_authors

def get_materials():
	#uuid, name, description, owner, upload_date, edit_date, ##authors, ##course_belongs, ##files
	result = db_exec_sql("select uuid, name,description,owner, upload_date, edit_date from materials")
	result1 = []
	for i in result:
		uuid = i[0]
		result1.append( i + (get_authorship(uuid), get_belongs(uuid), get_material_files(uuid),))
	return result1

def get_material(uuid):
	result = db_exec_sql("select uuid, name, description, owner, upload_date, edit_date from materials where uuid = ?", (uuid,))[0]
	uuid = result[0]
	result1 = result + (get_authorship(uuid), get_belongs(uuid), get_material_files(uuid),)
	return result1

def get_material_files(uuid):
	result = []
	uuid1 = uuid.replace('..','').replace('/','').replace('{','/').replace('}','')
	path = "materials" + uuid1
	if os.path.isdir(path):
		for j in os.listdir(path):
			i = unicode(j.decode('utf-8'))
			path1 = unicode(path + "/" + i)
			if os.path.isfile(path1.encode('utf-8')):
				temp = (path1, i, os.path.getsize(path1.encode('utf-8')),)
				result.append(temp)
	return result

def add_material(form):
	if ("material_name" in form):
		name = cgi.escape(form.getfirst("material_name",""))
		owner = os.environ["REMOTE_USER"]
		db_exec_sql("insert into materials (uuid, name, owner) select *, ?, ? from next_uuid", (str(name).decode('utf-8'), owner))

#Keep this
def del_material(uuid):
	db_exec_sql("delete from materials where uuid = ?", (uuid,))
	#TODO: need to delete belongs info
	path = 'materials' + uuid.replace('{','/').replace('}','')
	if os.path.isdir(path):
		for j in os.listdir(path):
			if os.path.isfile(path + "/" + j):
				os.remove(path + "/" + j)
		os.rmdir(path)

def del_author(uuid,uuid_author):
	db_exec_sql("delete from authorship where author_uuid = ? and material_uuid = ?", (uuid_author, uuid))

def add_author(uuid,uuid_author):
	db_exec_sql("insert into authorship (author_uuid, material_uuid) values (?, ?)", (uuid_author, uuid))

#TODO
def update_material(uuid):
	name = request.forms.get("material_name", None)
	if name:
		db_exec_sql("update materials set name= ?, edit_date = (datetime())  where uuid = ?", (name.decode('utf-8'), uuid,))
	description = request.forms.get("material_description", None)
	if description:
		db_exec_sql("update materials set description= ?, edit_date = (datetime()) where uuid = ?", (description.decode('utf-8'), uuid,))
	if "del_file" in form:
		files_to_delete = form.getlist("del_file")
		for filestodel in files_to_delete:
			filestodel = filestodel.replace('{','').replace('}','').replace('..','')
			os.remove( "materials/"+filestodel)
	if "del_belongs" in form:
		belongs_to_delete = form.getlist("del_belongs")
		for belongsdel in belongs_to_delete:
			db_exec_sql("delete from belongs where id = ?", (belongsdel,))
	#FIXME
	speciality = request.forms.get("speciality",None)
	year 	   = request.forms.get("year",None)
	study_form = request.forms.get("study_form",None)
	discipline = request.forms.get("discipline",None)
	if speciality and year and study_form and discipline:
		if(speciality == '1' or year == '0' or study_form == '1' or discipline == '1'):
			pass
		else:
			db_exec_sql("insert into belongs (material_uuid, speciality_uuid, student_year, study_form_uuid, discipline_uuid ) values ( ?, ?, ?, ?, ?)", (uuid, speciality, year, study_form, discipline))
	#FIXME
	if "attach" in form:
		attach = form["attach"]
		path = 'materials' + uuid.replace('{','/').replace('}','')
		try:
			os.mkdir(path)
		except:
			pass
		if attach.file and attach.filename !="":
			db_exec_sql("update materials set edit_date = (datetime()) where uuid = ?", (uuid,))
			filename=path+"/"+os.path.basename(attach.filename)
			open(filename,"w").write(attach.file.read())

def get_authorship(uuid):
	result = db_exec_sql("select authorship.author_uuid, authors.fio from authorship,authors where authorship.material_uuid = ? and authors.uuid = authorship.author_uuid", (uuid,))
	return result

def get_belongs(uuid):
	result = db_exec_sql("""
		select 
		    	belongs.id,
		    	speciality.name, 
		    	belongs.student_year, 
		    	study_form.study_form, 
		    	discipline.name,
		    	discipline.semester 
		from
			belongs, discipline, speciality, study_form
		where
				material_uuid = ? 
			and
				discipline.uuid = belongs.discipline_uuid
			and
				speciality.uuid = belongs.speciality_uuid
			and
		    		study_form.uuid = belongs.study_form_uuid 
			    	
		""", (uuid, ))
	return result
