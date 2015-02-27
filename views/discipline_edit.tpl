%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование дисциплины</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    Название:<input name="discipline_name" value="%s"><br>
	    Семестр:<input name="discipline_semester" value="%s"><br>
	    Описание<br>
	    <textarea name="discipline_description">%s</textarea><br>
	    <input type=submit value="Отредактировать">
	  </form>
	  </div>
	</div>
	</div>
	</div>

%include footer
