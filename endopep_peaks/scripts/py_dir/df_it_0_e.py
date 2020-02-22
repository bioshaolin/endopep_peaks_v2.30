import os
import sys
import subprocess
import re
import glob
import shlex
import operator
from collections import defaultdict
import pandas as pd
import numpy as np

##########################
# RESTRUCTURE CHAIN DATA #
##########################

e = open("e_out.txt", "r")

#######
#  E  #
#######

	############
	# read_csv #
	############

df_e = pd.read_csv(e, sep="\t", header=None, names=['date','plate','bot_id','test','peak_1','sn_1','peak_2','sn_2','peak_3','sn_3',\
'peak_4','sn_4','peak_5','sn_5','peak_6','sn_6'])
print(df_e)
df_e1 = df_e.round(decimals=12)

		##light_chain##
df_e1.insert(16, 'LC1', np.where(np.logical_and(df_e1['peak_1']>=1129.200000000000,df_e1['peak_1']<=1133.800000000000) , df_e1['peak_1'], ""))
df_e1.insert(17, 'sn_L_1', np.where(np.logical_and(df_e1['peak_1']>=1129.200000000000,df_e1['peak_1']<=1133.800000000000) , df_e1['sn_1'], ""))
df_e1.insert(18, 'LC2', np.where(np.logical_and(df_e1['peak_2']>=1129.200000000000,df_e1['peak_2']<=1133.800000000000) , df_e1['peak_2'], ""))
df_e1.insert(19, 'sn_L_2', np.where(np.logical_and(df_e1['peak_2']>=1129.200000000000,df_e1['peak_2']<=1133.800000000000) , df_e1['sn_2'], ""))
df_e1.insert(20, 'LC3', np.where(np.logical_and(df_e1['peak_3']>=1129.200000000000,df_e1['peak_3']<=1133.800000000000) , df_e1['peak_3'], ""))
df_e1.insert(21, 'sn_L_3', np.where(np.logical_and(df_e1['peak_3']>=1129.200000000000,df_e1['peak_3']<=1133.800000000000) , df_e1['sn_3'], ""))
df_e1.insert(22, 'LC4', np.where(np.logical_and(df_e1['peak_4']>=1129.200000000000,df_e1['peak_4']<=1133.800000000000) , df_e1['peak_4'], ""))
df_e1.insert(23, 'sn_L_4', np.where(np.logical_and(df_e1['peak_4']>=1129.200000000000,df_e1['peak_4']<=1133.800000000000) , df_e1['sn_4'], ""))
df_e1.insert(24, 'LC5', np.where(np.logical_and(df_e1['peak_5']>=1129.200000000000,df_e1['peak_5']<=1133.800000000000) , df_e1['peak_5'], ""))
df_e1.insert(25, 'sn_L_5', np.where(np.logical_and(df_e1['peak_5']>=1129.200000000000,df_e1['peak_5']<=1133.800000000000) , df_e1['sn_5'], ""))
df_e1.insert(26, 'LC6', np.where(np.logical_and(df_e1['peak_6']>=1129.200000000000,df_e1['peak_6']<=1133.800000000000) , df_e1['peak_6'], ""))
df_e1.insert(27, 'sn_L_6', np.where(np.logical_and(df_e1['peak_6']>=1129.200000000000,df_e1['peak_6']<=1133.800000000000) , df_e1['sn_6'], ""))
		##heavy_chain##
df_e1.insert(28, 'HC1', np.where(np.logical_and(df_e1['peak_1']>=2493.600000000000,df_e1['peak_1']<=2503.600000000000) , df_e1['peak_1'], ""))
df_e1.insert(29, 'sn_H_1', np.where(np.logical_and(df_e1['peak_1']>=2493.600000000000,df_e1['peak_1']<=2503.600000000000) , df_e1['sn_1'], ""))
df_e1.insert(30, 'HC2', np.where(np.logical_and(df_e1['peak_2']>=2493.600000000000,df_e1['peak_2']<=2503.600000000000) , df_e1['peak_2'], ""))
df_e1.insert(31, 'sn_H_2', np.where(np.logical_and(df_e1['peak_2']>=2493.600000000000,df_e1['peak_2']<=2503.600000000000) , df_e1['sn_2'], ""))
df_e1.insert(32, 'HC3', np.where(np.logical_and(df_e1['peak_3']>=2493.600000000000,df_e1['peak_3']<=2503.600000000000) , df_e1['peak_3'], ""))
df_e1.insert(33, 'sn_H_3', np.where(np.logical_and(df_e1['peak_3']>=2493.600000000000,df_e1['peak_3']<=2503.600000000000) , df_e1['sn_3'], ""))
df_e1.insert(34, 'HC4', np.where(np.logical_and(df_e1['peak_4']>=2493.600000000000,df_e1['peak_4']<=2503.600000000000) , df_e1['peak_4'], ""))
df_e1.insert(35, 'sn_H_4', np.where(np.logical_and(df_e1['peak_4']>=2493.600000000000,df_e1['peak_4']<=2503.600000000000) , df_e1['sn_4'], ""))
df_e1.insert(36, 'HC5', np.where(np.logical_and(df_e1['peak_5']>=2493.600000000000,df_e1['peak_5']<=2503.600000000000) , df_e1['peak_5'], ""))
df_e1.insert(37, 'sn_H_5', np.where(np.logical_and(df_e1['peak_5']>=2493.600000000000,df_e1['peak_5']<=2503.600000000000) , df_e1['sn_5'], ""))
df_e1.insert(38, 'HC6', np.where(np.logical_and(df_e1['peak_6']>=2493.600000000000,df_e1['peak_6']<=2503.600000000000) , df_e1['peak_6'], ""))
df_e1.insert(39, 'sn_H_6', np.where(np.logical_and(df_e1['peak_6']>=2493.600000000000,df_e1['peak_6']<=2503.600000000000) , df_e1['sn_6'], ""))
		##intact##
