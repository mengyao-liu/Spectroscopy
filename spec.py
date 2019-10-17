import numpy as np
import scipy
from scipy import ndimage
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy import wcs
plt.clf()


targets = {'C2','C6','C9','B1','H5','H6'}
v_sys = {'C2':79,'C9':77.4,'C6':75.4,'B1':27.2,'B2':27.65,'H5':44.7,'H6':45.2}

for target in targets:
    name = 'IRDC-'+target+'SiOimage'
    data, hdr = fits.getdata('new/'+target+'/SiO/'+name+'_slicebox_totalvel.fits', 0, header = True)
    spec = data.mean(1)



    #get velocity array
    refpix = hdr['CRPIX2']
    interval = hdr['CDELT2']
    refval = hdr['CRVAL2']
    n=hdr['NAXIS2']
    vel=((np.arange(n)-refpix+1)*interval+refval)/1000.


#baseline
#base_x = np.append(vel[np.where(vel<68.)],vel[np.where(vel>88.)])
#base_y = np.append(spec[np.where(vel<68.)],spec[np.where(vel>88.)])
#baseline = np.polyfit(base_x,base_y,1)
#spec = spec - baseline[0]*vel-baseline[1]




    smoothed = scipy.ndimage.filters.uniform_filter(spec,size=5)


    #plot
    fig = plt.figure(figsize=(7,7))
    ax=plt.axes([0.15,0.3,0.7,0.4])
    ax.plot(vel,smoothed,'k-',drawstyle='steps')
    if target == 'B1' or target == 'B2':
        plt.xlim(21.,91.)
    else:
        if target == 'H5' or target == 'H6':
            plt.xlim(28.4,98.4)
        else:
            plt.xlim(30.,100.)

    plt.ylim(-0.02,0.06)


    # find peak
    peak = spec.max()
    v0 = vel[int(np.where(spec==peak)[0])]
    print v0




    #some notation
    cloudx=[v_sys[target],v_sys[target]]
    cloudy=[-0.02,0.06]
    plt.plot(cloudx,cloudy,'m--')
    plt.xlabel("$V_{LSR}(km/s)$")
    plt.ylabel("$Jy/beam$")
#plt.text(9.4,-1.2,"$V_{cloud}$")
#plt.text(-32,4.8,"$SiO$",fontsize=15)
#plt.text(-85,4.8,"$B2$",fontsize=15)



    fig.savefig('new/'+target+'/SiO/'+'spec.eps')






