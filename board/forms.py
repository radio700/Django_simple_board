from django import forms
from board.models import Question,Answer

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['content']
    labels = {'content':'내용'}
    
