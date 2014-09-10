# -*- coding: utf-8 -*-
# Créé par jehan, le 10/11/2013
import math
a=input("entrez le nombre d'annees: ")
# 1 jours =  783 333 333 année
# 1 H = 97 222 222
# 1 mn = 1 620 370
# 1 s = 9066,3580246914
# 1 centieme = 270,0617 années
j=a/9066
jd=a/9066.3580246914
if j<60:
    jt=math.modf(jd)
    c=jt[0]*100
    print a,"annees egale a",j,"secondes",c,"centiemes"
elif j<3600:
    s=j%60
    m=j/60
    sr=jd-60*m
    srt=math.modf(sr)
    c=srt[0]*100
    print a,"annees egale a",m,"minutes",s,"secondes",c,"centiemes"
elif j<86400:
    h=j/3600
    modm=j%3600
    m=(j%3600)/60
    md=(jd-(h*3600))/60.0
    dmd=math.modf((jd-(h*3600))/60.0)
    s=modm%60
    sd=(dmd[0]*0.6)*100.0
    ct=math.modf(sd)
    c=ct[0]*100
    print a,"annees egale a",h,"heures",m,"minutes",s,"secondes",c,"centiemes. debug:",md,"mndeci",dmd[0],"partie deci"
elif j<518400 : #6 jours max
    d=j/86400
    j=j-(d*86400)
    h=j/3600
    modm=j%3600
    m=(j%3600)/60
    md=(jd-(h*3600))/60.0
    dmd=math.modf((jd-(h*3600))/60.0)
    s=modm%60
    sd=(dmd[0]*0.6)*100.0
    ct=math.modf(sd)
    c=ct[0]*100
    print a,"annees egale a",d,"jours",h,"heures",m,"minutes",s,"secondes",c,"centiemes. debug:",md,"mndeci",dmd[0],"partie deci"
else:
    print "au dela de 6 jour !",a
