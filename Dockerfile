# 1. ベースとなるOSとPythonのバージョンを指定（軽量なslim版を使用）
FROM python:3.12-slim

# 2. コンテナ内の作業ディレクトリを /app に設定
WORKDIR /app

# 3. ホスト（手元のPC）の requirements.txt をコンテナにコピー
COPY requirements.txt .

# 4. コンテナ内で必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# 5. プロジェクトのファイル一式をコンテナにコピー
COPY . .

# 6. コンテナが起動した時に実行するコマンド
CMD ["python", "hello_quants.py"]
