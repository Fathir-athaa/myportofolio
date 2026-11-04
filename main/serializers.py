from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Organization


class ExperienceSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)
    is_ongoing = serializers.BooleanField(read_only=True)
    image_urls = serializers.SerializerMethodField()
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "category_display",
            "ended_at", "is_ongoing", "image_urls",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Judul pengalaman tidak boleh kosong atau hanya berisi tag HTML."
            )
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def get_image_urls(self, obj):
        return [img.image.url for img in obj.images.all()]

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class OrganizationSerializer(serializers.ModelSerializer):
    is_ongoing = serializers.BooleanField(read_only=True)
    image_urls = serializers.SerializerMethodField()
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = [
            "id", "name", "role", "status", "is_active", "description",
            "is_ongoing", "image_urls",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_name(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError(
                "Nama organisasi tidak boleh kosong atau hanya berisi tag HTML."
            )
        return value

    def validate_role(self, value):
        return strip_tags(value).strip()

    def validate_status(self, value):
        return strip_tags(value).strip()

    def validate_description(self, value):
        return strip_tags(value).strip()

    def get_image_urls(self, obj):
        return [img.image.url for img in obj.images.all()]

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())