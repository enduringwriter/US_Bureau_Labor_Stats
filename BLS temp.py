import requests
import json
import prettytable
import pandas as pd

headers = {'Content-type': 'application/json'}

data = json.dumps({"seriesid": ['CUUR0000SA0', 'SUUR0000SA0'], "startyear": "2011", "endyear": "2014"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

for series in json_data['Results']['series']:
    x = prettytable.PrettyTable(["series id", "year", "period", "value", "footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        footnotes = ""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
        if 'M01' <= period <= 'M12':
            x.add_row([seriesId, year, period, value, footnotes[0:-1]])

    # If outputting only a txt file, use this: 
    # output = open(seriesId + '.txt', 'w')
    # output.write(x.get_string())
    # output.close()

    # Save data to a text file
    with open(seriesId + '.txt', 'w') as txt_file:
        txt_file.write(x.get_string())

    # Read the tab-separated text file into a DataFrame
    df = pd.read_csv(seriesId + '.txt', sep='\t')

    # Replace 'output_file.xlsx' with the desired output Excel file name
    output_file = 'seriesId' + '.xlsx'

    # Save the DataFrame to an Excel file
    df.to_excel(output_file, index=False)
