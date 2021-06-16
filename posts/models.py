from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class AuthorModel(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('name'))
    avatar = models.ImageField(upload_to='avatar', verbose_name=_('avatar'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class TagModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostModel(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('title'))
    image = models.ImageField(upload_to='posts', verbose_name=_('image'))
    banner = models.ImageField(upload_to='post_banner', verbose_name=_('banner'))
    content = RichTextField(verbose_name=_('content'))
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT,
                               related_name='posts', null=False, verbose_name=_('author'))

    tags = models.ManyToManyField(TagModel, related_name='posts', verbose_name=_('tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel,
                             related_name='comments',
                             on_delete=models.CASCADE,
                             verbose_name=_('post')
                             )
    name = models.CharField(max_length=25, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=17, null=True, blank=True, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

