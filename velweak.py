# Identify the line association and peak velocity with each 1.3mm continuum core within the "core region" defined by 3"x3" square centered at the continuum core.
# Threshold: there are more than 3 channels with signal above 2 sigma noise level, and the peak channel as well as its neighbor channels has signal above 2 sigma noise level
# We record the peak velocity of each line and take the mean value as the systematic velocity of the core.
import numpy as np
import matplotlib
from astropy.io import fits
from astropy import wcs
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.stats import sigma_clip
import glob


lines = ['DCN32','DCOp32','C18O21','CH3OH54','N2Dp32']
contin = np.loadtxt('output_coremass.txt',usecols=(0,2,4),dtype={'names': ('source','l','b'), 'formats': ('U2',np.float,np.float)})


velocity = np.zeros(shape=(len(lines),len(contin['source'])))
weird = np.array([])


for j in np.arange(len(lines)):
    line = lines[j]
    if line != 'N2Dp32':
        targets = glob.glob('IRDC*'+line+'*image.fits')
    else:
    	targets = glob.glob('IRDC*'+line+'*0dot2kms.fits')
    targets = np.sort(targets)
    print(len(targets))
    k = 0
    for target in targets:
        data, hdr = fits.getdata(target, 0, header = True)
        delt = abs(hdr['CDELT1'])*3600.
        vref = hdr['CRVAL3']*1e-3
        vpix = int(hdr['CRPIX3'])
        delv = hdr['CDELT3']*1e-3     
 

        w = wcs.WCS(hdr)
        num = np.where(contin['source']==target[5:7])
        for i in num[0]:
            c = SkyCoord(contin['l'][i], contin['b'][i], frame='galactic',unit=(u.deg, u.deg))
            ra = c.fk5.ra.degree
            dec = c.fk5.dec.degree   
            contin_pix = w.wcs_world2pix(ra, dec,0,0,0)[0:2]

            chip_3d = data[0, :, int(np.round(contin_pix[1]-1.5/delt)):(int(np.round(contin_pix[1]+1.5/delt))+1), int(np.round(contin_pix[0]-1.5/delt)):(int(np.round(contin_pix[0]+1.5/delt))+1)]
            chip_2d = chip_3d.mean(2)
            chip = chip_2d.mean(1)



            filtered_chip = sigma_clip(chip, 2, 5)   # 2 sigma, 5 iteration
            print(np.size(chip),np.ma.count(filtered_chip))
            noise = np.std(filtered_chip)
            index = np.where(chip==np.max(chip))[0]
            signal_chan = np.where(chip > 2*noise)[0]    
            if all([index>0, index<np.size(chip)-1, np.size(signal_chan)>=3]):
                if chip[index-1] > 2*noise   or  chip[index+1] > 2*noise  :               
                    if not np.ma.is_masked(filtered_chip[index]):
                        print('WEIRD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        weird = np.append(weird, [contin['source'][k],contin['l'][k],index,filtered_chip])
                    vel = (index+1-vpix)*delv+vref
                    velocity[j,k] = vel
                
            k+=1




f = open('velweak.dat','w')
for k in np.arange(np.shape(velocity)[1]):
    velarr = velocity[0:3,k]
    print(contin['source'][k],contin['l'][k],velocity[:,k],np.mean(velarr[velarr>0]),file=f)




f.close()





