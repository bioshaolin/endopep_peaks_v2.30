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

a = open("a_out.txt", "r")


#######
#  A  #
#######

	############
	# read_csv #
	############

df_a = pd.read_csv(a, sep="\t", header=None, names=['date','plate','bot_id','test','peak_1','sn_1','peak_2','sn_2','peak_3','sn_3',\
'peak_4','sn_4','peak_5','sn_5','peak_6','sn_6'])
print(df_a)
df_a1 = df_a.round(decimals=12)

		###light chain###
df_a1.insert(16, 'LC1', np.where(np.logical_and(df_a1['peak_1']>=0996.800000000000,df_a1['peak_1']<=1000.800000000000) , df_a1['peak_1'], ""))
df_a1.insert(17, 'sn_L_1', np.where(np.logical_and(df_a1['peak_1']>=0996.800000000000,df_a1['peak_1']<=1000.800000000000) , df_a1['sn_1'], ""))
df_a1.insert(18, 'LC2', np.where(np.logical_and(df_a1['peak_2']>=0996.800000000000,df_a1['peak_2']<=1000.800000000000) , df_a1['peak_2'], ""))
df_a1.insert(19, 'sn_L_2', np.where(np.logical_and(df_a1['peak_2']>=0996.800000000000,df_a1['peak_2']<=1000.800000000000) , df_a1['sn_2'], ""))
df_a1.insert(20, 'LC3', np.where(np.logical_and(df_a1['peak_3']>=0996.800000000000,df_a1['peak_3']<=1000.800000000000) , df_a1['peak_3'], ""))
df_a1.insert(21, 'sn_L_3', np.where(np.logical_and(df_a1['peak_3']>=0996.800000000000,df_a1['peak_3']<=1000.800000000000) , df_a1['sn_3'], ""))
df_a1.insert(22, 'LC4', np.where(np.logical_and(df_a1['peak_4']>=0996.800000000000,df_a1['peak_4']<=1000.800000000000) , df_a1['peak_4'], ""))
df_a1.insert(23, 'sn_L_4', np.where(np.logical_and(df_a1['peak_4']>=0996.800000000000,df_a1['peak_4']<=1000.800000000000) , df_a1['sn_4'], ""))
df_a1.insert(24, 'LC5', np.where(np.logical_and(df_a1['peak_5']>=0996.800000000000,df_a1['peak_5']<=1000.800000000000) , df_a1['peak_5'], ""))
df_a1.insert(25, 'sn_L_5', np.where(np.logical_and(df_a1['peak_5']>=0996.800000000000,df_a1['peak_5']<=1000.800000000000) , df_a1['sn_5'], ""))
df_a1.insert(26, 'LC6', np.where(np.logical_and(df_a1['peak_6']>=0996.800000000000,df_a1['peak_6']<=1000.800000000000) , df_a1['peak_6'], ""))
df_a1.insert(27, 'sn_L_6', np.where(np.logical_and(df_a1['peak_6']>=0996.800000000000,df_a1['peak_6']<=1000.800000000000) , df_a1['sn_6'], ""))
		##heavy chain##
df_a1.insert(28, 'HC1', np.where(np.logical_and(df_a1['peak_1']>=2302.900000000000,df_a1['peak_1']<=2312.100000000000) , df_a1['peak_1'], ""))
df_a1.insert(29, 'sn_H_1', np.where(np.logical_and(df_a1['peak_1']>=2302.900000000000,df_a1['peak_1']<=2312.100000000000) , df_a1['sn_1'], ""))
df_a1.insert(30, 'HC2', np.where(np.logical_and(df_a1['peak_2']>=2302.900000000000,df_a1['peak_2']<=2312.100000000000) , df_a1['peak_2'], ""))
df_a1.insert(31, 'sn_H_2', np.where(np.logical_and(df_a1['peak_2']>=2302.900000000000,df_a1['peak_2']<=2312.100000000000) , df_a1['sn_2'], ""))
df_a1.insert(32, 'HC3', np.where(np.logical_and(df_a1['peak_3']>=2302.900000000000,df_a1['peak_3']<=2312.100000000000) , df_a1['peak_3'], ""))
df_a1.insert(33, 'sn_H_3', np.where(np.logical_and(df_a1['peak_3']>=2302.900000000000,df_a1['peak_3']<=2312.100000000000) , df_a1['sn_3'], ""))
df_a1.insert(34, 'HC4', np.where(np.logical_and(df_a1['peak_4']>=2302.900000000000,df_a1['peak_4']<=2312.100000000000) , df_a1['peak_4'], ""))
df_a1.insert(35, 'sn_H_4', np.where(np.logical_and(df_a1['peak_4']>=2302.900000000000,df_a1['peak_4']<=2312.100000000000) , df_a1['sn_4'], ""))
df_a1.insert(36, 'HC5', np.where(np.logical_and(df_a1['peak_5']>=2302.900000000000,df_a1['peak_5']<=2312.100000000000) , df_a1['peak_5'], ""))
df_a1.insert(37, 'sn_H_5', np.where(np.logical_and(df_a1['peak_5']>=2302.900000000000,df_a1['peak_5']<=2312.100000000000) , df_a1['sn_5'], ""))
df_a1.insert(38, 'HC6', np.where(np.logical_and(df_a1['peak_6']>=2302.900000000000,df_a1['peak_6']<=2312.100000000000) , df_a1['peak_6'], ""))
df_a1.insert(39, 'sn_H_6', np.where(np.logical_and(df_a1['peak_6']>=2302.900000000000,df_a1['peak_6']<=2312.100000000000) , df_a1['sn_6'], ""))
		##intact##
