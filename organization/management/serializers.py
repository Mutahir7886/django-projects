from rest_framework import serializers
from .models import organizaations, Branches, users,co_relation


class BRNSerializer(serializers.ModelSerializer):
   id=serializers.IntegerField()
   class Meta:
        model = Branches
        fields = ('id','name', 'Address', 'organizaations')
        read_only_fields =('organizaations',)


class ORGSerializer(serializers.ModelSerializer):

    branches=BRNSerializer(many=True)

    class Meta:
        model = organizaations
        fields = ('id','name','branches')

    def create(self, validated_data):
        branches=validated_data.pop('branches')
        org = organizaations.objects.create(**validated_data)
        for branch in branches:
            Branches.objects.create(**branch,organizaations=org)
        return org

    def update(self, instance, validated_data):

        branches = validated_data.pop('branches')
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        keep_choices = []
        for branch in branches:
            if "id" in branch.keys():
                if Branches.objects.filter(id=branch["id"]).exists():
                    c = Branches.objects.get(id=branch["id"])
                    c.name = branch.get('name', c.name)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue

            else:
                c = Branches.objects.create(**branch, organizaations=instance)
                keep_choices.append(c.id)

        for branch in instance.branches:
            if branch.id not in keep_choices:
                branch.delete()

        return instance




class USRSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = ('name', 'id_num', 'Ranks')

class CorelationSer(serializers.ModelSerializer):
    class Meta:
        model = co_relation
        fields = ('users','branches')


class FINALSER(serializers.ModelSerializer):
    branch=serializers.IntegerField()
    class Meta:
        model=users
        fields=('name', 'id_num', 'Ranks','branch')

    def create(self, validated_data):
        branch = validated_data.pop('branch')
        user=users.objects.create(**validated_data)


        diction={'users':user.id,'branches':branch}
        #import pdb;
        #pdb.set_trace()

        vall=CorelationSer(data=diction)

        if vall.is_valid():
            vall.save()
        else:
           return  vall.errors
        return vall.data

