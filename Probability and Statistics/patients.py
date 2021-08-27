"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-28 04:20:00
Last Modified by:----
Last Modified time:----
Title : In a particular pain clinic, 10% of patients are prescribed narcotic pain killers. Overall,
five percent of the clinic’s patients are addicted to narcotics (including pain killers and illegal
substances). Out of all the people prescribed pain pills, 8% are addicts. If a patient is an addict,
write a program to find the probability that they will be prescribed pain pills?
"""

#probability of patient being prescribed narcotics
p_ppn=1/100

#probability that patient is an addict
p_addict=5/100

#probability of patient being an addict given he is prescribed narcotics
p_agppn=8/100 

#by bayes theorem 
#probability that patient is prescribed narcotics given that he/she is an addict
p_ppnga=(p_agppn*p_ppn)/p_addict
print('If a patient is an addict, the probability that they will be prescribed pain pills is {}'.format(p_ppnga))