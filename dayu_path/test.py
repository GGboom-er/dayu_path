import os


def batch_rename_files( folder_path, prefix='', suffix='', start_number=1 ):
    """
    批量重命名指定文件夹下的所有文件。

    参数：
        folder_path (str): 文件夹路径。
        prefix (str): 文件名前缀。
        suffix (str): 文件名后缀。
        start_number (int): 文件序号起始值。

    返回：
        None
    """
    if not os.path.exists(folder_path):
        print(f"文件夹路径不存在：{folder_path}")
        return

    files = os.listdir(folder_path)
    files.sort()  # 保证文件按顺序处理
    file_count = len(files)

    print(f"正在处理 {file_count} 个文件...")

    for i, file_name in enumerate(files, start=start_number):
        old_file_path = os.path.join(folder_path, file_name)

        # 检查是否是文件，跳过子文件夹
        if not os.path.isfile(old_file_path):
            continue

        # 获取文件扩展名
        file_extension = os.path.splitext(file_name)[1]

        # 生成新文件名
        new_name = f"{prefix}{i}{suffix}{file_extension}"
        new_file_path = os.path.join(folder_path, new_name)

        # 重命名文件
        try:
            os.rename(old_file_path, new_file_path)
            print(f"已重命名：{file_name} -> {new_name}")
        except Exception as e:
            print(f"重命名失败：{file_name} -> {new_name}, 错误：{e}")

    print("重命名完成！")


# 示例用法
folder = r"C:\Users\yuweiming\Documents\WXWork\1688853827944262\Cache\Video\2025-01"  # 修改为你的目标文件夹路径
batch_rename_files(folder, prefix="vido_", suffix="", start_number=1)
