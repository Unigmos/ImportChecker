#-------------------------------------------------------------------------------
# Name:         Import Checker
# Purpose:      Importしたライブラリを表示するデスクトップアプリケーション
#
# Author:       Shaneron
#
# Created:      2021/01/04
# Copyright:    (c) Shaneron 2021
#-------------------------------------------------------------------------------

def main():
    try:
        import time

        print("〇調査したいファイルをドラッグ&ドロップしてEnterを押してください。")
        read_file = input()

        import_contents, from_contents = check_import(read_file)

        print('・importしたライブラリはこちら↓\n')
        for content in import_contents:
            time.sleep(0.1)
            print(f"{content}")

        print('\n・importしたライブラリはこちら(fromスタート)↓\n')
        for content in from_contents:
            time.sleep(0.1)
            print(f"{content}")


        input("\nEnterで終了します。")

    except ModuleNotFoundError as NO_MODULE_ERROR:
        print(f"ModuleNotFoundError: {NO_MODULE_ERROR} at main")
    except FileNotFoundError as NOT_FOUND_ERROR:
        print(f"ModuleNotFoundError: {NOT_FOUND_ERROR} at main")

# importチェック処理
def check_import(path):
    import_data = []
    from_data = []

    with open(path, encoding="utf-8") as file_data:
        lines = file_data.readlines()

    replace_line = [linedata.replace(' ', '') for linedata in lines]
    replace_and_strip_line = [replacedata.replace('\n', '') for replacedata in replace_line]
    
    # import行の抽出
    for pyline in replace_and_strip_line:
        if pyline.startswith("import", 0):
            del_import = pyline.replace('import', '')
            import_data.append(del_import)
        elif pyline.startswith("from", 0):
            del_import = pyline.replace('from', 'from ')
            del_from = del_import.replace('import', ' import ')
            from_data.append(del_from)

    # セット→リストにすることで重複要素の削除
    import_data = list(set(import_data))
    from_data = list(set(from_data))

    return import_data, from_data

if __name__ == '__main__':
    main()