df_e1.insert(40, 'Intact1', np.where(np.logical_and(df_e1['peak_1']>=3607.800000000000,df_e1['peak_1']<=3622.200000000000) , df_e1['peak_1'], ""))
df_e1.insert(41, 'sn_I_1', np.where(np.logical_and(df_e1['peak_1']>=3607.800000000000,df_e1['peak_1']<=3622.200000000000) , df_e1['sn_1'], ""))
df_e1.insert(42, 'Intact2', np.where(np.logical_and(df_e1['peak_2']>=3607.800000000000,df_e1['peak_2']<=3622.200000000000) , df_e1['peak_2'], ""))
df_e1.insert(43, 'sn_I_2', np.where(np.logical_and(df_e1['peak_2']>=3607.800000000000,df_e1['peak_2']<=3622.200000000000) , df_e1['sn_2'], ""))
df_e1.insert(44, 'Intact3', np.where(np.logical_and(df_e1['peak_3']>=3607.800000000000,df_e1['peak_3']<=3622.200000000000) , df_e1['peak_3'], ""))
df_e1.insert(45, 'sn_I_3', np.where(np.logical_and(df_e1['peak_3']>=3607.800000000000,df_e1['peak_3']<=3622.200000000000) , df_e1['sn_3'], ""))
df_e1.insert(46, 'Intact4', np.where(np.logical_and(df_e1['peak_4']>=3607.800000000000,df_e1['peak_4']<=3622.200000000000) , df_e1['peak_4'], ""))
df_e1.insert(47, 'sn_I_4', np.where(np.logical_and(df_e1['peak_4']>=3607.800000000000,df_e1['peak_4']<=3622.200000000000) , df_e1['sn_4'], ""))
df_e1.insert(48, 'Intact5', np.where(np.logical_and(df_e1['peak_5']>=3607.800000000000,df_e1['peak_5']<=3622.200000000000) , df_e1['peak_5'], ""))
df_e1.insert(49, 'sn_I_5', np.where(np.logical_and(df_e1['peak_5']>=3607.800000000000,df_e1['peak_5']<=3622.200000000000) , df_e1['sn_5'], ""))
df_e1.insert(50, 'Intact6', np.where(np.logical_and(df_e1['peak_6']>=3607.800000000000,df_e1['peak_6']<=3622.200000000000) , df_e1['peak_6'], ""))
df_e1.insert(51, 'sn_I_6', np.where(np.logical_and(df_e1['peak_6']>=3607.800000000000,df_e1['peak_6']<=3622.200000000000) , df_e1['sn_6'], ""))
		###a_lc_noise###
df_e1.insert(52, 'a_non_E1', np.where(np.logical_and(df_e1['peak_1']>=0996.800000000000,df_e1['peak_1']<=1000.800000000000) , df_e1['peak_1'], ""))
df_e1.insert(53, 'sn_ae_1', np.where(np.logical_and(df_e1['peak_1']>=0996.800000000000,df_e1['peak_1']<=1000.800000000000) , df_e1['sn_1'], ""))
df_e1.insert(54, 'a_non_E2', np.where(np.logical_and(df_e1['peak_2']>=0996.800000000000,df_e1['peak_2']<=1000.800000000000) , df_e1['peak_2'], ""))
df_e1.insert(55, 'sn_ae_2', np.where(np.logical_and(df_e1['peak_2']>=0996.800000000000,df_e1['peak_2']<=1000.800000000000) , df_e1['sn_2'], ""))
df_e1.insert(56, 'a_non_E3', np.where(np.logical_and(df_e1['peak_3']>=0996.800000000000,df_e1['peak_3']<=1000.800000000000) , df_e1['peak_3'], ""))
df_e1.insert(57, 'sn_ae_3', np.where(np.logical_and(df_e1['peak_3']>=0996.800000000000,df_e1['peak_3']<=1000.800000000000) , df_e1['sn_3'], ""))
df_e1.insert(58, 'a_non_E4', np.where(np.logical_and(df_e1['peak_4']>=0996.800000000000,df_e1['peak_4']<=1000.800000000000) , df_e1['peak_4'], ""))
df_e1.insert(59, 'sn_ae_4', np.where(np.logical_and(df_e1['peak_4']>=0996.800000000000,df_e1['peak_4']<=1000.800000000000) , df_e1['sn_4'], ""))
df_e1.insert(60, 'a_non_E5', np.where(np.logical_and(df_e1['peak_5']>=0996.800000000000,df_e1['peak_5']<=1000.800000000000) , df_e1['peak_5'], ""))
df_e1.insert(61, 'sn_ae_5', np.where(np.logical_and(df_e1['peak_5']>=0996.800000000000,df_e1['peak_5']<=1000.800000000000) , df_e1['sn_5'], ""))
df_e1.insert(62, 'a_non_E6', np.where(np.logical_and(df_e1['peak_6']>=0996.800000000000,df_e1['peak_6']<=1000.800000000000) , df_e1['peak_6'], ""))
df_e1.insert(63, 'sn_ae_6', np.where(np.logical_and(df_e1['peak_6']>=0996.800000000000,df_e1['peak_6']<=1000.800000000000) , df_e1['sn_6'], ""))
		##a_hc_noise##
