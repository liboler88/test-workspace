import datetime
import sys

def main():
    now = datetime.datetime.now()
    print("================================")
    print(f"🚀 歡迎使用 Test Workspace")
    print(f"📅 現在時間: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python 版本: {sys.version.split()[0]}")
    print("================================")

if __name__ == "__main__":
    main()
