---
title: "Archive"
---
* Start postgreSQL:
{% highlight bash %}
pg_ctl -D /usr/local/var/postgres -l logfile start
{% endhighlight %}

* Stop postgreSQL:
{% highlight bash %}
pg_ctl -D /usr/local/var/postgres stop -s -m fast
{% endhighlight %}

* Create database:
{% highlight bash %}
createdb -Ouser_name -Eutf8 database_name
{% endhighlight %}

* Connect database
{% highlight bash %}
psql -U user_name database_name
{% endhighlight %}