df_e1.insert(64, 'a_non_E7', np.where(np.logical_and(df_e1['peak_1']>=2302.900000000000,df_e1['peak_1']<=2312.100000000000) , df_e1['peak_1'], ""))
df_e1.insert(65, 'sn_ae_7', np.where(np.logical_and(df_e1['peak_1']>=2302.900000000000,df_e1['peak_1']<=2312.100000000000) , df_e1['sn_1'], ""))
df_e1.insert(66, 'a_non_E8', np.where(np.logical_and(df_e1['peak_2']>=2302.900000000000,df_e1['peak_2']<=2312.100000000000) , df_e1['peak_2'], ""))
df_e1.insert(67, 'sn_ae_8', np.where(np.logical_and(df_e1['peak_2']>=2302.900000000000,df_e1['peak_2']<=2312.100000000000) , df_e1['sn_2'], ""))
df_e1.insert(68, 'a_non_E9', np.where(np.logical_and(df_e1['peak_3']>=2302.900000000000,df_e1['peak_3']<=2312.100000000000) , df_e1['peak_3'], ""))
df_e1.insert(69, 'sn_ae_9', np.where(np.logical_and(df_e1['peak_3']>=2302.900000000000,df_e1['peak_3']<=2312.100000000000) , df_e1['sn_3'], ""))
df_e1.insert(70, 'a_non_E10', np.where(np.logical_and(df_e1['peak_4']>=2302.900000000000,df_e1['peak_4']<=2312.100000000000) , df_e1['peak_4'], ""))
df_e1.insert(71, 'sn_ae_10', np.where(np.logical_and(df_e1['peak_4']>=2302.900000000000,df_e1['peak_4']<=2312.100000000000) , df_e1['sn_4'], ""))
df_e1.insert(72, 'a_non_E11', np.where(np.logical_and(df_e1['peak_5']>=2302.900000000000,df_e1['peak_5']<=2312.100000000000) , df_e1['peak_5'], ""))
df_e1.insert(73, 'sn_ae_11', np.where(np.logical_and(df_e1['peak_5']>=2302.900000000000,df_e1['peak_5']<=2312.100000000000) , df_e1['sn_5'], ""))
df_e1.insert(74, 'a_non_E12', np.where(np.logical_and(df_e1['peak_6']>=2302.900000000000,df_e1['peak_6']<=2312.100000000000) , df_e1['peak_6'], ""))
df_e1.insert(75, 'sn_ae_12', np.where(np.logical_and(df_e1['peak_6']>=2302.900000000000,df_e1['peak_6']<=2312.100000000000) , df_e1['sn_6'], ""))
		##a_intact_noise##
df_e1.insert(76, 'a_non_E13', np.where(np.logical_and(df_e1['peak_1']>=3280.700000000000,df_e1['peak_1']<=3293.700000000000) , df_e1['peak_1'], ""))
df_e1.insert(77, 'sn_ae_13', np.where(np.logical_and(df_e1['peak_1']>=3280.700000000000,df_e1['peak_1']<=3293.700000000000) , df_e1['sn_1'], ""))
df_e1.insert(78, 'a_non_E14', np.where(np.logical_and(df_e1['peak_2']>=3280.700000000000,df_e1['peak_2']<=3293.700000000000) , df_e1['peak_2'], ""))
df_e1.insert(79, 'sn_ae_14', np.where(np.logical_and(df_e1['peak_2']>=3280.700000000000,df_e1['peak_2']<=3293.700000000000) , df_e1['sn_2'], ""))
df_e1.insert(80, 'a_non_E15', np.where(np.logical_and(df_e1['peak_3']>=3280.700000000000,df_e1['peak_3']<=3293.700000000000) , df_e1['peak_3'], ""))
df_e1.insert(81, 'sn_ae_15', np.where(np.logical_and(df_e1['peak_3']>=3280.700000000000,df_e1['peak_3']<=3293.700000000000) , df_e1['sn_3'], ""))
df_e1.insert(82, 'a_non_E16', np.where(np.logical_and(df_e1['peak_4']>=3280.700000000000,df_e1['peak_4']<=3293.700000000000) , df_e1['peak_4'], ""))
df_e1.insert(83, 'sn_ae_16', np.where(np.logical_and(df_e1['peak_4']>=3280.700000000000,df_e1['peak_4']<=3293.700000000000) , df_e1['sn_4'], ""))
df_e1.insert(84, 'a_non_E17', np.where(np.logical_and(df_e1['peak_5']>=3280.700000000000,df_e1['peak_5']<=3293.700000000000) , df_e1['peak_5'], ""))
df_e1.insert(85, 'sn_ae_17', np.where(np.logical_and(df_e1['peak_5']>=3280.700000000000,df_e1['peak_5']<=3293.700000000000) , df_e1['sn_5'], ""))
df_e1.insert(86, 'a_non_E18', np.where(np.logical_and(df_e1['peak_6']>=3280.700000000000,df_e1['peak_6']<=3293.700000000000) , df_e1['peak_6'], ""))
df_e1.insert(87, 'sn_ae_18', np.where(np.logical_and(df_e1['peak_6']>=3280.700000000000,df_e1['peak_6']<=3293.700000000000) , df_e1['sn_6'], ""))
		##b_lc_noise##
