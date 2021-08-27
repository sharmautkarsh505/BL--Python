"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-28 03:07:00
Last Modified by:----
Last Modified time:----
Title :Given the following statistics, write a program to find the probability that a woman has
cancer if she has a positive mammogram result? One percent of women over 50 have breast cancer.Ninety 
percent of women who have breast cancer test positive on mammograms.Eight percent of women will have 
false positive,
"""
#probability of women with age>50 having cancer 
p_cancer=0.01
p_notcancer=1-p_cancer

#probability of +test given that individual has cancer
p_ptgc=0.9
#probability of having a positive test and have cancer
p_ptndc=p_ptgc*p_cancer
print(p_ptndc)
#probability of a positive test 
p_ptest=(p_ptndc)+(p_notcancer*0.08)
print(p_ptest)

#probability of woman has cancer given that she has a postive test
p_cgpt=p_ptndc/p_ptest
print(p_cgpt)





