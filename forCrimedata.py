import pandas as pd
import numpy as np
import datetime

def extract_data_by_year():
    
    crimes_05_15 = pd.read_csv('from_gtfs/Police_Blotter_2005-2015.csv', parse_dates = True,low_memory=False)
    crimes_16_19 = pd.read_csv('from_gtfs/police_Blotter_2016_2019.csv', parse_dates = True,low_memory=False)

    crimes_05_15['INCIDENTTIME'] = pd.to_datetime(crimes_05_15['INCIDENTTIME'])

    df = pd.DataFrame(crimes_05_15)
    print(df.head(3))

    #mask_2005 = (crimes_05_15['INCIDENTTIME'] >= '2005-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2006-01-01T00:00:00')
    #mask_2006 = (crimes_05_15['INCIDENTTIME'] >= '2006-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2007-01-01T00:00:00')
    #mask_2007 = (crimes_05_15['INCIDENTTIME'] >= '2007-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2008-01-01T00:00:00')
    #mask_2008 = (crimes_05_15['INCIDENTTIME'] >= '2008-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2009-01-01T00:00:00')
    #mask_2009 = (crimes_05_15['INCIDENTTIME'] >= '2009-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2010-01-01T00:00:00')
    #mask_2010 = (crimes_05_15['INCIDENTTIME'] >= '2010-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2011-01-01T00:00:00')
    #mask_2011 = (crimes_05_15['INCIDENTTIME'] >= '2011-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2012-01-01T00:00:00')
    #mask_2012 = (crimes_05_15['INCIDENTTIME'] >= '2012-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2013-01-01T00:00:00')
    mask_2013 = (crimes_05_15['INCIDENTTIME'] >= '2013-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2014-01-01T00:00:00')
    mask_2014 = (crimes_05_15['INCIDENTTIME'] >= '2014-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2015-01-01T00:00:00')
    mask_2015 = (crimes_05_15['INCIDENTTIME'] >= '2015-01-01T00:00:00') & (crimes_05_15['INCIDENTTIME'] < '2016-01-01T00:00:00')
    mask_2016 = (crimes_16_19['INCIDENTTIME'] >= '2016-01-01T00:00:00') & (crimes_16_19['INCIDENTTIME'] < '2017-01-01T00:00:00')
    mask_2017 = (crimes_16_19['INCIDENTTIME'] >= '2017-01-01T00:00:00') & (crimes_16_19['INCIDENTTIME'] < '2018-01-01T00:00:00')
    #mask_2018 = (crimes_16_19['INCIDENTTIME'] >= '2018-01-01T00:00:00') & (crimes_16_19['INCIDENTTIME'] < '2019-01-01T00:00:00')

    data_2013 = crimes_05_15.loc[mask_2013]
    data_2014 = crimes_05_15.loc[mask_2014]
    data_2015 = crimes_05_15.loc[mask_2015]
    data_2016 = crimes_16_19.loc[mask_2016]
    data_2017 = crimes_16_19.loc[mask_2017]
    #data_2018 = crimes_16_19.loc[mask_2018]

    result_2013 = pd.DataFrame(data_2013)
    result_2014 = pd.DataFrame(data_2014)
    result_2015 = pd.DataFrame(data_2015)
    result_2016 = pd.DataFrame(data_2016)
    result_2017 = pd.DataFrame(data_2017)
    #result_2018 = pd.DataFrame(data_2018)

    result_2013.to_csv('resultdata/blotter_crime_2013.csv')
    result_2014.to_csv('resultdata/blotter_crime_2014.csv')
    result_2015.to_csv('resultdata/blotter_crime_2015.csv')
    result_2016.to_csv('resultdata/blotter_crime_2016.csv')
    result_2017.to_csv('resultdata/blotter_crime_2017.csv')
    #result_2018.to_csv('resultdata/blotter_crime_2018.csv')

