# 專題三: 菈蠂芮

<br>
<h3>名稱由來</h3>
<p>取自Luxury - 奢華，本專題希望為使用者提供高品質的服務，故取名為luxury同音字 - 菈蠂芮 </p>

<h3>資料來源</h3>
<ul>
<li> Booking.com訂房網站</li>
<li>日期範圍 : 2022年6月1日~6月10日、區域範圍 : 六都<br></li>
</ul>

<h3>Method</h3>
<ul>
  <li><p>使用動態爬蟲-Selenium，抓取網站的資料，自動切換日期進行爬蟲，過程中還可以一邊進行data clean</p></li>
  <li><p>爬取的資料皆存放至MongoDB中</p></li>
  <li><p>使用Tkinter建立小程式介面，提供使用者查詢，並為使用者提供符合條件的前三名飯店資訊</p></li>
  <li><p>程式設計概念如下圖 : </p></li>
  <br>
  <img src="https://imgur.com/h7VO5h1.png" width="675" height="400"/><br>
</ul>

<h3>達成專題二的未來期望</h3>
<br>
<ol>
<img src="https://imgur.com/go6GMW6.png" width="675" height="400"/>
<ul>
  <br>
  <li>擴充縣市範圍 - 六都，因受到時間與設備限制，僅收錄六都<br></li>
  <li>入住日期 - 6月1日~6月10日，因受到時間與設備限制，僅提供入住一晚的選擇<br></li>
  <li>房型選擇 - 2人房或4人房<br></li>
  <li>增加資料來源，因受到時間與設備限制，所以不擴增，但擴增是可以落實<br></li>
  <li>增加Google Map資訊，因受到Tkinter限制，所以無法嵌入google map，改用按鈕方式導入<br></li>
  <li>將資料存放至Database，本專案使用MongoDB作為儲存空間<br></li>
  <li>增加使用客群，本專案不只針對商務客提供服務，也可以提供給想快速得到合宜飯店的使用者<br></li>
</ol>
</ul>

<br>
<h3>小程式 - 菈蠂芮</h3>

<br>
 下圖為小程式操作介面，可供使用者設定篩選條件<br>
<br>
<ol>
<img src="https://imgur.com/AZywR00.png" width="675" height="400"/><br>
</ol>
 經使用者設定的條件，其選項會變成紅色<br>
<br>
<ol>
<img src="https://imgur.com/OVkdYkg.png" width="675" height="400"/><br>
</ol>
 若使用者條件設定不完全、或是輸入價錢順序不對，皆會挑出提醒視窗，請使用者重新設定<br>
<br>
<ol>
<img src="https://imgur.com/SJ6VTpk.png" width="675" height="400"/><br>
</ol>
 若無符合條件的飯店，則會出現"無空房"的視窗通知使用者<br>
<br>
<ol>
<img src="https://imgur.com/9SffO70.png" width="675" height="400"/><br>
</ol>
 根據條件進行搜尋後，將為使用者提供3間飯店資訊，若符合飯店筆數少於3筆，也會讓使用者知道<br>
<br>
<ol>
<img src="https://imgur.com/cHzEtkM.png" width="675" height="400"/><br>
<p>僅有一間飯店</p>
<img src="https://imgur.com/rAkUbiA.png" width="675" height="400"/><br>
</ol>

 使用者查詢後的介面，利用考量因素評分進行排序，提供符合條件最高的前三間飯店資訊，提供的資訊如下 : <br>
 <ul>
    <li>查詢筆數<br></li>
    <li>飯店名稱<br></li>
    <li>飯店地址 : 若需要了解詳細地址，可點選google map按鈕，將引導使用者至google map網頁<br></li>
    <li>入住日期<br></li>
    <li>房間類型<br></li>
    <li>停車資訊<br></li>
    <li>價格<br></li>
    <li>使用者入對此飯店有興趣，可以點選booking的按鈕，將引導使用者至訂房頁面<br></li>
    <li>使用者若不喜歡，還可以點選上、下一筆按鈕切換<br></li><br>
 </ul>                                           
                                                               
<h3>未來期望</h3>
   <ul>
      <li>若有足夠經費可以升級硬體設備，技術層面即可達成24小時不停更新訂房網資訊，讓使用者擁有更多篩選條件<br></li>
   </ul>
