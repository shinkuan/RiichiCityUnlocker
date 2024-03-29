<br/>
<p align="center">
  <h1 align="center">麻雀一番街解鎖</h3>

  <p align="center">
Riichi City Unlocker<br>
基於MITM攻擊來解鎖全腳色、造型、物品<br>
    <br/>
    <br/>
    <br/>
    <br/>
    <a href="https://github.com/shinkuan/RiichiCityUnlocker/issues">Report Bug</a>
    .
    <a href="https://github.com/shinkuan/RiichiCityUnlocker/issues">Request Feature</a>
  </p>
</p>

# About The Project

https://github.com/shinkuan/RandomStuff/assets/35415788/2b364ad2-08ee-49c5-b67e-fce1aa862088


# Usage

## Basic usage

- 在使用這個MITM腳本之前，你應該知道要如何透過類似Proxifier之類的工具，將麻雀一番街的連線導向到mitmproxy。
- 如果你不知道該怎麼做，以下是簡短教學：
  - 下載並開啟Proxifier
  - 新增一個Proxy Server，IP: 127.0.0.1；PORT: 依你喜好
  - 新建一個Proxification Rule，選擇將Riichi City應用的連線導向到剛剛新建的Proxy Server

1. `git clone this`
2. Change the directory in [generateUserItemList.py:442](https://github.com/shinkuan/RiichiCityUnlocker/blob/9d794befa1b311458305d5a44810009c437cd01f/generateUserItemList.py#L442)
3. `cd RiichiCityUnlocker`
4. `python -m venv venv`
5. `venv\Scripts\activate.bat`
6. `pip install -r requirements.txt`
7. `mitmdump -s unlocker.py -p <PORT>`

## 聲明

本腳本僅供學習參考交流，請使用者於下載24小時內自行刪除，不得用於商業用途，否則後果自負。

此插件僅供學習參考交流，請使用者於下載24小時內自行刪除，不得用於商業用途，否則後果自負。

此插件僅供學習參考交流，請使用者於下載24小時內自行刪除，不得用於商業用途，否則後果自負。

### 警告：

雀魂遊戲官方可能會偵測並封號！

如產生任何後果與作者無關！

使用本腳本則表示同意此條款！

# TODO
 - [ ] 確保傳送到Server端的資料沒有使用Unlocker的跡象
 - [ ] 建立完整的物品表 __(Need Help)__
 - [ ] 還是有很多Bug

# Authors

* **Shinkuan** - [Shinkuan](https://github.com/shinkuan/)

## Support me

留個星星就可以啦
有問題可到 [Discord](https://discord.gg/Z2wjXUK8bN) 找我

# See Also

## [Akagi](https://github.com/shinkuan/Akagi)
![image](https://github.com/shinkuan/RandomStuff/assets/35415788/4f9b2e2f-059e-44a8-b11a-5b2ce28cb520)

## [MajsoulUnlocker](https://github.com/shinkuan/MajsoulUnlocker)

https://github.com/shinkuan/RandomStuff/assets/35415788/e5371e99-7c43-479f-adb6-c950dbac6a4d