df_a1.insert(40, 'Intact1', np.where(np.logical_and(df_a1['peak_1']>=3280.700000000000,df_a1['peak_1']<=3293.700000000000) , df_a1['peak_1'], ""))
df_a1.insert(41, 'sn_I_1', np.where(np.logical_and(df_a1['peak_1']>=3280.700000000000,df_a1['peak_1']<=3293.700000000000) , df_a1['sn_1'], ""))
df_a1.insert(42, 'Intact2', np.where(np.logical_and(df_a1['peak_2']>=3280.700000000000,df_a1['peak_2']<=3293.700000000000) , df_a1['peak_2'], ""))
df_a1.insert(43, 'sn_I_2', np.where(np.logical_and(df_a1['peak_2']>=3280.700000000000,df_a1['peak_2']<=3293.700000000000) , df_a1['sn_2'], ""))
df_a1.insert(44, 'Intact3', np.where(np.logical_and(df_a1['peak_3']>=3280.700000000000,df_a1['peak_3']<=3293.700000000000) , df_a1['peak_3'], ""))
df_a1.insert(45, 'sn_I_3', np.where(np.logical_and(df_a1['peak_3']>=3280.700000000000,df_a1['peak_3']<=3293.700000000000) , df_a1['sn_3'], ""))
df_a1.insert(46, 'Intact4', np.where(np.logical_and(df_a1['peak_4']>=3280.700000000000,df_a1['peak_4']<=3293.700000000000) , df_a1['peak_4'], ""))
df_a1.insert(47, 'sn_I_4', np.where(np.logical_and(df_a1['peak_4']>=3280.700000000000,df_a1['peak_4']<=3293.700000000000) , df_a1['sn_4'], ""))
df_a1.insert(48, 'Intact5', np.where(np.logical_and(df_a1['peak_5']>=3280.700000000000,df_a1['peak_5']<=3293.700000000000) , df_a1['peak_5'], ""))
df_a1.insert(49, 'sn_I_5', np.where(np.logical_and(df_a1['peak_5']>=3280.700000000000,df_a1['peak_5']<=3293.700000000000) , df_a1['sn_5'], ""))
df_a1.insert(50, 'Intact6', np.where(np.logical_and(df_a1['peak_6']>=3280.700000000000,df_a1['peak_6']<=3293.700000000000) , df_a1['peak_6'], ""))
df_a1.insert(51, 'sn_I_6', np.where(np.logical_and(df_a1['peak_6']>=3280.700000000000,df_a1['peak_6']<=3293.700000000000) , df_a1['sn_6'], ""))
		##b_lc_noise##
df_a1.insert(52, 'b_non_A1', np.where(np.logical_and(df_a1['peak_1']>=1756.500000000000,df_a1['peak_1']<=1763.700000000000) , df_a1['peak_1'], ""))
df_a1.insert(53, 'sn_ba_1', np.where(np.logical_and(df_a1['peak_1']>=1756.500000000000,df_a1['peak_1']<=1763.700000000000) , df_a1['sn_1'], ""))
df_a1.insert(54, 'b_non_A2', np.where(np.logical_and(df_a1['peak_2']>=1756.500000000000,df_a1['peak_2']<=1763.700000000000) , df_a1['peak_2'], ""))
df_a1.insert(55, 'sn_ba_2', np.where(np.logical_and(df_a1['peak_2']>=1756.500000000000,df_a1['peak_2']<=1763.700000000000) , df_a1['sn_2'], ""))
df_a1.insert(56, 'b_non_A3', np.where(np.logical_and(df_a1['peak_3']>=1756.500000000000,df_a1['peak_3']<=1763.700000000000) , df_a1['peak_3'], ""))
df_a1.insert(57, 'sn_ba_3', np.where(np.logical_and(df_a1['peak_3']>=1756.500000000000,df_a1['peak_3']<=1763.700000000000) , df_a1['sn_3'], ""))
df_a1.insert(58, 'b_non_A4', np.where(np.logical_and(df_a1['peak_4']>=1756.500000000000,df_a1['peak_4']<=1763.700000000000) , df_a1['peak_4'], ""))
df_a1.insert(59, 'sn_ba_4', np.where(np.logical_and(df_a1['peak_4']>=1756.500000000000,df_a1['peak_4']<=1763.700000000000) , df_a1['sn_4'], ""))
df_a1.insert(60, 'b_non_A5', np.where(np.logical_and(df_a1['peak_5']>=1756.500000000000,df_a1['peak_5']<=1763.700000000000) , df_a1['peak_5'], ""))
df_a1.insert(61, 'sn_ba_5', np.where(np.logical_and(df_a1['peak_5']>=1756.500000000000,df_a1['peak_5']<=1763.700000000000) , df_a1['sn_5'], ""))
df_a1.insert(62, 'b_non_A6', np.where(np.logical_and(df_a1['peak_6']>=1756.500000000000,df_a1['peak_6']<=1763.700000000000) , df_a1['peak_6'], ""))
df_a1.insert(63, 'sn_ba_6', np.where(np.logical_and(df_a1['peak_6']>=1756.500000000000,df_a1['peak_6']<=1763.700000000000) , df_a1['sn_6'], ""))
		##b_hc_noise##
