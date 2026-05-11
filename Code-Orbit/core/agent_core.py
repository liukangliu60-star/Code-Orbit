import os
import yaml
import aiohttp

class CodeOrbitAgent:
    def __init__(self, config_path="configs/mimo_config.yaml"):
        # 加载配置
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.api_key = self.config['auth']['api_key']
        self.base_url = self.config['auth']['base_url']
        self.project_context = ""

    async def ingest_repository(self, repo_path):
        """利用 MiMo 的 1M 超长窗口读取项目上下文"""
        print(f"🔍 正在索引项目路径: {repo_path}")
        context_parts = []
        for root, _, files in os.walk(repo_path):
            # 过滤掉不需要读取的文件夹
            if any(x in root for x in ['.git', '__pycache__', 'configs']):
                continue
            for file in files:
                if file.endswith(('.py', '.md', '.txt')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            context_parts.append(f"--- File: {file_path} ---\n{content}\n")
                    except Exception as e:
                        print(f"⚠️ 无法读取文件 {file}: {e}")
        
        self.project_context = "\n".join(context_parts)
        print(f"✅ 上下文装载完毕，共计 {len(self.project_context)} 字符")

    async def execute_task(self, task_description):
        """调用 MiMo-V2.5-Pro 进行逻辑规划与生成"""
        if self.api_key == "PENDING_ORBIT_TOKEN":
            return "⚠️ 错误: 请在 configs/mimo_config.yaml 中填入有效的 MiMo API Key。"

        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "model": self.config['model_settings']['primary_model'],
            "messages": [
                {"role": "system", "content": "你是一个基于小米 Orbit 计划开发的资深架构师智能体。"},
                {"role": "user", "content": f"项目背景:\n{self.project_context}\n\n任务目标: {task_description}"}
            ],
            "temperature": self.config['model_settings']['temperature']
        }

        async with aiohttp.ClientSession() as session:
            async def fetch():
                # 这里模拟实际请求逻辑
                return "MiMo-V2.5-Pro 已接收任务，正在基于 1M 上下文生成方案..."
            
            return await fetch()
