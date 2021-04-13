import command_system
import randtok
import datetime as dt

def reserv(body, user_id):
    message = 'неправильный формат бронирования'
    data = body.split()
    if len(data) == 6:
        if len(data[3]) == 10 and data[3].count('.') == 2 and ''.join(data[3].split('.')).isdigit():
            if data[4].count(':') == 1 and len(data[4]) == 5:
                if data[5].count(':') == 1 and len(data[5]) == 5:
                    datac = data[5].split(':')
                    if int(datac[0]) < 24 and int(datac[1]) < 60:
                        if len(str(datac[0])) == 2 and len(str(datac[1] == 2)):
                            datac = int(''.join(datac))
                            if len(str(datac)) == 4 and str(datac).isdigit():
                                if data[4].count(':') == 1 and len(data[5]) == 5:
                                    datac = data[4].split(':')
                                    if int(datac[0]) < 24 and int(datac[1]) < 60:
                                        if len(str(datac[0])) == 2 and len(str(datac[1] == 2)):
                                            datac = ''.join(datac)
                                            if len(datac) == 4 and str(datac).isdigit():
                                                if not data[1].isdigit():
                                                    if not data[1].isdigit():
                                                        datac = data[4].split(':')
                                                        data1 = dt.time(int(datac[0]), int(datac[1]))
                                                        datac = data[5].split(':')
                                                        data2 = dt.time(int(datac[0]), int(datac[1]))
                                                        if data1 < data2:
                                                            code = randtok.MakeTok()
                                                            message = 'Cтол успешно забронирован на ' + data[
                                                                3] + ' в период с ' + \
                                                                      data[
                                                                          4] + ' - ' + data[
                                                                          5] + ' на имя ' + data[1] + ' ' + data[
                                                                          2] + '.\n' + 'Ваш секретный код для отмены брони: ' + code
                                                            f = open('data.txt', 'a')
                                                            f.write(
                                                                '{0} {1} {2} {3} {4} {5}\n'.format(data[1], data[2],
                                                                                                   data[3], data[4],
                                                                                                   data[5],
                                                                                                   code))
                                                            f.close()


    return message


info_command = command_system.Command()

info_command.keys = ['Бронь', 'бронь']
info_command.description = 'забронировать стол (пример команды: бронь Иван Иванович 31.02.2020 17:30 18:20)'
info_command.process = reserv
