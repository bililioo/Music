# Music
> *这是一个使用Python实现的音乐下载网站。*

### 环境要求
* `Python3`
* `MySQL`

Python需要安装包`jinja2`、`aiohttp`、`aiohttp_cors`。

使用以下命令可以安装包：

```bash
$ pip3 install jinja2
$ pip3 install aiohttp
$ pip3 install aiohtt_cors
```
### 运行项目

- 创建本地数据库，在路径下执行以下命令：

    ```$ mysql -u root -p < music.sql ```

- 修改`config_override.py`文件中的配置，可参考`config_default.py`进行修改。

- 执行`music_source.py`将歌曲信息插入`music`表中。
- 执行`app.py`

### 已知问题
1. 不支持自动更新数据库数据；
2. 下载接口不支持断点续传，未能正确展示下载信息。