df_a1.insert(64, 'b_non_A7', np.where(np.logical_and(df_a1['peak_1']>=2277.700000000000,df_a1['peak_1']<=2286.900000000000) , df_a1['peak_1'], ""))
df_a1.insert(65, 'sn_ba_7', np.where(np.logical_and(df_a1['peak_1']>=2277.700000000000,df_a1['peak_1']<=2286.900000000000) , df_a1['sn_1'], ""))
df_a1.insert(66, 'b_non_A8', np.where(np.logical_and(df_a1['peak_2']>=2277.700000000000,df_a1['peak_2']<=2286.900000000000) , df_a1['peak_2'], ""))
df_a1.insert(67, 'sn_ba_8', np.where(np.logical_and(df_a1['peak_2']>=2277.700000000000,df_a1['peak_2']<=2286.900000000000) , df_a1['sn_2'], ""))
df_a1.insert(68, 'b_non_A9', np.where(np.logical_and(df_a1['peak_3']>=2277.700000000000,df_a1['peak_3']<=2286.900000000000) , df_a1['peak_3'], ""))
df_a1.insert(69, 'sn_ba_9', np.where(np.logical_and(df_a1['peak_3']>=2277.700000000000,df_a1['peak_3']<=2286.900000000000) , df_a1['sn_3'], ""))
df_a1.insert(70, 'b_non_A10', np.where(np.logical_and(df_a1['peak_4']>=2277.700000000000,df_a1['peak_4']<=2286.900000000000) , df_a1['peak_4'], ""))
df_a1.insert(71, 'sn_ba_10', np.where(np.logical_and(df_a1['peak_4']>=2277.700000000000,df_a1['peak_4']<=2286.900000000000) , df_a1['sn_4'], ""))
df_a1.insert(72, 'b_non_A11', np.where(np.logical_and(df_a1['peak_5']>=2277.700000000000,df_a1['peak_5']<=2286.900000000000) , df_a1['peak_5'], ""))
df_a1.insert(73, 'sn_ba_11', np.where(np.logical_and(df_a1['peak_5']>=2277.700000000000,df_a1['peak_5']<=2286.900000000000) , df_a1['sn_5'], ""))
df_a1.insert(74, 'b_non_A12', np.where(np.logical_and(df_a1['peak_6']>=2277.700000000000,df_a1['peak_6']<=2286.900000000000) , df_a1['peak_6'], ""))
df_a1.insert(75, 'sn_ba_12', np.where(np.logical_and(df_a1['peak_6']>=2277.700000000000,df_a1['peak_6']<=2286.900000000000) , df_a1['sn_6'], ""))
		##b_intact_noise##
df_a1.insert(76, 'b_non_A13', np.where(np.logical_and(df_a1['peak_1']>=4018.400000000000,df_a1['peak_1']<=4034.600000000000) , df_a1['peak_1'], ""))
df_a1.insert(77, 'sn_ba_13', np.where(np.logical_and(df_a1['peak_1']>=4018.400000000000,df_a1['peak_1']<=4034.600000000000) , df_a1['sn_1'], ""))
df_a1.insert(78, 'b_non_A14', np.where(np.logical_and(df_a1['peak_2']>=4018.400000000000,df_a1['peak_2']<=4034.600000000000) , df_a1['peak_2'], ""))
df_a1.insert(79, 'sn_ba_14', np.where(np.logical_and(df_a1['peak_2']>=4018.400000000000,df_a1['peak_2']<=4034.600000000000) , df_a1['sn_2'], ""))
df_a1.insert(80, 'b_non_A15', np.where(np.logical_and(df_a1['peak_3']>=4018.400000000000,df_a1['peak_3']<=4034.600000000000) , df_a1['peak_3'], ""))
df_a1.insert(81, 'sn_ba_15', np.where(np.logical_and(df_a1['peak_3']>=4018.400000000000,df_a1['peak_3']<=4034.600000000000) , df_a1['sn_3'], ""))
df_a1.insert(82, 'b_non_A16', np.where(np.logical_and(df_a1['peak_4']>=4018.400000000000,df_a1['peak_4']<=4034.600000000000) , df_a1['peak_4'], ""))
df_a1.insert(83, 'sn_ba_16', np.where(np.logical_and(df_a1['peak_4']>=4018.400000000000,df_a1['peak_4']<=4034.600000000000) , df_a1['sn_4'], ""))
df_a1.insert(84, 'b_non_A17', np.where(np.logical_and(df_a1['peak_5']>=4018.400000000000,df_a1['peak_5']<=4034.600000000000) , df_a1['peak_5'], ""))
df_a1.insert(85, 'sn_ba_17', np.where(np.logical_and(df_a1['peak_5']>=4018.400000000000,df_a1['peak_5']<=4034.600000000000) , df_a1['sn_5'], ""))
df_a1.insert(86, 'b_non_A18', np.where(np.logical_and(df_a1['peak_6']>=4018.400000000000,df_a1['peak_6']<=4034.600000000000) , df_a1['peak_6'], ""))
df_a1.insert(87, 'sn_ba_18', np.where(np.logical_and(df_a1['peak_6']>=4018.400000000000,df_a1['peak_6']<=4034.600000000000) , df_a1['sn_6'], ""))
		##e_lc_noise##
