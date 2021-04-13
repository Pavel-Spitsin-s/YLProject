import command_system


def broncan(body, user_id):
    tok = body.split()[1]
    f = open('data.txt', encoding='utf-8')
    t = f.readlines()
    dt = []
    for line in t:
        line = line.split(' ')
        line[5] = line[5][:-1]
        dt.append(line)
    n = 0
    for lines in dt:
        if lines[-1] == tok:
            break
        n += 1
    message = dt[n][0] + ' ' + dt[n][1] + ', '  'ваша бронь на ' + dt[n][2] + ' ' + 'была успешно отменена.'
    del dt[n]
    f.close()
    data = []
    for i in dt:
        i = ' '.join(i) + '\n'
        data.append(i)
    f = open('data.txt', 'wt', encoding='utf-8')
    for i in data:
        f.write(i)

    return message
info_command = command_system.Command()

info_command.keys = ['Отмена']
info_command.description = 'Удалить бронь(Пример: Отмена (Секретный код))'
info_command.process = broncan