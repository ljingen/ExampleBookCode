
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
                -----