df_a1.insert(88, 'e_non_A1', np.where(np.logical_and(df_a1['peak_1']>=1129.200000000000,df_a1['peak_1']<=1133.800000000000) , df_a1['peak_1'], ""))
df_a1.insert(89, 'sn_ea_1', np.where(np.logical_and(df_a1['peak_1']>=1129.200000000000,df_a1['peak_1']<=1133.800000000000) , df_a1['sn_1'], ""))
df_a1.insert(90, 'e_non_A2', np.where(np.logical_and(df_a1['peak_2']>=1129.200000000000,df_a1['peak_2']<=1133.800000000000) , df_a1['peak_2'], ""))
df_a1.insert(91, 'sn_ea_2', np.where(np.logical_and(df_a1['peak_2']>=1129.200000000000,df_a1['peak_2']<=1133.800000000000) , df_a1['sn_2'], ""))
df_a1.insert(92, 'e_non_A3', np.where(np.logical_and(df_a1['peak_3']>=1129.200000000000,df_a1['peak_3']<=1133.800000000000) , df_a1['peak_3'], ""))
df_a1.insert(93, 'sn_ea_3', np.where(np.logical_and(df_a1['peak_3']>=1129.200000000000,df_a1['peak_3']<=1133.800000000000) , df_a1['sn_3'], ""))
df_a1.insert(94, 'e_non_A4', np.where(np.logical_and(df_a1['peak_4']>=1129.200000000000,df_a1['peak_4']<=1133.800000000000) , df_a1['peak_4'], ""))
df_a1.insert(95, 'sn_ea_4', np.where(np.logical_and(df_a1['peak_4']>=1129.200000000000,df_a1['peak_4']<=1133.800000000000) , df_a1['sn_4'], ""))
df_a1.insert(96, 'e_non_A5', np.where(np.logical_and(df_a1['peak_5']>=1129.200000000000,df_a1['peak_5']<=1133.800000000000) , df_a1['peak_5'], ""))
df_a1.insert(97, 'sn_ea_5', np.where(np.logical_and(df_a1['peak_5']>=1129.200000000000,df_a1['peak_5']<=1133.800000000000) , df_a1['sn_5'], ""))
df_a1.insert(98, 'e_non_A6', np.where(np.logical_and(df_a1['peak_6']>=1129.200000000000,df_a1['peak_6']<=1133.800000000000) , df_a1['peak_6'], ""))
df_a1.insert(99, 'sn_ea_6', np.where(np.logical_and(df_a1['peak_6']>=1129.200000000000,df_a1['peak_6']<=1133.800000000000) , df_a1['sn_6'], ""))
		##e_hc_noise##
df_a1.insert(100, 'e_non_A7', np.where(np.logical_and(df_a1['peak_1']>=2493.600000000000,df_a1['peak_1']<=2503.600000000000) , df_a1['peak_1'], ""))
df_a1.insert(101, 'sn_ea_7', np.where(np.logical_and(df_a1['peak_1']>=2493.600000000000,df_a1['peak_1']<=2503.600000000000) , df_a1['sn_1'], ""))
df_a1.insert(102, 'e_non_A8', np.where(np.logical_and(df_a1['peak_2']>=2493.600000000000,df_a1['peak_2']<=2503.600000000000) , df_a1['peak_2'], ""))
df_a1.insert(103, 'sn_ea_8', np.where(np.logical_and(df_a1['peak_2']>=2493.600000000000,df_a1['peak_2']<=2503.600000000000) , df_a1['sn_2'], ""))
df_a1.insert(104, 'e_non_A9', np.where(np.logical_and(df_a1['peak_3']>=2493.600000000000,df_a1['peak_3']<=2503.600000000000) , df_a1['peak_3'], ""))
df_a1.insert(105, 'sn_ea_9', np.where(np.logical_and(df_a1['peak_3']>=2493.600000000000,df_a1['peak_3']<=2503.600000000000) , df_a1['sn_3'], ""))
df_a1.insert(106, 'e_non_A10', np.where(np.logical_and(df_a1['peak_4']>=2493.600000000000,df_a1['peak_4']<=2503.600000000000) , df_a1['peak_4'], ""))
df_a1.insert(107, 'sn_ea_10', np.where(np.logical_and(df_a1['peak_4']>=2493.600000000000,df_a1['peak_4']<=2503.600000000000) , df_a1['sn_4'], ""))
df_a1.insert(108, 'e_non_A11', np.where(np.logical_and(df_a1['peak_5']>=2493.600000000000,df_a1['peak_5']<=2503.600000000000) , df_a1['peak_5'], ""))
df_a1.insert(109, 'sn_ea_11', np.where(np.logical_and(df_a1['peak_5']>=2493.600000000000,df_a1['peak_5']<=2503.600000000000) , df_a1['sn_5'], ""))
df_a1.insert(110, 'e_non_A12', np.where(np.logical_and(df_a1['peak_6']>=2493.600000000000,df_a1['peak_6']<=2503.600000000000) , df_a1['peak_6'], ""))
df_a1.insert(111, 'sn_ea_12', np.where(np.logical_and(df_a1['peak_6']>=2493.600000000000,df_a1['peak_6']<=2503.600000000000) , df_a1['sn_6'], ""))
		##e_intact_noise##
df_a1.insert(112, 'e_non_A13', np.where(np.logical_and(df_a1['peak_1']>=3607.800000000000,df_a1['peak_1']<=3622.200000000000) , df_a1['peak_1'], ""))
df_a1.insert(113, 'sn_ea_13', np.where(np.logical_and(df_a1['peak_1']>=3607.800000000000,df_a1['peak_1']<=3622.200000000000) , df_a1['sn_1'], ""))
df_a1.insert(114, 'e_non_A14', np.where(np.logical_and(df_a1['peak_2']>=3607.800000000000,df_a1['peak_2']<=3622.200000000000) , df_a1['peak_2'], ""))
df_a1.insert(115, 'sn_ea_14', np.where(np.logical_and(df_a1['peak_2']>=3607.800000000000,df_a1['peak_2']<=3622.200000000000) , df_a1['sn_2'], ""))
df_a1.insert(116, 'e_non_A15', np.where(np.logical_and(df_a1['peak_3']>=3607.800000000000,df_a1['peak_3']<=3622.200000000000) , df_a1['peak_3'], ""))
df_a1.insert(117, 'sn_ea_15', np.where(np.logical_and(df_a1['peak_3']>=3607.800000000000,df_a1['peak_3']<=3622.200000000000) , df_a1['sn_3'], ""))
df_a1.insert(118, 'e_non_A16', np.where(np.logical_and(df_a1['peak_4']>=3607.800000000000,df_a1['peak_4']<=3622.200000000000) , df_a1['peak_4'], ""))
df_a1.insert(119, 'sn_ea_16', np.where(np.logical_and(df_a1['peak_4']>=3607.800000000000,df_a1['peak_4']<=3622.200000000000) , df_a1['sn_4'], ""))
df_a1.insert(120, 'e_non_A17', np.where(np.logical_and(df_a1['peak_5']>=3607.800000000000,df_a1['peak_5']<=3622.200000000000) , df_a1['peak_5'], ""))
df_a1.insert(121, 'sn_ea_17', np.where(np.logical_and(df_a1['peak_5']>=3607.800000000000,df_a1['peak_5']<=3622.200000000000) , df_a1['sn_5'], ""))
df_a1.insert(122, 'e_non_A18', np.where(np.logical_and(df_a1['peak_6']>=3607.800000000000,df_a1['peak_6']<=3622.200000000000) , df_a1['peak_6'], ""))
df_a1.insert(123, 'sn_ea_18', np.where(np.logical_and(df_a1['peak_6']>=3607.800000000000,df_a1['peak_6']<=3622.200000000000) , df_a1['sn_6'], ""))
		##f_lc_noise##
