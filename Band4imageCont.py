#######################################################################
# SELFCAL CONTINUUM
#######################################################################
# At Band 4 fractional bandwidth is large enough to require 
# nterms = 2

contdata='M17UC1_c3band4.cont.ms'
contspw=''
cell=['0.01arcsec']   
imsize = [2400,2400] # size of image in pixels.
robust=0.5
phasecenter=''
refant = 'DV16'


# If you messed up somehow and need to restart, restore your flags first ;)
flagmanager(vis=contdata,mode='restore',versionname='flagdata_1')
flagdata(vis=contdata,antenna='DA49&DA50')
########################

plotms(vis=contdata,yaxis='amp',xaxis='uvwave',
       avgchannel='60',coloraxis='spw',iteraxis='spw')


# try no multiscale
imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust)+'noscale')
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='data',phasecenter=phasecenter,
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       #scales=[0,5,15],
       savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask='',
       interactive=True,niter=1000000)
# max cycleniter = 1000
# include negative in the cleaning box - negative bowls that emerge with cleaning inside the source is due to multiscale and will be fixed

# Check the model
plotms(vis=contdata,yaxis='amp',xaxis='uvwave',ydatacolumn='model',
       avgchannel='60',coloraxis='spw',iteraxis='spw')


# try multiscale
imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust))
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='data',phasecenter=phasecenter,
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       scales=[0,5,15],
       savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask='',
       interactive=True,niter=1000000)
# max cycleniter = 1000
# include negative in the cleaning box - negative bowls that emerge with cleaning inside the source is due to multiscale and will be fixed

# Check the model
plotms(vis=contdata,yaxis='amp',xaxis='uvwave',ydatacolumn='model',
       avgchannel='60',coloraxis='spw',iteraxis='spw')

# 15000, 0.183


# Because of long baseline, start with global correction
os.system('rm -rf cont_c3band4_pcal1_obs')
gaincal(vis=contdata,caltable='cont_c3band4_pcal1_obs',gaintype='T',
        refant=refant,calmode='p',combine='scan,spw',
        solint='inf',minsnr=2.0,minblperant=6) # minbl: no smaller than 4! default 4. Any ant with bl less than this number will be flagged so...
# no solutions flagged

plotcal(caltable='cont_c3band4_pcal1_obs',xaxis='scan',yaxis='phase',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,-30,30])

plotcal(caltable='cont_c3band4_pcal1_obs',xaxis='scan',yaxis='phase',
        spw='',subplot=111,plotrange=[0,0,-30,30])

applycal(vis=contdata,gaintable=['cont_c3band4_pcal1_obs'],
         interp=['linearPD'],
         spwmap=[[0,0,0,0]],
         calwt=False,flagbackup=False) # calwt should always be False in selfcal. It is True and used in pipeline calibration already.


imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust)+'_p1')
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='corrected',phasecenter=phasecenter,
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       scales=[0,5,15],savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask=imagename.replace('_p1','')+'.mask',
       interactive=True,niter=1000000)

# Application of per obsid correction: some improvement.

#########

# See if per spw has enough signal for scan based, per spw solutions. 

os.system('rm -rf cont_c3band4_pcal2')
gaincal(vis=contdata,caltable='cont_c3band4_pcal2',gaintype='T',
        refant=refant,calmode='p',combine='spw',
        solint='inf',minsnr=2.0,minblperant=6)

plotcal(caltable='cont_c3band4_pcal2',xaxis='scan',yaxis='phase',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,-180,180])

plotcal(caltable='cont_c3band4_pcal2',xaxis='scan',yaxis='snr',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,0,130])

applycal(vis=contdata,
         gaintable=['cont_c3band4_pcal2'],
         interp=['linearperobs'],
         spwmap=[[0,0,0,0]],
         calwt=False,flagbackup=False)

imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust)+'_p2')
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='corrected',phasecenter=phasecenter,
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       scales=[0,5,15],savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask=imagename.replace('_p2','_p1')+'.mask',
       interactive=True,niter=1000000)

########

# First try shorter solint, but combining spw
os.system('rm -rf cont_c3band4_pcal3')
gaincal(vis=contdata,caltable='cont_c3band4_pcal3',gaintype='T',
        refant=refant,calmode='p',combine='spw',
        solint='14s',minsnr=2.0,minblperant=6) # read scan length in listobs, though the first one may be shorter due to slew

