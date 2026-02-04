# 🧪 Test Workspace

[![Python](https://img.shields.io/badge/Python-3.14.2-blue.svg)](https://www.python.org/)
[![Manager](https://img.shields.io/badge/Manager-uv-orange.svg)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

一個極致簡潔且穩定的 Python 專案範本，專為 Windows 環境與現代開發流程優化。整合了 [uv](https://github.com/astral-sh/uv) 套件管理器，提供隨插即用的開發體驗。

## 🌟 特色

- **極速環境管理**: 使用 `uv` 取代傳統 `pip`，同步速度提升 10 倍以上。
- **Windows 優化**: 內建終端機編碼修正（`sys.stdout` 重新包裝），完美解決繁體中文環境下的 `UnicodeEncodeError`。
- **一致性保證**: 透過 `.python-version` 與 `uv.lock` 鎖定運行環境，確保「在我這能跑，你那也能跑」。

## 🚀 快速開始

### 前置需求

必須安裝 [uv](https://github.com/astral-sh/uv)。若尚未安裝，請以系統管理員權限執行：

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 安裝與運行

1. **複製專案並進入目錄**
   ```bash
   git clone https://github.com/liboler88/test-workspace.git
   cd test-workspace
   ```

2. **建立虛擬環境並同步依賴**
   ```bash
   uv sync
   ```

3. **直接執行**
   ```bash
   uv run main.py
   ```

## 📂 檔案結構說明

| 檔案名稱 | 用途說明 |
| :--- | :--- |
| `main.py` | **核心進入點**。包含時間顯示與 Windows 編碼修正邏輯。 |
| `pyproject.toml` | **專案定義檔**。定義名稱、版本、Python 要求及依賴。 |
| `uv.lock` | **版本鎖定檔**。確保所有環境安裝的套件版本一致。 |
| `.python-version` | 指名此專案專用的 Python 版本 (`3.14.2`)。 |
| `.venv/` | 虛擬環境目錄。由 `uv` 自動管理（已在 Git 中忽略）。 |

## 🚢 生產環境與打包

### 1. 打包為獨立執行檔 (.exe)
適合分發給未安裝 Python 的使用者：
```bash
# 安裝打包工具
uv add --dev pyinstaller

# 生成單一 EXE 檔案
uv run pyinstaller --onefile main.py
```
輸出結果位於 `dist/main.exe`。

### 2. Docker 容器部署
```dockerfile
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY . .
RUN uv sync --frozen
CMD ["uv", "run", "main.py"]
```

## 🛠️ 開發常用指令

- **新增套件**: `uv add <package_name>`
- **進入虛擬環境**: `source .venv/bin/activate` (或 Windows: `.venv\Scripts\activate`)
- **檢查目前安裝**: `uv tree`

---
Developed by **[liboler88](https://github.com/liboler88)**
