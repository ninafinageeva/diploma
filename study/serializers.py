from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from study.models import Study, Materials
from users.models import User


class StudySerializer(serializers.ModelSerializer):

    class Meta:
        model = Study
        fields = '__all__'


class MaterialsSerializer(serializers.ModelSerializer):
    study_materials = SlugRelatedField(slug_field='title', queryset=Study.objects.all())

    class Meta:
        model = Materials
        fields = '__all__'
        