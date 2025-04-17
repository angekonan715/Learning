import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        dc_title = response.xpath('//meta[@name="DC.Title"]/@content').get()
        subheading = response.xpath('//span[@class = "subheading"]/text()').getall()
        author_name = response.xpath('//span[@class = "author-name"]/text()').get()
        date = response.xpath('//span[@class= "date"]/text()').get()
        author_company = response.xpath('//span[@class = "author-company"]/text()').get()
        description = response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get()
        number = response.xpath('//span[@class = "rfc-no"]/text()').get()
        text = w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        return {"Dc_Title": dc_title,
                "subhead": subheading, 
                "Author_name": author_name, 
                "description": description,
                "date": date,
                "author_company": author_company,
                "number": number,
                "text": text}
