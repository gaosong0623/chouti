from django.db import models

class SendMsg(models.Model):
    #primary_key：主键        AutoField：自增
    nid = models.AutoField(primary_key=True)
    #CharField：字符型字段   必需参数：max_length 规定最大长度
    code = models.CharField(max_length=6)
    #EmailField可能会报错，所以继续CharField，db_index=True：创建索引
    email = models.CharField(max_length=32, db_index=True)
    #IntegerField：整型字段  default：默认值
    times = models.IntegerField(default=0)
    #DateTimeField：日期和时间字段
    ctime = models.DateTimeField()


class UserInfo(models.Model):
    #用户表
    #自增主键
    nid = models.AutoField(primary_key=True)
    #字符串，unique=True：唯一
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField()
