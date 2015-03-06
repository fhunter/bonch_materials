%setdefault('button', 'Отредактировать')
%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование учебного материала</h2>
	  <div class="add_form">
	  <form id="material_add_form" method="post" action="" enctype="multipart/form-data">
	    <table>
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="{{uuid}}"/>
#		filelist = get_material_files(material[0])
#		for i in filelist:
#			html = u"""<a href="%s">%s</a>%s Байт""" % (i[0], i[1], i[2] )
#			html += "<input type=checkbox name=del_file value=\"%s/%s\">" % (uuid, i[1])
#			filedata += gen_table_row( u"Файлы", html )
#		filedata += "</table>" + u"""<input type="file" name="attach"  />"""
#		authorship_string = ""
#		tmp = get_authorship(uuid)
#		for j in tmp:
#			authorship_string += gen_table_row( u"Автор", j[1] + "<input type=checkbox name=del_author value=\"%s\">" % j[0])
#		authorship_string = "<table>%s</table>" % authorship_string
#		authorship_string += "<select name=author><option value=1></option>"
#		for j in get_authors():
#			authorship_string += u"""<option value="%s">%s</option>""" % (j[0],j[1])
#		authorship_string += "</select>"
#		belongs_string = get_belongs_string(uuid, True)
#		belongs_string += "<select name=speciality><option value=1></option>"
#		for j in get_speciality():
#			belongs_string += "<option value=\"%s\">%s</option>" % (j[0], j[2])
#		belongs_string += "</select><select name=year>"
#		belongs_string += "<option value=0></option>"
#		for j in range(1,7):
#			belongs_string += "<option value=%d>%d</option>" % (j,j)
#		belongs_string += "</select><select name=study_form><option value=1></option>"
#		for j in get_study_form():
#			belongs_string += "<option value=\"%s\">%s</option>" % (j[0], j[1])
#		belongs_string += "</select><select name=discipline><option value=1></option>"
##HERE GOES discipline + semester
#		for j in get_discipline():
#			belongs_string += "<option value=\"%s\">%s</option>" % (j[0], "%s - %s"% ( j[1], j[2]))
#		belongs_string += "</select>"
#	    	name = """<input name="material_name" value="%s">""" % material[1]
#		description = """<textarea name="material_description">%s</textarea>""" % material[2]
#		page = material_edit % (material[0],gen_table_row(u"Название",name)+gen_table_row(u"Дата заливки",material[4])+gen_table_row(u"Дата редактирования",material[5])+gen_table_row(u"Описание",description)+gen_table_row(u"Владелец",material[3])+gen_table_row(u"Авторы",authorship_string)+gen_table_row(u"Файлы",filedata)+ gen_table_row(u"Принадлежность",belongs_string))
#
	    </table>
	    <input type=submit value="{{button or 'Отредактировать'}}">
	  </form>
	  </div>
	</div>
	</div>
	</div>
%include footer

