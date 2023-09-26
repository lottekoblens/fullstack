import pandas
from json import loads, dumps

def turkijeinformatie () :
    alles = pandas.read_csv("tourist_numbers_Turkey.csv")

    # for i, aantal in alles.iterrows():
    # print(aantal[" ALMANYA"]," aantal bezoekers in date", aantal["Date"])


    result = alles[[" ALMANYA","Date"]].to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)