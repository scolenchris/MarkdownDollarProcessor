import os
import glob


# 读取post_file
def load_post_file(md_file):
    _post_str = ""
    with open(md_file, "r", encoding="utf-8") as f1:
        for eachline in f1:
            _post_str += eachline
    return _post_str


# 寻找$-$对或者$$-$$对
def find_next_dollar_pair(md_str):
    if len(md_str) == 0:
        return False, None
    head = -1
    end = -1

    for inx in range(len(md_str)):
        if md_str[inx] == "$" and head == -1:
            head = inx
            break

    if head == -1:
        return False, None

    # 跳过连续的$
    jump_head = head + 1
    for inx in range(head + 1, len(md_str)):
        if md_str[inx] == "$":
            jump_head += 1
        else:
            break

    # 判断寻找下一个有效$结尾
    for inx in range(jump_head, len(md_str)):
        if md_str[inx] == "$" and end == -1:
            end = inx
            break

    real_end = end + 1
    for inx in range(end + 1, len(md_str)):
        if md_str[inx] == "$":
            real_end += 1
        else:
            break

    return True, (head, real_end)


# 写入新的post_file
def write_post_file(md_file, u_post_str):
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(u_post_str)
    return True


def process_files_in_directory(directory):
    # 使用 glob 来获取所有的 Markdown 文件
    for md_file in glob.glob(os.path.join(directory, "*.md")):
        _post_str = load_post_file(md_file)
        u_post_str = _post_str  # Assuming the file content is already in utf-8

        new_post_str = ""
        ret = True
        while ret:
            ret, pos_pair = find_next_dollar_pair(u_post_str)
            if ret:
                start = pos_pair[0]
                end = pos_pair[1]
                # 提取 $...$ 或 $$...$$ 包裹的内容
                dollar_content = u_post_str[start:end]
                # 如果是多行公式，去掉换行符
                if dollar_content.startswith("$$") and dollar_content.endswith("$$"):
                    dollar_content = dollar_content.replace("\n", "")
                # 拼接 {% raw %} 和 {% endraw %}
                new_post_str += (
                    u_post_str[:start] + "{% raw %}" + dollar_content + "{% endraw %}"
                )
                u_post_str = u_post_str[end:]
            else:
                new_post_str += u_post_str

        write_post_file(md_file, new_post_str)


if __name__ == "__main__":
    directory_path = "./mk"  # 在这里设置你的文件夹路径
    process_files_in_directory(directory_path)