def tract_crime():
    
    crime_13 = pd.read_csv('resultdata/blotter_crime_2013.csv',low_memory=False,)
    crime_13_df = pd.DataFrame(crime_13)
    count = crime_13_df.groupby(['INCIDENTTRACT']).count()
    # print(count.head(3))
    total_crimes_tract = pd.DataFrame()
    total_crimes_tract['count'] = count['PK']
    total_crimes_tract.to_csv('resultdata/usetract_crime_2013.csv')

    crime_14 = pd.read_csv('resultdata/blotter_crime_2014.csv',low_memory=False,)
    crime_14_df = pd.DataFrame(crime_14)
    count = crime_14_df.groupby(['INCIDENTTRACT'],squeeze=True).count()
    total_crimes_tract14 = pd.DataFrame()
    total_crimes_tract14['count'] = count['PK']
    total_crimes_tract14.to_csv('resultdata/usetract_crime_2014.csv')

    crime_15 = pd.read_csv('resultdata/blotter_crime_2015.csv',low_memory=False,)
    crime_15_df = pd.DataFrame(crime_15)
    count = crime_15_df.groupby(['INCIDENTTRACT'],squeeze=True).count()
    total_crimes_tract15 = pd.DataFrame()
    total_crimes_tract15['count'] = count['PK']
    total_crimes_tract15.to_csv('resultdata/usetract_crime_2015.csv')

    crime_16 = pd.read_csv('resultdata/blotter_crime_2016.csv',low_memory=False,)
    crime_16_df = pd.DataFrame(crime_16)
    count = crime_16_df.groupby(['INCIDENTTRACT'],squeeze=True).count()
    total_crimes_tract16 = pd.DataFrame()
    total_crimes_tract16['count'] = count['PK']
    total_crimes_tract16.to_csv('resultdata/usetract_crime_2016.csv')

    crime_17 = pd.read_csv('resultdata/blotter_crime_2017.csv',low_memory=False,)
    crime_17_df = pd.DataFrame(crime_17)
    count = crime_17_df.groupby(['INCIDENTTRACT'],squeeze=True).count()
    total_crimes_tract17 = pd.DataFrame()
    total_crimes_tract17['count'] = count['PK']
    total_crimes_tract17.to_csv('resultdata/usetract_crime_2017.csv')

def tract_crime_v2():
    
    crime_13 = pd.read_csv('resultdata/crime_tract_2013mid.csv',low_memory=False,)
    crime_13_df = pd.DataFrame(crime_13)
    #df.dropna(subset=['name', 'born'])
    df13 = crime_13_df.dropna(subset=['census_block_geoid', 'zipcode'])
    count = df13.groupby(['census_block_geoid']).count()
    # print(count.head(3))
    #cc = pd.DataFrame(count)
    
    total_crimes_tract = pd.DataFrame()
    total_crimes_tract['count'] = count['zipcode']
    total_crimes_tract.to_csv('resultdata/v2_usetract_crime_2013.csv')

    crime_14 = pd.read_csv('resultdata/crime_tract_2014mid.csv',low_memory=False,)
    crime_14_df = pd.DataFrame(crime_14)
    df14 = crime_14_df.dropna(subset=['census_block_geoid', 'zipcode'])
    count = df14.groupby(['census_block_geoid'],squeeze=True).count()
    total_crimes_tract14 = pd.DataFrame()
    total_crimes_tract14['count'] = count['zipcode']
    total_crimes_tract14.to_csv('resultdata/v2_usetract_crime_2014.csv')

    crime_15 = pd.read_csv('resultdata/crime_tract_2015mid.csv',low_memory=False,)
    crime_15_df = pd.DataFrame(crime_15)
    df15 = crime_15_df.dropna(subset=['census_block_geoid', 'zipcode'])
    count = df15.groupby(['census_block_geoid'],squeeze=True).count()
    total_crimes_tract15 = pd.DataFrame()
    total_crimes_tract15['count'] = count['zipcode']
    total_crimes_tract15.to_csv('resultdata/v2_usetract_crime_2015.csv')

    crime_16 = pd.read_csv('resultdata/crime_tract_2016mid.csv',low_memory=False,)
    crime_16_df = pd.DataFrame(crime_16)
    df16 = crime_16_df.dropna(subset=['census_block_geoid', 'zipcode'])
    count = df16.groupby(['census_block_geoid'],squeeze=True).count()
    total_crimes_tract16 = pd.DataFrame()
    total_crimes_tract16['count'] = count['zipcode']
    total_crimes_tract16.to_csv('resultdata/v2_usetract_crime_2016.csv')

    crime_17 = pd.read_csv('resultdata/crime_tract_2017mid.csv',low_memory=False,)
    crime_17_df = pd.DataFrame(crime_17)
    df17 = crime_17_df.dropna(subset=['census_block_geoid', 'zipcode'])
    count = crime_17_df.groupby(['census_block_geoid'],squeeze=True).count()
    total_crimes_tract17 = pd.DataFrame()
    total_crimes_tract17['count'] = count['zipcode']
    total_crimes_tract17.to_csv('resultdata/v2_usetract_crime_2017.csv')



