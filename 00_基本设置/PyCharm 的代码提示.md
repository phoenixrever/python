下面是一套 **2025 年比较成熟的 Python + Visual Studio Code 终极配置**。
目标是：**代码提示、调试、错误显示、自动补全体验接近甚至超过 PyCharm**。

我分成 **4 部分**：插件、字体、settings.json、快捷键。

---

# 一、必装插件（核心）

### 1 Python 支持

**Python**

ID

```
ms-python.python
```

功能

- Python运行
- 调试
- 虚拟环境识别

---

### 2 代码分析引擎

**Pylance**

ID

```
ms-python.vscode-pylance
```

功能

- 自动补全
- 类型推断
- import建议

---

### 3 最快 Python Linter

**Ruff**

ID

```
charliermarsh.ruff
```

特点

- 比 pylint 快 **几十到上百倍**
- 自动修复问题

---

### 4 错误直接显示在代码行

**Error Lens**

ID

```
usernamehw.errorlens
```

效果

```
age = "18"   TypeError: expected int
```

不用看 Problems 面板。

---

### 5 AI 自动补全

**GitHub Copilot**

自动生成代码：

```
# read csv file
```

直接生成代码。

---

# 二、推荐字体（代码会好看很多）

推荐：

### 1

**JetBrains Mono**

特点

- ligatures
- Python很好看

---

### 2（很多人喜欢）

**Cascadia Code**

---

字体设置：

```
settings.json
```

```
"editor.fontFamily": "JetBrains Mono, Cascadia Code, Consolas",
"editor.fontLigatures": true
```

---

# 三、终极 settings.json

打开

```
Ctrl + Shift + P
Preferences: Open Settings (JSON)
```

复制：

```json
{
  "editor.fontSize": 16,
  "editor.fontFamily": "JetBrains Mono, Cascadia Code, Consolas",
  "editor.fontLigatures": true,

  "editor.formatOnSave": true,

  "editor.hover.enabled": true,
  "editor.parameterHints.enabled": true,
  "editor.inlineSuggest.enabled": true,

  "editor.minimap.enabled": false,

  "editor.guides.bracketPairs": true,
  "editor.bracketPairColorization.enabled": true,

  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  },

  "editor.suggestSelection": "first",

  "python.analysis.typeCheckingMode": "strict",

  "python.analysis.autoImportCompletions": true,

  "python.analysis.inlayHints.variableTypes": true,
  "python.analysis.inlayHints.functionReturnTypes": true,
  "python.analysis.inlayHints.callArgumentNames": true,

  "python.analysis.diagnosticMode": "workspace",

  "python.analysis.useLibraryCodeForTypes": true,

  "ruff.lint.enable": true,

  "errorLens.enabled": true,
  "errorLens.messageEnabled": true,
  "errorLens.followCursor": "activeLine"
}
```

---

# 四、Python开发最重要快捷键

在 **Visual Studio Code**：

### 运行代码

```
Ctrl + F5
```

---

### 调试

```
F5
```

---

### 单步执行

```
F10
```

---

### 进入函数

```
F11
```

---

### 重命名变量（超级好用）

```
F2
```

例如：

```
user_name
```

改名：

```
username
```

所有引用都会改。

---

### 自动导入模块

输入：

```
datetime
```

按

```
Ctrl + .
```

自动添加

```
import datetime
```

---

# 五、让 VSCode 更像 PyCharm 的主题

推荐：

**One Dark Pro**

或者

**Dracula Official**

---

# 六、Python开发者常用插件（进阶）

如果你继续学习 Python，可以再装：

### Jupyter

**Jupyter**

---

### Git 工具

**GitLens**

---

### 自动 docstring

**autoDocstring**

---

可以，但要先说明一个重要点：
**Visual Studio Code 的 `settings.json` 实际使用的是 JSONC（JSON with Comments）**，
所以 **是允许写注释的**（`//` 或 `/* */`）。

