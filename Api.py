import html

import requests
from lxml import etree


class APIHandler:
    def api_request_sender(self, start_date, end_date):
        # check start_date and end_date format
        # check that start_date should before _end date
        url = "http://www.mnb.hu/arfolyamok.asmx?wsdl"
        headers = {"content-type": "text/xml"}
        body = f"""<?xml version="1.0" encoding="utf-8"?> 
                    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://www.mnb.hu/webservices/">
                        <soapenv:Header/>
                            <soapenv:Body>
                                <web:GetExchangeRates>
                                <web:startDate>{start_date}</web:startDate>
                                <web:endDate>{end_date}</web:endDate>
                                <web:currencyNames>EUR</web:currencyNames>    
                                </web:GetExchangeRates>
                            </soapenv:Body> 
                    </soapenv:Envelope>"""

        return requests.post(url, data=body, headers=headers)

    def api_response_converter(self):
        api_respsone = self.api_request_sender()  # need two argument
        dom = html.unescape(api_respsone.text)

        tree = etree.XML(dom)

        # Use XPath to find Day elements, considering the namespaces
        namespaces = {
            "s": "http://schemas.xmlsoap.org/soap/envelope/",
            "mnb": "http://www.mnb.hu/webservices/",
        }

        api_data = {"Date": [], "Rate": []}

        days = tree.xpath("//mnb:Day", namespaces=namespaces)
        for day in days:
            date = day.get("date")
            rate = day.find(".//mnb:Rate", namespaces=namespaces).text
            api_data["Date"].append(date)
            api_data["Rate"].append(rate)
            # print(f"Date: {date}, Rate: {rate}")

        return api_data


# print(html.unescape(str(response.content)))
