from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('firstname', 'lastname', 'email', 'phone', 'jobtitle', 'centername', 'businessdesc', 'centerstatus', 'licensecap', 'country', 'comments', 'tnc')