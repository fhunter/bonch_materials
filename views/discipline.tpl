%include header
      <div id="UI_elements">
	<div id="discipline_admin" class="UI_tab" >
	  <h2>Управление списком дисциплин</h2>
	  <div class="add_form">
	  <form id="discipline_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    Название:<input name="discipline_name"><br>
	    Семестр:<input name="discipline_semester"><br>
	    Описание:<br>
	    <textarea name="discipline_description"></textarea>
	    <br>
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  %include refresh_btn action="./discipline"
	  <div id="discipline_list" class="UI_list">
      	  %include table headers = headers, width= width, data = data, editable = True
	  </div>
	</div>
	</div>
	</div>
%include footer
