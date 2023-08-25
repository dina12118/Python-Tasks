#rite python code to generate Init function of GPIO for AVR

reg = []
openb = '{'
closeb = '}'

for i in range(8):
    mode = input("please enter Bit {} mode in/out: ".format(i)).lower()
    if mode == 'in':
        reg.append('0')
    elif mode == 'out':
        reg.append('1')

reg.append('b')
reg.append('0')
reg.reverse()


init = f'void Init_PortA_DIR(void){openb}\n    DDRA = {"".join(reg)};\n {closeb}'


with open("init.c", 'w') as f:
    f.write(init)
