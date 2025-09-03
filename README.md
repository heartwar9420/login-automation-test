# Python 自動化登入測試 (QA Demo Project)

這是一個簡單的自動化測試專案，使用 **Python + Selenium + pytest** 實作，  
模擬使用者登入網站，並驗證登入結果是否正確。  
此專案示範了 **QA 自動化測試** 的基本流程，適合作為新手作品集展示。

測試網站來源：[The Internet - Login Page](https://the-internet.herokuapp.com/login)

## 功能
- 測試成功登入 (正確帳密)
- 測試失敗登入 (錯誤帳密)
- 測試空白登入 (邊界案例)
- 產生 HTML 測試報告 (pytest-html)

---

##  執行方式

1. 下載或 clone 專案
```bash
git clone https://github.com/你的帳號/python-login-automation-test.git
cd python-login-automation-test
````

2. 安裝套件

pip install -r requirements.txt

3. 執行測試

python -m pytest -v main.py

4.  產生 HTML 測試報告

python -m pytest -v main.py --html=report.html


---

##HTML 測試報告

![pytest html report](images/report.jpg)


