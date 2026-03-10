# AI-Clip-Tagger

画像から自動タグ生成と類似画像検索を行うAIシステムです。

以下のAIモデルを組み合わせて実装しています。

```
CLIP : 画像特徴量抽出
WD14 Tagger : 画像タグ生成
FAISS : 類似画像検索
```

画像をアップロードすると次の処理を行います。

```
1. WD14によるタグ生成
2. CLIPによる特徴量抽出
3. FAISSによる類似画像検索
```

---

# 機能

<img width="1517" height="805" alt="2026031001" src="https://github.com/user-attachments/assets/27e84294-d8c4-4636-85ce-b3dca65bb305" />
<img width="1532" height="712" alt="2026031002" src="https://github.com/user-attachments/assets/c330a13e-4d7b-4713-af29-7d90a3405ebd" />

## 1. 画像タグ生成

WD14 Taggerを使用して
画像のタグを自動生成します。

---

## 2. 類似画像検索

CLIPで画像特徴量を生成し、
FAISSで高速検索を行います。

---

# 起動時処理

サーバ起動時に次の処理を自動実行します。

```
datasetフォルダの画像
↓
CLIP特徴量生成
↓
FAISS index作成
↓
embeddings/index.faiss
```

---

# セットアップ

## 1. リポジトリ取得

```
git clone https://github.com/yourname/AI-Image-Tagger.git
cd AI-Image-Tagger
```

---

## 2. 仮想環境

```
python -m venv venv
```

### Linux / Mac

```
source venv/bin/activate
```

### Windows

```
venv\Scripts\activate
```

---

## 3. 依存ライブラリ

```
pip install -r requirements.txt
```

---

## 4. フォルダ作成

次のファイルを`AI-Clip-Tagger`フォルダに作成してください。
```
models
uploads
embeddings
dataset
```

---

# モデル配置

以下のページからモデルをダウンロードします。

```
https://huggingface.co/SmilingWolf/wd-v1-4-convnext-tagger-v2/tree/main
```

次のファイルを`models`フォルダに配置してください。

```
model.onnx
selected_tags.csv
```

---

# dataset

類似検索対象の画像を`dataset`フォルダに配置してください。

例

```
test1.png
test2.png
test3.png
```

---

# サーバ起動

```
uvicorn app:app --reload
```

起動後、以下のURLでAPIをテストできます。

```
http://127.0.0.1:8000/docs
```

---

# 使用モデル

WD14 Tagger

Copyright (c) SmilingWolf

モデルは再配布せず、
ユーザーがダウンロードして配置する形式を採用しています。
