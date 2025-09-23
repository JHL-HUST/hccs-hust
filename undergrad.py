#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量创建硕士生markdown文件的脚本
文件名格式: 名字_姓氏.md (例如: zhenyi_wang.md)
"""

import os

# 硕士生名单及其研究方向/备注
undergrad_students = [
    ("王桢毅", ""),
    ("段泓汲", ""),
    ("龚宇蒙", ""),
    ("贺继尧", ""),
    ("姜伟龙", ""),
    ("李晨阳", ""),
    ("曹瀚文", ""),
    ("伍仁杰", ""),
    ("丛林华", ""),
    ("匡智颉", ""),
    ("刘铭宸", ""),
    ("张睿涵", ""),
    ("李亦飞", ""),
    ("马跃", ""),
    ("于泽坤", ""),
    ("陈子旸", "对抗"),
    ("路浩博", "对抗"),
    ("程广圣", "对抗可解释性"),
    ("陈奕龙", "NLP对抗"),
    ("胡心如", "企业联培-电磁对抗"),
    ("刘心怡", "国优计划-CV"),
    ("马嘉骏", "企业联培-端到端优化"),
    ("张骁凯", "软院21-CV"),
    ("台欣未", "直博-GNN"),
    ("王子丹", "CV"),
    ("王可立", "CV"),
    ("林子垚", "图ML")
]

# 姓名到拼音的映射
name_pinyin_map = {
    "王桢毅": ("Zhenyi", "Wang"),
    "段泓汲": ("Hongji", "Duan"),
    "龚宇蒙": ("Yumeng", "Gong"),
    "贺继尧": ("Jiyao", "He"),
    "姜伟龙": ("Weilong", "Jiang"),
    "李晨阳": ("Chenyang", "Li"),
    "曹瀚文": ("Hanwen", "Cao"),
    "伍仁杰": ("Renjie", "Wu"),
    "丛林华": ("Linhua", "Cong"),
    "匡智颉": ("Zhijie", "Kuang"),
    "刘铭宸": ("Mingchen", "Liu"),
    "张睿涵": ("Ruihan", "Zhang"),
    "李亦飞": ("Yifei", "Li"),
    "马跃": ("Yue", "Ma"),
    "于泽坤": ("Zekun", "Yu"),
    "陈子旸": ("Ziyang", "Chen"),
    "路浩博": ("Haobo", "Lu"),
    "程广圣": ("Guangsheng", "Cheng"),
    "陈奕龙": ("Yilong", "Chen"),
    "胡心如": ("Xinru", "Hu"),
    "刘心怡": ("Xinyi", "Liu"),
    "马嘉骏": ("Jiajun", "Ma"),
    "张骁凯": ("Xiaokai", "Zhang"),
    "台欣未": ("Xinwei", "Tai"),
    "王子丹": ("Zidan", "Wang"),
    "王可立": ("Keli", "Wang"),
    "林子垚": ("Ziyao", "Lin")
}

def create_markdown_template(chinese_name, given_name, family_name, note=""):
    """创建markdown模板内容"""
    description = note if note else ""
    
    template = f"""---
name: {chinese_name}
image: 
role: undergrad
description: {description}
affiliation: 华中科技大学
aliases:
  - {given_name} {family_name}
links:
  home-page: 
  orcid: 
  email: 

---

职位：

简介：
"""
    return template

def create_files(output_dir="/Users/dekrt/Documents/Code/jhl-hust.github.io/_members"):
    """创建所有硕士生的markdown文件"""
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建目录: {output_dir}")
    
    # 为每个硕士生创建文件
    created_count = 0
    for chinese_name, note in undergrad_students:
        if chinese_name in name_pinyin_map:
            given_name, family_name = name_pinyin_map[chinese_name]
            
            # 文件名格式: 名字_姓氏.md (小写)
            filename = f"{given_name.lower()}_{family_name.lower()}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 创建markdown内容
            content = create_markdown_template(chinese_name, given_name, family_name, note)
            
            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            note_info = f" ({note})" if note else ""
            print(f"✓ 创建文件: {filename}{note_info}")
            created_count += 1
        else:
            print(f"✗ 警告: 未找到 {chinese_name} 的拼音映射")
    
    print(f"\n完成! 共创建 {created_count} 个markdown文件")
    print(f"文件保存在: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    create_files()