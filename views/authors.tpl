%include header
      <div id="UI_elements">
	<div id="author_admin" class="UI_tab" >
	  <h2>Управление списком авторов</h2>
	  <div class="add_form">
	  <form id="author_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    <input name="authors_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  %include refresh_btn action="./authors"
	  <div id="author_list" class="UI_list">
          %include table headers = headers, width= width, data = data, editable = True, action = "./authors/"
	  </div>
	</div>
	</div>
	</div>
%include footer
