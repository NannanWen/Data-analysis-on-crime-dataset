import pandas as pd 
import geopandas as gpd
from shapely.geometry import Polygon, Point
print('This may take a while...')
#assessment = pd.read_csv('from_gtfs/assessments2019.csv',index_col=False,low_memory=False)
assessment = pd.read_csv('from_gtfs/assessments2019test.csv',index_col=False,low_memory=False)
blocks = gpd.read_file('census_blocks/'
    + 'Allegheny_County_Census_Block_Groups_2016/'
    + 'Allegheny_County_Census_Block_Groups_2016.shp')
zipcodes = gpd.read_file('zip_codes/'
    + 'Allegheny_County_Zip_Code_Boundaries/'
    + 'Allegheny_County_Zip_Code_Boundaries.shp')
regions = gpd.read_file('ZillowNeighborhoods-PA/'
    + 'ZillowNeighborhoods-PA.shp')
block = dict()
region = dict()
zipcode = dict()
'''crimes['PK'] = crimes['PK'].astype(int)
crimes['X'] = crimes['X'].astype(int)
crimes['Y'] = crimes['Y'].astype(int)'''
for sid,zipcode in zip(assessment['PARID'],assessment['PROPERTYZIP']):
    '''print(type(lon)); exit()'''
    zipcode[sid] = None  
    region[sid] = None  
    block[sid] = None
    #crime = Point(lon,lat)
    for code,area in zip(zipcodes['ZIP'],zipcodes['geometry']):
        if area.contains(zipcode):
            zipcode[sid] = code
            break
    for rid,area in zip(regions['RegionID'],regions['geometry']):
        if area.contains(zipcode):
            region[sid] = rid
            break
    for geoid,area in zip(blocks['GEOID'],blocks['geometry']):
        if area.contains(zipcode):
            block[sid] = geoid
            break

df = pd.DataFrame()
df['assessment_id'] = zipcode['PARID']
df['census_block_geoid'] = df['assessment_id'].apply(lambda sid: block[sid])
df['zipcode'] = df['assessment_id'].apply(lambda sid: zipcode[sid])
df['region_id'] = df['assessment_id'].apply(lambda sid: region[sid])
regions = {rid:name for rid,name in zip(regions['RegionID'],regions['Name'])}
df['region_name'] = df['region_id'].apply(lambda rid: regions[rid] if rid is not None else None)
df.to_csv('resultdata/forassessment2019.csv')
print('Saved to forassessment2019.csv')
print('See README for description fo data acquired.')
