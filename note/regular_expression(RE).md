* ## 正则表达式常见表达
| 符号  | 意义                           |
| ----- | ------------------------------ |
| ^     | 匹配行的开头                   |
| $     | 匹配行的结尾                   |
| .     | 匹配任意单个字符               |
| [...] | 匹配I中的任意一个字符          |
| (...) | 设定分组                       |
| \     | 转义字符                       |
| \d    | 匹配数字[0-9]                  |
| \D    | 与\d相反                       |
| \w    | 匹配字母[a-z]，数字，下划线    |
| \w    | 与\w取反                       |
| \s    | 匹配空格                       |
| \S    | 与\s相反                       |
| +     | 前面的元素重复1次或多次        |
| *     | 前面的元素重复任意次           |
| ?     | 前面的元素重复0次或1次         |
| {n}   | 前面的元素重复n次              |
| {in,} | 前面的元素重复至少n次          |
| {n,m) | 前面的元素重复至少n次，至多m次 |