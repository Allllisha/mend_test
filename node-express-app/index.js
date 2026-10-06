/**
 * Mendスキャン練習用の小さなWebアプリ。
 * package.json の古いライブラリを実際に require して使うことで、
 * Reachability（脆弱なコードに到達するか）の分析対象になるようにしている。
 * 動かすことが目的ではなく、スキャンされることが目的。
 */

const express = require("express");
const _ = require("lodash");
const axios = require("axios");
const minimist = require("minimist");
const fetch = require("node-fetch");
const jwt = require("jsonwebtoken");
const ejs = require("ejs");

const SECRET = "practice-secret"; // 練習用。実案件ではコードに書かない

const app = express();
const args = minimist(process.argv.slice(2));

app.get("/", async (req, res) => {
  const url = req.query.url || "https://example.com";
  const resp = await axios.get(url, { timeout: 5000 });
  const merged = _.merge({}, { status: resp.status }, req.query);
  const html = ejs.render("<h1>Mend scan practice</h1><p>status: <%= status %></p>", merged);
  res.send(html);
});

app.get("/fetch", async (req, res) => {
  const resp = await fetch(req.query.url || "https://example.com");
  res.json({ status: resp.status });
});

app.get("/token", (req, res) => {
  const token = jwt.sign({ user: "arisa" }, SECRET, { algorithm: "HS256" });
  res.json({ token });
});

app.listen(args.port || 3000);
