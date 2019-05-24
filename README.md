### 定时任务

> 通过定时任务可以进行添加你的定时任务



#### 1.1 定时任务特点

- restful api 简单易定制
- 可接入可视化界面操作
- 定时任务统一管理
- 完全兼容 crontab
- 支持秒级定时任务
- 任务可搜索、暂停、编辑、删除



#### 1.2 用户使用说明

- 新增任务
  - job_id： 任务名称，建议为有意义的英文名称
  - 可执行命令： `Linux Bash` 命令，亦可将可执行程序放入指定的目录（使用docker 切记安装依赖）
  - 任务定时器： （秒、分、时、日、月、周）
    - 示例：每分钟的第20秒开始执行`pwd`命令

![](./doc/images/timed_task01.png)



- 编辑任务

![](./doc/images/timed_task02.png)



- 暂停恢复
  - 状态栏可以将任务暂停/恢复

![](./doc/images/timed_task03.jpg)



- 任务日志
  - 每条任务执行都会记录日志
  - 日志可根据Job_id、状态、关键字、时间范围等搜索

![timed_logs](./doc/images/timed_logs.jpg)

###  部署文档

> <font size="4" color="#dd0000">本服务只能启用一个进程</font> 
#### 创建数据库
```sql
create database `codo_cron` default character set utf8mb4 collate utf8mb4_unicode_ci;
```

#### 一、docker-compose 安装（推荐）

- 修改settings 配置 主要是MySQL数据库配置
- 执行 docker build . -t codo_cron_image
- docker-compose up -d
- 启动成功默认地址为 ip:9900

#### 二、本地安装

> 建议使用虚拟环境
> 具体参考Dockerfile 内的安装步骤
- 修改配置文件
- 安装依赖 
- - pip3 install --user --upgrade pip
- - pip3 install -U git+https://github.com/ss1917/ops_sdk.git
- - pip3 install -r /var/www/do_cron/doc/requirements.txt
- 从doc目录获取supervisor配置文件  使用 supervisor启动  supervisorctl restart 

#### 三、api文档 暂无

#### 四、服务注册（如果需要结合权限则需要注册）
> 示例
```
rewrite_conf = {
    [gw_domain_name] = {
        rewrite_urls = {
            {
                uri = "/cron",
                rewrite_upstream = "10.2.2.236:9900"
            },
            {
                uri = "/mg",
                rewrite_upstream = "mg.opendevops.cn:8010"
            },
            {
                uri = "/accounts",
                rewrite_upstream = "mg.opendevops.cn:8010"
            },
        }
    }
}
```

## License

Everything is [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

