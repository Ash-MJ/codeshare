from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'c_code', 'cpp_code' , 'p_code' , 'j_code' ,)