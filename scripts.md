---
layout: home
title: "Archive"
---
* [Writing scripts on Mac](

<a href="/">Professor Klaus-Jürgen Bathe</a>
[Reference](http://linuxcommand.org/lc3_wss0010.php)
{% highlight bash %}
#Step 1
##Write your script with vim:

#!/bin/bash
find . -name "*.h" -o -name "*.c" -o -name "*.cc"  -o -name "*.java"> cscope.files
cscope -bkq -i cscope.files
ctags -R

#Step 2
##Set permissions

chmod 755 <script_file_name>

#Step 3
##Add script file path to .zshrc
{% endhighlight %}

