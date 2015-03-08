%include header
  <div id="UI_elements">
      <div id="study_form_admin" class="UI_tab" >
      <h2>Управление списком форм обучения</h2>
      %include add_btn action="./study_form/add"
      %include refresh_btn action="./study_form"
      <div id="study_form_list" class="UI_list">
      %include table headers = headers, width= width, data = data, editable = [True, True], action="./study_form/"
      </div>
    </div>

  </div>
</div>
%include footer
