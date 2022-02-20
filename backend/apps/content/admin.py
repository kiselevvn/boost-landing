from django.contrib import admin
from .models import News, QuestionAnswer, Comment, Service, CategoryService, CategoryNews


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Новость в админке
    """

    list_display = (
        "title",
        "category_news",
        "date",
        "is_published",
        "is_published_landing",
    )
    list_filter = (
        "is_published",
        "is_published_landing",
    )


@admin.register(CategoryNews)
class CategoryNewsAdmin(admin.ModelAdmin):
    """
    Новость в админке
    """

    list_display = (
        "name",
        "date_created",
        "is_published",
    )
    list_filter = (
        "is_published",
    )


# @admin.register(QuestionAnswer)
# class QuestionAnswerAdmin(admin.ModelAdmin):
#     """
#     Вопрос ответ в админке
#     """

#     list_display = (
#         "question",
#         "date_updated",
#         "date_created",
#     )
#     list_filter = ("date_created",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Новость в админке
    """

    list_display = (
        "name",
        "date_created",
        "is_published_landing",
    )
    list_filter = ("is_published_landing",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Услуга
    """

    list_display = (
        "name",
        "category_service",
        "is_published",
    )
    list_filter = ("is_published","category_service",)


@admin.register(CategoryService)
class CategoryServiceAdmin(admin.ModelAdmin):
    """
    Категория услуги
    """

    list_display = (
        "name",
        "is_published",
    )
    list_filter = ("is_published",)
