# integrated intensity map with blue and red lobes
# large velocity range, start = 3*sigma_inte, step = 2*signa_inte sigma=0.02Jy/beam
# blue: 60~74.4km/s  red: 80.4~90km/s  v_sys = 77.4 km/s



import numpy as np
import aplpy
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy import wcs
plt.clf()

# obtain 2D fits from 3D fits
lamda = '70'
irimage = lamda+'C2.fits'
name = 'IRDC-C2SiOimage'
data, hdr = fits.getdata(name+'.pbcor.fits', 0, header = True)
# data.shape (1,150,216,216)
ra = hdr['CRVAL1']
dec = hdr['CRVAL2']
nxline = hdr['NAXIS1']
nyline = hdr['NAXIS2']
nvel = hdr['NAXIS3']
vref = int(hdr['CRVAL3']*1e-3)
vpix = int(hdr['CRPIX3'])
delv = hdr['CDELT3']*1e-3

# v_sys = 78 km/s


# blue lobe
v1 = 60.
v2 = 74.4
startblue = int((v1-vref)/delv)+vpix-1
endblue = int((v2-vref)/delv)+vpix-1
newblue = np.ndarray(shape=(1,1,endblue-startblue+1,nyline,nxline))
newblue[0,0,:,:,:]= data[0,startblue:endblue+1,:,:]
blue = newblue.sum(2)*abs(delv)    # integreting velocity dimension         
#fits.writeto(name+'blue2D_2.fits', blue, hdr, clobber=True)



# red lobe
v3 = 80.4
v4 = 90.
startred = int((v3-vref)/delv)+vpix-1
endred = int((v4-vref)/delv)+vpix-1
newred = np.ndarray(shape=(1,1,endred-startred+1,nyline,nxline))
newred[0,0,:,:,:]= data[0,startred:endred+1,:,:]
red = newred.sum(2)*abs(delv)    # integreting velocity dimension         
#fits.writeto(name+'red2D_2.fits', red, hdr, clobber=True)



# calculating overall noise and contouring levels
sigma = 0.02
nchanred = endred-startred+1
nchanblue = endblue-startblue+1
sigma_intered = sigma*abs(delv)*np.sqrt(nchanred)
sigma_inteblue = sigma*abs(delv)*np.sqrt(nchanblue)
levsred = np.arange(20)*6*sigma_intered+3*sigma_intered
levsblue = np.arange(20)*6*sigma_inteblue+3*sigma_inteblue

#sigma_inte = 0.01265  # 0.02*0.2*np.sqrt(10)
#levsred = np.arange(20)*0.08+0.15
#levsblue = np.arange(20)*0.08+0.15



# ploting
fig = plt.figure(figsize=(10,10))
#fig.text(0.45,0.93,name+' M0',size='xx-large')

# show box region
x_box = np.array([280.71465,280.71399,280.71737,280.71806])
y_box = np.array([-3.99585,-3.9967875,-3.9992528,-3.99835])
box = np.array([x_box,y_box])



# read IR image
irdata,h1 = fits.getdata(irimage, 0, header = True)
ir = np.ndarray(shape=(1,1,irdata.shape[1],irdata.shape[0]))
ir[0,0,:,:] = irdata[:,:]
fits.writeto(lamda+'um.fits', ir, h1, clobber=True)




f = aplpy.FITSFigure(lamda+'um.fits', subplot=[0.2,0.2,0.7,0.7], figure=fig,angle=90)
fred = fits.open(name+'red2D.fits')
fblue = fits.open(name+'blue2D.fits')
f.show_contour(fred,levels=levsred,colors='k',linewidths=0.8)
f.show_contour(fred,levels=levsred,colors='brown',linewidths=0.5)
f.show_contour(fblue,levels=levsblue,colors='blue',linewidths=0.5)

f.show_colorscale(cmap='hot')
#f.show_grayscale(vmax=40)
f.add_colorbar()



f.show_markers(ra,dec,edgecolor='black',facecolor='none', marker='+',s=500)
#f.show_markers(ralis,declis,edgecolor='black',facecolor='none', marker='*')
f.ticks.set_xspacing('auto')
f.ticks.set_length(5)
f.ticks.set_color('black')
f.show_markers(280.709528071, -4.05566638862,edgecolor='none',facecolor='k', marker='d',s=100)





fig.savefig('M0_'+name+lamda+'um.eps')
#fig.savefig('try2.eps')



