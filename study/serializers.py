from rest_framework import serializers

from study.models import Study, Materials


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'
        