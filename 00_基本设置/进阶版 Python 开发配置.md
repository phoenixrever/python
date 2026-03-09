下面是一份 **适配新版 Visual Studio Code 的 Python 最终稳定版 `settings.json`**。
特点：

- 不使用 **过时配置**
- 不会出现 **schema 报错**
- 适配 **Pylance**
- 适配 **Ruff**
- 体验接近 **PyCharm**

我给你 **完整注释版**（VSCode 支持 JSON 注释）。

---

# 最终推荐 settings.json

```jsonc
{
  // ---------- 编辑器基础 ----------

  // 字体大小
  "editor.fontSize": 14,

  // 推荐编程字体
  "editor.fontFamily": "JetBrains Mono, Cascadia Code, Consolas",

  // 启用字体连字
  "editor.fontLigatures": true,

  // 保存自动格式化
  "editor.formatOnSave": true,

  // ---------- Hover 提示 ----------

  // 悬停提示（新版必须用字符串）
  "editor.hover.enabled": "on",

  // Hover 延迟（毫秒）
  "editor.hover.delay": 300,

  // 函数参数提示
  "editor.parameterHints.enabled": true,

  // AI整行补全
  "editor.inlineSuggest.enabled": true,

  // ---------- 编辑体验 ----------

  // 关闭右侧代码缩略图
  "editor.minimap.enabled": false,

  // 括号辅助线
  "editor.guides.bracketPairs": true,

  // 括号颜色区分
  "editor.bracketPairColorization.enabled": true,

  // 自动补全触发条件
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true,
  },

  // 自动补全默认选第一个
  "editor.suggestSelection": "first",

  // ---------- Python 类型检查 ----------

  // 严格类型检查
  "python.analysis.typeCheckingMode": "strict",

  // 自动import补全
  "python.analysis.autoImportCompletions": true,

  // ---------- Python Inlay Hints ----------

  // 显示变量类型
  "python.analysis.inlayHints.variableTypes": true,

  // 显示函数返回类型
  "python.analysis.inlayHints.functionReturnTypes": true,

  // 显示函数参数名称
  "python.analysis.inlayHints.callArgumentNames": "all",

  // ---------- Python 诊断 ----------

  // 分析整个workspace
  "python.analysis.diagnosticMode": "workspace",

  // 使用库代码推断类型
  "python.analysis.useLibraryCodeForTypes": true,

  // 未定义变量直接报错
  "python.analysis.diagnosticSeverityOverrides": {
    "reportUndefinedVariable": "error",
  },

  // ---------- Ruff ----------

  // 启用 Ruff lint
  "ruff.lint.enable": true,

  // Python 默认 formatter 使用 Ruff
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
  },

  // 保存时自动修复并整理 import
  "editor.codeActionsOnSave": {
    "source.fixAll.ruff": "always",
    "source.organizeImports.ruff": "always",
  },

  // ---------- Debug ----------

  // 调试时在代码旁显示变量值
  "debug.showInlineValues": true,

  // ---------- Error Lens ----------

  // 错误直接显示在代码行
  "errorLens.enabled": true,

  // 显示错误文本
  "errorLens.messageEnabled": true,

  // 错误跟随光标
  "errorLens.followCursor": "activeLine",
}
```

---

# 这套配置需要的插件

必须安装：

1. **Python**
2. **Pylance**
3. **Ruff**
4. **Error Lens**

推荐：

5. **GitHub Copilot**

---

# 配置后的效果

你会得到：

### 1 类型提示

```python
age = 18        # : int
name = "Tom"    # : str
```

---

### 2 自动 import

输入：

```
datetime
```

自动提示：

```
from datetime import datetime
```

---

### 3 保存自动修复代码

Ruff 会自动：

- 删除 unused import
- 排序 import
- 修复 style

---

### 4 调试变量显示

调试时：

```python
x = 10
```

右侧显示：

```
x = 10
```

类似 **PyCharm Debug View**。

---

💡如果你愿意，我可以再给你 **Python开发者 VSCode 隐藏增强配置（高级版）**，会再增加：

- **自动 import 排序优化**
- **函数复杂度检测**
- **pytest 自动运行**
- **Git 提交检查**
- **项目模板**

很多 Python 开发者都不知道这些配置。
