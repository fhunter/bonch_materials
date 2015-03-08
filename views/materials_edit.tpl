%setdefault('button', 'Отредактировать')
%include header
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Редактирование учебного материала</h2>
	  <div class="add_form">
	  <form id="material_add_form" method="post" action="" enctype="multipart/form-data">
	    %include table data=data, headers=headers, width = width
	    <input type="hidden" name="action" value="update"/>
	    <input type="hidden" name="uuid" value="{{uuid}}"/>
	    <input type=submit value="{{button or 'Отредактировать'}}">
	  </form>
	  </div>
	</div>
	</div>
	</div>
%include footer