df_e1.insert(88, 'b_non_E1', np.where(np.logical_and(df_e1['peak_1']>=1756.500000000000,df_e1['peak_1']<=1763.700000000000) , df_e1['peak_1'], ""))
df_e1.insert(89, 'sn_be_1', np.where(np.logical_and(df_e1['peak_1']>=1756.500000000000,df_e1['peak_1']<=1763.700000000000) , df_e1['sn_1'], ""))
df_e1.insert(90, 'b_non_E2', np.where(np.logical_and(df_e1['peak_2']>=1756.500000000000,df_e1['peak_2']<=1763.700000000000) , df_e1['peak_2'], ""))
df_e1.insert(91, 'sn_be_2', np.where(np.logical_and(df_e1['peak_2']>=1756.500000000000,df_e1['peak_2']<=1763.700000000000) , df_e1['sn_2'], ""))
df_e1.insert(92, 'b_non_E3', np.where(np.logical_and(df_e1['peak_3']>=1756.500000000000,df_e1['peak_3']<=1763.700000000000) , df_e1['peak_3'], ""))
df_e1.insert(93, 'sn_be_3', np.where(np.logical_and(df_e1['peak_3']>=1756.500000000000,df_e1['peak_3']<=1763.700000000000) , df_e1['sn_3'], ""))
df_e1.insert(94, 'b_non_E4', np.where(np.logical_and(df_e1['peak_4']>=1756.500000000000,df_e1['peak_4']<=1763.700000000000) , df_e1['peak_4'], ""))
df_e1.insert(95, 'sn_be_4', np.where(np.logical_and(df_e1['peak_4']>=1756.500000000000,df_e1['peak_4']<=1763.700000000000) , df_e1['sn_4'], ""))
df_e1.insert(96, 'b_non_E5', np.where(np.logical_and(df_e1['peak_5']>=1756.500000000000,df_e1['peak_5']<=1763.700000000000) , df_e1['peak_5'], ""))
df_e1.insert(97, 'sn_be_5', np.where(np.logical_and(df_e1['peak_5']>=1756.500000000000,df_e1['peak_5']<=1763.700000000000) , df_e1['sn_5'], ""))
df_e1.insert(98, 'b_non_E6', np.where(np.logical_and(df_e1['peak_6']>=1756.500000000000,df_e1['peak_6']<=1763.700000000000) , df_e1['peak_6'], ""))
df_e1.insert(99, 'sn_be_6', np.where(np.logical_and(df_e1['peak_6']>=1756.500000000000,df_e1['peak_6']<=1763.700000000000) , df_e1['sn_6'], ""))
		##b_hc_noise##
df_e1.insert(100, 'b_non_E7', np.where(np.logical_and(df_e1['peak_1']>=2277.700000000000,df_e1['peak_1']<=2286.900000000000) , df_e1['peak_1'], ""))
df_e1.insert(101, 'sn_be_7', np.where(np.logical_and(df_e1['peak_1']>=2277.700000000000,df_e1['peak_1']<=2286.900000000000) , df_e1['sn_1'], ""))
df_e1.insert(102, 'b_non_E8', np.where(np.logical_and(df_e1['peak_2']>=2277.700000000000,df_e1['peak_2']<=2286.900000000000) , df_e1['peak_2'], ""))
df_e1.insert(103, 'sn_be_8', np.where(np.logical_and(df_e1['peak_2']>=2277.700000000000,df_e1['peak_2']<=2286.900000000000) , df_e1['sn_2'], ""))
df_e1.insert(104, 'b_non_E9', np.where(np.logical_and(df_e1['peak_3']>=2277.700000000000,df_e1['peak_3']<=2286.900000000000) , df_e1['peak_3'], ""))
df_e1.insert(105, 'sn_be_9', np.where(np.logical_and(df_e1['peak_3']>=2277.700000000000,df_e1['peak_3']<=2286.900000000000) , df_e1['sn_3'], ""))
df_e1.insert(106, 'b_non_E10', np.where(np.logical_and(df_e1['peak_4']>=2277.700000000000,df_e1['peak_4']<=2286.900000000000) , df_e1['peak_4'], ""))
df_e1.insert(107, 'sn_be_10', np.where(np.logical_and(df_e1['peak_4']>=2277.700000000000,df_e1['peak_4']<=2286.900000000000) , df_e1['sn_4'], ""))
df_e1.insert(108, 'b_non_E11', np.where(np.logical_and(df_e1['peak_5']>=2277.700000000000,df_e1['peak_5']<=2286.900000000000) , df_e1['peak_5'], ""))
df_e1.insert(109, 'sn_be_11', np.where(np.logical_and(df_e1['peak_5']>=2277.700000000000,df_e1['peak_5']<=2286.900000000000) , df_e1['sn_5'], ""))
df_e1.insert(110, 'b_non_E12', np.where(np.logical_and(df_e1['peak_6']>=2277.700000000000,df_e1['peak_6']<=2286.900000000000) , df_e1['peak_6'], ""))
df_e1.insert(111, 'sn_be_12', np.where(np.logical_and(df_e1['peak_6']>=2277.700000000000,df_e1['peak_6']<=2286.900000000000) , df_e1['sn_6'], ""))
		##b_intact_noise##
