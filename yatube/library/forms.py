from django import forms
from .models import Book, CD


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'genre_id', 'name', 'pages')


class CDForm(forms.ModelForm):
    class Meta:
        model = CD
        fields = ('name', 'email', 'title', 'artist')

    def clean_artist(self):
        data = self.cleaned_data['artist']
        artist = CD.objects.count(data)
        if data not in artist:
            raise forms.ValidationError(
                "Вы не можете передать диск этого автора, потому что у получателя нет ни одного диска от этого автора")
        return data
