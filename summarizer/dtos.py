from rest_framework import serializers


class ValidateYoutubeSummarizeParams(serializers.Serializer):
    link = serializers.URLField()
    percentage = serializers.IntegerField()


class ValidateSummarizeParams(serializers.Serializer):
    text = serializers.CharField()
    percentage = serializers.IntegerField()


class ValidateWikipediaSummarizeParams(serializers.Serializer):
    query = serializers.CharField()


class ValidateNewsArticleSummarizeParams(serializers.Serializer):
    link = serializers.URLField()
