from django import forms
from catalog.models import Product
from catalog.constants import FORBIDDEN_WORDS

class StyleFormMixin:
    fields: dict[str, forms.Field]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите название продукта"
        })
        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта"
        })
        self.fields["category"].widget.attrs.update({
            "class": "form-control"
        })
        self.fields["price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите цену продукта"
        })
        self.fields["on_sale"].widget.attrs.update({
            "class": "form-check-input"
        })


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "image", "on_sale"]

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




