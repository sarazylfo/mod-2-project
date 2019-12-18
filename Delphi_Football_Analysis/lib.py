import requests
from dotenv import load_dotenv
import os
load_dotenv()

class WeatherGetter():
    def __init__(self):
        self.BASE_URL = 'https://api.darksky.net'
        self.SECRET_KEY = os.getenv("DARK_SKY_KEY")
        
    def weather_getter(self, time):
#         [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS] -> 2012-03-31T15:00:00
#         time = '2019-11-11T15:00:00'
        forcast = requests.get(f"{self.BASE_URL}/forecast/{self.SECRET_KEY}/52.5200,13.4050,{time}")
        return forcast
    
class MongoHandler():
    def __init__(self, dbname, division_name):
        self.myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.mydb = self.myclient[dbname]
        self.schema_name = self.mydb[division_name]
        
    
    def create_doc(self, team_name, total_goals, total_wins, win_percentage):
        dic = {}
        dic['Team_Name'] = team_name
        dic['total_goals'] =  total_goals
        dic['total_wins'] = total_wins
        dic['rain_win_percentage'] = win_percentage
        return self.schema_name.insert_one(dic)
