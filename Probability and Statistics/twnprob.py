"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-28 02:11:00
Last Modified by:----
Last Modified time:----
Title : In my town, it's rainy one third of the days. Given that it is rainy, there will be heavy
traffic with probability 12, and given that it is not rainy, there will be heavy traffic with probability
14. If it's rainy and there is heavy traffic, I arrive late for work with probability 12. On the other
hand, the probability of being late is reduced to 18 if it is not rainy and there is no heavy traffic.
In other situations (rainy and no traffic, not rainy and traffic) the probability of being late is 0.25.
You pick a random day.
"""
import random
#probability that it will rain 
p_rain=1/3

#probability that it will not rain
p_notrain=1-p_rain

#probability that there will be traffic given it will rain 
p_tgr=1/2
#probability that there will be no traffic given it will rain
p_ntgr=1-p_tgr

#probability that there will be traffic given it will not rain
p_tgnr=1/4
#probability that there will be no traffic given it will not rain
p_ntgnr=1-p_tgnr

#probability that individual will be late given that there will be traffic and it will rain 
p_lgtndr=1/2
#probability that individual will not be late given that there will be traffic and it will rain 
p_lgtndr=1-p_lgtndr

#probability that the individual will be late given there will be no traffic and it will rain
p_lgntndr=1/4
#probability that the individual will not be late given there will be no traffic and it will rain
p_nlgntndr=1-p_lgntndr

#probability that the individual will be late given there will be traffic and it will not rain
p_lgtnndr=1/4
#probability that the individual will not be late given there will be traffic and it will not rain
p_nlgtnndr=1-p_lgtnndr

#probability that the individual will be late given there will be no traffic and it will not rain
p_lgntndnr=1/8
#probability that the individual will be not late given there will be no traffic and it will not rain
p_nlgntndnr=1-p_lgntndnr

#probability individual will be late and it will rain and there will be traffic 
p_lndrndt=p_rain*p_tgr*p_lgtndr
#probability individual will not be late and it will rain and there will be traffic
p_nlndrndt=p_rain*p_tgr*p_lgtndr

#probability that the individual will be late and there will be no traffic and it will rain
p_lndntndr=p_rain*p_ntgr*p_lgntndr
#probability that the individual will not be late and there will be no traffic and it will rain
p_nlndntndr=p_rain*p_ntgr*p_nlgntndr

#probability that the individual will be late and there will be traffic and it will not rain
p_lndtndnr=p_notrain*p_tgnr*p_lgtnndr
#probability that the individual will not be late and there will be traffic and it will not rain
p_nlndtndnr=p_notrain*p_tgnr*p_nlgtnndr

#probability that the individual will be late and there will be no traffic and it will not rain
p_lndntndnr=p_notrain*p_ntgnr*p_lgntndnr
#probability that the individual will not be late and there will be no traffic and it will not rain
p_nlndntndnr=p_notrain*p_ntgnr*p_nlgntndnr

#final prob check
if p_lndrndt+p_nlndrndt+p_lndntndr+p_nlndntndr+p_lndtndnr+p_nlndtndnr+p_lndntndnr+p_nlndntndnr==1:
    print('Verified')


questions = {'What is the probability that it\'s not raining and there is heavy traffic and I am not late?':p_nlndtndnr, 
            'What is the probability that I am late':(p_lndrndt+p_lndntndr+p_lndtndnr+p_lndntndnr), 
            'Given that I arrived late at work, what is the probability that it rained that day?':(p_lndrndt+p_lndntndr)/(p_lndrndt+p_lndntndr+p_lndtndnr+p_lndntndnr)}

print(questions.values())