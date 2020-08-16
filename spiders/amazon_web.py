import scrapy
from ..items import DynotifyItem

class AmazonWebSpider(scrapy.Spider):
    name = 'amazon_web'
    start_urls = ['https://www.amazon.in/s?k=phones&i=electronics&rh=n%3A1805560031%2Cp_n_operating_system_browse-bin%3A1485077031&dc&qid=1597564839&rnid=1485076031&ref=sr_nr_p_n_operating_system_browse-bin_1']

    def parse(self, response):
        items = DynotifyItem()
        all_section= response.css('.s-latency-cf-section')
        for d in all_section:
            mobile_name=d.css('.a-color-base.a-text-normal::text').extract()
            mobile_price = d.css('.a-price-whole::text').extract()
            price_discount = d.css('.a-letter-space+ span::text').extract()
            mobile_rating = d.css('.aok-align-bottom span.a-icon-alt::text').extract()
            mobile_image = d.css('.s-image::attr(src)').extract()

            items['mobile_name']=mobile_name
            items['mobile_price'] = mobile_price
            items['price_discount'] = price_discount
            items['mobile_rating'] = mobile_rating
            items['mobile_image'] = mobile_image

            yield items




