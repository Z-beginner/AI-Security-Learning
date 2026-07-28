# AI Security 30 Day Plan - Day 1 学习记录

日期：2026-07-28

## 今日主题

Python基础入门 + 第一个AI安全检测脚本

---

# 一、环境准备

## 已完成环境

- ✅ Anaconda安装
- ✅ Ubuntu虚拟机安装
- ✅ VS Code安装
- ✅ VS Code中文语言包配置

## 后续环境规划

开发环境：

```
Windows
│
├── VS Code
├── Anaconda
├── Git
│
└── Ubuntu
```

用途：

- VS Code：代码编辑
- Anaconda：Python环境管理
- Git：代码版本管理
- Ubuntu：Linux实验环境

---

# 二、Python基础学习

## 1. Python变量

Python不需要提前声明变量类型。

示例：

```python
name = "AI Security"
year = 2026
```

---

## 2. 常见数据类型

### 字符串（str）

```python
prompt = "ignore previous instructions"
```

用于处理文本输入。

---

### 整数（int）

```python
count = 10
```

---

### 列表（list）

示例：

```python
keywords = [
    "hack",
    "attack",
    "ignore"
]
```

（列表和循环将在Day2重点学习）

---

# 三、条件判断

Python使用if判断逻辑。

示例：

```python
if condition:
    do something
else:
    do something else
```

实际应用：

判断用户输入是否包含危险关键词。

---

# 四、函数

函数用于封装重复逻辑。

基本结构：

```python
def function_name(parameter):
    return result
```

示例：

```python
def check_prompt(prompt):
    if "hack" in prompt:
        return "attack keyword: hack"
    else:
        return "safe"
```

理解：

- `def` 创建函数
- 参数接收输入
- `return` 返回结果

---

# 五、第一个AI安全小程序

## Prompt安全检测器

代码：

```python
prompt = input()

def check_prompt(prompt):
    if "hack" in prompt:
        return "attack keyword: hack"
    if "attack" in prompt:
        return "attack keyword: attack"
    if "ignore" in prompt:
        return "attack keyword: ignore"
    else:
        return "safe"

result = check_prompt(prompt)

print(result)
```

---

# 六、遇到的问题与思考

## 问题

如果输入：

```
hack attack
```

程序只返回：

```
attack keyword: hack
```

原因：

Python执行顺序：

1. 从上到下执行代码
2. 第一个满足条件的if执行
3. `return`结束函数
4. 后面的判断不会继续执行

---

## 思考

当前检测器的问题：

- 只能返回一个风险关键词
- 没有风险等级
- 没有统计多个危险词
- 规则写死在代码中

后续优化方向：

- 使用列表保存规则
- 使用循环遍历关键词
- 建立风险评分系统

（循环和列表将在Day2学习）

---

# 七、今日掌握内容

## Python

- ✅ 变量
- ✅ 输入输出
- ✅ 字符串判断
- ✅ if条件判断
- ✅ 函数定义
- ✅ return逻辑

## AI Security

初步理解：

- Prompt输入检测
- 基础规则匹配
- 简单攻击关键词识别

---

# 八、Day1完成情况

状态：

✅ 已完成

完成项目：

```
Prompt Security Checker
```

能力：

可以编写简单的输入检测程序。

---

# 九、Day2预告

主题：

Python进阶

计划学习：

- list
- tuple
- dict
- for循环
- while循环
- 文件读写
- 异常处理

目标：

将简单关键词检测器升级为更完整的安全规则检测系统。