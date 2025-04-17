import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        subheading = response.xpath('//span[@class = "subheading"]/text()').getall()
        author_name = response.xpath('//span[@class = "author-name"]/text()').get()
        return {"subhead": subheading, 
                "Author_name": author_name}
