# -*- coding: utf-8 -*-from django.shortcuts import renderfrom TestModel.models import User# 接收POST请求数据def register_user(request):    ctx = {}    if 'username' in request.POST and request.POST['username'] and 'pwd' in request.POST and request.POST['pwd']:        user = User(name=request.POST['username'], pwd=request.POST['pwd'])        user.save()        ctx['rlt'] = "恭喜您注册成功！"    else:        ctx['rlt'] = "请输入账号和密码！"    return render(request, "register_form.html", ctx)