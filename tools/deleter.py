# coding=utf-8
import os


def deleter(file_path):
    """
    指定したディレクトリの中でMacの邪魔ファイルを消す
    :param file_path:
    :return:
    """
    for item in os.listdir(file_path):
        item = file_path + "/" + item
        if not os.path.isdir(item):
            if '._' in item or 'DS_Store' in item:
                print('delete this item :' + item)
                os.remove(item)
        else:
            deleter(item)


if __name__ == '__main__':
    print('PLEASE TEST MINIMUM STRUCTURE')
    print("if you have any losses, I cannot take responsibility.")
    print("put directory name you want to clean up")
    file_path = raw_input('>>> ')
    deleter(file_path)