#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量创建博士生markdown文件的脚本
文件名格式: 名字_姓氏.md (例如: meng_wang.md)
"""

import os

# 博士生名单 (姓名)
phd_students = [
    "汪萌",
    "张硕玺", 
    "陈劲松",
    "宁嘉",
    "朱建平",
    "李改潮",
    "高开元",
    "刘汉鹏",
    "江魏好",
    "杨超",
    "刘高",
    "李思哲",
    "裘天宝",
    "彭杨哲",
    "温俊锐",
    "姜丝雨",
    "丁仁华",
    "司马丙瑞",
    "董锡耀"
]

# 姓名到拼音的映射
name_pinyin_map = {
    "汪萌": ("Meng", "Wang"),
    "张硕玺": ("Shuoxi", "Zhang"),
    "陈劲松": ("Jingsong", "Chen"),
    "宁嘉": ("Jia", "Ning"),
    "朱建平": ("Jianping", "Zhu"),
    "李改潮": ("Gaichao", "Li"),
    "高开元": ("Kaiyuan", "Gao"),
    "刘汉鹏": ("Hanpeng", "Liu"),
    "江魏好": ("Weihao", "Jiang"),
    "杨超": ("Chao", "Yang"),
    "刘高": ("Gao", "Liu"),
    "李思哲": ("Sizhe", "Li"),
    "裘天宝": ("Tianbao", "Qiu"),
    "彭杨哲": ("Yangzhe", "Peng"),
    "温俊锐": ("Junrui", "Wen"),
    "姜丝雨": ("Siyu", "Jiang"),
    "丁仁华": ("Renhua", "Ding"),
    "司马丙瑞": ("Bingrui", "Sima"),
    "董锡耀": ("Xiyao", "Dong")
}

def create_markdown_template(chinese_name, given_name, family_name):
    """创建markdown模板内容"""
    template = f"""---
name: {chinese_name}
image: 
role: phd
description: 
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
    """创建所有博士生的markdown文件"""
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建目录: {output_dir}")
    
    # 为每个博士生创建文件
    for chinese_name in phd_students:
        if chinese_name in name_pinyin_map:
            given_name, family_name = name_pinyin_map[chinese_name]
            
            # 文件名格式: 名字_姓氏.md (小写)
            filename = f"{given_name.lower()}_{family_name.lower()}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 创建markdown内容
            content = create_markdown_template(chinese_name, given_name, family_name)
            
            # 写入文件
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ 创建文件: {filename}")
        else:
            print(f"✗ 警告: 未找到 {chinese_name} 的拼音映射")
    
    print(f"\n完成! 共创建 {len(phd_students)} 个markdown文件")
    print(f"文件保存在: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    create_files()