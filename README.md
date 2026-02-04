# 🧪 Test Workspace

一個基於 [uv](https://github.com/astral-sh/uv) 構建的簡潔 Python 專案範本。

## 🚀 快速開始

### 前置需求

請確保已安裝 `uv`。如果尚未安裝，可以使用以下指令：

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 安裝步法

1. **複製專案**
   ```bash
   git clone https://github.com/liboler88/test-workspace.git
   cd test-workspace
   ```

2. **同步環境**
   ```bash
   uv sync
   ```

### 執行程式

```bash
uv run main.py
```

## 📂 專案結構

- `main.py`: 專案主要入口點。
- `pyproject.toml`: 專案配置與依賴定義。
- `uv.lock`: 鎖定依賴版本，確保環境一致性。

## 🛠️ 開發說明

本專案使用 `uv` 進行管理，這是一個極速的 Python 套件與環境管理器。

- **新增依賴**: `uv add <package>`
- **執行測試**: 目前尚未建立測試腳本。

## 🚢 部署與發佈 (Deployment & Distribution)

### 1. 打包為執行檔 (Standalone Executable)

如果你需要將程式交給沒有安裝 Python 環境的使用者，可以將其打包：

```bash
# 安裝開發依賴
uv add --dev pyinstaller

# 執行打包 (Windows 會產出 .exe)
uv run pyinstaller --onefile main.py
```
執行檔將位於 `dist/main.exe`。

### 2. Docker 容器化

```dockerfile
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY . .
RUN uv sync --frozen

CMD ["uv", "run", "main.py"]
```

### 3. GitHub Actions CI/CD

建立 `.github/workflows/deploy.yml`：

```yaml
name: CI
on: [push]
jobs:
  run-app:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install uv
        uses: astral-sh/setup-uv@v5
      - name: Run logic
        run: uv run main.py
```

---
Created by [liboler88](https://github.com/liboler88)