df_a1.insert(124, 'f_non_A1', np.where(np.logical_and(df_a1['peak_1']>=1342.500000000000,df_a1['peak_1']<=1347.900000000000) , df_a1['peak_1'], ""))
df_a1.insert(125, 'sn_fa_1', np.where(np.logical_and(df_a1['peak_1']>=1342.500000000000,df_a1['peak_1']<=1347.900000000000) , df_a1['sn_1'], ""))
df_a1.insert(126, 'f_non_A2', np.where(np.logical_and(df_a1['peak_2']>=1342.500000000000,df_a1['peak_2']<=1347.900000000000) , df_a1['peak_2'], ""))
df_a1.insert(127, 'sn_fa_2', np.where(np.logical_and(df_a1['peak_2']>=1342.500000000000,df_a1['peak_2']<=1347.900000000000) , df_a1['sn_2'], ""))
df_a1.insert(128, 'f_non_A3', np.where(np.logical_and(df_a1['peak_3']>=1342.500000000000,df_a1['peak_3']<=1347.900000000000) , df_a1['peak_3'], ""))
df_a1.insert(129, 'sn_fa_3', np.where(np.logical_and(df_a1['peak_3']>=1342.500000000000,df_a1['peak_3']<=1347.900000000000) , df_a1['sn_3'], ""))
df_a1.insert(130, 'f_non_A4', np.where(np.logical_and(df_a1['peak_4']>=1342.500000000000,df_a1['peak_4']<=1347.900000000000) , df_a1['peak_4'], ""))
df_a1.insert(131, 'sn_fa_4', np.where(np.logical_and(df_a1['peak_4']>=1342.500000000000,df_a1['peak_4']<=1347.900000000000) , df_a1['sn_4'], ""))
df_a1.insert(132, 'f_non_A5', np.where(np.logical_and(df_a1['peak_5']>=1342.500000000000,df_a1['peak_5']<=1347.900000000000) , df_a1['peak_5'], ""))
df_a1.insert(133, 'sn_fa_5', np.where(np.logical_and(df_a1['peak_5']>=1342.500000000000,df_a1['peak_5']<=1347.900000000000) , df_a1['sn_5'], ""))
df_a1.insert(134, 'f_non_A6', np.where(np.logical_and(df_a1['peak_6']>=1342.500000000000,df_a1['peak_6']<=1347.900000000000) , df_a1['peak_6'], ""))
df_a1.insert(135, 'sn_fa_6', np.where(np.logical_and(df_a1['peak_6']>=1342.500000000000,df_a1['peak_6']<=1347.900000000000) , df_a1['sn_6'], ""))
		##f_hc_noise##
df_a1.insert(136, 'f_non_A7', np.where(np.logical_and(df_a1['peak_1']>=3777.300000000000,df_a1['peak_1']<=3792.500000000000) , df_a1['peak_1'], ""))
df_a1.insert(137, 'sn_fa_7', np.where(np.logical_and(df_a1['peak_1']>=3777.300000000000,df_a1['peak_1']<=3792.500000000000) , df_a1['sn_1'], ""))
df_a1.insert(138, 'f_non_A8', np.where(np.logical_and(df_a1['peak_2']>=3777.300000000000,df_a1['peak_2']<=3792.500000000000) , df_a1['peak_2'], ""))
df_a1.insert(139, 'sn_fa_8', np.where(np.logical_and(df_a1['peak_2']>=3777.300000000000,df_a1['peak_2']<=3792.500000000000) , df_a1['sn_2'], ""))
df_a1.insert(140, 'f_non_A9', np.where(np.logical_and(df_a1['peak_3']>=3777.300000000000,df_a1['peak_3']<=3792.500000000000) , df_a1['peak_3'], ""))
df_a1.insert(141, 'sn_fa_9', np.where(np.logical_and(df_a1['peak_3']>=3777.300000000000,df_a1['peak_3']<=3792.500000000000) , df_a1['sn_3'], ""))
df_a1.insert(142, 'f_non_A10', np.where(np.logical_and(df_a1['peak_4']>=3777.300000000000,df_a1['peak_4']<=3792.500000000000) , df_a1['peak_4'], ""))
df_a1.insert(143, 'sn_fa_10', np.where(np.logical_and(df_a1['peak_4']>=3777.300000000000,df_a1['peak_4']<=3792.500000000000) , df_a1['sn_4'], ""))
df_a1.insert(144, 'f_non_A11', np.where(np.logical_and(df_a1['peak_5']>=3777.300000000000,df_a1['peak_5']<=3792.500000000000) , df_a1['peak_5'], ""))
df_a1.insert(145, 'sn_fa_11', np.where(np.logical_and(df_a1['peak_5']>=3777.300000000000,df_a1['peak_5']<=3792.500000000000) , df_a1['sn_5'], ""))
df_a1.insert(146, 'f_non_A12', np.where(np.logical_and(df_a1['peak_6']>=3777.300000000000,df_a1['peak_6']<=3792.500000000000) , df_a1['peak_6'], ""))
df_a1.insert(147, 'sn_fa_12', np.where(np.logical_and(df_a1['peak_6']>=3777.300000000000,df_a1['peak_6']<=3792.500000000000) , df_a1['sn_6'], ""))
		##f5_lc_noise##
