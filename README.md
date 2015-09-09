# Collect Recaptcha Images

這個專案抓了很多 captcha 來給大家做 training 用，目前還沒加 tag，剛放上去跑。

## 資料來源

1. [上市 - 買賣日報表查詢系統](http://bsr.twse.com.tw/bshtm/)
2. [上櫃 - 券商買賣證券日報表查詢系統](http://www.tpex.org.tw/web/stock/aftertrading/broker_trading/brokerBS.php?l=zh-tw)

## 圖片們

`img` 裡面是上市買賣日報的 captcha 圖， `img2` 是上櫃的。

## TODO

1. 標上 10000 張的結果 (maybe 做個可以標記的頁面上大家反覆確認, build parse database)
2. machine learning or simple OCR approach
3. release api 架在 parse 上 (?)

## 智慧財產權

本專案所有圖片以及資料之智慧財產權由台灣證券交易所擁有，本人只提供程式供大眾作為參考

## 免責聲明

本人旨在為廣大投資人提供正確可靠之資訊及最好之服務，作為投資研究的參考依據，若因任何資料之不正確或疏漏所衍生之損害或損失，本人將不負法律責任。是否經由本網站使用下載或取得任何資料，應由您自行考量且自負風險，因任何資料之下載而導致您電腦系統之任何損壞或資料流失，您應負完全責任。