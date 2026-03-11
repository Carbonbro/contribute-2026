# NPC Practice Roster

> 專為北科大程式設計研究社 (NTUT NPC) 成員設計的沙盒儲存庫，用於練習開源貢獻流程。

## 目標

透過發起 **Pull Request (PR)** 將你的名字加到名冊中。在這個過程中，你將體驗完整的貢獻者旅程：

1. **Fork** 這個儲存庫到你自己的 GitHub 帳號。
2. 將你的 fork **Clone** 到本地端。
3. **建立分支 (Create a branch)**，進行修改並提交 (commit)。
4. **Push** 回你的 fork 並發起 PR。
5. 觀察在你的 PR 上執行的 **自動化 CI 檢查**。
6. 成功被合併 (merged) — 或者是從**合併衝突 (merge conflict)** 中存活下來。

## 快速開始

請完全照著 [CONTRIBUTING.md](CONTRIBUTING.md) 中的步驟進行 — 整個過程不到 10 分鐘。

## 儲存庫結構

```
contribute-2026/
├── .github/
│   └── workflows/
│       └── format-check.yml   # 自動化格式檢查
├── participants/
│   ├── README.md              # 貢獻者檔案模板
│   └── [YOUR_USERNAME].md       # ← 你要新增的檔案
├── roster.md                  # ← 你要修改的檔案
├── CONTRIBUTING.md            # 提供給貢獻者的逐步教學
└── README.md                  # 本檔案
```

## CI / 自動化檢查

每個 PR 都會觸發 GitHub Actions 的工作流程，用來驗證你的修改內容是否符合規定的格式。  
出現 **綠色勾勾** 代表你的 PR 可以被合併。如果出現 **紅色叉叉**，請重新閱讀 [CONTRIBUTING.md](CONTRIBUTING.md) 並推送修正。

## 屬於北科大 NPC 開源訓練營的一環

這個儲存庫被當作兩堂課程的教學工具：

| 週次 | 主題 | 關鍵活動 |
|------|-------|-------------|
| 1 | 貢獻者旅程 (Contributor's Journey) | 發起你的第一個 PR |
| 2 | 維護者視角 (Maintainer's Perspective) | 解決即時的合併衝突 |

## License

MIT — 歡迎自由 fork、混搭與學習。

詳見 [License](./LICENSE)。