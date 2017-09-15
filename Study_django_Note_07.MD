
1.在Chapter2 的 add comments to the post detail template，有个 {% if new_comment%}这个地方代码有错误
  需要在 views return一个flag,然后这里面捕获这个flag

**Chapter2 -----实现评论系统、标签系统**

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

**Chapter4 -----设计一个社交网站**

        +++++ 设计一个用户登录授权
        ----- step1. 定义一个form，在form里面设置用户的登录和密码信息
              LoginForm
        ----- step2. 实现登录的views 首先判断是get还是Post,如果是post，那么我们回去post的数据
              login_Form = LoginForm(request.POST)
              验证数据是否有效  login_form.is_valid(),有效我们就把里面的username和password取出来，进行验证授权
              user = authenticate(username=username,password=password)
              如果验证存在会返回一个User的对象，如果不存在，则返回空
              如果存在，我们就到session注册一下
              if user is not None:
                 if user.is_active:
                      login(request,user)
                      return ......
        ----- step3. 设计login.html，在里面，extends base.html，然后进行设计
        ----- step4. 设计url # url(r'^login/$', LoginView.as_view(), name='login'), 捕获用户的登录，当遇到访问account/login的请求
              就指到LoginView
        +++++ 如何知道当前是那个页面?
              step1.在Views的返回参数增加section, 告诉前端，当前所在的页面，例如 {'section':'dashboard'}
              step2.在前端的templates里面，对当前section进行判断和处理，例如:
              <li {% if section == 'dashboard' %} class="selected"{% endif %}><a href="{% url 'accounts:dashboard' %}">My Dashboard</a></li>
        +++++ 如何实现在message全局展示?
               step1.在setting里面，install django.contrib.messages
               step2.在views里面，from django.contrib import messages
                     messages.success(request,'更新成功')
                     支持 success() error() info() waring() debug()
               step3,在template里面，直接使用，不需要view返回
                      {% if messages %}
                        {% for message in messages %}
                            <li>{{message|safe}}</li>
                        {% endfor %}
                      {% endif %}
        +++++ 如何实现自定义认证后台及自定义认证后台用处?
            在实际工作中，我们需要自定义的认证后台，比如有的需要邮箱，有的需要使用手机号，django提供自定义认证后台
            按照顺序进行认证
            step1.在项目setting里添加认证后台 AUTHENTICATION_BACKENDS
            AUTHENTICATION_BACKENDS = (
                'django.contrib.auth.backends.ModelBackend',
            )
            step2.定义一个类 Class EmailAuthBacked(object),在这个类里面实现 def authenticate(),def get_user()
            step3.将这个类添加到Settings里面。
            AUTHENTICATION_BACKENDS = (
                'django.contrib.auth.backends.ModelBackend',
                'account.authentication.EmailAuthBacked',
            )
        +++++ django 数据模型中 null=True 和 blank=True 有什么区别?
            # null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
            # blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，
            # 比如 admin 界面下增加 model 一条记录的时候。直观的看到就是该字段不是粗体

        +++++ Django在admin模块中显示auto_now_add=True或auto_now=True的时间类型列
            auto_now=Ture，字段保存时会自动保存当前时间，但要注意每次对其实例执行save()的时候都会将当前时间保存，
            也就是不能再手动给它存非当前时间的值。
            auto_now_add=True，字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值。但是之后的save()
            是可以手动赋值的。也就是新实例化一个model，想手动存其他时间，就需要对该实例save()之后赋值然后再save()

        +++++在第五章的 dashboard.html里面，有一个 {% with request.user.images_created.count %}得到的值是空
             这个不知道为什么，无法定位错误原因。需要请教高手解决下，看看上面问题。

        +++++ 如何创建图片的缩略图？
            step1.先下载安装sorl-thumbnail,安装方式 pip install sorl-thumbnail==12.3;
            step2.需要安装并同步数据库， install_app(), migrate;
            step3.在模板里面 使用 {% load thumbnail %}
            step4.完整的使用缩略图的方式:定义一个300px的缩略图，第一次使用时，会创建缩略图
            {% thumbnail image.image "300x300" crop="center" as im %}
              <a href="{{ image.image.url }}">
              <img src="{{ im.url }}" class="image-detail">    </a>
             {% endthumbnail %}

        +++++ 实现AJAX的动态点击喜欢/不喜欢，不用每次点击进入一个新页面
            step1.在html的头部，加载jquery.min.js
            <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.1.0.min.js" type="text/javascript"></script>
            step2.添加ajax的代码，如下:
                <script>
                  $(document).ready(function(){
                    //此处放入将要执行的动作
                  });
                </script>
            step3.在网页模板里面，如下：
                <a href="#" data-id="{{ image.id }}" data-action="{% if request.user in users_like %}un{% endif %}like" class="like button">
                    {% if request.user not in users_like %}
                        Like
                    {% else %}
                        Unlike
                    {% endif %}
                </a>
            step4.实现ajax提交请求，如下:
            $(function(){
                $('#jsStayBtn').on('click', function(){
                    $.ajax({
                        cache: false,
                        type: "POST",
                        url:"{% url 'org:user_ask' %}",
                        data:$('#jsStayForm').serialize(),
                        async: true,
                        success: function(data) {
                            if(data.status == 'success'){
                                $('#jsStayForm')[0].reset();
                                alert("你已提交成功")
                            }else if(data.status == 'fail'){
                                $('#jsCompanyTips').html(data.msg)
                            }
                        },
                    });
                });
            })

            $(document).ready(function(){
                    $('a.like').click(function(e){
                        e.preventDefault();
                        $.post('{% url "images:like" %}',
                            {
                                id: $(this).data('id'),
                                action: $(this).data('action')
                            },
                            function(data){
                                if (data['status'] == 'ok')
                                {
                                    var previous_action = $('a.like').data('action');

                                    // toggle data-action
                                    $('a.like').data('action', previous_action == 'like' ? 'unlike' : 'like');
                                    // toggle link text
                                    $('a.like').text(previous_action == 'like' ? 'Unlike' : 'Like');

                                    // update total likes
                                    var previous_likes = parseInt($('span.count .total').text());
                                    $('span.count .total').text(previous_action == 'like' ? previous_likes + 1 : previous_likes - 1);
                                    alert('我被点击了');
                                }
                        });

                    });
            });
            step5.在项目路由器编写url
            url(r'^like/$', image_like, name='like'),
            step6.实现view里面的逻辑处理
            def image_like(request):
                image_id = request.POST.get('id', '')
                action = request.POST.get('action', '')

                if image_id and action:
                    try:
                        """从数据库获取所有图片"""
                        image = Image.objects.get(id=int(image_id))

                        if action =='like':
                            image.user_like.add(request.user)
                        else:
                            image.user_like.remove(request.user)
                        return JsonResponse({'status': 'ok'})
                    except:
                        pass
                return JsonResponse({'status': 'ok'})

        +++++ AJAX实现滚屏翻页功能，当页面查看到底部，自动滚动到下一页
               step1. 定义url，    url(r'^$', ImageListView.as_view(), name='list'),在这里，我们定义只要访问Image就进入list
               step2. 定义视图，分页使用系统自带的paginator, paginator = Paginator(all_images,3)
                                                        images = paginator.page(page) 获取当前页的数据，是一个queryset
               step3. 对请求处理，如果是is_ajax()请求，则返回ajax页面，否则，就返回普通页面
               step4. ajax脚本 ，对当天页面判断，是否滚动，如果滚动了，判断是否有页面，并且当前滚动到页面底部，如果滚动到底部，那么请求一页
                  并加载到list列表里面
        （第五章AJAX相关的学习的不会很好，manytomany的应用也不是很好）

