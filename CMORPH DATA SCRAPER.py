from selenium import webdriver

from selenium.webdriver.common.by import By

path = 'chromedriver'
driver = webdriver.Chrome(path)
years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']

for year in years:
    for month in months:
        if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
            a = ["%02d" % x for x in range(1,32)]
            for days in a:
                file = year+'/'+month+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+year+month+days+'.nc'
                url = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+file
                driver.get(url)
        elif month == '04' or month == '06' or month == '09' or month == '11':
            a = ["%02d" % x for x in range(1,31)]
            for days in a:
                file = year+'/'+month+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+year+month+days+'.nc'
                url = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+file
                driver.get(url)
        elif month =='02':
            if year == '2012' or year ==  '2016' :
                a = ["%02d" % x for x in range(1,30)]
            else:
                a = ["%02d" % x for x in range(1,29)]
            for days in a:
                file = year+'/'+month+'/CMORPH_V1.0_ADJ_0.25deg-DLY_00Z_'+year+month+days+'.nc'
                url = 'https://www.ncei.noaa.gov/data/cmorph-high-resolution-global-precipitation-estimates/access/daily/0.25deg/'+file
                driver.get(url)


        
          
                
        
