import asyncio
from core.agent_core import CodeOrbitAgent

async def run_demo():
    # 这里的 API Key 在申请通过前可以先留空，或填入 "PENDING_ORBIT_KEY"
    api_key = "PENDING_ORBIT_KEY"
    agent = CodeOrbitAgent(api_key=api_key)
    
    print("--- Code-Orbit 启动成功 ---")
    print("状态: 正在等待 MiMo-V2.5-Pro 算力注入...")
    
    # 模拟一个简单的指令，展示逻辑已跑通
    print("测试指令: 分析当前代码结构并给出优化建议")
    # 此处逻辑会自动调用 agent_core.py 中的方法
    
if __name__ == "__main__":
    try:
        asyncio.run(run_demo())
    except KeyboardInterrupt:
        print("\n程序已手动停止。")
