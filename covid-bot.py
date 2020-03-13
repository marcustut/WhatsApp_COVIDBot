from flask import Flask, request
import requests
from bs4 import BeautifulSoup
from twilio.twiml.messaging_response import MessagingResponse
import datetime

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    # WebScrapping Part
    page = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(page.content, 'html.parser')

    # covid all
    class_totalStats = soup.find(class_='content-inner')
    list_stats = class_totalStats.find_all(class_='maincounter-number')

    list_textStats = [stats.get_text().strip() for stats in list_stats]

    # covid country
    tableCountries = soup.find(id='main_table_countries_div')
    tbody_listCountries = tableCountries.find_all('tbody')[0]
    tr_listCountries = tbody_listCountries.find_all('tr')

    nested_listCountries = [country.find_all(
        'td') for country in tr_listCountries]

    # get every details of a country in a list
    details_Countries = []

    for country in nested_listCountries:
        detail_perCountry = []
        for detail in country:
            detail_perCountry.append(detail.get_text().strip())
        details_Countries.append(detail_perCountry)

    # convert every country name to lowercase
    for country in details_Countries:
        country[0] = country[0].lower()

    # -----------------------------------------------------------------------------------------------------------------------------------------------------

    # Whatsapp Bot Part

    # Get current time
    currentDT = datetime.datetime.now().strftime("_%a, %d-%m-%Y, %I:%M:%S%p_")

    help_msg = f'Current time: {currentDT}\n\nWelcome to the COVID-19 WhatsApp ChatBot.\n\n*List of Commands:*\ncovid help - display this help message.\ncovid all - show the worldwide COVID-19 status.\ncovid _country_ - show the COVID-19 status for this country.\n   _eg. covid Malaysia_\ncovid countrylist - show the list of countries that can be checked.'

    # msg.body(help_msg)

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'covid' or 'Covid' in incoming_msg:
        if 'all' in incoming_msg:
            status = f'*Worldwide*\n\n*Total Cases:* {list_textStats[0]}\n*Total Deaths:* {list_textStats[1]}\n*Total Recovered:* {list_textStats[2]}\n\n_reference taken from https://www.worldometers.info/coronavirus/_'
            msg.body(status)
        for country in details_Countries:
            for i in range(len(country)):
                if country[i] == '':
                    country[i] = 0
            if incoming_msg[6:] in country:
                country_name = country[0][0].upper() + country[0][1:]
                msg.body(
                    f'*National Coronavirus Status*\n_Country - {country_name}_\n{currentDT}\n\n*Total Cases:* {country[1]}\n*New Cases:* {country[2]}\n*Total Deaths:* {country[3]}\n*New Deaths:* {country[4]}\n*Total Recovered:* {country[5]}\n*Active Cases:* {country[6]}\n*Critical Cases:* {country[7]}\n*Total Cases per 1 million population:* {country[8]}\n\n_reference taken from https://www.worldometers.info/coronavirus/_')
        if 'countrylist' in incoming_msg:
            countrylist = []
            for country in details_Countries:
                country_name = country[0][0].upper() + country[0][1:]
                countrylist.append(country_name)
            msg.body(
                f'*List of Countries*\nUse it like this\neg. _covid Malaysia_\n\n{countrylist[0]}\n{countrylist[1]}\n{countrylist[2]}\n{countrylist[3]}\n{countrylist[4]}\n{countrylist[5]}\n{countrylist[6]}\n{countrylist[7]}\n{countrylist[8]}\n{countrylist[9]}\n{countrylist[10]}\n{countrylist[11]}\n{countrylist[12]}\n{countrylist[13]}\n{countrylist[14]}\n{countrylist[15]}\n{countrylist[16]}\n{countrylist[17]}\n{countrylist[18]}\n{countrylist[19]}\n{countrylist[20]}\n{countrylist[21]}\n{countrylist[22]}\n{countrylist[23]}\n{countrylist[24]}\n{countrylist[25]}\n{countrylist[26]}\n{countrylist[27]}\n{countrylist[28]}\n{countrylist[29]}\n{countrylist[30]}\n{countrylist[31]}\n{countrylist[32]}\n{countrylist[33]}\n{countrylist[34]}\n{countrylist[35]}\n{countrylist[36]}\n{countrylist[37]}\n{countrylist[38]}\n{countrylist[39]}\n{countrylist[40]}\n{countrylist[41]}\n{countrylist[42]}\n{countrylist[43]}\n{countrylist[44]}\n{countrylist[45]}\n{countrylist[46]}\n{countrylist[47]}\n{countrylist[48]}\n{countrylist[49]}\n{countrylist[50]}\n{countrylist[51]}\n{countrylist[52]}\n{countrylist[53]}\n{countrylist[54]}\n{countrylist[55]}\n{countrylist[56]}\n{countrylist[57]}\n{countrylist[58]}\n{countrylist[59]}\n{countrylist[60]}\n{countrylist[61]}\n{countrylist[62]}\n{countrylist[63]}\n{countrylist[64]}\n{countrylist[65]}\n{countrylist[66]}\n{countrylist[67]}\n{countrylist[68]}\n{countrylist[69]}\n{countrylist[70]}\n{countrylist[71]}\n{countrylist[72]}\n{countrylist[73]}\n{countrylist[74]}\n{countrylist[75]}\n{countrylist[76]}\n{countrylist[77]}\n{countrylist[78]}\n{countrylist[79]}\n{countrylist[80]}\n{countrylist[81]}\n{countrylist[82]}\n{countrylist[83]}\n{countrylist[84]}\n{countrylist[85]}\n{countrylist[86]}\n{countrylist[87]}\n{countrylist[88]}\n{countrylist[89]}\n{countrylist[90]}\n{countrylist[91]}\n{countrylist[92]}\n{countrylist[93]}\n{countrylist[94]}\n{countrylist[95]}\n{countrylist[96]}\n{countrylist[97]}\n{countrylist[98]}\n{countrylist[99]}\n{countrylist[100]}\n{countrylist[101]}\n{countrylist[102]}\n{countrylist[103]}\n{countrylist[104]}\n{countrylist[105]}\n{countrylist[106]}\n{countrylist[107]}\n{countrylist[108]}\n{countrylist[109]}\n{countrylist[110]}\n{countrylist[111]}\n{countrylist[112]}\n{countrylist[113]}\n{countrylist[114]}\n{countrylist[115]}\n{countrylist[116]}\n{countrylist[117]}\n{countrylist[118]}\n{countrylist[119]}\n{countrylist[120]}\n{countrylist[121]}\n{countrylist[122]}\n{countrylist[123]}\n{countrylist[124]}\n{countrylist[125]}\n{countrylist[126]}\n{countrylist[127]}')
        if 'help' in incoming_msg:
            msg.body(help_msg)

    else:
        msg.body('Try *covid all* or *covid Malaysia* to get the latest updates')

    return str(resp)


if __name__ == '__main__':
    app.run()
