# mend_test

Mend CLI のスキャンを練習するための使い捨てプロジェクト。
「1フォルダ＝1アプリ」構成で、言語ごとに検出のされ方を比較できる。

**注意：各アプリの依存は既知の脆弱性がある古いバージョンをわざと固定している。**
本番コードやテンプレートとして流用しないこと。

## 構成

| フォルダ | 言語 / マニフェスト | 入れてある代表的な脆弱性 |
|---|---|---|
| `python-flask-app/` | Python / requirements.txt | Flask 2.0.1, requests 2.25.1, PyJWT 1.7.1 など |
| `node-express-app/` | Node.js / package.json | lodash 4.17.15（プロトタイプ汚染）, axios 0.21.0（SSRF）, minimist 1.2.0 など |
| `java-maven-app/` | Java / pom.xml | log4j-core 2.14.1（**Log4Shell CVE-2021-44228**）, jackson-databind 2.9.10.4, commons-text 1.9（Text4Shell） |
| `go-app/` | Go / go.mod | jwt-go v3.2.0（CVE-2020-26160）, golang.org/x/text v0.3.5, gin v1.6.3 |

各アプリは依存を実際に import する最小コード付き（Reachability分析の対象になるようにするため）。

## 事前準備（依存をローカルに解決しておくとスキャン精度が上がる）

```bash
# Python
cd python-flask-app && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && cd ..

# Node.js
cd node-express-app && npm install && cd ..

# Java（Maven が必要： brew install maven）
cd java-maven-app && mvn -q dependency:resolve && cd ..

# Go
cd go-app && go mod download && cd ..
```

## スキャン手順

```bash
# ログイン（初回のみ・ブラウザ認証）
mend auth login

# リポジトリルートでまとめてスキャン（結果は画面に出るだけ）
mend dep

# デモ組織に結果を登録
mend dep --update --scope "G-Gravity_Demo//Arisa-Test//mend_test"
```

フォルダごとに別プロジェクトとして登録したい場合は、各フォルダに移動して
`--scope "G-Gravity_Demo//Arisa-Test//<フォルダ名>"` を付けて実行する。

## 練習の流れ

1. スキャンして Vulnerabilities 一覧を見る（CVE・CVSS・EPSS）
2. 言語ごとの検出のされ方（直接依存・間接依存）を比較する
3. どれから直すか優先順位を考える（例：Log4Shell は CVSS 10.0 かつ KEV 掲載）
4. マニフェストのバージョンを修正版に上げる
5. 再スキャンして検出数が減ることを確認する
