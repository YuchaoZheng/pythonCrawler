import scrapy
from  ..items import ZufangItem

class GanjiSpider(scrapy.Spider):
    name = "zufang"
    start_urls = ['http://bj.ganji.com/fang1/']

    '''
    爬虫启动时，爬取链接成功后自动回调的函数
    '''
    def parse(self, response):
        print(response)
        zf = ZufangItem()
        title_list = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        money_lisr = response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i,j in zip(title_list, money_lisr):
            zf['title'] = i
            zf['money'] = j
            yield zf