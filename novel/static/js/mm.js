UA = navigator.userAgent.toLowerCase();
url = window.location;
url = url.toString();
if((UA.indexOf('iphone') != -1 || UA.indexOf('mobile') != -1 || UA.indexOf('android') != -1 || UA.indexOf('ipad') != -1 || UA.indexOf('windows ce') != -1 || UA.indexOf('ipod') != -1) && UA.indexOf('ipod') == -1) {
if (url.match(/^http:\/\/www\.quanshuwang\.com\/$/) || url.match(/^http:\/\/www\.quanshuwang\.com$/)) { Go('http:\/\/m\.quanshuwang\.com'); }
if (url.match(/\/book_\d+?\.html/)){id = url.match(/\/book_(\d+?)\.html/);Go('http://m.quanshuwang.com/book_'+id[1]+'.html');}
if (url.match(/\/book\/\d+?\/\d+?\/\d+?\.html/)){id = url.match(/\/book\/(\d+?)\/(\d+?)\/(\d+?)\.html/);Go('http://m.quanshuwang.com/mbook/'+id[1]+'/'+id[2]+'/'+id[3]+'.html');}
}
function Go(url) { window.location = url;}