---
title: "Archive"
---
* Step 1: Write a script with your favorite editor (e.g. vim):
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
* Step 3: Add script file path to .zshrc (export PATH=$PATH:script_directory)
* [Reference 1](http://linuxcommand.org/lc3_wss0010.php)
* [Reference 2](https://www.gnu.org/software/bash/manual/bashref.html#Bash-Conditional-Expressions)