df_e1.insert(112, 'b_non_E13', np.where(np.logical_and(df_e1['peak_1']>=4018.400000000000,df_e1['peak_1']<=4034.600000000000) , df_e1['peak_1'], ""))
df_e1.insert(113, 'sn_be_13', np.where(np.logical_and(df_e1['peak_1']>=4018.400000000000,df_e1['peak_1']<=4034.600000000000) , df_e1['sn_1'], ""))
df_e1.insert(114, 'b_non_E14', np.where(np.logical_and(df_e1['peak_2']>=4018.400000000000,df_e1['peak_2']<=4034.600000000000) , df_e1['peak_2'], ""))
df_e1.insert(115, 'sn_be_14', np.where(np.logical_and(df_e1['peak_2']>=4018.400000000000,df_e1['peak_2']<=4034.600000000000) , df_e1['sn_2'], ""))
df_e1.insert(116, 'b_non_E15', np.where(np.logical_and(df_e1['peak_3']>=4018.400000000000,df_e1['peak_3']<=4034.600000000000) , df_e1['peak_3'], ""))
df_e1.insert(117, 'sn_be_15', np.where(np.logical_and(df_e1['peak_3']>=4018.400000000000,df_e1['peak_3']<=4034.600000000000) , df_e1['sn_3'], ""))
df_e1.insert(118, 'b_non_E16', np.where(np.logical_and(df_e1['peak_4']>=4018.400000000000,df_e1['peak_4']<=4034.600000000000) , df_e1['peak_4'], ""))
df_e1.insert(119, 'sn_be_16', np.where(np.logical_and(df_e1['peak_4']>=4018.400000000000,df_e1['peak_4']<=4034.600000000000) , df_e1['sn_4'], ""))
df_e1.insert(120, 'b_non_E17', np.where(np.logical_and(df_e1['peak_5']>=4018.400000000000,df_e1['peak_5']<=4034.600000000000) , df_e1['peak_5'], ""))
df_e1.insert(121, 'sn_be_17', np.where(np.logical_and(df_e1['peak_5']>=4018.400000000000,df_e1['peak_5']<=4034.600000000000) , df_e1['sn_5'], ""))
df_e1.insert(122, 'b_non_E18', np.where(np.logical_and(df_e1['peak_6']>=4018.400000000000,df_e1['peak_6']<=4034.600000000000) , df_e1['peak_6'], ""))
df_e1.insert(123, 'sn_be_18', np.where(np.logical_and(df_e1['peak_6']>=4018.400000000000,df_e1['peak_6']<=4034.600000000000) , df_e1['sn_6'], ""))
		##f_lc_noise##
df_e1.insert(124, 'f_non_E1', np.where(np.logical_and(df_e1['peak_1']>=1342.500000000000,df_e1['peak_1']<=1347.900000000000) , df_e1['peak_1'], ""))
df_e1.insert(125, 'sn_fe_1', np.where(np.logical_and(df_e1['peak_1']>=1342.500000000000,df_e1['peak_1']<=1347.900000000000) , df_e1['sn_1'], ""))
df_e1.insert(126, 'f_non_E2', np.where(np.logical_and(df_e1['peak_2']>=1342.500000000000,df_e1['peak_2']<=1347.900000000000) , df_e1['peak_2'], ""))
df_e1.insert(127, 'sn_fe_2', np.where(np.logical_and(df_e1['peak_2']>=1342.500000000000,df_e1['peak_2']<=1347.900000000000) , df_e1['sn_2'], ""))
df_e1.insert(128, 'f_non_E3', np.where(np.logical_and(df_e1['peak_3']>=1342.500000000000,df_e1['peak_3']<=1347.900000000000) , df_e1['peak_3'], ""))
df_e1.insert(129, 'sn_fe_3', np.where(np.logical_and(df_e1['peak_3']>=1342.500000000000,df_e1['peak_3']<=1347.900000000000) , df_e1['sn_3'], ""))
df_e1.insert(130, 'f_non_E4', np.where(np.logical_and(df_e1['peak_4']>=1342.500000000000,df_e1['peak_4']<=1347.900000000000) , df_e1['peak_4'], ""))
df_e1.insert(131, 'sn_fe_4', np.where(np.logical_and(df_e1['peak_4']>=1342.500000000000,df_e1['peak_4']<=1347.900000000000) , df_e1['sn_4'], ""))
df_e1.insert(132, 'f_non_E5', np.where(np.logical_and(df_e1['peak_5']>=1342.500000000000,df_e1['peak_5']<=1347.900000000000) , df_e1['peak_5'], ""))
df_e1.insert(133, 'sn_fe_5', np.where(np.logical_and(df_e1['peak_5']>=1342.500000000000,df_e1['peak_5']<=1347.900000000000) , df_e1['sn_5'], ""))
df_e1.insert(134, 'f_non_E6', np.where(np.logical_and(df_e1['peak_6']>=1342.500000000000,df_e1['peak_6']<=1347.900000000000) , df_e1['peak_6'], ""))
df_e1.insert(135, 'sn_fe_6', np.where(np.logical_and(df_e1['peak_6']>=1342.500000000000,df_e1['peak_6']<=1347.900000000000) , df_e1['sn_6'], ""))
		##f_hc_noise##