df_a1.insert(148, 'f5_non_A1', np.where(np.logical_and(df_a1['peak_1']>=1870.300000000000,df_a1['peak_1']<=1877.700000000000) , df_a1['peak_1'], ""))
df_a1.insert(149, 'sn_f5a_1', np.where(np.logical_and(df_a1['peak_1']>=1870.300000000000,df_a1['peak_1']<=1877.700000000000) , df_a1['sn_1'], ""))
df_a1.insert(150, 'f5_non_A2', np.where(np.logical_and(df_a1['peak_2']>=1870.300000000000,df_a1['peak_2']<=1877.700000000000) , df_a1['peak_2'], ""))
df_a1.insert(151, 'sn_f5a_2', np.where(np.logical_and(df_a1['peak_2']>=1870.300000000000,df_a1['peak_2']<=1877.700000000000) , df_a1['sn_2'], ""))
df_a1.insert(152, 'f5_non_A3', np.where(np.logical_and(df_a1['peak_3']>=1870.300000000000,df_a1['peak_3']<=1877.700000000000) , df_a1['peak_3'], ""))
df_a1.insert(153, 'sn_f5a_3', np.where(np.logical_and(df_a1['peak_3']>=1870.300000000000,df_a1['peak_3']<=1877.700000000000) , df_a1['sn_3'], ""))
df_a1.insert(154, 'f5_non_A4', np.where(np.logical_and(df_a1['peak_4']>=1870.300000000000,df_a1['peak_4']<=1877.700000000000) , df_a1['peak_4'], ""))
df_a1.insert(155, 'sn_f5a_4', np.where(np.logical_and(df_a1['peak_4']>=1870.300000000000,df_a1['peak_4']<=1877.700000000000) , df_a1['sn_4'], ""))
df_a1.insert(156, 'f5_non_A5', np.where(np.logical_and(df_a1['peak_5']>=1870.300000000000,df_a1['peak_5']<=1877.700000000000) , df_a1['peak_5'], ""))
df_a1.insert(157, 'sn_f5a_5', np.where(np.logical_and(df_a1['peak_5']>=1870.300000000000,df_a1['peak_5']<=1877.700000000000) , df_a1['sn_5'], ""))
df_a1.insert(158, 'f5_non_A6', np.where(np.logical_and(df_a1['peak_6']>=1870.300000000000,df_a1['peak_6']<=1877.700000000000) , df_a1['peak_6'], ""))
df_a1.insert(159, 'sn_f5a_6', np.where(np.logical_and(df_a1['peak_6']>=1870.300000000000,df_a1['peak_6']<=1877.700000000000) , df_a1['sn_6'], ""))
		##f5_hc_noise##
df_a1.insert(160, 'f5_non_A7', np.where(np.logical_and(df_a1['peak_1']>=3248.500000000000,df_a1['peak_1']<=3261.500000000000) , df_a1['peak_1'], ""))
df_a1.insert(161, 'sn_f5a_7', np.where(np.logical_and(df_a1['peak_1']>=3248.500000000000,df_a1['peak_1']<=3261.500000000000) , df_a1['sn_1'], ""))
df_a1.insert(162, 'f5_non_A8', np.where(np.logical_and(df_a1['peak_2']>=3248.500000000000,df_a1['peak_2']<=3261.500000000000) , df_a1['peak_2'], ""))
df_a1.insert(163, 'sn_f5a_8', np.where(np.logical_and(df_a1['peak_2']>=3248.500000000000,df_a1['peak_2']<=3261.500000000000) , df_a1['sn_2'], ""))
df_a1.insert(164, 'f5_non_A9', np.where(np.logical_and(df_a1['peak_3']>=3248.500000000000,df_a1['peak_3']<=3261.500000000000) , df_a1['peak_3'], ""))
df_a1.insert(165, 'sn_f5a_9', np.where(np.logical_and(df_a1['peak_3']>=3248.500000000000,df_a1['peak_3']<=3261.500000000000) , df_a1['sn_3'], ""))
df_a1.insert(166, 'f5_non_A10', np.where(np.logical_and(df_a1['peak_4']>=3248.500000000000,df_a1['peak_4']<=3261.500000000000) , df_a1['peak_4'], ""))
df_a1.insert(167, 'sn_f5a_10', np.where(np.logical_and(df_a1['peak_4']>=3248.500000000000,df_a1['peak_4']<=3261.500000000000) , df_a1['sn_4'], ""))
df_a1.insert(168, 'f5_non_A11', np.where(np.logical_and(df_a1['peak_5']>=3248.500000000000,df_a1['peak_5']<=3261.500000000000) , df_a1['peak_5'], ""))
df_a1.insert(169, 'sn_f5a_11', np.where(np.logical_and(df_a1['peak_5']>=3248.500000000000,df_a1['peak_5']<=3261.500000000000) , df_a1['sn_5'], ""))
df_a1.insert(170, 'f5_non_A12', np.where(np.logical_and(df_a1['peak_6']>=3248.500000000000,df_a1['peak_6']<=3261.500000000000) , df_a1['peak_6'], ""))
df_a1.insert(171, 'sn_f5a_12', np.where(np.logical_and(df_a1['peak_6']>=3248.500000000000,df_a1['peak_6']<=3261.500000000000) , df_a1['sn_6'], ""))
		##f_f5_intact_noise##
