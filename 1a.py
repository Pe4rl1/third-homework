par1 = [a for a in input().split()]
par2 = [a for a in input().split()]

for a in range(0,len(par1)):
    gipotinuza = (int(par1[a])**2+int(par2[a])**2)**0.5
    ploshad = int(par1[a])*int(par2[a])/2
    print(f'Треугольник {a + 1} с катетами {int(par1[a])} and {int(par2[a])} имеет S {ploshad} and гипотенузу {gipotinuza}')