import command_system
def rasp(body, user_id):
    f = open('data.txt')
    data = []
    rasp = ''
    _data = []
    data_listed = []
    datan = body.split()[1]
    for line in f:
        line = line[:-8]
        data.append(line)
    f.close()
    for i in data:
        i = i.split(' ')
        data_listed.append(i)
    for i in data_listed:
        if i[2] == datan:
            _data.append(i)
    rasp += 'Расписание на ' + datan + ':\n' + '   ФИ Дата Время начала Время окончания\n'
    for i in _data:
        h = 1
        for j in i:
            if h == 5:
                rasp += j + '\n'
            else:
                rasp += j + ' '
                h += 1
    return rasp


info_command = command_system.Command()

info_command.keys = ['Расписание', 'расписание']
info_command.description = 'Вывод расписания(Например:Расписание 29.04.2020)'
info_command.process = rasp