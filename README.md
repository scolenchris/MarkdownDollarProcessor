# MarkdownDollarProcessor
A Python script to process Markdown files by detecting content wrapped in $...$ or $$...$$ and adding {% raw %} and {% endraw %} tags when necessary (e.g., when {{ or }} are present) to prevent misinterpretation by template engines like Jekyll and Hexo.
