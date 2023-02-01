from rest_framework import serializers
from . import Functions
import json

    
class LongTermSerializer(serializers.Serializer):
    Predictions = serializers.SerializerMethodField()
    Previous= serializers.SerializerMethodField()
    
    def get_Predictions(self, obj):
        request=self.context.get("request")
        company=request.query_params.get('company')
        variable=request.query_params.get('variable')
        return Functions.getLongTermPredictions(30, company, variable)
    
    
    def get_Previous(self, obj):
        request=self.context.get("request")
        company=request.query_params.get('company')
        variable=request.query_params.get('variable')
        return Functions.getLongTermData(100,company,variable)


    
class ShortTermSerializer(serializers.Serializer):
    Predictions = serializers.SerializerMethodField()
    Previous= serializers.SerializerMethodField()
    
    def get_Predictions(self, obj):
        request=self.context.get("request")
        company=request.query_params.get('company')
        return Functions.getShortTermPredictions(8, company)
    
    
    def get_Previous(self, obj):
        request=self.context.get("request")
        company=request.query_params.get('company')
        return Functions.getShortTermData(40,company)
