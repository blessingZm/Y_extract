"""
将Y文件数据写入数据库
"""
import os
import sqlite3
from Parse_Y import ParseYfile


def write_datas(db_file, y_file, config='db_config.ini'):
    parse_y = ParseYfile(y_file)
    db = sqlite3.connect(db_file)
    cu = db.cursor()
    with open(config, 'r') as f:
        for line in f.readlines():
            buf = line.split()
            table_name = buf[0]
            index_name = buf[1:]
            create_table_command = """
            create table if not exists {} ({} PRIMARY KEY(ObserveTime))""".format(table_name,
                                                                                  ' char(20),'.join(index_name) +
                                                                                  ' char(20),')
            cu.execute(create_table_command)
            for datas in getattr(parse_y, table_name)():
                insert_datas = "','".join(datas)
                insert_command = "insert into {} values ('{}')".format(table_name, insert_datas)
                try:
                    cu.execute(insert_command)
                except Exception as e:
                    print(e)
                    pass
            db.commit()


def get_st_configs(config='st_config.ini'):
    st_ids = []
    with open(config, 'r') as f:
        f.readline()
        while True:
            buf = f.readline()
            if '=' in buf:
                break
            st_ids.append(buf.strip())
        start_end_year = f.readline().split()
        start_year = start_end_year[0]
        end_year = start_end_year[1]
    return st_ids, start_year, end_year


if __name__ == "__main__":
    stIds, startYear, endYear = get_st_configs()
    for stId in stIds:
        YDir = os.path.join('.\Y_files', stId)
        Yfiles = os.listdir(YDir)
        dbFile = os.path.join(r'.\db_files', 'Y_' + str(stId) + '.db')
        for yFile in Yfiles:
            if int(yFile[7: 11]) in range(int(startYear), int(endYear) + 1):
                write_datas(dbFile, os.path.join(YDir, yFile))
                print("{}站{}年的数据写入{}文件完成！".format(stId, yFile[7: 11], dbFile))
