from rest_framework import serializers
from models import habilidadesModel

class habilidadesSerializer(serializers.ModelSerializer):
	id_usuario = serializers.ReadOnlyField(source='id_usuario.username')
	class Meta:
		model = habilidadesModel
		field = ('id_usuario','id_categoria','nhabilidad','descripcion','estado',)