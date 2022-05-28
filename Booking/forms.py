from msilib.schema import RadioButton
from django import forms
type_choices=(
    ('one-way','ONE-WAY'),
    ('return','RETURN'),
    ('multi-city','MULTI-CITY'),
)
class BookForm(forms.Form):
    ticket_type=forms.ChoiceField(choices=type_choices,widget=RadioButton)