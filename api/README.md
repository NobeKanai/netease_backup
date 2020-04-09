# API

目前爬虫尚未开发， 但是可以使用 Binaryify 的 [NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi) 搭建一个临时的api接口

您需要安装docker， 这是必要的， 即使是[app](../app)部分的部署也需要用到<code>docker</code>和<code>docker-compose</code>工具



您可以通过下面的方法启动一个临时的api

## 拉取镜像

```
docker pull binaryify/netease_cloud_music_api
```

## 启动服务

```
docker run -d -p 3000:3000 binaryify/netease_cloud_music_api
```

接下来你可以访问[localhost:3000](http://127.0.0.1:3000)来测试是否成功启动api