下面是 **逐行带注释的最终版本**，我把每个配置的作用都写在旁边。

```jsonc
{
  // 编辑器字体大小
  "editor.fontSize": 14,

  // 编辑器字体优先级（如果没有 JetBrains Mono 会自动使用 Cascadia Code 或 Consolas）
  "editor.fontFamily": "JetBrains Mono, Cascadia Code, Consolas",

  // 启用编程字体连字（如 != → 特殊符号）
  "editor.fontLigatures": true,

  // 保存文件时自动格式化代码
  "editor.formatOnSave": true,

  // 鼠标悬停时显示函数说明、类型信息、文档
  "editor.hover.enabled": true,

  // 输入函数时自动显示参数提示
  "editor.parameterHints.enabled": true,

  // 启用整行智能补全（Copilot 或 AI 补全需要）
  "editor.inlineSuggest.enabled": true,

  // 关闭右侧代码缩略图（minimap），减少干扰
  "editor.minimap.enabled": false,

  // 显示括号层级辅助线
  "editor.guides.bracketPairs": true,

  // 不同括号使用不同颜色（更容易看嵌套结构）
  "editor.bracketPairColorization.enabled": true,

  // 自动补全触发条件
  "editor.quickSuggestions": {
    // 普通代码中启用补全
    "other": true,

    // 注释中不触发补全
    "comments": false,

    // 字符串中允许补全
    "strings": true,
  },

  // 自动补全时优先选择第一个建议
  "editor.suggestSelection": "first",

  // Python 类型检查模式
  // strict = 最严格（类似 PyCharm 的检查级别）
  "python.analysis.typeCheckingMode": "strict",

  // 自动补全时允许自动导入模块
  // 例如输入 datetime 会提示 from datetime import datetime
  "python.analysis.autoImportCompletions": true,

  // 在代码中显示变量类型提示
  // 例如：age = 18 : int
  "python.analysis.inlayHints.variableTypes": true,

  // 显示函数返回类型提示
  "python.analysis.inlayHints.functionReturnTypes": true,

  // 显示函数调用时参数名称
  // 例如：open(file="test.txt", mode="r")
  "python.analysis.inlayHints.callArgumentNames": true,

  // 诊断范围
  // workspace = 整个项目分析
  "python.analysis.diagnosticMode": "workspace",

  // 使用库代码推断类型（提高第三方库提示准确性）
  "python.analysis.useLibraryCodeForTypes": true,

  // 诊断严重级别覆盖
  "python.analysis.diagnosticSeverityOverrides": {
    // 未定义变量直接报错
    "reportUndefinedVariable": "error",
  },

  // 启用 Ruff 代码检查
  // Ruff 是目前最快的 Python linter
  "ruff.lint.enable": true,

  // 保存时自动修复 Ruff 可以修复的问题
  "editor.codeActionsOnSave": {
    "source.fixAll.ruff": true,
  },

  // 启用 Error Lens
  // 错误会直接显示在代码行后面
  "errorLens.enabled": true,

  // 显示错误文本
  "errorLens.messageEnabled": true,

  // 错误信息跟随光标所在行
  "errorLens.followCursor": "activeLine",
}
```

---

## 这套配置的整体效果

在 **Visual Studio Code** 里会得到类似 **PyCharm** 的体验：

1. **变量类型直接显示**

```python
age = 18        # : int
name = "Tom"    # : str
```

2. **自动导入**

输入

```
datetime
```

自动提示

```
from datetime import datetime
```

3. **未定义变量立即报错**

```
print(a)
      ^
Undefined variable
```

4. **保存自动修复代码**

来自 **Ruff**

---

如果你愿意，我还可以给你 **一份 Python 开发者的 VSCode 隐藏配置（进阶版）**，会再增加：

- **函数复杂度检测**
- **自动 import 排序**
- **Python 调试优化**
- **变量值直接显示在代码右侧（像 PyCharm Debug）**

很多人用 VSCode 都不知道这些。