df_e1.insert(136, 'f_non_E7', np.where(np.logical_and(df_e1['peak_1']>=3777.300000000000,df_e1['peak_1']<=3792.500000000000) , df_e1['peak_1'], ""))
df_e1.insert(137, 'sn_fe_7', np.where(np.logical_and(df_e1['peak_1']>=3777.300000000000,df_e1['peak_1']<=3792.500000000000) , df_e1['sn_1'], ""))
df_e1.insert(138, 'f_non_E8', np.where(np.logical_and(df_e1['peak_2']>=3777.300000000000,df_e1['peak_2']<=3792.500000000000) , df_e1['peak_2'], ""))
df_e1.insert(139, 'sn_fe_8', np.where(np.logical_and(df_e1['peak_2']>=3777.300000000000,df_e1['peak_2']<=3792.500000000000) , df_e1['sn_2'], ""))
df_e1.insert(140, 'f_non_E9', np.where(np.logical_and(df_e1['peak_3']>=3777.300000000000,df_e1['peak_3']<=3792.500000000000) , df_e1['peak_3'], ""))
df_e1.insert(141, 'sn_fe_9', np.where(np.logical_and(df_e1['peak_3']>=3777.300000000000,df_e1['peak_3']<=3792.500000000000) , df_e1['sn_3'], ""))
df_e1.insert(142, 'f_non_E10', np.where(np.logical_and(df_e1['peak_4']>=3777.300000000000,df_e1['peak_4']<=3792.500000000000) , df_e1['peak_4'], ""))
df_e1.insert(143, 'sn_fe_10', np.where(np.logical_and(df_e1['peak_4']>=3777.300000000000,df_e1['peak_4']<=3792.500000000000) , df_e1['sn_4'], ""))
df_e1.insert(144, 'f_non_E11', np.where(np.logical_and(df_e1['peak_5']>=3777.300000000000,df_e1['peak_5']<=3792.500000000000) , df_e1['peak_5'], ""))
df_e1.insert(145, 'sn_fe_11', np.where(np.logical_and(df_e1['peak_5']>=3777.300000000000,df_e1['peak_5']<=3792.500000000000) , df_e1['sn_5'], ""))
df_e1.insert(146, 'f_non_E12', np.where(np.logical_and(df_e1['peak_6']>=3777.300000000000,df_e1['peak_6']<=3792.500000000000) , df_e1['peak_6'], ""))
df_e1.insert(147, 'sn_fe_12', np.where(np.logical_and(df_e1['peak_6']>=3777.300000000000,df_e1['peak_6']<=3792.500000000000) , df_e1['sn_6'], ""))
		##f5_lc_noise##
df_e1.insert(148, 'f5_non_E1', np.where(np.logical_and(df_e1['peak_1']>=1870.300000000000,df_e1['peak_1']<=1877.700000000000) , df_e1['peak_1'], ""))
df_e1.insert(149, 'sn_f5e_1', np.where(np.logical_and(df_e1['peak_1']>=1870.300000000000,df_e1['peak_1']<=1877.700000000000) , df_e1['sn_1'], ""))
df_e1.insert(150, 'f5_non_E2', np.where(np.logical_and(df_e1['peak_2']>=1870.300000000000,df_e1['peak_2']<=1877.700000000000) , df_e1['peak_2'], ""))
df_e1.insert(151, 'sn_f5e_2', np.where(np.logical_and(df_e1['peak_2']>=1870.300000000000,df_e1['peak_2']<=1877.700000000000) , df_e1['sn_2'], ""))
df_e1.insert(152, 'f5_non_E3', np.where(np.logical_and(df_e1['peak_3']>=1870.300000000000,df_e1['peak_3']<=1877.700000000000) , df_e1['peak_3'], ""))
df_e1.insert(153, 'sn_f5e_3', np.where(np.logical_and(df_e1['peak_3']>=1870.300000000000,df_e1['peak_3']<=1877.700000000000) , df_e1['sn_3'], ""))
df_e1.insert(154, 'f5_non_E4', np.where(np.logical_and(df_e1['peak_4']>=1870.300000000000,df_e1['peak_4']<=1877.700000000000) , df_e1['peak_4'], ""))
df_e1.insert(155, 'sn_f5e_4', np.where(np.logical_and(df_e1['peak_4']>=1870.300000000000,df_e1['peak_4']<=1877.700000000000) , df_e1['sn_4'], ""))
df_e1.insert(156, 'f5_non_E5', np.where(np.logical_and(df_e1['peak_5']>=1870.300000000000,df_e1['peak_5']<=1877.700000000000) , df_e1['peak_5'], ""))
df_e1.insert(157, 'sn_f5e_5', np.where(np.logical_and(df_e1['peak_5']>=1870.300000000000,df_e1['peak_5']<=1877.700000000000) , df_e1['sn_5'], ""))
df_e1.insert(158, 'f5_non_E6', np.where(np.logical_and(df_e1['peak_6']>=1870.300000000000,df_e1['peak_6']<=1877.700000000000) , df_e1['peak_6'], ""))
df_e1.insert(159, 'sn_f5e_6', np.where(np.logical_and(df_e1['peak_6']>=1870.300000000000,df_e1['peak_6']<=1877.700000000000) , df_e1['sn_6'], ""))
		##f5_hc_noise##
df_e1.insert(160, 'f5_non_E7', np.where(np.logical_and(df_e1['peak_1']>=3248.500000000000,df_e1['peak_1']<=3261.500000000000) , df_e1['peak_1'], ""))
df_e1.insert(161, 'sn_f5e_7', np.where(np.logical_and(df_e1['peak_1']>=3248.500000000000,df_e1['peak_1']<=3261.500000000000) , df_e1['sn_1'], ""))
df_e1.insert(162, 'f5_non_E8', np.where(np.logical_and(df_e1['peak_2']>=3248.500000000000,df_e1['peak_2']<=3261.500000000000) , df_e1['peak_2'], ""))
df_e1.insert(163, 'sn_f5e_8', np.where(np.logical_and(df_e1['peak_2']>=3248.500000000000,df_e1['peak_2']<=3261.500000000000) , df_e1['sn_2'], ""))
df_e1.insert(164, 'f5_non_E9', np.where(np.logical_and(df_e1['peak_3']>=3248.500000000000,df_e1['peak_3']<=3261.500000000000) , df_e1['peak_3'], ""))
df_e1.insert(165, 'sn_f5e_9', np.where(np.logical_and(df_e1['peak_3']>=3248.500000000000,df_e1['peak_3']<=3261.500000000000) , df_e1['sn_3'], ""))
df_e1.insert(166, 'f5_non_E10', np.where(np.logical_and(df_e1['peak_4']>=3248.500000000000,df_e1['peak_4']<=3261.500000000000) , df_e1['peak_4'], ""))
df_e1.insert(167, 'sn_f5e_10', np.where(np.logical_and(df_e1['peak_4']>=3248.500000000000,df_e1['peak_4']<=3261.500000000000) , df_e1['sn_4'], ""))
df_e1.insert(168, 'f5_non_E11', np.where(np.logical_and(df_e1['peak_5']>=3248.500000000000,df_e1['peak_5']<=3261.500000000000) , df_e1['peak_5'], ""))
df_e1.insert(169, 'sn_f5e_11', np.where(np.logical_and(df_e1['peak_5']>=3248.500000000000,df_e1['peak_5']<=3261.500000000000) , df_e1['sn_5'], ""))
df_e1.insert(170, 'f5_non_E12', np.where(np.logical_and(df_e1['peak_6']>=3248.500000000000,df_e1['peak_6']<=3261.500000000000) , df_e1['peak_6'], ""))
df_e1.insert(171, 'sn_f5e_12', np.where(np.logical_and(df_e1['peak_6']>=3248.500000000000,df_e1['peak_6']<=3261.500000000000) , df_e1['sn_6'], ""))
		##f_f5_intact_noise##
