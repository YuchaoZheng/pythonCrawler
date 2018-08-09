scrapy shell url
view(response)



###XPath
response.xpath(".//*[@id='puid-3483995925']/dl/dd[5]/div[1]/span[1]").extract()
//*[@id="puid-3483995925"]/dl/dd[5]/div[1]/span[1]注意把双引号改为单引号

response.xpath("url").extract()
response.xpath("url/text()").extract()

len(response.xpath("url/text()").extract()) 查看长度

scrapy提供很多种子程序，其中crawl用于启动scrapy项目的一个爬虫。

>scrapy crawl 项目名

(访问过于频繁会要求图片验证)

