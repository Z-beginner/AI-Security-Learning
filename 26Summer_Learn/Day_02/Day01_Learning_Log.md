# AI Security Learning Plan - Day2 Report

日期：2026-07-29

主题：
Python数据结构与Prompt安全检测器升级

---

# 1. 今日学习目标

- 掌握 Python 常用数据结构
- 理解 list 与 dictionary 的区别
- 学习 list + dictionary 的组合使用
- 学习函数 def 与 return 的作用
- 将 Prompt 检测器进行升级
- 实现多关键词检测与风险等级聚合

---

# 2. Python知识学习

## 2.1 List（列表）

### 基本概念

List 用于保存多个数据。

语法：

```python
list_name = [
    element1,
    element2,
    element3
]
```

例如：

```python
fruits = [
    "apple",
    "banana",
    "mango"
]
```

---

## 常用操作

### 添加元素

```python
fruits.append("pear")
```

### 删除元素

```python
fruits.remove("banana")
```

### 修改元素

```python
fruits[2] = "orange"
```

### 获取长度

```python
len(fruits)
```

---

# 2.2 Dictionary（字典）

## 基本概念

Dictionary 使用 key-value 保存数据。

格式：

```python
{
    key: value
}
```

例如：

```python
attack_rules = {
    "hack": "high",
    "attack": "medium",
    "ignore": "medium"
}
```

表示：

```
hack    -> high
attack  -> medium
ignore  -> medium
```

---

## 访问字典数据

例如：

```python
attack_rules["hack"]
```

结果：

```
high
```

---

# 2.3 List + Dictionary组合

实际项目中，经常需要保存多个对象的信息。

例如：

```python
report = [
    {
        "keyword": "hack",
        "risk": "high"
    },
    {
        "keyword": "ignore",
        "risk": "medium"
    }
]
```

数据结构：

```
list
 |
 |-- dictionary
 |
 |-- dictionary
```

应用场景：

- 安全日志
- 模型检测结果
- 数据分析结果

---

# 3. Python函数学习

## 3.1 def

函数用于封装一段代码。

例如：

```python
def check_prompt(prompt):
    ...
```

作用：

将检测逻辑封装成一个可以重复使用的工具。

---

## 3.2 return

return 用于返回结果。

区别：

print：

```
显示给人看
```

return：

```
交给其他代码继续处理
```

例如：

```python
result = check_prompt(prompt)
```

result 可以继续参与判断。

---

# 4. Prompt安全检测器升级

## 4.1 攻击规则

建立关键词风险映射：

```python
attack_rules = {
    "hack": "high",
    "attack": "medium",
    "ignore": "medium"
}
```

---

# 4.2 多关键词检测

升级前：

发现一个关键词后结束。

升级后：

可以检测多个攻击关键词。

例如：

输入：

```
hack ignore
```

输出：

```
hack -> high
ignore -> medium
```

---

# 4.3 结构化输出

检测结果改为：

```python
{
    "keyword": "hack",
    "risk": "high"
}
```

多个结果：

```python
[
    {
        "keyword": "hack",
        "risk": "high"
    },
    {
        "keyword": "ignore",
        "risk": "medium"
    }
]
```

---

# 5. 风险聚合（Risk Aggregation）

## 5.1 问题

如果同时出现多个攻击：

```
hack
ignore
attack
```

需要判断整体风险等级。

---

## 5.2 风险等级映射

建立：

```python
risk_level = {
    "safe": 0,
    "medium": 1,
    "high": 2
}
```

通过数字比较风险。

---

## 5.3 最高风险计算

逻辑：

```
初始化：
max_risk = safe

遍历所有检测结果：

如果当前风险等级更高：

更新 max_risk
```

例如：

输入：

```
hack ignore
```

结果：

```
Max risk: high
```

---

# 6. 今日项目成果

项目：

```
prompt_checker_v3promax.py
```

实现功能：

## 输入

用户Prompt：

```
hack ignore
```

---

## 检测

匹配攻击规则：

```
hack
ignore
```

---

## 输出

检测结果：

```python
{
    "keyword": "hack",
    "risk": "high"
}
```

风险等级：

```
Max risk: high
```

---

# 7. 今日遇到的问题与解决

## 问题1：为什么return只能输出一个结果？

原因：

return执行后函数立即结束。

错误：

```python
for keyword in list:
    return result
```

正确：

```python
for keyword in list:
    collect result

return result
```

---

## 问题2：为什么字典需要{}？

原因：

```
[] 保存多个元素

{} 描述一个对象的信息
```

---

## 问题3：为什么print和return不同？

print：

```
输出给用户
```

return：

```
返回数据给程序继续处理
```

---

## 问题4：为什么不能直接比较high和medium？

错误：

```python
"high" > "medium"
```

Python无法理解风险等级。

解决：

转换：

```
safe -> 0
medium -> 1
high -> 2
```

---

# 8. 今日代码能力总结

已掌握：

- [x] list
- [x] dictionary
- [x] list嵌套dictionary
- [x] for循环
- [x] if判断
- [x] def函数
- [x] return返回
- [x] 数据结构设计
- [x] 风险等级映射
- [x] 风险聚合

---

# 9. Day2总结

今天从Python基础数据结构出发，
完成了一个简化版 Prompt Injection Detector。

项目流程：

```
用户输入
    |
    v
关键词规则匹配
    |
    v
生成检测结果
    |
    v
风险等级判断
    |
    v
输出安全分析结果
```

相比Day1：

Day1：

```
简单关键词检测
```

Day2：

```
结构化安全检测器
+
风险评估
```

已经开始接近真实AI安全工具设计。

---

# 10. Day3计划

主题：

Python工程化基础

学习：

- 文件读写
- 日志保存
- try/except异常处理
- import模块
- 项目结构整理

目标：

将单文件检测器升级为：

```
AI_security/

├── main.py
├── detector.py
├── rules.py
└── logs/
```

形成更接近真实项目的结构。

---

Day2完成 ✅