df_e1.insert(172, 'f_non_E13', np.where(np.logical_and(df_e1['peak_1']>=5100.800000000000,df_e1['peak_1']<=5121.200000000000) , df_e1['peak_1'], ""))
df_e1.insert(173, 'sn_fe_13', np.where(np.logical_and(df_e1['peak_1']>=5100.800000000000,df_e1['peak_1']<=5121.200000000000) , df_e1['sn_1'], ""))
df_e1.insert(174, 'f_non_E14', np.where(np.logical_and(df_e1['peak_2']>=5100.800000000000,df_e1['peak_2']<=5121.200000000000) , df_e1['peak_2'], ""))
df_e1.insert(175, 'sn_fe_14', np.where(np.logical_and(df_e1['peak_2']>=5100.800000000000,df_e1['peak_2']<=5121.200000000000) , df_e1['sn_2'], ""))
df_e1.insert(176, 'f_non_E15', np.where(np.logical_and(df_e1['peak_3']>=5100.800000000000,df_e1['peak_3']<=5121.200000000000) , df_e1['peak_3'], ""))
df_e1.insert(177, 'sn_fe_15', np.where(np.logical_and(df_e1['peak_3']>=5100.800000000000,df_e1['peak_3']<=5121.200000000000) , df_e1['sn_3'], ""))
df_e1.insert(178, 'f_non_E16', np.where(np.logical_and(df_e1['peak_4']>=5100.800000000000,df_e1['peak_4']<=5121.200000000000) , df_e1['peak_4'], ""))
df_e1.insert(179, 'sn_fe_16', np.where(np.logical_and(df_e1['peak_4']>=5100.800000000000,df_e1['peak_4']<=5121.200000000000) , df_e1['sn_4'], ""))
df_e1.insert(180, 'f_non_E17', np.where(np.logical_and(df_e1['peak_5']>=5100.800000000000,df_e1['peak_5']<=5121.200000000000) , df_e1['peak_5'], ""))
df_e1.insert(181, 'sn_fe_17', np.where(np.logical_and(df_e1['peak_5']>=5100.800000000000,df_e1['peak_5']<=5121.200000000000) , df_e1['sn_5'], ""))
df_e1.insert(182, 'f_non_E18', np.where(np.logical_and(df_e1['peak_6']>=5100.800000000000,df_e1['peak_6']<=5121.200000000000) , df_e1['peak_6'], ""))
df_e1.insert(183, 'sn_fe_18', np.where(np.logical_and(df_e1['peak_6']>=5100.800000000000,df_e1['peak_6']<=5121.200000000000) , df_e1['sn_6'], ""))

df_e2 = df_e1.drop(['test','peak_1','sn_1','peak_2','sn_2','peak_3','sn_3',\
'peak_4','sn_4','peak_5','sn_5','peak_6','sn_6'], axis=1)
df_e2.set_index('date', inplace=True)
print(df_e2)
df_e2.to_csv("e_df.txt", sep="\t")



#######
#  E  #
#######

e_df = open("e_df.txt", "r")
		############
		# read_csv #
		############
