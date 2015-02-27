# vim: set fileencoding=utf-8 :
import cgi
from my_db import *
from my_speciality import get_speciality_by_uuid,get_speciality
from my_study_form import get_study_form_by_uuid,get_study_form
from my_discipline import get_discipline_by_uuid,get_discipline
from my_author import get_authors

material_edit = u"""
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование учебного материала</h2>
	  <div class="add_form">
	  <form id="material_add_form" method="post" action="" enctype="multipart/form-data">
	    <table>
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    %s
	    </table>
	    <input type=submit value="Обновить">
	  </form>
	  </div>
	</div>
	</div>
	</div>
	"""

def get_materials():
	result = db_exec_sql("select uuid, name,description,owner, upload_date, edit_date from materials")
	return result

def get_belongs_string(uuid, editdelete = False):
	belongs = get_belongs(uuid)
	if belongs != []:
		belongs1 = []
		belongs_string = "<table><tr>"
		for j in [ u"Специальность", u"Год", u"Форма обучения", u"Дисциплина", u"Семестр" ]:
			belongs_string += "<td class=field_name>%s</td>" % j
		if editdelete:
			belongs_string += "<td></td>"
		belongs_string += "</tr>"
		for j in belongs:
			element = (get_speciality_by_uuid(j[1])[0][0],j[2],get_study_form_by_uuid(j[3])[0][0],get_discipline_by_uuid(j[4])[0][0],get_discipline_by_uuid(j[4])[0][1])
			belongs_string += "<tr>"
			for i in element:
				belongs_string += "<td class=field_value>%s</td>" % i
			if editdelete:
				belongs_string += "<td><input type=checkbox name=del_belongs value=%s></td>" % j[0]
			belongs_string += "</tr>"
		belongs_string += "</table>"
		return belongs_string
	else:
		return ""

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

