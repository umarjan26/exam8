from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'grade')

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if 1 > grade or grade > 5:
            raise ValidationError(
                f"Значение оценки некорретное. Интервал между 1 и 5")
        return grade


class ReviewModerForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'grade', 'status')

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if 1 > grade or grade > 5:
            raise ValidationError(
                f"Значение оценки некорретное. Интервал между 1 и 5")
        return grade