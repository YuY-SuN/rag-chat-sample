#!/bin/bash

# データベースファイル名の定義
DATABASE="chat-history.db"

# 既存のデータベースファイルがある場合は削除
if [ -f "$DATABASE" ]; then
    echo "既存のデータベースファイルが見つかりました: $DATABASE"
    echo "終了します。"
    exit 0
fi

# SQLファイルを使用してデータベースとテーブルを作成
echo "データベースとテーブルを作成中..."
sqlite3 $DATABASE < db/create_tables.sql

# 確認メッセージ
if [ -f "$DATABASE" ]; then
    echo "データベースが作成されました: $DATABASE"
    exit 0
else
    echo "データベースの作成に失敗しました"
    exit 1
fi

