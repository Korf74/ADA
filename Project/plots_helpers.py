#Slider Function
import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_notebook, show, ColumnDataSource
from bokeh.models import ColumnDataSource, FactorRange,Text, LinearAxis,SingleIntervalTicker,CustomJS, Slider, DataRange1d
from bokeh.layouts import column, widgetbox
from bokeh.models.glyphs import VBar
from bokeh.models.ranges import Range1d
from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import FactorRange, DataRange1d
from bokeh.models.ranges import Range1d
from bokeh.models.axes import LinearAxis
import folium
import json
import os
from branca.colormap import linear
from time_slider_choropleth import TimeSliderChoropleth

def year_slider_plot(title, dict_data, x_range, y_range, x_label, y_label, text_x, text_y):
	title = title
	sources = {}
	years = np.ndarray.tolist(np.arange(2000,2017,1))
	for y in years:
		y_str = "_"+str(y)
		sources[y_str] = ColumnDataSource(data=dict(x=dict_data[y_str][x_label], y = dict_data[y_str][y_label]))

	dict_of_sources = dict(zip(
	              [x for x in years],
	              ['_%s' % x for x in years]))
	js_source_array = str(dict_of_sources).replace("'", "")
	plot = figure(x_range=x_range,y_range=y_range, plot_height=350,
	      toolbar_location=None, tools="",title = title )

	plot.xaxis.axis_label = x_label
	plot.yaxis.axis_label = y_label
	plot.xgrid.grid_line_color = None
	plot.ygrid.grid_line_color = None


	code = """
	    var year = year_slider.get('value'),
	        sources = %s,
	        new_source_data = sources[year].get('data');
	    renderer_source.set('data', new_source_data);
	    text_source.set('data', {'year': [String(year)]});
	""" % js_source_array
	#Callback
	callback = CustomJS(args=sources, code=code)
	# Add the bars
	renderer_source = sources['_%s' % years[0]]

	bar_glyph = VBar(x="x", top="y", bottom=0, width=0.5, fill_color='#3288bd')
	bar_renderer = plot.add_glyph(renderer_source, bar_glyph)
	text_source = ColumnDataSource({'year': ['%s' % years[0]]})
	text        = Text(
	                  x=text_x, y=text_y, text='year',
	                  text_font_size='50pt',
	                  text_color='#EEEEEE'
	                  )
	plot.add_glyph(text_source, text)
	year_slider = Slider(start=years[0], end=years[-1],value=years[0] ,step=1,
	                    title="Year", callback=callback)
	callback.args["year_slider"] = year_slider
	callback.args["text_source"] = text_source
	callback.args["renderer_source"] = renderer_source

	layout = column(
	    plot,
	    widgetbox(year_slider))#,sizing_mode='scale_width')


	return layout


def country_tab(country_name, deaths, ratio):
	date = np.arange(2000,2017,1,dtype=np.int64) # stop value excluded
	date = date.astype('str')
	p = figure(x_range=FactorRange(*date), plot_height=350, toolbar_location=None, tools="", title="Ratio vs Death")
	p.yaxis.axis_label = "Death"
	p.xaxis.axis_label = "Year"
	p.vbar(x=date, top = deaths, width=0.9, alpha=0.5)
	p.extra_y_ranges = {"Ratio": Range1d(start=0.8, end=2)}
	p.add_layout(LinearAxis(y_range_name="Ratio", axis_label="Ratio"), "right")
	p.line(x=date, y=ratio, color = "red", line_width = 2, y_range_name="Ratio")
	tab = Panel(child=p, title = country_name)
	return tab

def world_map_data_processing(country_filename, year_filename):
    json_filename = "world_countries.geojson"
    geo_json = json.load(open(json_filename))

    article_country = pd.read_csv(country_filename)
    article_sum_year = pd.read_csv(year_filename)

    article_sum_year = article_sum_year.merge(article_country,on='Year')
    map_index= [] 
    for i in geo_json['features']:
        map_index.append(i['id'])
        
    article_sum_year["Ratio"] = article_sum_year["NbArticles"]/article_sum_year['NbArticles_Year']
    article_sum_year = article_sum_year[article_sum_year.Year > 1999]
    article_sum_year = article_sum_year[article_sum_year.Year < 2017]
    article_sum_year = article_sum_year.set_index('ActionGeo_CountryCode')
    
    nato_to_iso = pd.read_csv("nato_to-iso3.csv")

    nato_to_iso = nato_to_iso.set_index('Trigram')

    index_nato = nato_to_iso.index
    index_country = article_sum_year.index

    replace_dict= dict()
    
    for i in map_index:
        if i in index_nato:
            code = nato_to_iso['Digram'].loc[i]
            if code in index_country:
                replace_dict[code] = i

    
    
    
    update_dict =     {'EZ': 'CZE', 
     'GM': 'DEU',
     'MJ': 'MNE',
     'RS': 'RUS',
     'AE': 'ARE',
     'YM': 'YEM',
     'RI': "SRB",
     'GA': 'GMB' ,
     'GB': 'GAB',
     'UK': 'GBR' }
    

    replace_dict.update(update_dict)

    article_sum_year = article_sum_year.reset_index()   

    s = pd.Series(replace_dict, name='Trigram')
    s.index.name = 'ActionGeo_CountryCode'
    s = s.reset_index()
    
    article_sum_year = article_sum_year.merge(s, on='ActionGeo_CountryCode')
    
    return (article_sum_year,map_index)
    
    
def world_map_visu(article_sum_year,map_index):
    json_filename = "world_countries.geojson"
    geo_json = json.load(open(json_filename))
    
    year_index = pd.date_range(start="2000-1-1",periods=17,freq='A').strftime('%s')
    year_index

    color_per_year = article_sum_year.copy()
    color_per_year = color_per_year.set_index("Trigram")
    article_sum_year = article_sum_year.set_index('ActionGeo_CountryCode')
    

    #create styledata
    styledata = {}

    for country in map_index:
        if country in color_per_year.index:
            color = np.asarray(color_per_year['Ratio'].loc[country])

            if color.shape[0] == 17 :
                df = pd.DataFrame(
                    {'color': color,
                     'opacity': np.ones((17,))*0.71},
                      index = year_index)


                styledata[country] = df





    max_color, min_color= 0, 0, 

    for country, data in styledata.items():
        max_color = max(max_color, data['color'].max())
        min_color = min(max_color, data['color'].min())            


    cmap = linear.YlOrRd.scale(min_color, max_color)

    for country, data in styledata.items():
        data['color'] = data['color'].apply(cmap)




    styledict = {
        str(country): data.to_dict(orient='index') for
        country, data in styledata.items()
    }    

    m = folium.Map(
        location=[46.3, 7],
        tiles='Mapbox Bright',
        zoom_start=2
    )

    folium.GeoJson(geo_json).add_to(m)



    g = TimeSliderChoropleth(
        geo_json,
        styledict=styledict,

    ).add_to(m)    


    return m

    
    
            
    
