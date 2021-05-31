系统搭建关键问题

1. 图片的上传和显示
参考博客:
https://blog.csdn.net/c_beautiful/article/details/79755368
https://blog.csdn.net/qq_33961117/article/details/84636343
2. 关于head的一些东西
viewport https://www.cnblogs.com/zhoujingye/p/12512986.html
rel https://www.w3school.com.cn/tags/att_link_rel.asp
3. Advantages of Bootstrap:
Easy to use: Anybody with just basic knowledge of HTML and CSS can start using Bootstrap
Responsive features: Bootstrap's responsive CSS adjusts to phones, tablets, and desktops
Mobile-first approach: In Bootstrap 3, mobile-first styles are part of the core framework
Browser compatibility: Bootstrap is compatible with all modern browsers (Chrome, Firefox, Internet Explorer, Edge, Safari, and Opera)
4. 除了系统功能，还能给网页加什么？
   1. 各个算法功能的介绍
   2. 算法功能的预览图
   3. 一些装饰物？
5. bootstrap中一些可能用到的功能:
   1. 折叠 https://www.w3schools.com/bootstrap/bootstrap_collapse.asp
   2. tabs/pills https://www.w3schools.com/bootstrap/bootstrap_tabs_pills.asp
   3. 
   4. orms https://www.w3schools.com/bootstrap/bootstrap_forms.asp
   5. inputs https://www.w3schools.com/bootstrap/bootstrap_forms_inputs.asp https://www.w3schools.com/bootstrap/bootstrap_forms_inputs2.asp
   6. media https://www.w3schools.com/bootstrap/bootstrap_media_objects.asp
6. 图片一直显示不出来？
   1. settings中的`STATICFILES_DIR`写成`STATICFILES_DIRS`
      1. 更正：这并没有错误
   2. 正确的修改方式是将`STATICFILES_DIRS`中的`os.path.join(BASE_DIR, 'static'),`改成`'static',`
   3. 这似乎是django3的特性，这提示我们遇到问题先找官方文档
7. 关于form
   1. https://www.w3schools.com/html/html_form_attributes_form.asp
   2. https://www.w3schools.com/bootstrap/bootstrap_forms.asp
   3. 鉴定不同表单 https://www.itranslater.com/qa/details/2125175904266617856
   4. https://developer.mozilla.org/zh-CN/docs/learn/Server-side/Django/Forms
8.  deraindop遇到的问题
   1. cuda out of memory 
      1. https://www.huaweicloud.com/articles/3c027240b0b3ecd7c6e4eefaac1dc36e.html
      2. https://segmentfault.com/a/1190000022589080
      3. 解决：添加with torch.no_grad():，pytorch版本过高
9. 这个教程好像不错 https://developer.mozilla.org/zh-CN/
10. https://blog.csdn.net/kuanggudejimo/article/details/82901035