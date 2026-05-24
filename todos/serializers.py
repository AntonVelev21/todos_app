from rest_framework.serializers import ModelSerializer

from todos.models import Todo, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'category', 'state', 'is_done']
        read_only_fields = ['id']


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if validated_data['is_done']:
            instance.state = True
            instance.save()
        return instance



class TodoNestedSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'category', 'state']
        read_only_fields = ['id']
