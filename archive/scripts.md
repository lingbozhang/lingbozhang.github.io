---
layout: home
title: "Archive"
---
* Step 1: Write your script with vim:
{% highlight bash %}
#!/bin/bash
find . -name "*.h" -o -name "*.c" -o -name "*.cc"  -o -name "*.java"> cscope.files
cscope -bkq -i cscope.files
ctags -R
{% endhighlight %}
* Step 2: Set permissions
{% highlight bash %}
chmod 755 <script_file_name>
{% endhighlight %}
* Step 3: Add script file path to .zshrc

