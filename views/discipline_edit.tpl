%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование дисциплины</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="{{uuid}}"/>
	    Название:<input name="discipline_name" value="{{name}}"><br>
	    Семестр:<input name="discipline_semester" value="{{semester}}"><br>
	    Описание<br>
	    <textarea name="discipline_description">{{description}}</textarea><br>
	    <input type=submit value="Отредактировать">
	  </form>
	  </div>
	</div>
	</div>
	</div>

%include footer
