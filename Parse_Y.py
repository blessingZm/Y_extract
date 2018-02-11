"""
解析Y文件
"""
import os
import codecs


class ParseYfile:
    def __init__(self, y_file):
        self.year = os.path.split(y_file)[-1][7: 11]
        self.datas = []
        with codecs.open(y_file, 'rb', 'gbk') as yf:
            while True:
                bf = yf.readline()
                if "??????" in bf:
                    break
                self.datas.append(bf)

    def infos(self):
        datas = [self.year]
        infos = self.datas[0].strip()
        for i, d in enumerate(infos.split()[: 5]):
            if i < 3:
                datas.append(d)
            else:
                datas.append(str(int(d) / 10))
        yield datas

    def pp(self):
        datas_buf = self.datas[2: 15]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                for j, d in enumerate(buf):
                    if j in [4, 6]:
                        datas.append(d)
                    else:
                        try:
                            datas.append(str(int(d) / 10))
                        except ValueError:
                            datas.append(d)
            else:
                observe_time = self.year
                datas.append(observe_time)
                for dd in buf[: 4]:
                    try:
                        datas.append(str(int(dd) / 10))
                    except ValueError:
                        datas.append(dd)
                datas.append(buf[4] + '-' + buf[5])
                datas.append(str(int(buf[6]) / 10))
                datas.append(buf[7] + '-' + buf[8][: -1])
            yield datas

    def tt(self):
        datas_buf = self.datas[29: 42]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                buf = buf[9:]
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                for j, d in enumerate(buf):
                    if j in [4, 6]:
                        datas.append(d)
                    else:
                        try:
                            datas.append(str(int(d) / 10))
                        except ValueError:
                            datas.append(d)
            else:
                observe_time = self.year
                datas.append(observe_time)
                for dd in buf[: 4]:
                    try:
                        datas.append(str(int(dd) / 10))
                    except ValueError:
                        datas.append(dd)
                datas.append(buf[4] + '-' + buf[5])
                datas.append(str(int(buf[6]) / 10))
                datas.append(buf[7] + '-' + buf[8][: -1])
            yield datas

    def uu(self):
        datas_buf = self.datas[57: 70]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                for j, d in enumerate(buf):
                    datas.append(d)
            else:
                observe_time = self.year
                datas.append(observe_time)
                for dd in buf[: 2]:
                    datas.append(dd)
                datas.append(buf[2] + '-' + buf[3][: -1])
            yield datas

    # 降水量
    def rrr(self):
        datas_buf = self.datas[98: 111]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                buf = buf[9:]
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                for j, d in enumerate(buf):
                    if j == 2:
                        datas.append(d)
                    else:
                        try:
                            datas.append(str(int(d) / 10))
                        except ValueError:
                            datas.append('0.0')
            else:
                observe_time = self.year
                datas.append(observe_time)
                for dd in buf[: 2]:
                    try:
                        datas.append(str(int(dd) / 10))
                    except ValueError:
                        datas.append('0.0')
                datas.append(buf[2] + '-' + buf[3][: -1])
            yield datas

    # 各级降水日数
    def dif_levels_rain_days(self):
        datas_buf = self.datas[111: 124]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                for j, d in enumerate(buf):
                    try:
                        datas.append(str(int(d)))
                    except ValueError:
                        datas.append('0')
            else:
                observe_time = self.year
                datas.append(observe_time)
                for dd in buf:
                    try:
                        datas.append(str(int(dd)))
                    except ValueError:
                        datas.append('0')
            yield datas

    # 各时段年最大降水量
    def dif_time_maxR(self):
        datas_buf = self.datas[124: 139]
        datas = []
        observe_time = self.year
        datas.append(observe_time)
        for i, data in enumerate(datas_buf):
            buf = data.split()
            try:
                datas.append(str(int(buf[0]) / 10))
            except ValueError:
                datas.append('0.0')
        yield datas

    # 最长连续降水日数
    def continu_rain_days(self):
        datas_buf = self.datas[139: 152]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                datas.append(str(int(buf[0])))
                try:
                    datas.append(str(int(buf[1]) / 10))
                except ValueError:
                    datas.append(buf[1])
                for j in range(2, 6, 2):
                    datas.append(buf[j] + '-' + buf[j + 1])
            else:
                observe_time = self.year
                datas.append(observe_time)
                datas.append(str(int(buf[0])))
                try:
                    datas.append(str(int(buf[1]) / 10))
                except ValueError:
                    datas.append(buf[1])
                datas.append('-'.join(buf[2: 5]))
                datas.append('-'.join(buf[5: 7]) + '-' + buf[7][: -1])
            yield datas

    # 最长连续无降水日数
    def continu_no_rain_days(self):
        datas_buf = self.datas[152: 165]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                datas.append(str(int(buf[0])))
                for j in range(1, 5, 2):
                    datas.append(buf[j] + '-' + buf[j + 1])
            else:
                observe_time = self.year
                datas.append(observe_time)
                datas.append(str(int(buf[0])))
                datas.append('-'.join(buf[1: 4]))
                datas.append('-'.join(buf[4: 6]) + '-' + buf[6][: -1])
            yield datas

    # 25类天气日数
    def weather_days(self):
        datas_buf = self.datas[166: 179]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
            else:
                observe_time = self.year
            datas.append(observe_time)
            for d in buf:
                if '=' in d:
                    d = d[: -1]
                try:
                    datas.append(str(int(d)))
                except ValueError:
                    datas.append('0')
            yield datas

    # 初终日期数据及无霜日数
    def begin_end_date(self):
        datas_buf = self.datas[179: 188]
        datas = []
        observe_time = self.year
        datas.append(observe_time)
        for i, data in enumerate(datas_buf):
            buf = data.split()
            if i < 7:
                datas.append('-'.join(buf[: 2]) + '/' + '-'.join(buf[2: 4]))
                try:
                    datas.append(str(int(buf[4])))
                except ValueError:
                    datas.append('0')
                datas.append('-'.join(buf[5:]))
            elif i == 8:
                datas.append(str(int(buf[0][: -1])))
        yield datas

    def Le(self):
        datas_buf = self.datas[189: 202]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
            else:
                observe_time = self.year
            datas.append(observe_time)
            for d in buf:
                if '=' in d:
                    d = d[: -1]
                try:
                    datas.append(str(int(d) / 10))
                except ValueError:
                    datas.append(d)
            yield datas

    # 平均风速段
    def ws(self):
        datas_buf = self.datas[231: 244]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
                datas.append(observe_time)
                for j, d in enumerate(buf):
                    if j in [0, 1, 4]:
                        datas.append(str(int(d) / 10))
                    elif 'P' in d:
                        datas.append(d.replace('P', ''))
                    else:
                        datas.append(d)
            else:
                observe_time = self.year
                datas.append(observe_time)
                datas.append(str(int(buf[0]) / 10))
                for j in range(1, 9, 4):
                    datas.append(str(int(buf[j]) / 10))
                    if "P" in buf[j + 1]:
                        datas.append(buf[j + 1].replace('P', ''))
                    else:
                        datas.append(buf[j + 1])
                    if j < 2:
                        datas.append('-'.join(buf[j + 2: j + 4]))
                    else:
                        datas.append(buf[j + 2] + '-' + buf[j + 3][: -1])
            yield datas

    # 16个风向平均风速
    def dif_wd_ws(self):
        datas_buf = self.datas[244: 292]
        for line in self.datas[304: 308]:
            datas_buf.append(line)
        for i in range(13):
            datas = []
            data = datas_buf[i * 4: i * 4 + 4]
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
            else:
                observe_time = self.year
            datas.append(observe_time)
            for d in data:
                buf = d.split()
                if i < 12:
                    for dd in buf[2:: 5]:
                        try:
                            datas.append(str(int(dd) / 10))
                        except ValueError:
                            datas.append('0.0')
                else:
                    for dd in buf[2:: 6]:
                        try:
                            datas.append(str(int(dd) / 10))
                        except ValueError:
                            datas.append('0.0')
            yield datas

    # 各风向频率
    def dif_wd_frequecy(self):
        datas_buf = self.datas[244: 292]
        c_buf = self.datas[292: 304]
        for line in self.datas[308: 309]:
            c_buf.append(line)
        for line in self.datas[304: 308]:
            datas_buf.append(line)
        for i in range(13):
            datas = []
            data = datas_buf[i * 4: i * 4 + 4]
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
            else:
                observe_time = self.year
            datas.append(observe_time)
            for d in data:
                buf = d.split()
                if i < 12:
                    for dd in buf[3:: 5]:
                        try:
                            datas.append(str(int(dd)))
                        except ValueError:
                            datas.append('0')
                else:
                    for dd in buf[3:: 6]:
                        try:
                            datas.append(str(int(dd)))
                        except ValueError:
                            datas.append('0')
            c_data = c_buf[i].split()[-1]
            try:
                if '=' in c_data:
                    datas.append(str(int(c_data[: -1])))
                else:
                    datas.append(str(int(c_data)))
            except ValueError:
                datas.append('0')
            yield datas

    # 各风向最大风速
    def dif_wd_wsMax(self):
        datas_buf = self.datas[244: 292]
        for line in self.datas[304: 308]:
            datas_buf.append(line)
        for i in range(13):
            datas = []
            data = datas_buf[i * 4: i * 4 + 4]
            if i < 12:
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
            else:
                observe_time = self.year
            datas.append(observe_time)
            for d in data:
                buf = d.split()
                if i < 12:
                    for dd in buf[4:: 5]:
                        try:
                            datas.append(str(int(dd) / 10))
                        except ValueError:
                            datas.append('0.0')
                else:
                    for dd in buf[4:: 6]:
                        try:
                            datas.append(str(int(dd) / 10))
                        except ValueError:
                            datas.append('0.0')
            yield datas

    def ss(self):
        datas_buf = self.datas[378: 391]
        for i, data in enumerate(datas_buf):
            buf = data.split()
            datas = []
            if i < 12:
                buf = buf[3:]
                observe_time = self.year + '-' + '{:0>2}'.format(str(i + 1))
            else:
                observe_time = self.year
            datas.append(observe_time)
            for j, d in enumerate(buf):
                if '=' in d:
                    d = d[: -1]
                if j == 1:
                    datas.append(d)
                elif j == 0:
                    try:
                        datas.append(str(int(d) / 10))
                    except ValueError:
                        datas.append('0.0')
                else:
                    try:
                        datas.append(str(int(d)))
                    except ValueError:
                        datas.append('0')
            yield datas


if __name__ == "__main__":
    file = r'.\Y_files\57461\Y57461-2016.TXT'
    parseY = ParseYfile(file)
    for dddd in parseY.begin_end_date():
        print(dddd)
