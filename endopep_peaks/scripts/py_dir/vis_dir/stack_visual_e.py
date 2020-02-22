import os
import sys
import argparse
import subprocess
import re
import glob
import shlex
import operator
from collections import defaultdict
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import ListedColormap, LinearSegmentedColormap, Normalize
import matplotlib.patches as patches
from mpl_toolkits.axes_grid1 import make_axes_locatable


df_0 = pd.read_csv("endo.csv")
df_00 = pd.read_csv("~/endopep_peaks/scripts/py_dir/vis_dir/reference.csv")
df = pd.concat([df_00,df_0],ignore_index=True)

fig, axes = plt.subplots(nrows=3,ncols=1, sharex=True)

######
# e1 #
######

df_7 = df[['bot_id','Peak_1_E','sn_Peak_1_E']]
df_7.set_index('bot_id', inplace=True)
df_7['sn_Peak_1_E'] = df_7['sn_Peak_1_E'].fillna(df_7['sn_Peak_1_E'].min())
df_7 = df_7.round(3)
print(df_7)

z6 = df_7['sn_Peak_1_E'].min()
print(z6)
df_7['sn_Peak_1_E'] = np.where(df_7['sn_Peak_1_E']==0, z6, df_7['sn_Peak_1_E'])
print(df_7)

