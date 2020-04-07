# Netease Cloud Song List Backup

用来备份网易云歌单， 防止因网易云版权丢失导致歌单歌曲丢失。

**项目正在开发阶段**

### 构思:
- API: 爬虫， 爬取网易云音乐歌单具体数据并提供响应的接口(目前只需要提供两个接口)
- APP: 主程序， 定时同步歌单(只增加不减少)到内存(一个list，只储存歌曲的id)
， 每次更新(如果出现新增单曲)，就触发本地化函数储存到Mysql数据库
- WEB: 一个web程序(RESTFUL API)， 提供查看歌单列表
- FRONTEND: 前端...可选