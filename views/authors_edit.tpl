%setdefault('button', 'Отредактировать')
%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование автора</h2>
	  <div class="add_form">
	  <form id="study_form_edit_form" method="post" action="">
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="{{uuid}}"/>
	    ФИО:<input name="authors_name" value="{{fio}}"><br>
	    <input type=submit value="{{button or 'Отредактировать'}}">
	  </form>
	  </div>
	</div>
	</div>
	</div>

%include footer
