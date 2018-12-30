---
layout: home
title: "Archive"
---
## Writing scripts on Mac
[Reference](http://linuxcommand.org/lc3_wss0010.php)
### Step 1
Write your script with vim:
{% highlight bash %}
#!/bin/bash
find . -name "*.h" -o -name "*.c" -o -name "*.cc"  -o -name "*.java"> cscope.files
cscope -bkq -i cscope.files
ctags -R
{% endhighlight %}
### Step 2
Set permissions
{% highlight bash %}
chmod 755 <script_file_name>
{% endhighlight %}
### Step 3
Move your script file to /bin directory