df_a1.insert(172, 'f_non_A13', np.where(np.logical_and(df_a1['peak_1']>=5100.800000000000,df_a1['peak_1']<=5121.200000000000) , df_a1['peak_1'], ""))
df_a1.insert(173, 'sn_fa_13', np.where(np.logical_and(df_a1['peak_1']>=5100.800000000000,df_a1['peak_1']<=5121.200000000000) , df_a1['sn_1'], ""))
df_a1.insert(174, 'f_non_A14', np.where(np.logical_and(df_a1['peak_2']>=5100.800000000000,df_a1['peak_2']<=5121.200000000000) , df_a1['peak_2'], ""))
df_a1.insert(175, 'sn_fa_14', np.where(np.logical_and(df_a1['peak_2']>=5100.800000000000,df_a1['peak_2']<=5121.200000000000) , df_a1['sn_2'], ""))
df_a1.insert(176, 'f_non_A15', np.where(np.logical_and(df_a1['peak_3']>=5100.800000000000,df_a1['peak_3']<=5121.200000000000) , df_a1['peak_3'], ""))
df_a1.insert(177, 'sn_fa_15', np.where(np.logical_and(df_a1['peak_3']>=5100.800000000000,df_a1['peak_3']<=5121.200000000000) , df_a1['sn_3'], ""))
df_a1.insert(178, 'f_non_A16', np.where(np.logical_and(df_a1['peak_4']>=5100.800000000000,df_a1['peak_4']<=5121.200000000000) , df_a1['peak_4'], ""))
df_a1.insert(179, 'sn_fa_16', np.where(np.logical_and(df_a1['peak_4']>=5100.800000000000,df_a1['peak_4']<=5121.200000000000) , df_a1['sn_4'], ""))
df_a1.insert(180, 'f_non_A17', np.where(np.logical_and(df_a1['peak_5']>=5100.800000000000,df_a1['peak_5']<=5121.200000000000) , df_a1['peak_5'], ""))
df_a1.insert(181, 'sn_fa_17', np.where(np.logical_and(df_a1['peak_5']>=5100.800000000000,df_a1['peak_5']<=5121.200000000000) , df_a1['sn_5'], ""))
df_a1.insert(182, 'f_non_A18', np.where(np.logical_and(df_a1['peak_6']>=5100.800000000000,df_a1['peak_6']<=5121.200000000000) , df_a1['peak_6'], ""))
df_a1.insert(183, 'sn_fa_18', np.where(np.logical_and(df_a1['peak_1']>=5100.800000000000,df_a1['peak_1']<=5121.200000000000) , df_a1['sn_1'], ""))

df_a2 = df_a1.drop(['test','peak_1','sn_1','peak_2','sn_2','peak_3','sn_3',\
'peak_4','sn_4','peak_5','sn_5','peak_6','sn_6'], axis=1)
df_a2.set_index('date', inplace=True)
print(df_a2)
df_a2.to_csv("a_df.txt", sep="\t")

#####################
# FORMAT CHAIN DATA #
#####################

a_df = open("a_df.txt", "r")

#######
#  A  #
#######

		############
		# read_csv #
		############
df_aa = pd.read_csv(a_df, sep="\t", header=None, skiprows=1, names=['date','plate','bot_id','LC1','sn_L_1','LC2','sn_L_2','LC3','sn_L_3','\
LC4','sn_L_4','LC5','sn_L_5','LC6','sn_L_6','HC1','sn_H_1','HC2','sn_H_2','HC3','sn_H_3','HC4','sn_H_4','HC5','sn_H_5','HC6','sn_H_6','Intact1','sn_I_1','Intact2','\
sn_I_2','Intact3','sn_I_3','Intact4','sn_I_4','Intact5','sn_I_5','Intact6','sn_I_6','b_non_A1','sn_ba_1','b_non_A2','sn_ba_2','b_non_A3','sn_ba_3','b_non_A4','\
sn_ba_4','b_non_A5','sn_ba_5','b_non_A6','sn_ba_6','b_non_A7','sn_ba_7','b_non_A8','sn_ba_8','b_non_A9','sn_ba_9','b_non_A10','sn_ba_10','b_non_A11','\
sn_ba_11','b_non_A12','sn_ba_12','b_non_A13','sn_ba_13','b_non_A14','sn_ba_14','b_non_A15','sn_ba_15','b_non_A16','sn_ba_16','b_non_A17','\
sn_ba_17','b_non_A18','sn_ba_18','e_non_A1','sn_ea_1','e_non_A2','sn_ea_2','e_non_A3','sn_ea_3','e_non_A4','sn_ea_4','e_non_A5','sn_ea_5','e_non_A6\
','sn_ea_6','e_non_A7','sn_ea_7','e_non_A8','sn_ea_8','e_non_A9','sn_ea_9','e_non_A10','sn_ea_10','e_non_A11','sn_ea_11','e_non_A12','sn_ea_12','\
','e_non_A13','sn_ea_13','e_non_A14','sn_ea_14','e_non_A15','sn_ea_15','e_non_A16','sn_ea_16','e_non_A17','sn_ea_17','e_non_A18','sn_ea_18','\
','f_non_A1','sn_fa_1','f_non_A2','sn_fa_2','f_non_A3','sn_fa_3','f_non_A4','sn_fa_4','f_non_A5','sn_fa_5','f_non_A6','sn_fa_6','f_non_A7','sn_fa_7','\
','f_non_A8','sn_fa_8','f_non_A9','sn_fa_9','f_non_A10','sn_fa_10','f_non_A11','sn_fa_11','f_non_A12','sn_fa_12','f5_non_A1','sn_f5a_1','\
','f5_non_A2','sn_f5a_2','f5_non_A3','sn_f5a_3','f5_non_A4','sn_f5a_4','f5_non_A5','sn_f5a_5','f5_non_A6','sn_f5a_6','f5_non_A7','sn_f5a_7','\
','f5_non_A8','sn_f5a_8','f5_non_A9','sn_f5a_9','f5_non_A10','sn_f5a_10','f5_non_A11','sn_f5a_11','f5_non_A12','sn_f5a_12','f_non_A13','sn_fa_13','\
','f_non_A14','sn_fa_14','f_non_A15','sn_fa_15','f_non_A16','sn_fa_16','f_non_A17','sn_fa_17','f_non_A18','sn_fa_18'])
print(df_aa)

