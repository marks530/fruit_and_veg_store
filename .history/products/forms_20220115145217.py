from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        name = [(c.id, c.name) for c in categories] #was supplier c.get_supplier()

        self.fields['category'].choices = name  # was supplier
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'