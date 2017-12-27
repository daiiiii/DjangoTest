from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags


# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model 类。
    Category 只需要一个简单的分类名 name 就可以了。
    CharField 指定了分类名 name 的数据类型，CharField 是字符型，
    CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
    当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
    Django 内置的全部类型可查看文档：
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = "文章分类"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = "文章标签"


class Catalog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="上级目录")
    CHOICES = (("P", u"父菜单"), ("S", u"子菜单"))
    menu_level = models.CharField(max_length=2, choices=CHOICES, verbose_name="目录级别")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '目录'
        verbose_name_plural = '目录'


class Post(models.Model):
    title = models.CharField("标题", max_length=70)

    body = models.TextField("内容")

    created_time = models.DateField("创建时间")
    modified_time = models.DateField("修改时间")
    excerpt = models.CharField("摘要", max_length=200, blank=True)
    views = models.PositiveIntegerField("阅读量", default=0)
    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category, verbose_name="分类")
    catalog = models.ForeignKey(Catalog, default=1, verbose_name="目录")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")

    STATUS_CHOICES = ((0, '显示'), (1, '隐藏'),)
    status = models.IntegerField("状态", default=0, choices=STATUS_CHOICES, editable=False)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            md = markdown.Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:60]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    # 文章按时间排序
    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])



