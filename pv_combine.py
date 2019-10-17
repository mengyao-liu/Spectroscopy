import numpy as np
import aplpy
import matplotlib.pyplot as plt
from astropy.io import fits
plt.clf()


targets = ['C2','C6','C9','B1','B2','H6']
v_sys = {'C2':79,'C9':77.4,'C6':75.4,'B1':27.2,'B2':27.65,'H5':44.7,'H6':45.2}
width = {'C9':77.,'C6':39.,'C2':30.,'B1':44.766677,'B2':35.319,'H5':42.037419,'H6':27.639866}

fig = plt.figure(figsize=(25,40))
#fig.text(0.45,0.93,target,size='xx-large')



i = 0
for y in [0.835,0.672,0.509,0.346,0.183,0.02]:  

    target = targets[i]
        
    # obtain 2D fits from 3D fits
    name = 'IRDC-'+target+'SiOimage'


    #sigma = 0.014
    sigma = 0.02/np.sqrt(width[target])
    levs = np.arange(20)*3*sigma+8*sigma


    f = aplpy.FITSFigure('new/'+target+'/SiO/'+name+'_slicebox0.fits',dimensions=[1,0],subplot=[0.05,y,0.85,0.152], figure=fig)
    f.show_colorscale(cmap='rainbow',aspect='auto',smooth=1)
    f.show_contour(levels=levs,dimensions=[1,0],colors='black',linewidths=0.3)
        
        
    f.show_lines([np.array([[v_sys[target]-60.,v_sys[target]+60.],[0,0]])],linestyles='dashed',edgecolor='m',linewidths=1.0)
    f.show_lines([np.array([[v_sys[target],v_sys[target]],[-30.,30.]])],linestyles='dashed',edgecolor='m',linewidths=1.0)


              
    #f.add_label(64,4,target,size='xx-large',color='k')    
    fig.text(0.065,y+0.142,target,size='xx-large')
    f.add_colorbar()
    #f.colorbar.set_location('top')
    f.colorbar.set_font(size='large')


    f.tick_labels.set_font(size='xx-large')
    f.axis_labels.hide()
        
        
    if i == 6:
        f.axis_labels.show()

    
    
    
   
    i+=1


#fig.text(0.42,0.92,'PV Diagram',size='xx-large')        
fig.savefig('pv_combine.eps')
