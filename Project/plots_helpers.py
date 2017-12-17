#Slider Function
import numpy as np
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
