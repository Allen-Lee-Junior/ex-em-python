metros = float(input('A distancia em metros :'))
print(' A medida de  {} coresponde a ...'.format(metros,))
mm = metros * 1000
cm = metros * 100
dm = metros * 10
dam =metros / 10
hm = metros / 100
km = metros / 1000
print('{}mm.\n{}cm.\n{}dm.\n{}dam.\n{}hm.\n{}km.\n'.format(mm, cm, dm, dam, hm, km, ))