def del_material(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		db_exec_sql("delete from materials where uuid = ?", (uuid,))
		path = 'materials' + uuid.replace('{','/').replace('}','')
		if os.path.isdir(path):
			for j in os.listdir(path):
				if os.path.isfile(path + "/" + j):
					os.remove(path + "/" + j)
			os.rmdir(path)

def update_material(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		material = db_exec_sql("select uuid, name, description, owner, upload_date, edit_date from materials where uuid = ?", (uuid,))
		material= material[0]
		name = material[1]
		description = material[2]
		if "material_name" in form:
			name= cgi.escape(form.getfirst("material_name",""))
			db_exec_sql("update materials set name= ?, edit_date = (datetime())  where uuid = ?", (name.decode('utf-8'), uuid,))
		if "material_description" in form:
			description = cgi.escape(form.getfirst("material_description",""))
			db_exec_sql("update materials set description= ?, edit_date = (datetime()) where uuid = ?", (description.decode('utf-8'), uuid,))
		if "del_author" in form:
			authors_to_delete = form.getlist("del_author")
			for author in authors_to_delete:
				db_exec_sql("delete from authorship where author_uuid = ? and material_uuid = ?", (author, uuid))
		if "del_file" in form:
			files_to_delete = form.getlist("del_file")
			for filestodel in files_to_delete:
				filestodel = filestodel.replace('{','').replace('}','').replace('..','')
				os.remove( "materials/"+filestodel)
		if "del_belongs" in form:
			belongs_to_delete = form.getlist("del_belongs")
			for belongsdel in belongs_to_delete:
				db_exec_sql("delete from belongs where id = ?", (belongsdel,))
		if "author" in form:
			author = cgi.escape(form.getfirst("author",""))
			if author != "1":
				db_exec_sql("insert into authorship (author_uuid, material_uuid) values (?, ?)", (author, uuid))
		if ("speciality" in form) and ("year" in form) and ("study_form" in form) and ("discipline" in form):
			speciality = cgi.escape(form.getfirst("speciality",""))	
			year       = cgi.escape(form.getfirst("year",""))	
			study_form = cgi.escape(form.getfirst("study_form",""))	
			discipline = cgi.escape(form.getfirst("discipline",""))
			if(speciality == '1' or year == '0' or study_form == '1' or discipline == '1'):
			    pass
			else:
				db_exec_sql("insert into belongs (material_uuid, speciality_uuid, student_year, study_form_uuid, discipline_uuid ) values ( ?, ?, ?, ?, ?)", (uuid, speciality, year, study_form, discipline))
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

def edit_material(form):
	if "uuid" in form:
		uuid = cgi.escape(form.getfirst("uuid",""))
		material = db_exec_sql("select uuid, name, description, owner, upload_date, edit_date from materials where uuid = ?", (uuid,))
		material = material[0]

		filedata = "<table>"
		filelist = get_material_files(material[0])
		for i in filelist:
			html = u"""<a href="%s">%s</a>%s Байт""" % (i[0], i[1], i[2] )
			html += "<input type=checkbox name=del_file value=\"%s/%s\">" % (uuid, i[1])
			filedata += gen_table_row( u"Файлы", html )
		filedata += "</table>" + u"""<input type="file" name="attach"  />"""
		authorship_string = ""
		tmp = get_authorship(uuid)
		for j in tmp:
			authorship_string += gen_table_row( u"Автор", j[1] + "<input type=checkbox name=del_author value=\"%s\">" % j[0])
		authorship_string = "<table>%s</table>" % authorship_string
		authorship_string += "<select name=author><option value=1></option>"
		for j in get_authors():
			authorship_string += u"""<option value="%s">%s</option>""" % (j[0],j[1])
		authorship_string += "</select>"
		belongs_string = get_belongs_string(uuid, True)
		belongs_string += "<select name=speciality><option value=1></option>"
		for j in get_speciality():
			belongs_string += "<option value=\"%s\">%s</option>" % (j[0], j[2])
		belongs_string += "</select><select name=year>"
		belongs_string += "<option value=0></option>"
		for j in range(1,7):
			belongs_string += "<option value=%d>%d</option>" % (j,j)
		belongs_string += "</select><select name=study_form><option value=1></option>"
		for j in get_study_form():
			belongs_string += "<option value=\"%s\">%s</option>" % (j[0], j[1])
		belongs_string += "</select><select name=discipline><option value=1></option>"
#HERE GOES discipline + semester
		for j in get_discipline():
			belongs_string += "<option value=\"%s\">%s</option>" % (j[0], "%s - %s"% ( j[1], j[2]))
		belongs_string += "</select>"
	    	name = """<input name="material_name" value="%s">""" % material[1]
		description = """<textarea name="material_description">%s</textarea>""" % material[2]
		page = material_edit % (material[0],gen_table_row(u"Название",name)+gen_table_row(u"Дата заливки",material[4])+gen_table_row(u"Дата редактирования",material[5])+gen_table_row(u"Описание",description)+gen_table_row(u"Владелец",material[3])+gen_table_row(u"Авторы",authorship_string)+gen_table_row(u"Файлы",filedata)+ gen_table_row(u"Принадлежность",belongs_string))
		print_ui(page )
		exit(0)

material_case = { "edit": edit_material, "delete": del_material, "add": add_material, "update": update_material }

def material_showui(form):
	if is_post():
		action = form.getfirst("action","")
		if action in material_case:
			material_case[action](form)
	result=get_materials()
	table = u""
	for i in result:
		table += """<div class="list_element">"""
		table += "<table>"
		table += gen_table_row( u"Название" , i[1])
		table += gen_table_row( u"Дата заливки" , i[4])
		if i[5] == None:
			table += gen_table_row( u"Дата редактирования" , u"Никогда")
		else:
			table += gen_table_row( u"Дата редактирования" , i[5])
		table += gen_table_row( u"Заливал", i[3])
		tmp = get_authorship(i[0])
		for j in tmp:
			table += gen_table_row( u"Автор", j[1])
		table += gen_table_row_wide( u"Описание", i[2])

		belongs_string = get_belongs_string(i[0],False)
		if belongs_string !="":
			table += gen_table_row(u"Принадлежность", belongs_string)

		filelist = get_material_files(i[0])
		for j in filelist:
			html = u"""<a href="%s">%s</a>%s Байт""" % (j[0], j[1], j[2] )
			table += gen_table_row( u"Файлы", html )

		table += "</table>"
		table += insert_edit_delete_btn(i[0], "delete_material")
		table += "</div>"


def get_authorship(uuid):
	result = db_exec_sql("select authorship.author_uuid, authors.fio from authorship,authors where authorship.material_uuid = ? and authors.uuid = authorship.author_uuid", (uuid,))
	return result

def get_belongs(uuid):
	result = db_exec_sql("select id,speciality_uuid, student_year, study_form_uuid, discipline_uuid from belongs where material_uuid = ?", (uuid, ))
	return result