plotcal(caltable='cont_c3band4_pcal3',xaxis='time',yaxis='phase',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,-180,180])  # do anything? They are true. Even if they look bad, if snr is high then it is fine.

plotcal(caltable='cont_c3band4_pcal3',xaxis='scan',yaxis='snr',
        spw='',iteration='antenna',subplot=321) # those low snr points in each subfig may be the starting scan after coming back from calibrator and have less time
# DA49,50,63,65 SNR~5


# Since combining spw got mostly good solutions, try not combining spw, but exclude the low S/N spw
os.system('rm -rf cont_c3band4_pcal3_spw')
gaincal(vis=contdata,caltable='cont_c3band4_pcal3_spw',gaintype='T',
        refant=refant,calmode='p',combine='',spw='0,1,3',
        solint='14s',minsnr=2.0,minblperant=6)

plotcal(caltable='cont_c3band4_pcal3_spw',xaxis='time',yaxis='phase',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,-180,180])

plotcal(caltable='cont_c3band4_pcal3_spw',xaxis='scan',yaxis='snr',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,0,30])
# DA42,49,50,59,61,63,65 SNR~5


# The shorter time with independent spw doesn't seem to have quite enough 
# S/N, so decided to use just the shorter solint with combined spw.

applycal(vis=contdata,
         gaintable=['cont_c3band4_pcal3'],
         interp=['linearperobs'],
         spwmap=[[0,0,0,0]],
         calwt=False,flagbackup=False)

imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust)+'_p3')
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='corrected',phasecenter=phasecenter,
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       scales=[0,5,15],savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask=imagename.replace('_p3','_p2')+'.mask',
       interactive=True,niter=1000000)


# Substantial improvement again
# Note the final cleaned flux from the casa logger:
# 2018-12-19 22:29:25 INFO task_tclean	[M17UC1_c3band4.continuum_multiR0.5_p3] Total Model Flux : 0.202686(tt0)-0.0886556(tt1)


############################################
# Attempt amplitude selfcal
############################################

# Back up the continuum dataset so that _pcal3 contains the final phase model in case of restart.
os.system('cp -r '+contdata+' '+contdata+'_pcal3')

# Need to judge how much of the total flux is represented in the image model
# check upon where the model match the data, may not reach the shortest point
plotms(vis=contdata,yaxis='amp',xaxis='uvwave',avgtime='14',ydatacolumn='model',
       avgchannel='60',coloraxis='spw',spw='0,1,3')
# peak: 0.2-0.205  

plotms(vis=contdata,yaxis='amp',xaxis='uvwave',avgtime='14',ydatacolumn='corrected',
       avgchannel='60',coloraxis='spw',spw='0,1,3')
# peak: ~0.2

# apply the phase-only solutions before solving for amplitudes.
# Try using the scan length but solving the 3 wide spws independently.
# The independent spw was noisy so repeated with combine='spw'.
os.system('rm -rf cont_c3band4_apcal')
gaincal(vis=contdata,caltable='cont_c3band4_apcal',gaintype='T',
        gaintable=['cont_c3band4_pcal3'],
        interp=['linearperobs'],
        spwmap=[[0,0,0,0]],
        refant=refant,calmode='ap',combine='spw',spw='0,1,3',
        solint='inf',minsnr=3.0,minblperant=6)

os.system('rm -rf cont_c3band4_apcal_uv')
gaincal(vis=contdata,caltable='cont_c3band4_apcal_uv',gaintype='T',
        gaintable=['cont_c3band4_pcal3'],
        interp=['linearperobs'],
        spwmap=[[0,0,0,0]],
        uvrange='>140klambda', # plotms amp vs uvwave sparse. This is long baseline data so there is not enough short baseline spacing
# very long baseline also sparse, can we exclude those for amp cal too? will that influence the final reso? may flag the long baseline ant and will influence the reso
        refant=refant,calmode='ap',combine='spw',spw='0,1,3',
        solint='inf',minsnr=3.0,minblperant=6)


plotcal(caltable='cont_c3band4_apcal',xaxis='scan',yaxis='phase',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,-180,180])

plotcal(caltable='cont_c3band4_apcal',xaxis='scan',yaxis='amp',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,0.7,1.3])
# DV02, DV03, PM02 points ~0.7-0.8

plotcal(caltable='cont_c3band4_apcal',xaxis='scan',yaxis='snr',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,0,0])
# DA49,DA50,DA63,DA65 very low ~5, most distant ant

