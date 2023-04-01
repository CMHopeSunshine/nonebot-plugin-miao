<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-miao

_✨ 让Bot的发言添加一些奇怪的口癖! ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/CMHopeSunshine/nonebot-plugin-miao.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-miao">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-miao.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

通过on_calling_api钩子，给你的Bot的纯文本发言添加一些奇怪的口癖(。

## 💿 安装

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```shell
nb plugin install nonebot-plugin-miao
```

## ✨ 例子
以内置的echo插件(作用是复读你的话)为例
```
- /echo 诶嘿
- 诶嘿喵

- /echo 诶呦你干嘛
- 诶呦你干嘛旺
```

## 🔧 配置项

在你的bot的配置文件(.env.*)中添加以下配置项(不区分大小写)

|       配置项        |    默认值     |                     说明                      |
|:----------------:|:----------:|:-------------------------------------------:|
|    miao_words    | ["喵", "旺"] |                    口癖词列表                    |
| miao_probability |    0.5     |                   添加口癖的概率                   |
|  miao_position   |    end     | 添加口癖的位置，可选start(开头)、end(结尾)、random(句子中随机位置) |
|    miao_count    |     1      |                  最多添加的词数量                   |

## 💝 鸣谢

- [Nonebot](https://github.com/nonebot/nonebot2): 本项目的基础，非常好用的聊天机器人框架。
