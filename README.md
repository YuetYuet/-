# 專題三: 菈蠂芮

<br>
<h3>資料來源</h3>
<ul>
<li> Booking.com訂房網站</li>
<li>日期範圍 : 2022年6月1日~6月10日、區域範圍 : 六都<br></li>
</ul>

<h3>User</h3>
  <p>目標客群 : 所有人</p>

<h3>Method</h3>
<ul>
  <li><p>使用動態爬蟲-Selenium，抓取網站的資料，自動切換日期進行爬蟲，直到已設定的結束日期，過程中一邊進行data clean。</p></li>
  <li><p>爬取的資料皆存放至MongoDB中。</p></li>
  <li><p>使用Tkinter建立小程式介面，提供使用者查詢，並為使用者提供符合條件的前三名飯店資訊。</p></li>
  <li><p>程式設計概念如下圖 : </p></li>
  <br>
  <img src="https://imgur.com/D30UKii.png" width="675" height="350"/><br>
</ul>


<h3>小程式-訂房好幫手</h3>
<br>
<ul>
  <ol>
  <img src="https://imgur.com/DxHeyRV.png" width="675" height="350"/><br>
  <br>
   上圖為小程式操作介面，可供使用者選擇居住地區與入住日期<br>
  <br>
  <img src="https://imgur.com/YPd3Kg7.png" width="675" height="350"/><br>
  <br>
   上圖為使用者查詢後的介面，提供評分最高的前三間飯店資訊，提供的資訊如下 : <br>
   <ol>
   <br>
   <ul>
      <li>訂房網站<br></li>
      <li>飯店名稱<br></li>
      <li>飯店地址<br></li>
      <li>入住日期<br></li>
      <li>房間類型 : 均為雙人房<br></li>
      <li>價格 : 其費用為入住一晚的價格，包含早餐<br></li>
      <li>推薦指數<br></li><br>
   </ul>
   </ol>
   推薦指數的計算方式，採用訂房網站針對住宿地點、清潔程度、設施與設備、舒適程度、員工素質與服務...等5個項目，使用加權計算。<br>
   <br>
   權重的分配是透過問卷調查，統計100位作答者對挑選飯店的考量順序，得出以下結果 : <br><br>
   <ol>
   <ul>
      <li>住宿地點 權重3<br></li>
      <li>清潔程度 權重3<br></li>
      <li>設施與設備 權重2<br></li>
      <li>舒適程度 權重1<br></li>
      <li>員工素質與服務 權重1<br></li>
   </ul>
   </ol>
   <br/>
   <ol>
   <img src="https://imgur.com/yH1a3o0.png" width="600" height="400" /><br/>
   </ol>
   </ol>
</ul>

<h3>未來期望</h3>
   <ul>
      <li>將區域擴大至變六都或全台灣<br></li>
      <li>入住日期範圍增加<br></li>
      <li>房型選擇多樣化<br></li>
      <li>增加資料來源，例如 : Hotel.com之類的訂房網<br></li>
      <li>增加Google Map資訊<br></li>
      <li>將資料存放至Database<br></li>
   </ul>