plotcal(caltable='cont_c3band4_apcal',xaxis='scan',yaxis='amp',
        spw='',subplot=111)
# 0.7-1.5  symmetric about 1

plotcal(caltable='cont_c3band4_apcal_uv',xaxis='scan',yaxis='phase',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,-180,180])

plotcal(caltable='cont_c3band4_apcal_uv',xaxis='scan',yaxis='amp',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,0.7,1.3])
# DV02,DV03,PM02 some outlier points ~0.7-0.8
# flag DV02 at scan 36,56,60,84; DV03 at scan 33,36,60; PM02 at scan 24,25,52,65,83

plotcal(caltable='cont_c3band4_apcal_uv',xaxis='scan',yaxis='snr',
        spw='',iteration='antenna',subplot=321,plotrange=[0,0,0,0])
# DA49,DA65 low, DA50,DA63 very low

plotcal(caltable='cont_c3band4_apcal_uv',xaxis='scan',yaxis='amp',
        spw='',subplot=111) 
# 0.7-1.7
# flag DA50 at scan 56  0.7-1.3


applycal(vis=contdata,
         gaintable=['cont_c3band4_pcal3','cont_c3band4_apcal_uv'],
         interp=['linearperobs','linearperobs'],
         spwmap=[[0,0,0,0],[0,0,0,0]],
         calwt=False,flagbackup=False)
# [4*[0],4*[0],4*[0]]


# this step should happen before applycal???
# flag outliers? pay attention to systematic   
plotms(vis=contdata,yaxis='amp',xaxis='uvwave',avgtime='14',ydatacolumn='corrected',
       avgchannel='60',coloraxis='spw',spw='0,1,3')


imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust)+'_ap')
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='corrected',phasecenter=phasecenter,
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       scales=[0,5,15],savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask=imagename.replace('_ap','_p3')+'.mask',
       interactive=True,niter=1000000)



# compare the uv coverage of Band 6 and Band 4 to make the image with the same uvrange
contdata='M17UC1_c3band4.cont.ms'
plotms(vis=contdata,yaxis='amp',xaxis='uvwave',avgtime='14',ydatacolumn='corrected',
       avgchannel='60',coloraxis='spw',spw='',plotfile='Band4_plotms.png')
plotms(vis=contdata,yaxis='amp',xaxis='uvwave',avgtime='14',ydatacolumn='corrected',
       avgchannel='60',coloraxis='spw',spw='',plotrange=[0,500000,0,0],plotfile='Band4_plotms_500klambda.png')



# make an image with uv>19k
contdata='M17UC1_c3band4.cont.ms'
imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust)+'_ap_19kuv')
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='corrected',phasecenter=phasecenter,uvrange='>19klambda',
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       scales=[0,5,15],savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask=imagename.replace('_ap_19kuv','_ap')+'.mask',
       interactive=True,niter=1000000)



# make an image with uv>210k to cross check the flux
contdata='M17UC1_c3band4.cont.ms'
imagename=contdata.replace('.ms', 'inuum_multiR'+str(robust)+'_ap_210kuv')
os.system('rm -rf '+imagename+'.*')
tclean(vis=contdata,
       imagename=imagename,
       imsize=imsize,cell=cell,spw=contspw,
       datacolumn='corrected',phasecenter=phasecenter,uvrange='>210klambda',
       specmode='mfs',deconvolver='mtmfs',nterms=2,
       scales=[0,5,15],savemodel='modelcolumn',
       weighting='briggs',robust=robust,gridder='standard',
       mask=imagename.replace('_ap_210kuv','_ap')+'.mask',
       interactive=True,niter=1000000)






# Example to flag DV03 completely, probably want to do the same flag to line data
# flagdata(vis=contdata,antenna='DV03')



# Plot Band 4 and 6 UV coverage
plotms(vis=B4,yaxis='amp',xaxis='uvwave',uvrange='40~590klambda',avgchannel='60',avgtime='60',gridrows=2,title='Band 4',spw='0,1,3') 

plotms(vis=B6,yaxis='amp',xaxis='uvwave',uvrange='40~590klambda',avgchannel='60',avgtime='60',gridrows=2,title='Band 6',spw='1~3,5~7',clearplots=False,rowindex=1,plotindex=1,plotfile='B4B6_uvcoverage.png')



