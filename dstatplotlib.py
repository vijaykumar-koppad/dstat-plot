#!/usr/bin/python

import sys
import pylab as pl
import datetime as DT
from matplotlib import dates
from matplotlib.backends.backend_pdf import PdfPages


def plot_cpu_usr_sys(dstat_dict):

    figs = [x for x in dstat_dict.keys() if "cpu" in x]
    if not figs:
        print "No CPU data available to plot"
    datetimes = [DT.datetime.strptime(t, "%d-%m %H:%M:%S")
                 for t in dstat_dict['time']]
    hfmt = dates.DateFormatter('%H:%M:%S')
    if len(figs) == 1:
        plots = [plots]
    for i in range(len(figs)):
        f, plots = pl.subplots(1)
        plots.plot(datetimes, dstat_dict[figs[i]]['usr'], 'r-', label="usr",
                   linewidth=.5)
        plots.plot(datetimes, dstat_dict[figs[i]]['sys'], 'b-', label="sys",
                   linewidth=.5)
        plots.set_title(figs[i]+" usr/sys")
        plots.legend(loc='best')
        plots.xaxis.set_major_locator(dates.MinuteLocator())
        plots.xaxis.set_major_formatter(hfmt)
        pl.xticks(rotation='vertical')
        pl.subplots_adjust(bottom=.15)
        pl.autoscale()
        fil = figs[i]+"-usr-sys.svg"
        print fil
        pl.savefig(fil, format="svg")


def plot_cpu_hiq_siq(dstat_dict):

    figs = [x for x in dstat_dict.keys() if "cpu" in x]
    if not figs:
        print "No CPU data available to plot"
    datetimes = [DT.datetime.strptime(t, "%d-%m %H:%M:%S")
                 for t in dstat_dict['time']]
    hfmt = dates.DateFormatter('%H:%M:%S')
    if len(figs) == 1:
        plots = [plots]
    for i in range(len(figs)):
        f, plots = pl.subplots(1)
        plots.plot(datetimes, dstat_dict[figs[i]]['usr'], 'r-', label="usr",
                   linewidth=.5)
        plots.plot(datetimes, dstat_dict[figs[i]]['sys'], 'b-', label="sys",
                   linewidth=.5)
        plots.set_title(figs[i]+" usr/sys")
        plots.legend(loc='best')
        plots.xaxis.set_major_locator(dates.SecondLocator())
        plots.xaxis.set_major_formatter(hfmt)
        pl.xticks(rotation='vertical')
        pl.subplots_adjust(bottom=.15)
        pl.autoscale()
        fil = figs[i]+" usr-sys"
        print fil
        pl.savefig(fil, format="svg")


def embed_html(dstat_dict):
    fd = open("html", 'w')
    head = ' <!DOCTYPE html>\
    <html>\
    <body>\
    <h1>My first SVG</h1>\
    '
        
    tail = '</body>\
    </html>\
    '
    
    fd.write(head)
    for i in range(4):
        data_uri = open('cpu'+str(i)+' usage usr-sys.svg', 'rb').read().encode
        ('base64').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
        fd.write(img_tag)

    fd.write(tail)
    fd.close()
