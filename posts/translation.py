from modeltranslation.translator import register, TranslationOptions
from posts.models import PostModel


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)






