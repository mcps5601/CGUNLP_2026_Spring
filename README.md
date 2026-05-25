# CGUNLP_2026_Spring

<p align="center">
  <img src="assets/banner.png" alt="自然語言處理與應用" width="100%">
</p>

# 自然語言處理與應用 🧠💬
> 把「文字」變成「可以算、可以學、可以生成」的東西：從詞向量一路到 Transformer / LLM / RAG，以及更現代的 NLP

- 📅 學期：`2026 Spring`
- 🧑‍🏫 授課教師：林英嘉（長庚大學人工智慧學系）
- 🧾 科目代碼：`AIM125` & `HDM014`
- 💻 使用語言：Python (PyTorch / Transformers)
- 🗣️ 授課語言：中文（含部分英文教材）
- [`課程影片 YouTube 播放清單`](https://www.youtube.com/playlist?list=PL0bwsTyVtLVz7p_FSYBS75KnuUh-6QbBy)

---

## 課程進度（16 週）🗓️
> 以實際上課狀況微調；詳細教材與作業說明見各週資料夾。

| Week 🗓️ | Topic 🏫 | Slide 📽️ | Code  | Video 🎬 |
|---:|---|---|---|---|
| 1 | 自然語言處理介紹以及本課程綱要 | [`pdf`](./slides/w1_intro_0223.pdf) [`ppt`](./slides/w1_intro_0223.pptx) |  | [`Video1`](https://youtu.be/cWZ08blKpXM) [`Video2`](https://youtu.be/SaVCTUpCPLU) [`Video3`](https://youtu.be/DL-r6bPDfls) |
| 2 | 文字向量基礎與詞嵌入模型 | [`pdf`](./slides/w2_vectors_0302.pdf) [`ppt`](./slides/w2_vectors_0302.pptx) |  | [`Video1`](https://youtu.be/6S9jGIwlE74) [`Video2`](https://youtu.be/-WOuNRyqW8M) [`Video3`](https://youtu.be/nacFGcUtzps)  |
| 3 | 遞迴神經網路與長短期記憶網路 | [`pdf`](./slides/w3_rnns_0309.pdf) [`ppt`](./slides/w3_rnns_0309.pptx) | [`LSTM`](./code/NN_中文文本分類.ipynb) | [`Video1`](https://youtu.be/M4ft-Z4S0EM) [`Video2`](https://youtu.be/zJoZwHhmzN8) [`Video3`](https://youtu.be/l_dl2_OjuaE)  |
| 4 | 注意力機制與現代字詞分割演算法 | [`pdf`](./slides/w4_attn_subwords_0316.pdf) [`ppt`](./slides/w4_attn_subwords_0316.pptx)  |  [`BPE`](./code/bpe_tutorial.ipynb) | [`Video1`](https://youtu.be/jfCVnbl3XeM) [`Video2`](https://youtu.be/hC9x6-CTilc) [`Video3`](https://youtu.be/Wk2oQWVeNm0)  |
| 5 | Transformer 模型架構介紹 | [`pdf`](./slides/w5_transformer_0323.pdf) [`ppt`](./slides/w5_transformer_0323.pptx)  |  |  [`Video1`](https://youtu.be/zOnPoY-GlaY) [`Video2`](https://youtu.be/jj9zVVvYGs4) [`Video3`](https://youtu.be/Y8Q755ItO7g)  |
| 6 | Encoder-based models | [`pdf`](./slides/w6_bert_0330.pdf) [`ppt`](./slides/w6_bert_0330.pptx)  | [`BERT_QA`](./code/bert_family_qa.ipynb) | [`Video1`](https://youtu.be/DvCNcQb_A0U) [`Video2`](https://youtu.be/8VXh3WqH78I) [`Video3`](https://youtu.be/O36DIJbz9Hk) |
| 7 | 清明連假 |  |  |  |
| 8 | Decoder-based models | [`pdf`](./slides/w8_decoder_0413.pdf) [`ppt`](./slides/w8_decoder_0413.pptx) |  |  [`Video2`](https://youtu.be/ffjatvp7tvQ) [`Video3`](https://youtu.be/LykVppfMF7I) |
| 9 | 期中考 |  |  |  |
| 10 | HuggingFace Tutorial | [`pdf`](./slides/w10_huggingface_0427.pdf) [`ppt`](./slides/w10_huggingface_0427.pptx)  | [`gpt2`](./code/gpt2_summarization.ipynb) [`t5`](./code/t5_summarization.ipynb) |  |
| 11 | LLM-1: LLM Intro and RAG | [`pdf`](./slides/w11_llm_rag_0504.pdf) [`ppt`](./slides/w11_llm_rag_0504.pptx)  |  |  |
| 12 | LLM-2: Evaluations | [`pdf`](./slides/w12_llm2_0511.pdf) [`ppt`](./slides/w12_llm2_0511.pptx)  | [`Qwen3`](./code/qwen3_tutorial.ipynb) |  |
| 13 | LLM-3: Efficient Training | [`pdf`](./slides/w13_llm3_0518.pdf) [`ppt`](./slides/w13_llm3_0518.pptx)  | [`PEFT`](./code/lm_peft.ipynb) |  |
| 14 | State Space Models and Mamba | [`pdf`](./slides/w14_mamba_0525.pdf) [`ppt`](./slides/w14_mamba_0525.pptx)  |  |  |
| 15 | 小組實作成果報告 (1) |  |  |  |
| 16 | 小組實作成果報告 (2) |  |  |  |

## 作業 (Assignments) 📝
| Index | Topic 🏫 | 說明 |Deadline |
|---:|---|---|---|
| 1 | [詞向量與詞嵌入實作](./assignments/assignment_1/) | [`Slide`](https://docs.google.com/presentation/d/18JHMCYYwA4s0VnOkeugiOGX5mfFh6kG29xzv53j3J1A/edit?usp=sharing) |2026-03-23 23:59 |
| 2 | [基於 Transformer 的主題分類器](./assignments/assignment_2/) | [`Slide`](https://docs.google.com/presentation/d/1P3k3GzXGBsROG7oDmEItemrsJT3l4f9U1qr0PLfwLgI/edit?usp=sharing) | 2026-04-12 23:59 |
| 3 | [命名實體辨識](./assignments/assignment_3/) | [`Slide`](https://docs.google.com/presentation/d/1QJ5m0usA7skhqSX143OI6irE2zVY_PUUGiko6qDhWDE/edit?usp=sharing) | 2026-05-03 23:59 |
| 4 | [函數呼叫功能](./assignments/assignment_4/) | [`Slide`](https://docs.google.com/presentation/d/1DYMTWIYCAKHIL9yVS2hLVkrbXhROtJlvXUiR-HFqQKU/edit?usp=sharing) | 2026-05-25 23:59 |

## Term Project (小組專題) 🏆
- Final Project 佔學期總成績 30%
  - [`說明 Slide`](./slides/w8_project_0413.pptx)
  - [`說明 Video`](https://youtu.be/Zapxrvti7oU)

| 查核點 (週次) | 對象: 繳交內容 | 分數佔比 |
|---|---|---|
| Checkpoint1 (Week 12) | All teams: 進度報告 PPT (5 pages)檔案 | 5% |
| Checkpoint2 (Week 14) | All teams: 進度報告 PPT (5+5 pages*)檔案<br>Selected teams: 取5組 (1題目1組) 於課堂中報告，1組10min，此週報告組別得 Checkpoint1 和 Checkpoint2 滿分 | 5% |
| Checkpoint3 (Week 15-16) | All teams: 最終口頭報告 | 10% |
| Checkpoint4 (Week 16-17) | All teams: 書面報告檔案 | 10% |

*繼承Checkpoint1內容+實作
