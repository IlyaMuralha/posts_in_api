from rest_framework.serializers import (IntegerField, CharField, Serializer)
from notesapp.models import Note


class NoteSerializer(Serializer):
    id = IntegerField(read_only=True)
    # атрибут required указывает что поле обязательно к заполнению
    title = CharField(required=True)
    text = CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