**Chapter6 -----创建用户粉丝系统和用户广播系统继承redis**

        +++++ 在用户的详情页,直接使用include方法未生效.
              在例子中,作者直接使用
              {% include "images/image/list_ajax.html" with images=user.images_created.all %}
              这个并没有生效，导致该用户创建的图片没有显示出来。
              解决办法:
              把上面的句子替换成下面代码,可以正确显示：
              {% for image in user.images_created.all %}
                <div class="image">
                    <a href="{{ image.get_absolute_url }}">
                        {% thumbnail image.image "300x300" crop="100%" as im %}
                            <a href="{{ image.get_absolute_url }}">
                                <img src="{{ im.url }}">
                            </a>
                        {% endthumbnail %}
                    </a>
                    <div class="info">
                        <a href="{{ image.get_absolute_url }}" class="title">{{ image.title }}</a>
                    </div>
                </div>
            {% endfor %}

        ++++++为什么在模板中，{{% with total_followers=user.followers.count %}},无法正确生效?

              系统中 User的 followers是一个多对多的字段。

        ++++++ 显示收藏/取消的按钮交互设计
               step1.我们需要在html里面, 对提交视图 data-action 进行动态赋值 unfollow/follow
               "{% if request.user in user.followers.all %} un{% endif %} follow"
               step2. 对链接文案动态赋值 Follow/Unfollow
                <!--显示用户是收藏还是取消收藏的按钮-->
                <a href="#", data-id="{{ user.id }}" data-action="{% if request.user in user.followers.all %}un
                {% endif %}follow" class="follow button">
                    {% if request.user not in user.followers.all %}
                        Follow
                    {% else %}
                        Unfollow
                    {% endif %}
                </a>
        +++++++ 创建AJAX类型的view去支持用户的关注/取消关注操作
                step0. 设计数据库表 Contact(models.Model),有3个字段，user1,user2,created
                step1. 第一步先编写一个url,这个url是用户关注/去关注的url； url(r'^user/like/$', UserLikeView.as_view(), name='user_follow')
                step2. 在view里面定义视图, UserLikeView(), 先取出来 要关注的用户id和具体的动作(like/unlike),如果这个值都有，那么开始验证行为
                       如果是like,那么就到数据库表里面填写一条记录，如果是unlike，就到数据库表删除一条记录
                step3. 设计template，定义一个连接，连接有id和action，点击后可以被ajax动态设置
                               <a href="#", data-id="{{ user.id }}" data-action="{% if request.user in user.followers.all %}un{% endif %}follow" class="follow button">
                                    {% if request.user not in user.followers.all %}
                                        Follow
                                    {% else %}
                                        Unfollow
                                    {% endif %}
                                </a>
                step4.关键设计jquery脚本，先初始化，然后制造一个post，里面有url、data、回调函数等
        +++++++ 如何实现一个Model的用户关注同一个model的用户？
                # Add following field to User dynamically 自己表用户关注自己表用户，这句话很关键
                User.add_to_class('following',
                              models.ManyToManyField('self',
                                                     through=Contact,
                                                     related_name='followers',
                                                     symmetrical=False))

        +++++++ 一个典型的JQuery的使用方式
                step1. 创建jquery的准备环境
                $(ducument).ready(function(){
                    //Do anything in here
                });
                step2. 在里面执行选择对应的控件被点击
                $(ducument).ready(function(){
                    //Do anything in here
                    $("a.follow").click(function(e){
                        //做一些当 class=follow的 <a>元素被点击，将执行这里面的事情
                    });
                });
                step3. 在点击后，我们将执行一个post发送数据的操作
                 $(ducument).ready(function(){
                    //Do anything in here
                    $("a.follow").click(function(e){
                        //做一些当 class=follow的 <a>元素被点击，将执行这里面的事情  $.post(URL,data,callback);
                        $.post(
                            'account:user_follow',
                            {
                                id:$(this).data('id'),
                                action:$(this).data('action'),
                            },
                            function(e){
                                //做一些回调函数要做的事情
                            }
                        )
                    });
                });
        +++++++ 为什么在查询时候,两个句子执行结果完全不同？
                if action == 'follow':
                    # Contact.objects.get_or_create(user_from=request.user, user_to=user)
                    con = Contact.objects.get_or_create(user_form=request.user, user_to=user)
                else:
                    Contact.objects.filter(user_from=request.user, user_to=user).delete()

                return JsonResponse({'status': 'ok'})

                这个查找到了原因，因为在Contact里面定义的字段是 user_form，但是这里面是user_from，一个是from，
                一个是form，所以导致根本查不到结果;
        +++++++ContentTypes是干嘛用?
            'django.contrib.contenttypes',  # 内容管理框架，能够跟踪项目中所有model并提供和model交互的通用接口
            使用起来和 auth或者admin一样 from django.contrib.contenttypes
            Django 包含一个contenttypes 应用，它可以追踪安装在你的Django 项目里的所有应用，并提供一个高层次的、
            通用的接口用于与你的模型进行交互
        ++++++++ 设计一个Feed流系统的步骤
                step1. 设计数据库,里面需要有user,feeds类型,创建时间
                step2. 设计一个生成feeds的方法，这里面需要注意，需要在1分钟内避免多次添加;
                step3. 到具体的事物方法内，当事物完成，添加生成feeds的方法
                step4. 在一个页面，进行集中展示

        ++++++ 了解prefetch_related和select_related这两个方法的不同
               ?

        ++++++Django 的value/value_list/flat 有什么作用?
              step1. 定义一个model
              class Building(models.Model):
                    corporation = models.ForeignKey('company.Corporation', verbose_name=u'学校',related_name='buildings')
                    number = models.CharField(u'楼栋编号',max_length=10, unique = True, db_index=True)
                    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)
                    获取building的number字段列表
                    In [1]: from apps.dormitory.models import Building

                    In [2]: buildings = Building.objects.values('number')

                    In [3]: buildings
                    Out[3]: [{'number': u'1'}, {'number': u'2'}, {'number': u'3'}, {'number': u'4'}, {'number': u'5'}]

                    In [4]: buildings_ = Building.objects.values_list('number')

                    In [5]: buildings_
                    Out[5]: [(u'1',), (u'2',), (u'3',), (u'4',), (u'5',)]

                    In [6]: buildings_list = Building.objects.values_list('number', flat=True)

                    In [7]: buildings_list
                    Out[7]: [u'1', u'2', u'3', u'4', u'5']
                    从以上代码可以看出:

                    values方法可以获取number字段的字典列表。

                    values_list可以获取number的元组列表。

                    values_list方法加个参数flat=True可以获取number的值列表。

        +++++++ Django 的signals
                 signals在  django.db.models.signals
                 1.pre_save() and post_save() ,send before or after calling the save() method of models
                 2.pre_delete() and post_delete() ,sent before or after calling the delete()method of models or
                   querySet()
                 3.m2m_changed: Sent when a ManyToManyField on a model is changed



        +++++++ 如何使用Django的信号机制(signal)
                step1. 在django中提供几种内置的信号源，分别为pre_save()\post_save()\pre_delete()\post_delete()\m2m_change
                step2. 定义一个receiver信号接收器，例如：
                    @receiver(m2m_changed, sender=Image.user_like.throut)
                step3. 在app里面定义apps.py，并导入信号模块， 例如：
                        from django.apps import AppConfig
                        class ImagesConfig(AppConfig):
                            name = 'images'
                            verbose_name = 'Image bookmarks'
                            def ready(self):
                               # import signal handlers
                               import images.signals
                step4. 在app的init.py里面告诉Django加载我们app的那个应用配置
                        default_app_config = 'images.apps.ImagesConfig'

        +++++++ 如何安装、使用Reis?
                