df_aa.dropna(axis=1, how="all", inplace=True)
print(df_aa)

		#######################
		# formatting A chains #
		#######################
df_aa.columns = df_aa.columns.str.replace('^LC\d+', 'LC_A', regex=True)
s = df_aa.stack()
df_aa = s.unstack()
df_aa.columns = df_aa.columns.str.replace('sn_L_\d+', 'sn_LC_A', regex=True)
s2 = df_aa.stack()
df_aa = s2.unstack()
df_aa.columns = df_aa.columns.str.replace('^HC\d+', 'HC_A', regex=True)
s3 = df_aa.stack()
df_aa = s3.unstack()
df_aa.columns = df_aa.columns.str.replace('sn_H_\d+', 'sn_HC_A', regex=True)
s4 = df_aa.stack()
df_aa = s4.unstack()
df_aa.columns = df_aa.columns.str.replace('^Intact\d+', 'Intact_A', regex=True)
s5 = df_aa.stack()
df_aa = s5.unstack()
df_aa.columns = df_aa.columns.str.replace('sn_I_\d+', 'sn_Intact_A', regex=True)
s6 = df_aa.stack()
df_aa = s6.unstack()

df_aa.drop([col for col in df_aa.columns if 'b_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_ba_' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'e_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_ea_' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'f_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_fa_' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'f5_non_A' in col], axis=1, inplace=True)
df_aa.drop([col for col in df_aa.columns if 'sn_f5a_' in col], axis=1, inplace=True)


cols = df_aa.columns.tolist()
cols.insert(0, cols.pop(cols.index('date')))
cols.insert(1, cols.pop(cols.index('plate')))
cols.insert(2, cols.pop(cols.index('bot_id')))
cols.insert(3, cols.pop(cols.index('LC_A')))
cols.insert(4, cols.pop(cols.index('sn_LC_A')))
cols.insert(5, cols.pop(cols.index('HC_A')))
cols.insert(6, cols.pop(cols.index('sn_HC_A')))
cols.insert(7, cols.pop(cols.index('Intact_A')))
cols.insert(8, cols.pop(cols.index('sn_Intact_A')))
df_aa = df_aa.reindex(columns=cols)

df_aa1 = df_aa.drop(df_aa.index[0])
print(df_aa1)
df_aa1.to_csv("a_final_df.txt", sep="\t")


df_final = df_aa1[::2]
df_final.to_csv("test3.csv", sep="\t")
print(df_final)
df_final = df_final.loc[:, ~df_final.columns.str.contains('^Unnamed')]
df_final = df_final.loc[:, ~df_final.columns.duplicated()]
#df_final.to_csv("test.csv", sep="\t")

df_final_2 = df_final[['date','plate','bot_id','LC_A','HC_A','Intact_A']]
df_final_2.columns = ['date','plate','bot_id','Peak_1_A','Peak_2_A','Intact_A']

df_final_3 = df_final_2.round(decimals=1)
df_final_3['Peak_1_A'].values[df_final_3['Peak_1_A'] > 0] = 1
df_final_3['Peak_2_A'].values[df_final_3['Peak_2_A'] > 0] = 1
df_final_3['Intact_A'].values[df_final_3['Intact_A'] > 0] = 1

df_final_3 = df_final_3.sort_values(['date', 'plate', 'bot_id']).fillna(0)

df_4 = df_final_3.copy()
df_4.drop_duplicates(subset=None,keep='first', inplace=True)

'''
df_4['A_bool'] = df_4['Peak_1_A'] != df_4['Peak_2_A']
df_4['B_bool'] = df_4['Peak_1_B'] != df_4['Peak_2_B']
df_4['E_bool'] = df_4['Peak_1_E'] != df_4['Peak_2_E']
df_4['F_bool'] = df_4['Peak_1_F'] != df_4['Peak_2_F']
print(df_4)
'''

df_4['Peak_1_A'] = np.where(np.logical_and(df_4['Peak_1_A']==0,df_4['Peak_2_A']==1) , -1 , df_4['Peak_1_A'])
df_4['Peak_2_A'] = np.where(np.logical_and(df_4['Peak_1_A']==1,df_4['Peak_2_A']==0) , -1 , df_4['Peak_2_A'])


def high_1(val):
	if val > 0:
		color = '#009933'
	elif val == -1:
		color = '#FFCC33'
	else:
		color = '#FF6666'
	return 'background-color: %s' % color

df_4 = df_4.reset_index(drop=True).style.applymap(high_1, subset=pd.IndexSlice[:, ['Peak_1_A','Peak_2_A','Intact_A']])
df_4.to_excel("endopep_peak_list_b.xlsx", index=False)



print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
