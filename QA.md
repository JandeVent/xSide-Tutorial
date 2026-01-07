# 提问时间

## 1. 为什么布局 API 使用字符串 ID，而不是对象引用

---

在 xSide 中，菜单、工具栏、状态栏等 UI 布局 API 统一使用字符串 ID（而非对象引用） 来组织和定位 Action、Widget 与 ToolWindow。这一设计是有明确架构动机的。

---

### 1. 插件化系统中，对象引用是不可控依赖

在插件式架构下：
* Action / Widget / ToolWindow 往往定义在不同插件中
* 插件的加载顺序 **不可假定**
* 插件可能：
  * 不存在
  * 延迟加载
  * 被禁用或替换

如果布局 API 依赖对象引用：
```python
# ❌ 不可行的设计
xside.window.addMainWindowAction(saveAction)
```

那么调用方必须：
* import 对方模块
* 确保对象已创建
* 持有其生命周期

这会导致：
* 插件之间产生**隐式耦合**
* 插件顺序敏感
* 运行时脆弱（某插件缺失即崩溃）

---
### 2. 字符串 ID 是稳定、可声明的契约

字符串 ID 的本质是一个显式的契约（Contract）：
```text
"save-all"
"file-menu"
"terminal"
```

它具备以下特性：
* 与对象实例生命周期无关
* 可提前声明、后续绑定
* 可用于跨插件通信
* 可用于配置、序列化、脚本化

在 xSide 中：
> 对象是实现细节，ID 才是系统接口。

---
### 3. 支持“先声明能力，后决定布局”

通过字符串 ID，xSide 支持以下模式：

```python
# 插件 A
xside.window.registerAction(saveAction)

# 插件 B（甚至在之后加载）
xside.window.addMainWindowAction('save-all')
```

这意味着:
* Action 的定义与 UI 呈现彻底解耦
* 布局决策可以由以下对象完成：
  * Host App
  * UI 插件
  * 用户配置

这是插件式 IDE 必须具备的能力。

---
### 4. 布局逻辑可以分散，而不是集中

使用对象引用，往往会迫使你：
* 在一个地方集中创建 UI
* 把“菜单结构”写成一坨代码

而使用字符串 ID：
* 插件只声明：
  * 我提供哪些 Action
  * 我希望它出现在哪里
* 布局代码可以：
  * 分布在不同插件中
  * 在不同阶段执行
  * 根据条件（平台 / 模式 / 配置）生效

