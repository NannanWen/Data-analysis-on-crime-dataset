import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import geopandas as gpd
import numpy as np
#import constants as const
from shapely.geometry import Polygon, mapping
from shapely.geometry import Point
from descartes import PolygonPatch
from matplotlib.collections import PatchCollection
import matplotlib.colors as clr
import matplotlib
import mpld3
import folium

def pittmap():
    map_osm = folium.Map(location=[40.444565,-79.953274],zoom_start=10)
    map_osm.save('pittmap.html')


def map():
    phi_tdi = pd.read_csv('resultdata/norm_crime_2013v2.csv')
    kappa_tdi = pd.read_csv('resultdata/norm_crime_2013v2.csv')
    eq_tdi = pd.read_csv('resultdata/norm_crime_2013v2.csv')
    shapes = gpd.read_file('census_blocks/Allegheny_County_Census_Block_Groups_2016/Allegheny_County_Census_Block_Groups_2016.shp')
    shapes['geoid'] = shapes['GEOID'].astype(int)
    phi_tdi['geoid'] = phi_tdi['GEO.tract'].astype(int)
    kappa_tdi['geoid'] = kappa_tdi['GEO.tract'].astype(int)
    eq_tdi['geoid'] = eq_tdi['GEO.tract'].astype(int)
    phi_tdi.sort_values(by='geoid',inplace=True)
    kappa_tdi.sort_values(by='geoid',inplace=True)
    eq_tdi.sort_values(by='geoid',inplace=True)
    shapes.sort_values(by='geoid',inplace=True)
    map_osm = folium.Map(location=[40.444565,-79.953274],zoom_start=10)
    values = zip(shapes['geometry'],phi_tdi['norm_count'],kappa_tdi['norm_count'],eq_tdi['norm_count'])
    def style_function(attrs):
        return {'fillColor' : attrs['properties']['fill'],
                'fillOpacity' : attrs['properties']['fill-opacity'],
                'color' : attrs['properties']['stroke'],
                'weight': attrs['properties']['stroke-width']
        }
    for poly,phi,kappa,eq in values:
        data = mapping(poly)
        vals = [phi,kappa,eq]
        val = max(vals) if all([v is not None for v in vals]) else None
        data = {
            "type": "Feature",
            "properties": {
                "stroke": "#555555",
                "stroke-width": .75,
                "stroke-opacity": 1,
                "fill-opacity": 0.5,
                "fill": ('#ffffff' if val is None   #check why val is not None here in cases it should be
                        else '#ff0000' if val > 2 
                        else '#ffa500' if val > 1 
                        else '#ffff00' if val > 0 
                        else '#00ff00' if val == 0.0
                        else '#ffffff')
            },
            "geometry": mapping(poly)
        }
        area = folium.GeoJson(data,style_function = style_function)
        area.add_child(folium.Popup(folium.Html(
            '<b>TDI (connectivity): </b> '+str(round(phi,2))
            +' <br><b>TDI (availability): </b> '+str(round(kappa,2))
            +' <br><b>TDI (equal weight): </b> '+str(round(eq,2))+' <br>',script=True)))
        area.add_to(map_osm)
    map_osm.save('interactive_map.html')


