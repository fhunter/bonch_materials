%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование специальности</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    Шифр:<input name="speciality_code" value="%s"><br>
	    Название:<input name="speciality_name" value="%s"><br>
	    Описание<br>
	    <textarea name="speciality_description">%s</textarea><br>
	    <input type=submit value="Отредактировать">
	  </form>
	  </div>
	</div>
	</div>
	</div>
%include footer
