---
title: 人才队伍
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

华中科技大学John Hopcroft计算中心汇聚了一批在计算机科学领域享有国际声誉的杰出学者和优秀青年人才。中心以图灵奖得主John Hopcroft教授为学术带头人，何琨教授为执行主任，研究领域横跨理论计算机科学、算法设计与分析、机器学习、数据挖掘、人工智能等前沿方向。团队成员在国际顶级期刊和会议上发表高质量学术论文，承担国家重大科研项目，致力于推动计算科学理论与应用的创新发展。

我们坚持"引进与培养并重"的人才发展战略，为优秀人才提供良好的学术环境和发展平台，努力建设一支具有国际竞争力的高水平人才队伍。

# {% include icon.html icon="fa-regular fa-envelope" %}中心主任

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}

# {% include icon.html icon="fa-regular fa-envelope" %}客座教授

{% include list.html data="members" component="portrait" filter="role == 'vp'" %}

# {% include icon.html icon="fa-regular fa-envelope" %}博士后

{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}


# {% include icon.html icon="fa-regular fa-envelope" %}博士生

{% include list.html data="members" component="portrait" filter="role == 'phd'" %}

# {% include icon.html icon="fa-regular fa-envelope" %}硕士生

{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}


# {% include icon.html icon="fa-regular fa-envelope" %}本科生




{% include section.html background="images/background.png" dark=true %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/members/team_photos/team_photo_1.png" %}
{% include figure.html image="images/members/team_photos/team_photo_2.png" %}
{% include figure.html image="images/members/team_photos/team_photo_3.png" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
