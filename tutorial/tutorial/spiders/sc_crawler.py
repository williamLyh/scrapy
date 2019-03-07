from tutorial.items import TutorialItem
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "sc_crawler"
    start_urls = [
        'https://www.goodreads.com/quotes/tag/shakespeare'
    ]

    def parse(self, response):

        line_list = response.xpath('//div[@class="quoteText"]/text()').getall()
        line = u' '.join([ele.strip() for ele in line_list if not ele.isspace()])

        for ele in line.split(u'\u2015'):
            if not ele.isspace():
                item = TutorialItem()
                item['line'] = ele.encode('utf-8')
                yield item

        with open('line.txt', 'w+') as f:
            f.write(line.encode('utf-8'))
            f.close()

        next_page = response.xpath("//a[@class='next_page']/@href").get()
        if next_page is not None:
            yield scrapy.Request(
                'https://www.goodreads.com'+next_page,
                callback=self.parse
            )

