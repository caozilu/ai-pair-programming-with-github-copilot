# AI Pair Programming with GitHub Copilot - Expense Calculator

A Django-based expense tracking application developed with AI pair programming assistance.

## 项目概述

这是一个使用Django框架开发的费用计算器应用，包含以下功能：
- 费用记录管理
- 数据统计与分析
- RESTful API接口

## 环境要求

- Python 3.6+
- Django 3.2.8

## 安装指南

1. 克隆项目仓库
```bash
git clone https://github.com/caozilu/ai-pair-programming-with-github-copilot.git
```

2. 进入项目目录
```bash
cd ai-pair-programming-with-github-copilot/expense_calculator
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 数据库迁移
```bash
python manage.py migrate
```

## 运行项目

启动开发服务器：
```bash
python manage.py runserver
```

访问地址：http://localhost:8000

## 使用说明

1. 管理员界面
- 访问/admin使用内置管理后台
- 默认管理员账号：admin/admin

2. API接口
- 所有API端点位于/api/路径下
- 使用DRF提供的Web界面进行测试

## 项目结构

```
expense_calculator/
├── expense_calculator/    # Django项目核心
├── expenses/             # 费用管理应用
├── templates/            # 前端模板
├── manage.py             # 管理脚本
└── requirements.txt      # 依赖列表
```

## 贡献指南

1. Fork项目
2. 创建特性分支
3. 提交Pull Request

## 许可证

MIT License