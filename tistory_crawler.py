import feedparser
import time
URL="https://renovatio-dev-hyuns.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

postings = []
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        postings.append(f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']})\n")

# print(markdown_text)
markdown_text = f"""
# 인공지능에 가치를 느끼는 안드로이드 개발자 정현석입니다. 👋
주 관심분야는 안드로이드 네이티브이며  
현재는 AI, ComputerVision 을 공부중입니다.   
</br>
</br>
## 📊 Github Stats 📊
![](./profile-3d-contrib/profile-night-rainbow.svg)


## ⚔ SKILL ⚔
<table style="table-layout: fixed">
  <tr>
    <td>
      <a href="https://solved.ac/profile/hyuns6677">
        <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=hyuns6677" alt="Solved.ac 프로필" style="width: 100%;">
      </a>
    </td>
    <td style="width: 400px;">
      <img src="https://img.shields.io/badge/Android-3DDC84?style=flat&logo=Android&logoColor=white"/>
        <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white"/>
        <img src="https://img.shields.io/badge/VisualStudioCode-007ACC?style=flat&logo=VisualStudioCode&logoColor=white"/>
        <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=SQLite&logoColor=white"/> </br>
        <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=Jupyter&logoColor=white"/>
        <img src="https://img.shields.io/badge/Numpy-013243?style=flat&logo=Numpy&logoColor=white"/>
        <img src="https://img.shields.io/badge/Pandas-150458?style=flat&logo=Pandas&logoColor=white"/>
        <img src="https://img.shields.io/badge/GoogleColab-F9AB00?style=flat&logo=GoogleColab&logoColor=white"/> </br>
        <img src="https://img.shields.io/badge/kotlin-7F52FF?style=flat&logo=kotlin&logoColor=white"/>
        <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/java-F7DF1E?style=flat&logo=java&logoColor=white"/>
        <img src="https://img.shields.io/badge/openCV-5C3EE8?style=flat&logo=openCV&logoColor=white"/>
      </td>
  </tr>
</table>



## 운영중인 블로그
[![Tistory's Badge](https://github-readme-tistory-card.vercel.app/api/badge?name=renovatio&theme=default)](https://renovatio-dev-hyuns.tistory.com)  
{postings[0]}  
{postings[1]}  
{postings[2]}  
{postings[3]}  
{postings[4]}  
<!--
[![Velog's GitHub stats](https://velog-readme-2.vercel.app/api/badge-stats?color=dark&name=renovatio_hyuns)](https://velog.io/@renovatio_hyuns)  
[![Velog's GitHub stats](https://velog-readme-stats.vercel.app/api?name=renovatio_hyuns&color=dark)](https://velog-readme-stats.vercel.app/api/redirect?name=renovatio_hyuns)
-->
"""
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
