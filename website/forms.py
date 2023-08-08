from django import forms
from .models import Record

# add record form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget = forms.TextInput(attrs={"placholder":"First Name", "class":"form-control"}), label = "First Name ")
    last_name = forms.CharField(max_length=50, required=True, widget = forms.TextInput(attrs={"placholder":"Last Name", "class":"form-control"}), label = "Last Name ")
    email = forms.CharField(max_length=100, required=False, widget = forms.TextInput(attrs={"placholder":"Email", "class":"form-control"}), label = "Email ")
    phone = forms.CharField(max_length=10, required=False, widget = forms.TextInput(attrs={"placholder":"Phone", "class":"form-control"}), label = "Phone ")
    affilation = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={"placholder":"Affilation", "class":"form-control"}), label = "Affilation ")
    position = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={"placholder":"Position", "class":"form-control"}), label = "Position ")
    city = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={"placholder":"City", "class":"form-control"}), label = "City ")
    state = forms.CharField(max_length=2, required=False, widget = forms.TextInput(attrs={"placholder":"State", "class":"form-control"}), label = "State (Shortform only)")
    zipcode = forms.CharField(max_length=5, required=False, widget = forms.TextInput(attrs={"placholder":"Zipcode", "class":"form-control"}), label = "ZipCode ")
    county = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={"placholder":"County", "class":"form-control"}), label = "County ")
    country = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={"placholder":"Country", "class":"form-control"}), label = "Country ")
    activity_type= forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={"placholder":"Activity Type", "class":"form-control"}), label = "Activity Type ")
    activity_name = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={"placholder":"Activity Name", "class":"form-control"}), label = "Activity Name ")
    year = forms.CharField(max_length=4, required=False, widget = forms.TextInput(attrs={"placholder":"Year", "class":"form-control"}), label = "Year ")
    section = forms.CharField(max_length=10, required=False, widget = forms.TextInput(attrs={"placholder":"Section", "class":"form-control"}), label = "Section ")
    pass_fail = forms.CharField(max_length=10, required=False, widget = forms.widgets.TextInput(attrs={"placholder":"Pass/Fail", "class":"form-control"}), label = "Pass/Fail ")
    fee = forms.CharField(max_length=10, required=False, widget = forms.TextInput(attrs={"placholder":"Fee", "class":"form-control"}), label = "Fee ")
    sponsor = forms.CharField(max_length=50, required=False, widget = forms.TextInput(attrs={'placholder':'Sponsor', "class":"form-control"}), label = "Sponsor ")

    class Meta:
        model = Record
        exclude = ("user",)