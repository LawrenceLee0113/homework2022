# zigyabqsyqpydety
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from itertools import count
import smtplib

import json

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "CSIEJAR ID重設密碼"  #郵件標題
content["from"] = "csiejarjar@gmail.com"  #寄件者
content["to"] = "example@gmail.com" #收件者
content.attach(MIMEText("Demo python send email"))  #郵件內容

class mail():
    def __init__(self,title="this is title",text="this is content"):
        self.sender = "lawrencelee0113@gmail.com"#你的gmail
        self.sender_key = "lfmmdjhubnxwcovx"##你的應用程式密碼
        self.content = MIMEMultipart()  #建立MIMEMultipart物件
        self.content["subject"] = title  #郵件標題
        self.content["from"] = self.sender  #寄件者
        self.content.attach(MIMEText(text,"html"))  #郵件內容
    def send(self,to = None):
        if to == None:
            print("u need type some email")
        else:
            self.content["to"] = to
            ### Create SSL for trustworthy
            with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
                try:
                    smtp.ehlo()  # 驗證SMTP伺服器
                    smtp.starttls()  # 建立加密傳輸
                    smtp.login(self.sender, self.sender_key)  # 登入寄件者gmail
                    smtp.send_message(self.content)  # 寄送郵件
                    print("Complete!")
                except Exception as e:
                    print("Error message: ", e)

# f = open("log.json","w")
def mail(mail):
    with open("py\log.json","r") as f:
        data = json.load(f)


    if mail in data["send_log"]:
        data["send_log"][mail] += 1
    else:
        data["send_log"][mail] = 1

    amount = len(data["send_log"].items())
    send_amount = 0
    for i in data["send_log"].items():
        send_amount += i[1]
    print(amount)
    print(send_amount)

    with open("py\log.json","w") as f:
        json.dump(data,f)


# amount = 0
# mail_amount = 0
mail("lawrcee01013@gmail.com")
a = mail("來自Ting-Kai Lee 個人網站的回信",f"""

挖... 沒想到你真的輸入你的信箱了<br>
那... 我就回個信給你吧<br>
<br>
<br>
你是第 {amount} 個按下寄信的人<br>
而到目前為止，已經寄出了 {mail_amount} 封信<br>
<br>
至於信件內容要寫甚麼呢...<br>
<br>
其實我也不知道 <br>
我就分享一位我最西歡的詩人的詩吧<br>
<br>
<br>
<i>
我是個戀足癖，大概從小就有自覺，而真正覺醒大概是國二，原因是我姊。
<br>
有天我放學後洗完澡，走出來客廳就看到家姊趴在沙發上玩手機
<br>
如下圖所示，就是趴在沙發上，雙腳向上
<br>
那時候青春期，是性慾不太能受控的年紀，而一看到我姊潔白的腳，懸空來回擺動著，我就不自主的興奮了。
<br>
我先是觀看了幾十秒，在她認真玩手機時慢慢靠過去，就為了看得更仔細
<br>
大概到距離半公尺時，我姊已經注意到我
<br>
👩「你洗完澡囉? 今天要自己買晚餐喔」
<br>
👨「對阿~妳可以洗了 啊晚餐妳要吃甚麼?」
<br>
接著就一段姊弟的普通日常對話。
<br>
而對話告一段落時，我也站沙發在旁邊假裝看電視一會
<br>
<br>
接著，我慢慢地將跨下(只有穿四角褲)慢慢接近姊姊的腳，而當腳與褲襠碰觸到的一瞬間，我全身酥麻了起來。
<br>
而我姊此時還沒注意到她的腳有碰到什麼，還沉浸在手機當中
<br>
我就想趁我姊還沒發現以前多享受一會，結過享受不到幾秒…
<br>
👩「你是在幹嘛啊?」
<br>
👨「沒有啊…我在看電視啊…」
<br>
因為我太心虛了，連講話都不清楚，我此刻只覺得丟臉的要死，好想死啊~
<br>
而我姊並沒表示出不爽，比較偏向想笑+傻眼
<br>
👩「你知道很假嗎? 你真的很變態耶~」
<br>
我姊只是笑笑的用腳多踹我胯下幾次，那時是我第一次感受何謂性高潮
<br>
看到我被踢還露出興奮又猥褻的笑容，我姊不但沒罵我，似乎還能理解我包容我
<br>
👩「借你用幾分鐘啦~」
<br>
我姊說完就只是笑笑地頭轉回去繼續玩手機。
<br>
「為什麼?」我本來想問，但問這種問題好像會更奇怪，我就靜靜的[使用]姊姊的腳
<br>
就這樣，之後的幾年時間，我姊都願意在身旁沒人的時候，借我腳滿足我這胎哥鬼，平常就是讓我舔腳、觸碰之類，她心情好時，還會幫我足交，導致之後我看A片時，幾乎對性交場景無感，只有足交影片能滿足我。
<br>
 <br>
<br>
而我上大學交了女友後，也開始與女友有些親密行為，在性愛過程，我幾乎是無感的，所以還挺持久的。
<br>
但滿足的似乎只有對方，正常性行為根本無法滿足我，而跟女友提起這方面東西時，她只是不能理解，覺得這行為很不正常，因此拒絕了。
<br>
而就在我交女友後，我姊也拒絕再為我做這些了，她給我的理由是這算是出軌，只有我單身時才能願意幫我。
<br>
難道我要為了這種事，跟我現任女友分手嗎?
<br>
其實讓姊姊幫忙做這種事，我自己也知道很怪，但全天下也只有我姊願意包容我這胎哥人，如果她不是我姐姐就好了…
<br>
----------by 🈸🈸仇女大將軍 的分享
</i>
<br><br>
好啦 其實這不是我喜歡的詩拉 其實我連這首都是隨便抄的 呵呵...
<br>
祝我100分
""")
a.send("lawrencelee0113@gmail.com")
