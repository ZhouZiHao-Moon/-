import requests,re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/65.0.3325.146 Safari/537.36'
}
response = requests.get('http://www.ntzx.cn/Category_10/Index.aspx',headers=headers)
html = response.text
results = re.findall('<tr><td>.*?</td><td><a .*?>(.*?)</a></td><td>(.*?)</td></tr>',html)
for result in results:
    title = re.search('<font .*?>(.*?)</font>',result[0])
    if title:
        print(title.group(1), result[1])
    else:
        print(result[0],result[1])