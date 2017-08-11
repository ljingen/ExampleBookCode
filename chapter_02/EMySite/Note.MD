
1.在Chapter2 的 add comments to the post detail template，有个 {% if new_comment%}这个地方代码有错误
  需要在 views return一个flag,然后这里面捕获这个flag

Chapter2 -----实现评论系统、标签系统
         +++++ 评论系统(比较原始)
                 -----先创建评论model:Comment
                 -----再创建model对应的Form:CommentForm
                 -----在Views里面对get和post进行处理，返回 comments,post处理提交，
                 -----到template里面设置对应模板，根据return的
                 -----url里面处理 url(r'^(?P<post_id>\d+)/detail/', post_detail, name ='post_detail')
         +++++ 标签系统
                ----- 先安装一份第三方的Taggit  pip install django-taggit
                ----- 在项目里面 的install app 里面加入这个app
                ----- 具体用法，进入到 blog的model.py添加django-taggit的TagableManager  from taggit.managers import
                TaggableManager
                -----  这个插件有一个问题，对中文tag,会导致tag.slug 生成的只有_2  _1这样的，导致传参失败
         +++++ 读过这个还读过:
                ----- step1 ，返回当前帖子的所有标签
                    post_tags_ids = post.tags.values_list('id', flat=True)
                ----- step2 ，返回带有这些标签的所有帖子
                    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
                ----- step3 ，在返回的帖子列表中排除当前的帖子，避免推荐相同的帖子
                    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
                ----- step4 ，通过和当前共享标签的数量，对剩余帖子列表进行排序，如果有两个或多个帖子拥有相同数量的标签，推荐
                              最近的帖子
                     similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
                ----- step5 , 限制我们想要推荐的帖子数量
                     similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

