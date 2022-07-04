from operator import imod
from modeltranslation.translator import register, TranslationOptions
from home.models import HomeArticleModel


@register(HomeArticleModel)
class ArticleTranslation(TranslationOptions):
    fields = ('title', 'body')
