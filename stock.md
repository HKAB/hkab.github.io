---
layout: page
title: Stock News Summarization 📈
permalink: /stock/
---

<ul>
    <li>Thông tin được tổng hợp bởi AI, có thể <b>không chính xác</b>!</li>
</ul>

<div class="posts">
  {% for post in site.stocks %}
    <article class="post">

      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>

      <div class="entry">
        {{ post.excerpt }}
      </div>

      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
    </article>
  {% endfor %}
</div>