df_ea = pd.read_csv(e_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','LC1','sn_L_1','LC2','sn_L_2','LC3','sn_L_3','LC4','sn_L_4','\
LC5','sn_L_5','LC6','sn_L_6','HC1','sn_H_1','HC2','sn_H_2','HC3','sn_H_3','HC4','sn_H_4','HC5','sn_H_5','HC6','sn_H_6','Intact1','sn_I_1','Intact2','sn_I_2','Intact3','sn_I_3','\
Intact4','sn_I_4','Intact5','sn_I_5','Intact6','sn_I_6','a_non_E1','sn_ae_1','a_non_E2','sn_ae_2','a_non_E3','sn_ae_3','a_non_E4','sn_ae_4','a_non_E5','\
sn_ae_5','a_non_E6','sn_ae_6','a_non_E7','sn_ae_7','a_non_E8','sn_ae_8','a_non_E9','sn_ae_9','a_non_E10','sn_ae_10','a_non_E11','sn_ae_11','\
a_non_E12','sn_ae_12','a_non_E13','sn_ae_13','a_non_E14','sn_ae_14','a_non_E15','sn_ae_15','a_non_E16','sn_ae_16','a_non_E17','sn_ae_17','\
a_non_E18','sn_ae_18','b_non_E1','sn_be_1','b_non_E2','sn_be_2','b_non_E3','sn_be_3','b_non_E4','sn_be_4','b_non_E5','sn_be_5','b_non_E6','\
sn_be_6','b_non_E7','sn_be_7','b_non_E8','sn_be_8','b_non_E9','sn_be_9','b_non_E10','sn_be_10','b_non_E11','sn_be_11','b_non_E12','sn_be_12','\
b_non_E13','sn_be_13','b_non_E14','sn_be_14','b_non_E15','sn_be_15','b_non_E16','sn_be_16','b_non_E17','sn_be_17','b_non_E18','sn_be_18','\
f_non_E1','sn_fe_1','f_non_E2','sn_fe_2','f_non_E3','sn_fe_3','f_non_E4','sn_fe_4','f_non_E5','sn_fe_5','f_non_E6','sn_fe_6','f_non_E7','\
sn_fe_7','f_non_E8','sn_fe_8','f_non_E9','sn_fe_9','f_non_E10','sn_fe_10','f_non_E11','sn_fe_11','f_non_E12','sn_fe_12','f5_non_E1','\
sn_f5e_1','f5_non_E2','sn_f5e_2','f5_non_E3','sn_f5e_3','f5_non_E4','sn_f5e_4','f5_non_E5','sn_f5e_5','f5_non_E6','sn_f5e_6','\
f5_non_E7','sn_f5e_7','f5_non_E8','sn_f5e_8','f5_non_E9','sn_f5e_9','f5_non_E10','sn_f5e_10','f5_non_E11','sn_f5e_11','f5_non_E12','\
sn_f5e_12','f_non_E13','sn_fe_13','f_non_E14','sn_fe_14','f_non_E15','sn_fe_15','f_non_E16','sn_fe_16','f_non_E17','sn_fe_17','f_non_E18','sn_fe_18'])
print(df_ea)

df_ea.dropna(axis=1, how="all", inplace=True)
print(df_ea)

		#######################
		# formatting E chains #
		#######################
df_ea.columns = df_ea.columns.str.replace('^LC\d+', 'LC_E', regex=True)
s = df_ea.stack()
df_ea = s.unstack()
df_ea.columns = df_ea.columns.str.replace('sn_L_\d+', 'sn_LC_E', regex=True)
s2 = df_ea.stack()
df_ea = s2.unstack()
df_ea.columns = df_ea.columns.str.replace('^HC\d+', 'HC_E', regex=True)
s3 = df_ea.stack()
df_ea = s3.unstack()
df_ea.columns = df_ea.columns.str.replace('sn_H_\d+', 'sn_HC_E', regex=True)
s4 = df_ea.stack()
df_ea = s4.unstack()
df_ea.columns = df_ea.columns.str.replace('^Intact\d+', 'Intact_E', regex=True)
s5 = df_ea.stack()
df_ea = s5.unstack()
df_ea.columns = df_ea.columns.str.replace('sn_I_\d+', 'sn_Intact_E', regex=True)
s6 = df_ea.stack()
df_ea = s6.unstack()

df_ea.drop([col for col in df_ea.columns if 'a_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_ae_' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'b_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_be_' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'f_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_fe_' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'f5_non_E' in col], axis=1, inplace=True)
df_ea.drop([col for col in df_ea.columns if 'sn_f5e_' in col], axis=1, inplace=True)

cols = df_ea.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_E')))
cols.insert(4, cols.pop(cols.index('sn_LC_E')))
cols.insert(5, cols.pop(cols.index('HC_E')))
cols.insert(6, cols.pop(cols.index('sn_HC_E')))
cols.insert(7, cols.pop(cols.index('Intact_E')))
cols.insert(8, cols.pop(cols.index('sn_Intact_E')))
df_ea = df_ea.reindex(columns=cols)

df_ea1 = df_ea.drop(df_ea.index[0])
print(df_ea1)
df_ea1.to_csv("e_final_df.txt", sep="\t")

df_final = df_ea1[::2]
df_final.to_csv("test3.csv", sep="\t")
print(df_final)
df_final = df_final.loc[:, ~df_final.columns.str.contains('^Unnamed')]
df_final = df_final.loc[:, ~df_final.columns.duplicated()]
#df_final.to_csv("test.csv", sep="\t")

def highlight_1(s):
	color = '#FF6666'
	return 'background-color: %s' % color
def highlight_2(s):
	color = '#FF9999'
	return 'background-color: %s' % color
def highlight_3(s):
	color = '#009933'
	return 'background-color: %s' % color
def highlight_4(s):
	color = '#00CC66'
	return 'background-color: %s' % color
def highlight_5(s):
	color = '#FFFF66'
	return 'background-color: %s' % color
def highlight_6(s):
	color = '#FFFF99'
	return 'background-color: %s' % color
def highlight_7(s):
	color = '#6699FF'
	return 'background-color: %s' % color
def highlight_8(s):
	color = '#99CCFF'
	return 'background-color: %s' % color

df_final_2 = df_final[['date','plate','bot_id','LC_E','sn_LC_E','HC_E','sn_HC_E','Intact_E','sn_Intact_E']]
df_final_2.columns = ['date','plate','bot_id','Peak_1_E','sn_Peak_1_E','Peak_2_E','sn_Peak_2_E','Intact_E','sn_Intact_E']
df_final_3 = df_final_2.copy()
df_final_2 = df_final_2.sort_values(['date', 'plate', 'bot_id'])
df_final_2 = df_final_2.reset_index(drop=True).style.applymap(highlight_5, subset=pd.IndexSlice[:, ['Peak_1_E','Peak_2_E','Intact_E']]) \
.applymap(highlight_6, subset=pd.IndexSlice[:, ['sn_Peak_1_E', 'sn_Peak_2_E', 'sn_Intact_E']])

print(df_final_2)
df_final_2.to_excel("endopep_peak_list_0.xlsx", index=False)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
