# APP
APP 是项目的核心部分， 主要负责定时检测和写入数据库

## 使用方法

您需要在本目录下创建一个 <code>.env</code> 文件，并提供环境变量<code>DATABASE_URL</code>


例如
```
DATABASE_URL=mysql+pymysql://root:password@localhost/kanai?charset=utf8mb4
```
这不是必要的， 但是使用默认的sqlite数据库在更新alembic的script时可能会出现奇怪的问题


然后安装依赖并初始化数据库
```
pip install -r requirements.txt
alembic upgrade head
```


最后， 执行下面内容来将您的歌单实例化到本地吧
```
python main.py -id xxxxxxx
```
TIP: <code>xxxxxxx</code> 指网易云音乐歌单id

您可以使用下面的命令获取详细的使用方法
```
python main.py --help
```

尽管目前的参数只有一个