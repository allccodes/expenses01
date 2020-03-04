import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


class Expenses():

    def calcExpenses(self):
        source = requests.get('http://www.base.gov.pt/Base/pt/ResultadosPesquisa?type=contratos&query=texto%3D%26tipo%3D0%26tipocontrato%3D0%26cpv%3D%26numeroanuncio%3D%26aqinfo%3D%26adjudicante%3D506566307%26adjudicataria%3D%26desdeprecocontrato_false%3D%26desdeprecocontrato%3D%26ateprecocontrato_false%3D%26ateprecocontrato%3D%26desdedatacontrato%3D%26atedatacontrato%3D%26desdedatapublicacao%3D2020-01-01%26atedatapublicacao%3D2020-12-31%26desdeprazoexecucao%3D%26ateprazoexecucao%3D%26desdedatafecho%3D%26atedatafecho%3D%26desdeprecoefectivo_false%3D%26desdeprecoefectivo%3D%26ateprecoefectivo_false%3D%26ateprecoefectivo%3D%26pais%3D0%26distrito%3D0%26concelho%3D0').text
        soup = BeautifulSoup(source, 'lxml')

        table = soup.find_all('table', id='resultadosContractos')[0]
        rows = table.find_all('tr')

        count = 0
        total = 0

        for row in rows:
            if count != 0:
                columns = row.find_all('td', style='white-space: nowrap')
                number = columns[0].text.split('€')[0]
                number = number.rstrip()
                number = number.replace('.','').replace(',','.')
                number = float(number)
                total += number
            count += 1

        #print(total)
        total = format_currency(total, 'EUR', locale='pt_PT')
        return total


#ex = Expenses()
#print(ex.calcExpenses())