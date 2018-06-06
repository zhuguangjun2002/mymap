===============================================

--------------------------------
python manage.py dumpdata > chinamobile_all_dump.json
python manage.py loaddata chinamobile_all_dump.json
--------------------------------

# 导出部分应用的数据，如`auth`,`reporter`.
# 然后恢复他们
--------------------------------
python manage.py dumpdata auth > auth_dump.json
python manage.py dumpdata reporter > reporter_dump.json
python manage.py loaddata auth_dump.json
python manage.py loaddata reporter_dump.json
--------------------------------


===============================================
一、简单的数据导出与导入（简单的迁移）
1. django 项目提供了一个导出的方法 `python manage.py dumpdata`, 不指定 `appname` 时默认为导出`所有的app`
--------------------------------
python manage.py dumpdata [appname] > appname_data.json
--------------------------------
比如,我们有一个项目叫 `mysite`, 里面有一个 `app` 叫 `blog` ,我们想导出 `blog` 的`所有数据`

--------------------------------
python manage.py dumpdata blog > blog_dump.json
--------------------------------

2. 数据导入,不需要指定 `appname`

--------------------------------
python manage.py loaddata blog_dump.json
--------------------------------
备注：一些常用的

--------------------------------
python manage.py dumpdata auth > auth.json # 导出用户数据
--------------------------------
优点：可以兼容各种支持的数据库，也就是说，以前用的是 `SQLite3`，可以导出后，用这种方法导入到 `MySQL`, `PostgreSQL`等`数据库`，反过来也可以。
缺点：`数据量`大的时候，`速度`相对较慢，`表`的关系比较`复杂`的时候可以`导入不成功`。
===============================================

二、 用`数据库`自带的`导出导入命令`

假定 `Django` 用的`数据库`名称为 `zqxt`

1. 在 `PostgreSQL` 中：

# 导出数据库 zqxt 到 zqxt.sql 文件中
--------------------------------
pg_dump zqxt > zqxt.sql
--------------------------------

# 导入数据库到 新的服务器
--------------------------------
psql zqxt -f zqxt.sql
--------------------------------

#注意：数据导入导出可能需要`数据库``超级权限`,用 `sudo su postgres` 切换到`数据库超级用户` `postgres`

总结：
其它的数据库，请自行搜索如何导入导出，整个`数据库导出`的好处,就是对`数据之间的关系`处理比较省事，
比如,`自强学堂`里面的很多`教程`，`上一篇`和`下一篇`是`一个一对一的关系`，这样的话用 `python manage.py dumpdata` `无法导出``教程与教程的关系`，但是`数据库整个导出`就没有任何问题，当然也可以写一个`脚本`去`导出关系`再`导入`。
`Django` 自带的 `python manage.py dumpdata` 和 `python manage.py loaddata` 最大的好处就是可以`跨数据库`进行`导入导出`。
===============================================
