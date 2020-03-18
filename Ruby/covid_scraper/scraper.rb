require 'httparty'
require 'nokogiri'

def scraper
    url = "https://www.worldometers.info/coronavirus/"
    unparsed = HTTParty.get(url)
    parsed = Nokogiri::HTML(unparsed)
    table = parsed.css('tbody').first
    rows = table.css('tr')

    output_list = []
    
    for row in rows
        
        cells = row.css('td')
        name = cells.first.text.strip
        tot = cells[1].text.gsub(/[,]/ ,"").to_i
        
        if tot < 30
            break
        end

        new_cases = cells[2].text.gsub(/[,]/ ,"").to_i
        if tot-new_cases > 0
            change = ((1.0*tot)/(tot-new_cases))-1
        else
            change = 1
        end

        change *= 100
        change = change.round
        output_list << [-change,tot,name]
    
    end

    output_list = output_list.sort 

    for country in output_list
        puts "#{country.last} +#{-1*country.first}% #{country[1]}" 
    end
end

scraper