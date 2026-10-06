# mend_test

Mend CLI のスキャンを練習するための使い捨てプロジェクト。

**注意：requirements.txt は既知の脆弱性がある古いバージョンをわざと固定している。**
本番コードやテンプレートとして流用しないこと。

## 使い方

```bash
# 依存をローカルに解決（スキャン精度のため）
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# ログイン（初回のみ・ブラウザ認証）
mend auth login

# ローカルでスキャン（結果は画面に出るだけ）
mend dep

# デモ組織に結果を登録
mend dep --update --scope "G-Gravity_Demo//Arisa-Test//mend_test"
```

## 練習の流れ

1. スキャンして Vulnerabilities 一覧を見る（CVE・CVSS・EPSS）
2. どれから直すか優先順位を考える
3. requirements.txt のバージョンを修正版に上げる
4. 再スキャンして検出数が減ることを確認する
