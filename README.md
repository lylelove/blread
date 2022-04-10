![blread](https://socialify.git.ci/lylelove/blread/image?description=1&font=Inter&forks=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F61548984%3Fv%3D4&name=1&owner=1&pattern=Signal&stargazers=1&theme=Light)

# 以哔哩哔哩专栏为后端进行Github Action自动部署的Hexo博客

------

本项目通过Github Action运行python文件，自动爬取哔哩哔哩专栏文章并清洗写入markdown文件中，清洗操作参考了http2text库，并略微进行修改。

在清洗并存储于_post文件夹后通过Github Action自动实现Hexo部署。

------

## 快速开始

### Github Action 相关

Fork本项目，自行修改项目名称。

后修改.github/workflows/main.yml文件：

```
# 这里放环境变量,需要替换成你自己的
env:
  # Hexo 编译后使用此 git 用户部署到 github 仓库
  GIT_USER: lylelove
  # Hexo 编译后使用此 git 邮箱部署到 github 仓库
  GIT_EMAIL: lylelove@163.com
  # Hexo 编译后要部署的 github 仓库
  GIT_DEPLOY_REPO: lylelove/blread
  # Hexo 编译后要部署到的分支
  GIT_DEPLOY_BRANCH: gh_page
  # 注意替换为你的 GitHub 源仓库地址
  GIT_SOURCE_REPO: git@github.com:lylelove/blread.git
  # 哔哩哔哩专栏id
  BILIBILI_MID: 34828543
```

获取部署密钥，具体教程请自行百度Hexo搭建教程

复制**私钥**（.pub）文件内容，在 仓库 `Settings` -> `Secrets` -> `New repository secret` 页面上添加。

1. 在 `Name` 输入框填写 `HEXO_DEPLOY_PRI`
2. 在 `Value` 输入框填写私钥内容

### Hexo相关

自行修改_config.yml文件。

### Github Pages相关

上述步骤均完成后，自行进行第一次Action。

成功运行后开启Pages功能，Source选择gh_page。

------

## 注意事项

哔哩哔哩专栏中删除的文章并没有在GitHub中删除，本项目只是使其在首页中隐藏，若要完全删除需自行在source/_posts中删除。

本项目无法实现哔哩哔哩专栏与Hexo博客同步更新，默认同步时间间隔是两个小时，可在.github/workflows/main.yml中进行修改：

```
schedule:
    - cron: 0 */2 * * * 
```

其他问题请提Issue，欢迎star本项目。

------

请作者喝杯咖啡~

![mm_facetoface_collect_qrcode_1649575198468.png](https://s2.loli.net/2022/04/10/XI7nPMawpL6jWf1.png)

