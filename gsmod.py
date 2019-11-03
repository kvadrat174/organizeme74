import oauth2client
import datetime
import conf1
import gspread
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials



scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

sh = gspread.authorize(credentials)
global wks
#wks = sh.open("testlist").sheet1

# ВЫБИРАЕМ ДОКУМЕНТ ИСХОДЯ ИЗ ID

def id_check(a):

    global wks
    if a== conf1.bossid:

        wks = sh.open(conf1.name_boss).sheet1

        return wks

    # return 'bossid';
    elif a== conf1.mishaid:
        wks = sh.open(conf1.name_misha).sheet1

        return wks


     #return 544728777
    elif a== conf1.kirillid:

        wks = sh.open(conf1.name_kirill).sheet1
        return wks
    else:
        wks = sh.open("testlist");
        return wks

    #return conf1.kirillid





def income1(val,x,y):
    #values_list = wks.row_values(val)

    return wks.update_cell(val,x,y);









