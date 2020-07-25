require 'httparty'
require 'nokogiri'
require 'byebug'

def scraper

    ads = []
    url = "https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/page-"

    puts "How many pages do you want to read?"
    n_pages = (gets).to_i

    for i in 1..n_pages
        unparsed = HTTParty.get(url + i.to_s)
        parsed = Nokogiri::HTML(unparsed)
        
        table = parsed.css('ol').select {|x| x.attr('class') == "discussionListItems"}.first
        rows = table.css('li')
        ads += rows
    end

    output = []

    for ad in ads
        links = ad.css('a')
        title_link = links.select {|x| x.attr('class') == "PreviewTooltip"}.first
        tag_link = links.select {|x| x.attr('class') == "prefixLink"}.first
        next if tag_link == nil
        title = title_link.text
        ad_url = "https://klocksnack.se/" + title_link.attr('href')

        tag = tag_link.css('span')
        next if tag == "Viktigt" or tag == "Avslutad"
 
        unparsed_ad = HTTParty.get(ad_url)
        return if unparsed_ad.body.nil? or unparsed_ad.body.empty?
        parsed_ad = Nokogiri::HTML(unparsed_ad)

        price_box = parsed_ad.css('div').select {|x| x.attr('class') == "pairsRows secondaryContent"}
        price_box.length == 0 ? next : price_box = price_box.first
        price = price_box.css('dd').first.text.delete "\n"
        price = price[0..-2] + "000" if price[-1] == "k"

        if price != "0" && price != "O"
            output << [price.to_i, title, ad_url]
        end
       
    end

    output = output.sort

    for watch in output
        price = watch[0]
        title = watch[1]
        link = watch[2]
        puts "------------------------------------------"
        puts "... " + title
        puts "... Price: " + price.to_s
        puts "... Link: " + link
        puts "------------------------------------------"
        puts
    end

    byebug
end

scraper