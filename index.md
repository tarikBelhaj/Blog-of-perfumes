---
layout: default
title: Welcome
---

# Welcome to the Blog of Perfumes

Discover the world of perfumes with our comprehensive guides and reviews. Stay tuned for the latest trends and tips in the world of fragrances.
---
layout: blog
title: Blog
---

{% for post in site.posts %}
  <div class="post">
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <p>{{ post.date | date: "%B %d, %Y" }} - By {{ post.author }}</p>
    <p>{{ post.excerpt }}</p>
    <a href="{{ post.url }}" class="read-more">Read More</a>
  </div>
{% endfor %}

