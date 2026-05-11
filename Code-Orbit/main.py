import asyncio
import sys
from core.agent_core import CodeOrbitAgent

async def main():
    print("🚀 Code-Orbit 智能体启动中...")
    
    # 1. 初始化 Agent
    agent = CodeOrbitAgent()
    
    # 2. 自动读取当前项目作为上下文（展示超长上下文处理能力）
    await agent.ingest_repository(".")
    
    # 3. 模拟执行一个研发任务
    task = "分析当前项目的 core/agent_core.py，建议如何增加对 MiMo 视觉模态接口的支持。"
    
    print(f"\n💬 正在处理任务: {task}")
    result = await agent.execute_task(task)
    
    print("\n--- MiMo 返回结果 ---")
    print(result)
    print("\n✅ 演示运行结束。")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