**Chapter7 -----建立一个在线商店系统**

        +++++++ 如何使用系统的Session
                 session框架允许你为匿名或者登陆用户保存任何数据，session数据会保存在服务器端,在cookies里面会包含session 
                在session中设置变量 :request.session['foo'] = 'bar' # 定义一个foo变量，并赋值为bar
                检索、查找session中的变量: reqeust.session.get('foo') # 从session中取出foo变量的值
                删除一个你存在session里面的数据: del request.session['foo'] # 从session中删除key为foo的字典
                
                在session里面，数据是以字典形式保存的  {'foo':{'quantity':1,'delete':True}}

        +++++++ ContextProcessors的作用
                是一个Python的函数，
                接受request为参数，并返回一个已经添加了请求上下文的字典
                当你需要一个在所有模板都需要处理的东西时,ContextProcessors非常有用
        
        +++++++ 使用ContextProcessors的方法。
                step1. 首先在项目任意地方定义一个context_processors.py文件,在里面定义一个函数,接受参数和返回都设定好
                def cart(request):
                    return {'cart':Cart(request)}
                关键是，这个接受的是一个request,返回的是一个字典
                
                step2. 到settings，在template的context里面，加入这个上下文处理器,例如 'cart.context_processors.cart'
                这样每次发起RequestContext,这个cart都会被使用；
                step3. 进入到任意一个django模板里面，就可以使用这个cart了，和使用返回值一样的方式
        
        +++++++ Creating customer orders
                step1.向用户展示一张订单表，让用户填写数据
                step2.根据用户输入的数据生成Order实例,并生成对应的OrderItem实例
                step3.清空购物车,把用户重定向到成功页
        
        
        +++++++ Inline类型
                设计一个model未inline类型，这样就可以把这个放到另外一个model里面，和另一个model
                具有同一个管理页面
        
        ++++++++ 订单管理及订单生成
                 step1.创建订单的前段页面
                 step2.在url配置订单的相关配置
                 step3.实现订单的model
                 step4.实现订单的admin页面
                 step5.实现前段需要的Form
                 step6.实现订单的View
        ++++++++ 购物车、订单、订单物品的关系
                 购物车有很多商品,直接保存到session里面的，一个request.session['cart'],取出来的是字典
                 {
                    '1':{'qunatity':10,'price':20.90},
                    '2':{'qunatity':10,'price':20.90},
                    '3':{'qunatity':10,'price':20.90},
                    '4':{'qunatity':10,'price':20.90},
                    '5':{'qunatity':10,'price':20.90},
                 }
                 购物车生成订单，一个订单含有用户信息，城市信息是否支持等信息，并含有很多商品
                 
                 一个购物车商品, 指向一个订单，指向一个物品，并具有价格和数量
        
        +++++++ 如何生成一个购物车？
        
        
        +++++++ 如何在contextprocessors里面，保存cart，让所有的模板都可以用
        
        +++++++ 如何点击订单生成一个订单记录
        
        
        +++++++ 如何将订单里面每个物品都展示出来？
        
        
        +++++++ 如何进行异步任务调度，比如，创建完了一个任务，会产生一个发送邮件的动作
                发送邮件将在几分钟后开始？简称Celery定时任务
        
        +++++++  how to launch asynchronous tasks with Celery
                这个章节我们没有学习他。
        
        
        +++++++  


**Chapter9 -----拓展你的商店**
