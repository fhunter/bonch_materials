%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование формы обучения</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="%s"/>
	    Название:<input name="study_form_name" value="%s"><br>
	    <input type=submit value="Отредактировать">
	  </form>
	  </div>
	</div>
	</div>
	</div>
%include footer
