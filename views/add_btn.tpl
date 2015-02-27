<div class="add_button"><table><tr><td>
	<form action="{{action}}" method="post">
		%if defined('uuid'):
		<input type="hidden" name="uuid" value="{{uuid}}"/>
		%end
		<input type="hidden" name="action" value="add"/>
		<input type=submit value="Добавить"/>
	</form>
	</td>
	</tr></table>
</div>
