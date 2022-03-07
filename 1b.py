par = [a for a in input().split()]

por = 0
for a in range(0,len(par),2):
    por+=1
    gipotinuza = (int(par[a])**2+int(par[a+1])**2)**0.5
    ploshad = int(par[a])*int(par[a+1])/2
    print(f'Треугольник {por} с катетами {int(par[a])} and {int(par[a+1])} имеет S {ploshad} and гипотенузу {gipotinuza}')