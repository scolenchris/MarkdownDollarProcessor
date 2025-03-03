# MarkdownDollarProcessor

## Description

**English:**  
MarkdownDollarProcessor is a Python script designed to process Markdown files. It detects content wrapped in `$...$` or `$$...$$` (typically math equations) and adds `{% raw %}` and `{% endraw %}` tags only when the content contains `{{` or `}}`. This prevents template engines like Jekyll,Hexo from misinterpreting the content as part of their syntax.

**中文：**  
MarkdownDollarProcessor 是一个用于处理 Markdown 文件的 Python 脚本。它会检测 `$...$` 或 `$$...$$` 包裹的内容（通常是数学公式），并在内容包含 `{{` 或 `}}` 时，批量自动添加 `{% raw %}` 和 `{% endraw %}` 标签，以防止 Jekyll,Hexo 等模板引擎误解析这些内容。

---

## Features

- **English:**

  - Detects math expressions wrapped in `$...$` or `$$...$$`.
  - Adds `{% raw %}` and `{% endraw %}` only when `{{` or `}}` is present.
  - Handles both single-line (`$...$`) and multi-line (`$$...$$`) math expressions.
  - Keeps the original formatting of Markdown files where no modifications are needed.

- **中文：**
  - 检测 `$...$` 或 `$$...$$` 包裹的数学表达式。
  - 仅在内容包含 `{{` 或 `}}` 时添加 `{% raw %}` 和 `{% endraw %}`。
  - 支持单行公式（`$...$`）和多行公式（`$$...$$`）。
  - 对无需修改的 Markdown 文件保持其原始格式。

---

## Installation

**Prerequisites:**

- Python 3.x installed on your system.

**Steps:**

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/MarkdownDollarProcessor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MarkdownDollarProcessor
   ```

---

## Usage

**English:**

1. Place your Markdown files (with `.md` extension) in a directory.
2. Update the `directory_path` variable in the script to point to the folder containing your Markdown files:
   ```python
   directory_path = "./your-directory"
   ```
3. Run the script:
   ```bash
   python dollar.py
   ```
4. The script will process all `.md` files in the directory and modify them in place.

**中文说明：**

1. 将你的 Markdown 文件（后缀为 `.md`）放置在一个文件夹中。
2. 修改脚本中的 `directory_path` 变量，指向包含 Markdown 文件的文件夹路径：
   ```python
   directory_path = "./your-directory"
   ```
3. 运行脚本：
   ```bash
   python dollar.py
   ```
4. 脚本会处理目录中的所有 `.md` 文件，并直接修改它们。

---

## Example

**Input Markdown File (`example.md`):**

```markdown
This is a test file.

Here is an inline math expression: $E=mc^2$.

Here is a block math expression:

$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}.
$$

Here is a formula with Liquid syntax: ${{ a + b }}$.

Here is another formula with closing braces: $a + b = }}$.

Some text without dollar signs.
```

**Output Markdown File (`example.md` after running the script):**

```markdown
This is a test file.

Here is an inline math expression: $E=mc^2$.

Here is a block math expression:
$$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}.$$

Here is a formula with Liquid syntax: {% raw %}${{ a + b }}${% endraw %}.

Here is another formula with closing braces: {% raw %}$a + b = }}${% endraw %}.

Some text without dollar signs.
```

---

## Notes

- **English:**

  - The script modifies files **in place**, so make sure to back up your files if needed.
  - Only files with `.md` extension will be processed.
  - The script does not process files recursively; you need to place all `.md` files in a single directory.

- **中文说明：**
  - 脚本会直接修改文件，请确保在运行前备份你的文件。
  - 仅处理 `.md` 扩展名的文件。
  - 脚本不会递归处理文件夹，你需要将所有 `.md` 文件放置在同一个目录中。

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

**English:**  
Contributions are welcome! Feel free to open issues or submit pull requests.

**中文说明：**  
欢迎贡献代码！请随时提交问题或拉取请求。

---

### Repository Summary

- **Repository Name:** `MarkdownDollarProcessor`
- **Description (English):** A Python script to process Markdown files by detecting `$...$` or `$$...$$` content and adding `{% raw %}` and `{% endraw %}` when necessary.
- **Description (中文):** 一个用于处理 Markdown 文件的 Python 脚本，检测 `$...$` 或 `$$...$$` 包裹的内容，并在必要时添加 `{% raw %}` 和 `{% endraw %}`。
