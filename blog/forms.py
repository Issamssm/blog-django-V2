from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget



class PostCreatForm(forms.ModelForm):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={'style' : "width:88%;",'class' : 'bordder-[#E9EDF4] rounded-md border bg-[#FCFDFE] py-3 px-5 text-body-color text-body-color placeholder-[#ACB6BE] outline-none transition focus:border-primary focus-visible:shadow-none mb-6','placeholder':'Title of post'}))
    content = forms.CharField(label='', widget=CKEditorWidget())
    image = forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={'style' : "grid-column: span 2 / span 2; width:138px;padding:1rem 0;",'class':"custom-file-input bg-[#FCFDFE] "}))
    class Meta:
        model = Post
        fields = ['title','content','image']