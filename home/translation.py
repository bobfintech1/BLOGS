from operator import imod
from modeltranslation.translator import register, TranslationOptions
from home.models import HomeArticleModel, HomeCarouselModel


@register(HomeCarouselModel)
class CarouselTranslation(TranslationOptions):
    fields = ('title', 'body')


@register(HomeArticleModel)
class ArticleTranslation(TranslationOptions):
    fields = ('title', 'body')
