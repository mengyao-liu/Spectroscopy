# integrated intensity map with blue and red lobes
# large velocity range, start = 6*sigma_inte, step = 3*signa_inte
# blue: 10~77.4km/s  red: 83.4~130km/s  v_sys = 80.4 km/s



import numpy as np
import aplpy
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy import wcs
import scipy.ndimage as ndimage


plt.clf()
fig = plt.figure(figsize=(10,10))


distance = 1.98
#ra = 275.10341667
#dec = -16.19305297
#r = 0.4
ra = 275.1032749
dec = -16.19283764
r = 1.3

f = aplpy.FITSFigure('M17UC1_c3band4.continuum_multiR0.5_ap_19kuv.image.fits', subplot=[0.1,0.1,0.8,0.8],figure=fig)
f.recenter(ra,dec,r/3600.)
#f.show_colorscale(cmap='jet')
f.show_colorscale(cmap='afmhot',stretch='log',vmin=-0.001,vmid=-0.01,vmax=0.013)
#f.show_colorscale(cmap='afmhot',stretch='log',vmin=-0.001,vmid=-0.002,vmax=0.013)
f.add_colorbar()
f.colorbar.set_font(weight='bold', stretch='normal', family='sans-serif', style='normal', variant='normal')
f.colorbar.set_axis_label_font(size='x-large', weight='bold', stretch='normal', family='sans-serif', style='normal', variant='normal')
f.colorbar.set_axis_label_text('Intensity  Jy/beam')
f.colorbar.set_axis_label_rotation(270)
f.colorbar.set_axis_label_pad(20)


sigma_contin = 4.4e-5
minl = 4*sigma_contin  # 4, 350, 7
maxl = 350*sigma_contin
steps = 7
dist = np.log10(maxl)-np.log10(minl)
logstep = 10**(dist/steps)
n = np.arange(steps+1)
llog2= logstep**(n)*minl
f.show_contour(levels=llog2[:-1],colors='k',linewidths=2.,smooth=1)
f.show_contour(levels=llog2[:-1],colors='w',linewidths=1.5,smooth=1)


f.add_label(275.1033750,-16.1929216,'M17-UC1',color='white',size=25)

#fig.text(0.15,0.83,'Cycle 3   2.1mm continuum',color='white',size=30)
fig.text(0.15,0.83,'2.1mm continuum',color='white',size=30)



#fnir = fits.open('M17UC1_K_NACO_cal_cut0.fits')
#disk = [178]
#f.show_contour(fnir,levels=disk,colors='k',linewidths=1.2,smooth=1)
#f.show_contour(fnir,levels=disk,colors='c',linewidths=1.0,smooth=1)


f.add_beam()
f.beam.set_frame(True)
f.beam.set(facecolor='white', edgecolor='black')

#scalebar = np.array(([ra+0.000205,ra+0.000205-0.5/distance/3600.],[dec-0.000182,dec-0.000182]))
#f.show_lines([scalebar],edgecolor='w',linewidths=2.0,zorder=5)

# 12 GHz CH3OH masers Xu 2011
f.show_markers(275.1034375,-16.1931433,edgecolor='k',facecolor='c', marker='X',s=180,zorder=5)

# 6 GHz OH maser Caswell 1997
f.show_markers(275.1033792,-16.1928167,edgecolor='k',facecolor='m', marker='P',s=180,zorder=5)

# 1.7 GHz OH maser 
f.show_markers(275.1035018,-16.1929559,edgecolor='k',facecolor='pink', marker='P',s=180,zorder=5)  # Brogan 2001
f.show_markers(275.1031250,-16.1930278,edgecolor='k',facecolor='pink', marker='P',s=180,zorder=5)  # Caswell 1998

# 6.7 GHz CH3OH maser Caswell 1997
f.show_markers(275.1032667,-16.1929417,edgecolor='k',facecolor='g', marker='X',s=180,zorder=5)



# scale bar
dist=1.98 #kpc
size=0.5
scale=np.round(size*1000*dist)
f.add_scalebar(size*np.cos(dec*np.pi/180)/3600.,'%.1f" = %d AU' %(size,scale),corner='bottom right',zorder=5000)
f.scalebar.set_color('white')
f.scalebar.set(linewidth=2)
f.scalebar.set_font(size=18, weight='bold', stretch='normal', family='sans-serif', style='normal', variant='normal')



f.axis_labels.set_xtext('Right Ascension (J2000)')
f.axis_labels.set_ytext('Declination (J2000)')
f.axis_labels.set_font(size='x-large', weight='bold', stretch='normal', family='sans-serif', style='normal', variant='normal')
f.tick_labels.set_style('colons')
f.tick_labels.set_font(size='xx-large', weight='bold', stretch='normal', family='sans-serif', style='normal', variant='normal')
#f.ticks.set_xspacing(0.25*15/3600.)
#f.ticks.set_yspacing(2.0/3600.)
#f.ticks.set_minor_frequency(4)
#f.tick_labels.set_xformat('hh:mm:ss.s')
#f.tick_labels.set_yformat('dd:mm:ss')
f.axis_labels.set_xpad(5)
f.axis_labels.set_ypad(-20)
#f.frame.set_color('black')
f.ticks.set_color('k')
f.ticks.set_linewidth(2)




fig.savefig('M17_Band4_cont_large.eps',bbox_inches='tight')



