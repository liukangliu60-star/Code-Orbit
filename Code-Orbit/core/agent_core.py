import asyncio
import os
from mimo_sdk import MiMoClient

class CodeOrbitAgent:
    def __init__(self, api_key):
        # 接入 MiMo-V2.5-Pro 模型
        self.client = MiMoClient(api_key=api_key, base_url="https://api.xiaomimimo.com/v2.5")
        self.project_context = ""

    async def ingest_repository(self, repo_path):
        """
        利用 MiMo 的 1M 超长上下文，读取整个代码库
        """
        print(f"🔍 正在收割项目上下文: {repo_path}")
        context_stream = []
        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(('.py', '.md')):
                    with open(os.path.join(root, file), 'r') as f:
                        context_stream.append(f"--- File: {file} ---\n{f.read()}\n")
        
        self.project_context = "\n".join(context_stream)
        print(f"✅ 上下文装载完毕，共计 {len(self.project_context)} 字符")

    async def plan_and_execute(self, task_description, image_path=None):
        """
        核心 Agent 逻辑：规划 + 生成
        """
        prompt = f"""
        你是一个基于小米 Orbit 计划开发的资深架构师智能体。
        
        【项目上下文】:
        {self.project_context[:500000]} # 假设读取前 50w 字符
        
        【用户任务】:
        {task_description}
        
        请根据上下文和任务，给出详细的架构修改方案并生成核心代码。
        """

        # 如果有架构图，调用全模态接口
        messages = [{"role": "user", "content": prompt}]
        if image_path:
            messages.append({"role": "user", "content": {"type": "image", "path": image_path}})

        print("🚀 MiMo-V2.5-Pro 正在思考规划中...")
        response = await self.client.chat.completions.create(
            model="mimo-v2.5-pro",
            messages=messages,
            temperature=0.2 # 保持代码生成的严谨性
        )
        
        return response.choices[0].message.content

# --- 使用示例 ---
async def main():
    # 填入你未来领到的 API Key
    agent = CodeOrbitAgent(api_key="MIMO_ORBIT_XXXX_XXXX")
    
    # 1. 读取本地项目
    await agent.ingest_repository("./my_awesome_app")
    
    # 2. 提出开发需求（可结合架构图）
    result = await agent.plan_and_execute(
        task_description="请根据现有代码风格，在接口层增加一个支持异步 Webhook 回调的模块。",
        image_path="./architecture_v2.png"
    )
    
    print("\n--- Code-Orbit 生成方案 ---\n")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())