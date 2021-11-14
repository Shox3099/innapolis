cfS = 0.02212389380530973; # растояние от одного семечка до другого / радиус подсолнечника
vitCount = 11; #Колличество витков (из центра)
sunCount = 10; #Колличество подсолнухов на 1 м2
gld = 1.61803398875;gldScore = cfS;count = 1;score = 1;i = 0;z = 1;al=0
while i <= 0:gldScore  = cfS + ((z+z)*cfS)/gld;i = (i + ((gld *(gldScore - 1))*100));z = z*2;count += 1;print(str(count))
for al in range(count): score+=al;

print(sunCount * score * ( 1000 / score * 1) / 10000) #биологическая урожайность