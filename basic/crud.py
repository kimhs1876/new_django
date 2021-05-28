class VectorTest(object):
    ls = ['abcd', 786, 2.23, 'john', 70.2]
    tinyls = [123, 'john']
    tp = ('abcd', 786, 2.23, 'john', 70.2)
    tinytp = (123, 'john')
    dt = {'abcd': 786, 'john': 70.2}
    tinydt = {'홍':'30세'}

# -- lsit --

    def ls_create(self):
        self.ls.append(100)
    def ls_read(self):
        print(self.ls())
    def ls_update(self):
        self.ls.extend(self.tinyls)
        print(self.ls)
    def ls_delete(self):
        self.ls.remove(786)

# -- tuple --

    def tp_create(self):
        print('불가능')
        self.tp = self.tp + (100,)
        print(self.tp)

    def tp_read(self):
        print(self.tp)
    def tp_merge(self):
        self.tp = self.tp + self.tinytp
    def tp_delete(self):
        print('불가능')


# -- dictionary --

    def dt_create(self):
        self.dt["tom"] = 100 #키는 내부적으로 list이기 때문에 []을 쓴다
        print(self.dt)
    def dt_read(self):
        print(self.dt())
    def dt_update(self):
        self.dt.update(self.tinyls)
    def dt_delete(self):
        del self.dt[0]


    @staticmethod
    def main():
        v = VectorTest()
        while 1:
            menu = int(input('0.Exit\n'
                             'LIST : 1.Create, 2.Read ,3.Udate, 4.Delete\n'
                             'TUPLE : 5.Create, 6.Read ,7.Udate, 8.Delete\n'
                             'DICTIONARY : 9.Create, 10.Read ,11.Udate, 12.Delete\n'
                             ))
            if menu == 0:
                print('--Exit--')
                break
            elif menu == 1:
                v.ls_create()
            elif menu == 2:
                v.ls_read()
            elif menu == 3:
                v.ls_update()
            elif menu == 4:
                v.ls_delete()
            elif menu == 5:
                v.tp_create()
            elif menu == 6:
                v.tp_read()
            elif menu == 7:
                v.tp_update()
            elif menu == 8:
                v.tp_delete()
            elif menu == 9:
                v.dt_create()
            elif menu == 10:
                v.dt_read()
            elif menu == 11:
                v.dt_update()
            elif menu == 12:
                v.dt_delete()
            else:
                print('--Wrong Number--')

VectorTest.main()





