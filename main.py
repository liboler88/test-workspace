import datetime
import sys
import io

# 解決 Windows 終端機編碼問題
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():
    now = datetime.datetime.now()
    print("================================")
    print("Welcome to Test Workspace")
    print(f"現在時間: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python 版本: {sys.version.split()[0]}")
    print("================================")

if __name__ == "__main__":
    main()
