from api import linode

for l in linode.view():
    print(l.label)
    for d in linode.disk.view(l.linodeid):
        print('\t', d.label)
