"""
fc_utils.py — Function Calling 作業共用工具（學生不需要修改此檔）

提供：
  - call_llm(messages)       → 呼叫 Groq LLM 並回傳純文字
  - parse_json_output(text)  → 從模型輸出抓出一個 JSON 物件
  - lookup_db(section, key)  → 從 mock_data 查表（支援大小寫與中文別名）
  - load_db(path)            → 載入 mock_data.json
  - run_tests(run_agent, db) → 跑 5 題並輸出 fc_log.json
"""

import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
_client = None


def set_model(name: str) -> None:                                                                                                                          
    global GROQ_MODEL                                                                                                                                      
    GROQ_MODEL = name


def _get_client() -> Groq:
    global _client
    if _client is None:
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key or api_key == "這裡是你的API_KEY":
            raise RuntimeError(
                "找不到 GROQ_API_KEY，請先在 .env 中填入 Groq API Key。"
            )
        _client = Groq(api_key=api_key)
    return _client


def call_llm(messages: list[dict], max_tokens: int = 512, temperature: float = 0.0) -> str:
    """呼叫 Groq LLM，回傳模型輸出的純文字。"""
    resp = _get_client().chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message.content


def parse_json_output(text: str) -> dict:
    """
    從模型輸出抓出一個 JSON 物件，容錯處理：
      1. 去除 <think>...</think> 思考區塊（Qwen3 / DeepSeek 用）
      2. 去除 markdown code block (```json ... ```)
      3. 用 greedy 正則抓最外層 { ... } 並 json.loads
      4. 全部失敗 → 回 {"final": <原文>}
    """
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    text = re.sub(r"```(?:json)?\s*", "", text)
    text = text.strip().rstrip("`").strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)  # greedy：抓最外層
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    return {"final": text}


def lookup_db(section: dict, key: str):
    """從 section 的 data + aliases 兩層查 key（不分大小寫，支援中文別名）。"""
    data = section.get("data", {})
    aliases = section.get("aliases", {})

    if key in data:
        return data[key]

    key_upper = key.upper()
    for k, v in data.items():
        if k.upper() == key_upper:
            return v

    canonical = aliases.get(key)
    if canonical and canonical in data:
        return data[canonical]

    return None


def load_db(path: str = "mock_data.json") -> dict:
    """載入 mock_data.json。"""
    return json.loads(Path(path).read_text(encoding="utf-8"))


# ── 正式測驗（共 5 題，滿分 100 分）────────────────────────────────
FIXED_QUERIES = [
    {"Q": "Q1", "query": "請問蘋果公司(AAPL)目前的股價是多少？"},
    {"Q": "Q2", "query": "台北(Taipei)現在的天氣如何？"},
    {"Q": "Q3", "query": "請給我最新的科技(tech)新聞"},
    {"Q": "Q4", "query": "請問微軟(MSFT)的股價是多少？"},
    {"Q": "Q5", "query": "你好！請問你是什麼人工智慧模型？"},
]


def run_tests(run_agent_fn, db: dict, output_file: str = "fc_log.json") -> list[dict]:
    """
    依序跑 5 題，把每題的 model_call / final_answer 寫進 fc_log.json。

    Args:
        run_agent_fn: 學生在 notebook 中定義的 run_agent(query, db) 函式
        db: 載入的 mock_data 字典
        output_file: 輸出檔名

    Returns:
        results 列表（也會寫入 fc_log.json）
    """
    print(f"使用模型：{GROQ_MODEL}\n")

    results = []
    for item in FIXED_QUERIES:
        print(f"  {item['Q']}：{item['query']}")
        try:
            result = run_agent_fn(item["query"], db)
        except Exception as e:
            result = {"model_call": "Error", "final_answer": f"執行錯誤：{e}"}

        results.append({
            "Q": item["Q"],
            "query": item["query"],
            "model_call": result.get("model_call", ""),
            "final_answer": result.get("final_answer", ""),
        })

    log_data = {"model": GROQ_MODEL, "results": results}
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 完成，結果已寫入 {output_file}（共 {len(results)} 題）")
    return results
