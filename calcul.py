import numpy as np
import aplpy
import matplotlib.pyplot as plt
from astropy.io import fits

targets = ['B1','B2','C2','C6','C9','H6']
velocity = {'sys':{'C2':79,'C9':77.4,'C6':75.4,'B1':27.2,'B2':26.0,'H5':44.7,'H6':45.2},'blue1':{'C2':65,'C9':60.,'C6':60,'B1':21,'B2':21.,'H5':28.4,'H6':40},'blue2':{'C2':76,'C9':74.4,'C6':72.4,'B1':24.2,'B2':23.,'H5':41.7,'H6':42.2},'red1':{'C2':82,'C9':80.4,'C6':78.4,'B1':30.2,'B2':29.,'H5':47.7,'H6':48.2},'red2':{'C2':95,'C9':100.,'C6':90,'B1':80,'B2':45,'H5':75,'H6':70}}
width = {'C9':77.,'C6':39.,'C2':30.,'B1':44.766677,'B2':52.,'H5':42.037419,'H6':27.639866}   #image
boxl = {'C9':25.495132,'C6':12.625,'C2':8.80358,'B1':12.9287,'B2':12.9,'H5':11.4411,'H6':4.11749}    #"
redl = {'B1':11.23,'B2':12.9,'C9':16.18,'C6':3.25,'C2':3.36,'H6':2.75}
bluel = {'B1':2.85,'B2':6.75,'C9':8.39,'C6':8.75,'C2':4.98,'H6':0.01}
distance = {'C9':5.0,'C6':5.0,'C2':5.0,'B1':2.4,'B2':2.4,'H5':2.9,'H6':2.9,'A2':4.8}  #kpc
T_ex = 18.
E_upper = 31.259 # K
pixel = 0.125 #"
beam = 1.24*0.78*np.pi/4./np.log(2)
# freq = 217.10498 GHz
# abundace_ratio = 1e9
# m_H2 = 2*1.674e-24g
# miu = 1.36
# tau/1-exp(-tau) = tau
# mu_d = 3.098 D  1 D = 1e-18 statC*cm
# A = 0.00051967
# Q_rot = 1.2632
# 1 Jy = 1e-23 ergs/s/cm^2/Hz
# Qiu 3*1.38065**2*3.**2*1.36*1.674*3.085677**2/(np.pi**4*6.62607*3.098**2*217.10498**4)*1e-9 = 8.1e-20
# 4pi/(h*c*Aul)*Q_rot/gu = 4.*np.pi*1.2632/(11.*0.00051967*6.62607e-27*3e10) = 1.3969613010671876e+19
# 1.36*1e9*2*1.67353e-24*3.08567758e21**2*1e-23*1e5/2e33 = 2.1670727963803464e-23


f = open('property.txt','w')

for i in range(6):
    target = targets[i]
    if target == 'B2':
        name = 'IRDC-B2largeSiOimage'
    else:
        name = 'IRDC-'+target+'SiOimage'
    data, hdr = fits.getdata('new/'+target+'/SiO/'+name+'_slicebox_totalvel.fits', 0, header = True)
    # data.shape (400,204)

    D = distance[target]                  # kpc
    length = boxl[target]*D*1e3/206265.   # pc

    vpix = int(hdr['CRPIX2'])
    vref = hdr['CRVAL2']*1e-3
    delv = hdr['CDELT2']*1e-3
   


    v1 = velocity['blue1'][target]
    v2 = velocity['blue2'][target]
    startblue = int((v1-vref)/delv)+vpix-1
    endblue = int((v2-vref)/delv)+vpix-1
    v3 = velocity['red1'][target]
    v4 = velocity['red2'][target]
    startred = int((v3-vref)/delv)+vpix-1
    endred = int((v4-vref)/delv)+vpix-1


    data = data*width[target]
    fluxb = data.sum(1)[startblue:endblue+1]
    vb_channel = np.arange(endblue-startblue+1)*delv+v1
    vb = abs(vb_channel-velocity['sys'][target])
    fluxr = data.sum(1)[startred:endred+1]
    vr_channel = np.arange(endred-startred+1)*delv+v1
    vr = abs(vr_channel-velocity['sys'][target])
    print np.sum(data.sum(1)[startblue:endred+1])*abs(delv)*pixel**2/beam  # Jy km/s




    mass_blue = np.exp(E_upper/T_ex)*D**2*pixel**2/beam*np.sum(fluxb)*abs(delv)*1.397*2.167e-4
    mass_red = np.exp(E_upper/T_ex)*D**2*pixel**2/beam*np.sum(fluxr)*abs(delv)*1.397*2.167e-4
    moment = np.exp(E_upper/T_ex)*D**2*pixel**2/beam*np.sum(fluxb*vb)*abs(delv)*1.397*2.167e-4 + np.exp(E_upper/T_ex)*D**2*pixel**2/beam*np.sum(fluxr*vr)*abs(delv)*1.397*2.167e-4
    energy = np.exp(E_upper/T_ex)*D**2*pixel**2/beam*np.sum(fluxb*vb**2)*abs(delv)*1.397*2.167e-4 + np.exp(E_upper/T_ex)*D**2*pixel**2/beam*np.sum(fluxr*vr**2)*abs(delv)*1.397*2.167e-4    # 1e43
    # lum = (T_ex+0.92)*np.exp(16.59/T_ex)*D**2*tau*pixel**2*np.sum(lalala*v**3)*abs(delv)/(2.0*R)*eff0/eff*4.2e-8*const
    t_dyn_blue = bluel[target]*distance[target]/(velocity['sys'][target]-velocity['blue1'][target])*4740.47*1e-3  # 1e3
    t_dyn_red = redl[target]*distance[target]/(velocity['red2'][target]-velocity['sys'][target])*4740.47*1e-3   # 1e3
    M_dot = (mass_blue/t_dyn_blue+mass_red/t_dyn_red)*10.   # 1e-4
    P_dot = moment/((t_dyn_blue+t_dyn_red)/2.)*10.   # 1e-4
     


    print >> f,target,'&','%0.3f'%mass_blue,'&','%0.2f'%(bluel[target]*distance[target]*1e3/206265.),'&','%0.2f'%t_dyn_blue,'&','%0.3f'%mass_red,'&','%0.2f'%(redl[target]*distance[target]*1e3/206265.),'&','%0.2f'%t_dyn_red,'&','%0.2f'%(mass_blue+mass_red),'&','%0.2f'%moment,'&','%0.2f'%energy,'&','%0.2f'%M_dot,'&','%0.2f'%P_dot,'\\\\'


f.close()