def normilization():

    pop_13 = pd.read_csv('from_gtfs/population2013/ACS_13_5YR_B01003_with_ann.csv',low_memory=False)
    pop_13_df = pd.DataFrame(pop_13)
    #print(len(pop_13_df))
    print(pop_13_df.head(3))

    crim_13 = pd.read_csv('resultdata/usetract_crime_2013.csv',low_memory=False)
    crim_13_df = pd.DataFrame(crim_13)
    crim_13_df = crim_13_df.dropna(subset=['INCIDENTTRACT', 'count'])
    print(crim_13_df.head(3))

    population_13 = dict()
    #crime_13 = dict()

    for tract, count in zip(crim_13['INCIDENTTRACT'], crim_13['count']):
        population_13[tract] = None
        for tractpop, pop in zip(pop_13['GEO.display-label'],pop_13['pop']):
            ##tmp = (int(tractpop / 100)) % 420030000
            ##print(tmp)
            tmp = tractpop.split(',')
            
            tt = [int(s) for s in tmp[0].split(' ') if s.isdigit()]
            #print(type(tt))
            if(len(tt) >= 1):
                t = tt[0]
                if(pop != 0):
                    population_13[t] = float(count / pop)
                else:
                    population_13[t] = 1

    df = pd.DataFrame()
    df['GEO.tract'] = crim_13['INCIDENTTRACT']
    df['norm_count'] = df['GEO.tract'].apply(lambda sid: population_13[sid])
    print(df.head(3))
    df.to_csv('resultdata/norm_crime_2013.csv')

def normilization_v2():

    #pop_13 = pd.read_csv('from_gtfs/population2013/ACS_13_5YR_B01003_with_ann.csv',low_memory=False)
    #pop_13 = pd.read_csv('from_gtfs/population2014/ACS_14_5YR_B01003_with_ann.csv',low_memory=False)
    #pop_13 = pd.read_csv('from_gtfs/population2015/ACS_15_5YR_B01003_with_ann.csv',low_memory=False)
    #pop_13 = pd.read_csv('from_gtfs/population2016/ACS_16_5YR_B01003_with_ann.csv',low_memory=False)
    pop_13 = pd.read_csv('from_gtfs/population2017/ACS_17_5YR_B01003_with_ann.csv',low_memory=False)
    pop_13_df = pd.DataFrame(pop_13)
    #print(len(pop_13_df))
    print(pop_13_df.head(3))

    #crim_13 = pd.read_csv('resultdata/v2_usetract_crime_2013.csv',low_memory=False)
    #crim_13 = pd.read_csv('resultdata/v2_usetract_crime_2014.csv',low_memory=False)
    #crim_13 = pd.read_csv('resultdata/v2_usetract_crime_2015.csv',low_memory=False)
    #crim_13 = pd.read_csv('resultdata/v2_usetract_crime_2016.csv',low_memory=False)
    crim_13 = pd.read_csv('resultdata/v2_usetract_crime_2017.csv',low_memory=False)
    crim_13_df = pd.DataFrame(crim_13)
    #crim_13_df = crim_13_df.
    print(crim_13_df.head(3))

    population_13 = dict()
    #crime_13 = dict()

    for tract, count in zip(crim_13['census_block_geoid'], crim_13['count']):
        #print(tract)
        #population_13[tract] = None
        for tractpop, pop in zip(pop_13['GEO.id2'],pop_13['pop']):
            tmp = (int)(tract / 10)
            #print(tmp)
            if(tmp == tractpop):
                if(pop != 0):
                    #print(tmp)
                    population_13[tract] = float(count / pop)
                else:
                    population_13[tract] = 1
                #print(tmp)
                
    #df = pd.DataFrame(population_13)

    #print(df.head(2))
           
    df = pd.DataFrame()
    #df['GEO.tract'] = crim_13['census_block_geoid']
    df['GEO.tract'] = crim_13['census_block_geoid']
    df['norm_count'] = df['GEO.tract'].apply(lambda sid: population_13[sid])
    print(df.head(3))
    #df.to_csv('resultdata/norm_crime_2013v2.csv')
    #df.to_csv('resultdata/norm_crime_2014v2.csv')
    #df.to_csv('resultdata/norm_crime_2015v2.csv')
    #df.to_csv('resultdata/norm_crime_2016v2.csv')
    df.to_csv('resultdata/norm_crime_2017v2.csv')



def test():
    crimes_13 = pd.read_csv('resultdata/crime_tract_2013mid.csv', parse_dates = True,low_memory=False)
    crimes_13_df = pd.DataFrame(crimes_13)
    print(len(crimes_13_df))
    print(crimes_13_df.head(3))

    count = crimes_13_df.groupby(['census_block_geoid']).count()
    # print(count.head(3))
    total_crimes_tract = pd.DataFrame()
    total_crimes_tract['count'] = count['zipcode']
    total_crimes_tract.to_csv('resultdata/interactivemap_2013.csv')

def test2():
    crime_13 = pd.read_csv('resultdata/crime_tract_2013mid.csv',low_memory=False,)
    crime_13_df = pd.DataFrame(crime_13)
    #df.dropna(subset=['name', 'born'])
    df13 = crime_13_df.dropna(subset=['census_block_geoid', 'zipcode'])
    count = df13.groupby(['census_block_geoid']).count()
    # print(count.head(3))
    cc = pd.DataFrame(count)
    cc.to_csv('resultdata/tt.csv')


    
