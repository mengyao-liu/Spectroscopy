'''
25 	25 	X1075110361#ALMA_RB_04#BB_1#SW-01 	FDM 	132.154 GHz 	133.092 GHz 	134.029 GHz 	1.875 GHz 	LSB_Continuum(ID=0) 	480 	3.906 MHz 	8.799 km/s
27 	27 	X1075110361#ALMA_RB_04#BB_2#SW-01 	FDM 	134.050 GHz 	134.987 GHz 	135.925 GHz 	1.875 GHz 	LSB_Continuum(ID=0) 	480 	3.906 MHz 	8.675 km/s
29 	29 	X1075110361#ALMA_RB_04#BB_3#SW-01 	FDM 	146.969 GHz 	147.086 GHz 	147.203 GHz 	234.375 MHz 	CH3CN_v_0_8_5__7_5___F_9_8 	1920 	122.070 kHz 248.805 m/s
31 	31 	X1075110361#ALMA_RB_04#BB_4#SW-01 	FDM 	144.237 GHz 	145.175 GHz 	146.112 GHz 	1.875 GHz 	USB_Continuum(ID=0) 	480 	3.906 MHz 	8.067 km/s

  3    M17UC1        0      25    133105         23                     
  3    M17UC1        1      27    135005         23                  
  3    M17UC1        2      29    147103.902     23           
  3    M17UC1        3      31    145200         23           
'''


linedata='M17UC1_c3band4.ms.contsub'
applycal(vis=linedata,
         gaintable=['cont_c3band4_pcal3','cont_c3band4_apcal_uv'],
         interp=['linearperobs','linearperobs'],
         spwmap=[[0,0,0,0],[0,0,0,0]],
         calwt=False,flagbackup=False)

# spw 29
cell=['0.01arcsec']   
imsize = [1000,1000]
robust=1.0
velstart='-215.0km/s'
chans=952
width='0.5km/s'
outframe='LSRK'
threshold='10.0mJy'
data='M17UC1_c3band4.ms.contsub'
spw='2'
molename='CH3CN8_7'
restfreq='147103.902MHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=False,niter=0,threshold=threshold)




# spw 25
cell=['0.01arcsec']   
imsize = [1000,1000]
robust=1.0
velstart='-2082.0km/s'
chans=419
width='10.0km/s'
outframe='LSRK'
threshold='10.0mJy'
data='M17UC1_c3band4.ms.contsub'
spw='0'
molename='spw25'
restfreq='133105MHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=False,niter=0,threshold=threshold)



# spw 27
cell=['0.01arcsec']   
imsize = [1000,1000]
robust=1.0
velstart='-2043.0km/s'
chans=413
width='10.0km/s'
outframe='LSRK'
threshold='10.0mJy'
data='M17UC1_c3band4.ms.contsub'
spw='1'
molename='spw27'
restfreq='135005MHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=False,niter=0,threshold=threshold)


# spw 31
cell=['0.01arcsec']   
imsize = [1000,1000]
robust=1.0
velstart='-1885.0km/s'
chans=384
width='10.0km/s'
outframe='LSRK'
threshold='10.0mJy'
data='M17UC1_c3band4.ms.contsub'
spw='3'
molename='spw31'
restfreq='145200MHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',-
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=False,niter=0,threshold=threshold)


#############################################################
# Small line cubes in spw29


cell=['0.01arcsec']   
imsize = [1000,1000]
robust=1.0
velstart='10.0km/s'
chans=40
width='0.5km/s'
outframe='LSRK'
threshold='0mJy'
data='M17UC1_c3band4.ms.contsub'
spw='2'
molename='CH3CN_K2'
restfreq='147.16324410GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=True,niter=1000000,threshold=threshold)

immoments(imagename=imagename,outfile='mom0_30-100_IRDC-C9SiOimage.image.ex',chans='0~350',moments=[0],excludepix=excludepix)



molename='CH3CN_K3'
restfreq='147.14906830GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',uvtaper='',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=True,niter=1000000,threshold=threshold)


molename='CH3CN_K4'
restfreq='147.12923020GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',uvtaper='',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=True,niter=1000000,threshold=threshold)

molename='CH3CN_K5'
restfreq='147.10373800GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',uvtaper='',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',
      interactive=True,niter=1000000,threshold=threshold)

#############################################################
# Use uvtaper to increase sensitivity


plotms(vis=data,yaxis='amp',xaxis='uvwave',
       avgchannel='60',spw='2')


molename='CH3CN_K5'
restfreq='147.10373800GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper5200k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='5200klambda',
      interactive=True,niter=1000000,threshold=threshold)
immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K5_taper5200k.image',chans='12~28',moments=[0])



molename='CH3CN_K5'
restfreq='147.10373800GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper4000k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='4000klambda',
      interactive=True,niter=1000000,threshold=threshold)
immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K5_taper4000k.image',chans='12~28',moments=[0])



molename='CH3CN_K5'
restfreq='147.10373800GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper4500k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='4500klambda',
      interactive=True,niter=1000000,threshold=threshold)
immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K5_taper4500k.image',chans='12~28',moments=[0])



molename='CH3CN_K4'
restfreq='147.12923020GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper5200k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='5200klambda',
      interactive=True,niter=1000000,threshold=threshold)
immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K4_taper5200k.image',chans='12~28',moments=[0])



molename='CH3CN_K4'
restfreq='147.12923020GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper4000k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='4000klambda',
      interactive=True,niter=1000000,threshold=threshold)
immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K4_taper4000k.image',chans='12~28',moments=[0])



molename='CH3CN_K4'
restfreq='147.12923020GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper4500k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='4500klambda',
      interactive=True,niter=1000000,threshold=threshold)
immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K4_taper4500k.image',chans='12~28',moments=[0])



molename='CH3CN_K4'
restfreq='147.12923020GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper5000k'
os.system('rm -rf '+imagename+'.*')

tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='5000klambda',
      interactive=True,niter=1000000,threshold=threshold)
immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K4_taper5000k.image',chans='12~28',moments=[0])

 
# Maybe 4500 the best?  5200 very similar to 5000. peak 4500>4000>5200>5000>none  rms similar

molename='CH3CN_K2'
restfreq='147.16324410GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper5200k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='5200klambda',
      interactive=True,niter=1000000,threshold=threshold)

immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K2_taper5200k.image',chans='12~28',moments=[0])
exportfits(imagename='mom0_16-24_CH3CN_K2_taper5200k.image', fitsimage='mom0_16-24_CH3CN_K2_taper5200k.image.fits',velocity=True,overwrite=True)


molename='CH3CN_K2'
restfreq='147.16324410GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper4500k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='4500klambda',
      interactive=True,niter=1000000,threshold=threshold)

immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K2_taper4500k.image',chans='12~28',moments=[0])





molename='CH3CN_K3'
restfreq='147.14906830GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper5200k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,199343

      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='5200klambda',
      interactive=True,niter=1000000,threshold=threshold)

immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K3_taper5200k.image',chans='12~28',moments=[0])


molename='CH3CN_K3'
restfreq='147.14906830GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_taper4500k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='4500klambda',
      interactive=True,niter=1000000,threshold=threshold)

immoments(imagename=imagename+'.image',outfile='mom0_16-24_CH3CN_K3_taper4500k.image',chans='12~28',moments=[0])



# make a cube of CH3CN8_7 K=0,1,2,3,4,5 together
cell=['0.01arcsec']   
imsize = [1000,1000]
robust=1.0
velstart='-50.0km/s'
chans=420
width='0.5km/s'
outframe='LSRK'
threshold='0mJy'
data='M17UC1_c3band4.ms.contsub'
spw='2'
molename='CH3CN8_7'
restfreq='147.14906830GHz' # K3
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_clean'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='',
      interactive=True,niter=1000000,threshold=threshold)



imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_clean_taper4500k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='4500klambda',
      interactive=True,niter=1000000,threshold=threshold)


# make a cube for H35 alpha

cell=['0.01arcsec']   
imsize = [1000,1000]
robust=1.0
velstart='-30.0km/s'
chans=50
width='2km/s'
outframe='LSRK'
threshold='0mJy'
data='M17UC1_c3band4.ms.contsub'
spw='2'
molename='H35alpha'
restfreq='147.04687800GHz'
imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_clean'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='',uvtaper='', # mask should not exceed the continuum
      interactive=True,niter=1000000,threshold=threshold)


imagename=data.replace('.ms.contsub','.contsub_')+molename+'_'+restfreq+'_clean_taper4500k'
os.system('rm -rf '+imagename+'.*')
tclean(vis=data,
      imagename=imagename,observation='',spw=spw,
      imsize=imsize,cell=cell,
      gridder='standard',restoringbeam='common',
      weighting='briggs',robust=robust,datacolumn='corrected',
      specmode='cube',start=velstart,nchan=chans,width=width,interpolation='nearest',
      restfreq=restfreq,outframe=outframe,chanchunks=-1,
      mask='M17UC1_c3band4.contsub_H35alpha_147.04687800GHz_clean.mask',uvtaper='4500klambda', # same mask
      interactive=True,niter=1000000,threshold=threshold)

















