# Code-Orbit: 基于 MiMo-V2.5 的自动化研发智能体

## 🚀 项目简介
Code-Orbit 是专为小米 “百万亿 Token 创造者激励计划” 开发的下一代研发助手。它深度集成 MiMo-V2.5 系列大模型，旨在通过超长上下文和全模态能力，解决复杂项目中的代码审计、架构解析与任务规划。

## ✨ 核心特性
- **项目级上下文感知**：利用 MiMo 1M 超长窗口，实现对整个代码仓库的深度理解。
- **多模态架构解析**：支持通过架构图（Vision）直接生成基础代码框架。
- **异步 Agent 架构**：基于 `asyncio` 构建，支持高并发的代码扫描与生成任务。

## 📁 文件结构
- `main.py`: 程序启动入口。
- `core/agent_core.py`: 核心智能体逻辑，封装了 MiMo-V2.5-Pro 的调用链路。
- `configs/mimo_config.yaml`: API 与模型参数配置。
- `requirements.txt`: 环境依赖项。

## 🛠️ 快速开始
1. 安装依赖：`pip install -r requirements.txt`
2. 配置 API Key：在 `mimo_config.yaml` 中填入你的 MiMo Orbit API Key。
3. 运行：`python main.py`

## 🎯 接入计划
本项目目前正处于原型测试阶段，计划在获得 Orbit 计划的 **Max Plan (16亿 Tokens)** 支持后，进行百万行级别代码库的压力测试，并探索与 OpenCode 生态的深度集成。