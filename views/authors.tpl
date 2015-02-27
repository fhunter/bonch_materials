%include header
      <div id="UI_elements">
	<div id="author_admin" class="UI_tab" >
	  <h2>Управление списком авторов</h2>
	  %include add_btn action="./authors/add"
	  %include refresh_btn action="./authors"
	  <div id="author_list" class="UI_list">
          %include table headers = headers, width= width, data = data, editable = True, action = "./authors/"
	  </div>
	</div>
	</div>
	</div>
%include footer
