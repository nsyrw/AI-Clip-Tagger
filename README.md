# AI-Clip-Tagger

画像から自動タグ生成と類似画像検索を行うAIシステムです。

以下のAIモデルを組み合わせて実装しています。

CLIP : 画像特徴量抽出
WD14 Tagger : アニメ画像タグ生成
FAISS : 類似画像検索

画像をアップロードすると次の処理を行います。

1. WD14 によるタグ生成
2. CLIP による特徴量抽出
3. FAISS による類似画像検索

---

# 機能

## 1. 画像タグ生成

WD14 Tagger を使用して
画像のタグを自動生成します。

例

```
input image → tags

1girl
blue hair
smile
long hair
```

---

## 2. 類似画像検索

CLIP で画像特徴量を生成し、
FAISS で高速検索を行います。

例

```
query image

↓

similar images

image1.png
image3.png
image7.png
```

---

# 起動時処理

サーバ起動時に次の処理を自動実行します。

```
dataset フォルダの画像
↓
CLIP特徴量生成
↓
FAISS index 作成
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

# モデル配置

以下のページからモデルをダウンロードします。

```
https://huggingface.co/SmilingWolf/wd-v1-4-convnext-tagger-v2/tree/main
```

次のファイルを `models` フォルダに配置してください。

```
model.onnx
selected_tags.csv
```

---

# dataset

類似検索対象の画像を
`dataset` フォルダに配置してください。

例

```
dataset/
image1.png
image2.png
image3.png
```

---

# サーバ起動

```
uvicorn app:app --reload
```

起動後、以下の URL で API をテストできます。

```
http://127.0.0.1:8000/docs
```

---

# API

## 画像解析

```
POST /analyze
```

### request

```
image file
```

### response

```json
{
  "tags": [
    "1girl",
    "smile",
    "blue hair"
  ],
  "similar_images": [
    "image1.png",
    "image3.png"
  ]
}
```

---

# 使用モデル

WD14 Tagger

Copyright (c) SmilingWolf

モデルは再配布せず、
ユーザーがダウンロードして配置する形式を採用しています。
