from Support import getSoup
import re,requests,json
from prettytable import PrettyTable
#This module helps to create better output.
from bs4 import BeautifulSoup


def getSoup(url):
    Resp = requests.get(url,headers = headers)
    Resp.encoding = Resp.apparent_encoding
    Soup = BeautifulSoup(Resp.text,'html.parser')
    return Soup


def getStationID():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9108'
    Soup = getSoup(url)
    Stations = str(Soup).split('@')
    Station_dic = {}
    for station in Stations:
        try:
            stationName = station.split('|')[1]
            stationID = station.split('|')[2]
            Station_dic[stationName] = stationID
        except:
            pass
    return Station_dic


def getTicketLink(url):
    Resp = requests.get(url,headers=headers)
    Trains = Resp.json()['data']['result']
    T = PrettyTable()
    T.field_names = ['TrainNumber', 'LeaveTime', 'ArriveTime', 'TimeCost', 'Private', 'FirstClass', 'SecondClass', 'NoSeat']
    for train in Trains:
        trainID = train.split('|')[3]
        LeaveTime = train.split('|')[8]
        ArriveTime = train.split('|')[9]
        CostTime = train.split('|')[10]
        PrivateSeats = train.split('|')[-7]
        NoSeat = train.split('|')[-8]
        SecondClass = train.split('|')[-9]
        FirstClass = train.split('|')[-13]
        T.add_row([trainID, LeaveTime, ArriveTime, CostTime, PrivateSeats, FirstClass, SecondClass, NoSeat])
    print(T)


headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }


Station_dic = getStationID()

train_date = input('请输入出发日期：')
from_station = input('请输入出发地：')
to_station = input('请输入目的地：')

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+train_date + '&leftTicketDTO.from_station=' +Station_dic[from_station]+'&leftTicketDTO.to_station=' + Station_dic[to_station] + '&purpose_codes=ADULT'
print(url)
getTicketLink(url)
