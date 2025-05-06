import os
import re
from datetime import datetime
import pathlib

def update_config_toml(config_path, animation_dir, photos_dir):
    """
    指定されたディレクトリにある yyyymmdd.gif と yyyymmdd.webp ファイルの名前を
    yyyy-mm-dd 形式に変換し、gif は古い順、webp は古い順に config.toml に書き込みます。

    Args:
        config_path (str): config.toml のパス。
        animation_dir (str): .gif ファイルがあるディレクトリのパス。
        photos_dir (str): .webp ファイルがあるディレクトリのパス。
    """

    # 絶対パスを取得
    base_path = pathlib.Path(__file__).parent.resolve()
    config_path = os.path.join(base_path, config_path)
    animation_dir = os.path.join(base_path, animation_dir)
    photos_dir = os.path.join(base_path, photos_dir)
    photos_imgs_dir = os.path.join(photos_dir, "imgs")  # photos/imgs ディレクトリの絶対パス

    gif_files = []
    webp_files = []

    # .gif ファイルの処理
    if os.path.exists(animation_dir) and os.path.isdir(animation_dir):
        for filename in os.listdir(animation_dir):
            match = re.match(r"(\d{8})\.gif$", filename)
            if match:
                date_str = match.group(1)
                date_obj = datetime.strptime(date_str, "%Y%m%d")
                formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
                gif_files.append((date_obj, formatted_date, 0))  # (日付オブジェクト, フォーマット済み日付, フォーマット)
        gif_files.sort(key=lambda item: item[0])  # 日付オブジェクトでソート

    # .webp ファイルの処理
    if os.path.exists(photos_dir) and os.path.isdir(photos_dir):
        if os.path.exists(photos_imgs_dir) and os.path.isdir(photos_imgs_dir):  # photos/imgs の存在を確認
            for filename in os.listdir(photos_imgs_dir):
                match = re.match(r"(\d{8})\.webp$", filename)
                if match:
                    date_str = match.group(1)
                    date_obj = datetime.strptime(date_str, "%Y%m%d")
                    formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
                    webp_files.append((date_obj, formatted_date, 1))  # (日付オブジェクト, フォーマット済み日付, フォーマット)
            webp_files.sort(key=lambda item: item[0])  # 日付オブジェクトでソート

    # 結果の統合
    files_list = [item[1] for item in gif_files] + [item[1] for item in webp_files]
    format_list = [item[2] for item in gif_files] + [item[2] for item in webp_files]

    # config.toml の読み込みと更新
    try:
        with open(config_path, 'r') as f:
            lines = f.readlines()

        updated_lines = []
        in_extra_section = False
        found_files = False
        found_format = False

        for line in lines:
            if line.strip() == "[extra]":
                updated_lines.append(line)
                in_extra_section = True
            elif in_extra_section:
                if line.strip().startswith("files ="):
                    updated_lines.append(f"files = {files_list}\n")
                    found_files = True
                elif line.strip().startswith("format ="):
                    updated_lines.append(f"format = {format_list}\n")
                    found_format = True
                else:
                    updated_lines.append(line)
            else:
                updated_lines.append(line)

        # [extra] セクションが存在しない場合の追加
        if not in_extra_section:
            updated_lines.append("\n[extra]\n")
            updated_lines.append(f"files = {files_list}\n")
            updated_lines.append(f"format = {format_list}\n")
        elif not found_files:
            updated_lines.insert(updated_lines.index("[extra]\n") + 1, f"files = {files_list}\n")
        elif not found_format:
            updated_lines.insert(updated_lines.index("[extra]\n") + 1 + (1 if found_files else 0), f"format = {format_list}\n")

        # config.toml への書き込み
        with open(config_path, 'w') as f:
            f.writelines(updated_lines)

        print(f"config.toml を更新しました。\nfiles: {files_list}\nformat: {format_list}")

    except FileNotFoundError:
        print(f"エラー: {config_path} が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    config_file = "config.toml"
    animation_directory = "animation"
    photos_directory = "photos"

    update_config_toml(config_file, animation_directory, photos_directory)