#fig_a3, ax_a3 = plt.subplots()
colormap_3 = LinearSegmentedColormap.from_list('colorbar', ['#FFCC66','#FFCC00'], N=1000)
norm_e = Normalize(vmin=min(df_7['sn_Peak_1_E']),vmax=max(df_7['sn_Peak_1_E']))
colors = [colormap_3(norm_e(v)) for v in df_7['sn_Peak_1_E']]
plot_7 = df_7['Peak_1_E'].plot(ax=axes[0],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([1129.200,1133.800])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

######
# e2 #
######

df_8 = df[['bot_id','Peak_2_E','sn_Peak_2_E']]
df_8.set_index('bot_id', inplace=True)
df_8['sn_Peak_2_E'] = df_8['sn_Peak_2_E'].fillna(df_8['sn_Peak_2_E'].min())
df_8 = df_8.round(3)
print(df_8)

z7 = df_8['sn_Peak_2_E'].min()
print(z7)
df_8['sn_Peak_2_E'] = np.where(df_8['sn_Peak_2_E']==0, z7, df_8['sn_Peak_2_E'])
print(df_8)

#fig_a3, ax_a3 = plt.subplots()
colormap_3 = LinearSegmentedColormap.from_list('colorbar', ['#FFCC66','#FFCC00'], N=1000)
norm_e2 = Normalize(vmin=min(df_8['sn_Peak_2_E']),vmax=max(df_8['sn_Peak_2_E']))
colors = [colormap_3(norm_e2(v)) for v in df_8['sn_Peak_2_E']]
plot_8 = df_8['Peak_2_E'].plot(ax=axes[1],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([2493.600,2503.600])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

######
# ie #
######

df_9 = df[['bot_id','Intact_E','sn_Intact_E']]
df_9.set_index('bot_id', inplace=True)
df_9['sn_Intact_E'] = df_9['sn_Intact_E'].fillna(df_9['sn_Intact_E'].min())
df_9 = df_9.round(3)
print(df_9)

z8 = df_9['sn_Intact_E'].min()
print(z8)
df_9['sn_Intact_E'] = np.where(df_9['sn_Intact_E']==0, z8, df_9['sn_Intact_E'])
print(df_9)

#fig_a3, ax_a3 = plt.subplots()
colormap_3 = LinearSegmentedColormap.from_list('colorbar', ['#FFCC66','#FFCC00'], N=1000)
norm_e3 = Normalize(vmin=min(df_9['sn_Intact_E']),vmax=max(df_9['sn_Intact_E']))
colors = [colormap_3(norm_e3(v)) for v in df_9['sn_Intact_E']]
plot_9 = df_9['Intact_E'].plot(ax=axes[2],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([3607.800,3622.200])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

############
# together #
############

axes[0].set_title('Peak_1_E', fontsize=7, loc='left')
axes[0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[1].set_title('Peak_2_E', fontsize=7, loc='left')
axes[1].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[2].set_title('Intact_E', fontsize=7, loc='left')
axes[2].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=True)
axes[2].get_xticklabels()[0].set_color('red')
axes[2].get_xticklabels()[1].set_color('red')
axes[2].get_xticklabels()[2].set_color('red')
axes[0].tick_params(axis='y', labelsize=7)
axes[1].tick_params(axis='y', labelsize=7)
axes[2].tick_params(axis='y', labelsize=7)

x_axis = axes[2].axes.get_xaxis()
x_axis.set_label_text('bot_id')
x_label = x_axis.get_label()
x_label.set_visible(False)

axes[0].set_facecolor('#D4D4D4')
axes[1].set_facecolor('#D4D4D4')
axes[2].set_facecolor('#D4D4D4')


fig.set_facecolor('#ECECEC')
lower_bg_1 = patches.Rectangle((0, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_2 = patches.Rectangle((0.25, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_3 = patches.Rectangle((0.50, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_4 = patches.Rectangle((0.75, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
lower_bg_5 = patches.Rectangle((0, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_6 = patches.Rectangle((0.25, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_7 = patches.Rectangle((0.50, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_8 = patches.Rectangle((0.75, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
fig.patches.extend([lower_bg_1,lower_bg_2,lower_bg_3,lower_bg_4,\
lower_bg_5,lower_bg_6,lower_bg_7,lower_bg_8])

fig.text(0.0,0.003, '*Reference measurements are mean values of specimen-type validations.', fontsize=6)
fig.suptitle('Peak Values', fontsize=10,x=0.5 ,y=1, weight='bold')
fig.tight_layout()


date = time.strftime("%m.%d.%Y")
fig.savefig('Peak_Values'+'_'+date+'.png',dpi=900)
#mng = plt.get_current_fig_manager()
#mng.window.showMaximized()
#plt.show()

###########################
# Separate colorbar plots #
###########################

fig_2, axc = plt.subplots(nrows=1,ncols=3,constrained_layout=False, sharex=True)

### e1 ###
sm_7 = plt.cm.ScalarMappable(cmap=colormap_3, norm=norm_e)
sm_7.set_array([])
c7 = plt.colorbar(sm_7,ax=axc[0],pad=0.05 ,orientation='vertical')
c7.set_label('Peak_1_E', fontsize=7)

### e2 ###
sm_8 = plt.cm.ScalarMappable(cmap=colormap_3, norm=norm_e2)
sm_8.set_array([])
c8 = plt.colorbar(sm_8,ax=axc[1],pad=0.05 ,orientation='vertical')
c8.set_label('Peak_2_E', fontsize=7)

### ie ###
sm_9 = plt.cm.ScalarMappable(cmap=colormap_3, norm=norm_e3)
sm_9.set_array([])
c9 = plt.colorbar(sm_9,ax=axc[2],pad=0.05 ,orientation='vertical')
c9.set_label('Intact_E', fontsize=7)

fig_2.delaxes(axc[0])
fig_2.delaxes(axc[1])
fig_2.delaxes(axc[2])
fig_2.suptitle('SN Gradient Legend', fontsize=10, y=1, weight='bold')

fig_2.set_facecolor('#D4D4D4')
lower_bg_1 = patches.Rectangle((0, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_2 = patches.Rectangle((0.25, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_3 = patches.Rectangle((0.50, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_4 = patches.Rectangle((0.75, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
lower_bg_5 = patches.Rectangle((0, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_6 = patches.Rectangle((0.25, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_7 = patches.Rectangle((0.50, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_8 = patches.Rectangle((0.75, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
fig_2.patches.extend([lower_bg_1,lower_bg_2,lower_bg_3,lower_bg_4,\
lower_bg_5,lower_bg_6,lower_bg_7,lower_bg_8])
fig_2.tight_layout()


#mng = plt.get_current_fig_manager()
#mng.window.showMaximized()
fig_2.savefig('SN_Gradient_Legend'+'_'+date+'.png',dpi=900)
plt.show()
