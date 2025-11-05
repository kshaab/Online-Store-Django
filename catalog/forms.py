from django import forms
from catalog.models import Product
from catalog.constants import FORBIDDEN_WORDS
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "image"]

    def clean_name(self):
        name = self.cleaned_data.get("name").lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError("Название содержит запрещенное слово")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description").lower().strip()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError("Описание содержит запрещенное слово")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price




