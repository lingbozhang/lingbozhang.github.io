---
title:  "HDFS source code analysis - 1"
categories: [Distributed Systems]
tags: [HDFS]
mathjax: true
---
## Preface
<p align="justify">
Nowadays, big data and cloud computing are two most important high-tech tends. As data storage and computation power requirements increase every year, the vertical scaling techniques will be the most effective solution. Fortunately, it is still an active area far from mature, which gives us great opportunities in both research and industry. As a young researcher and engineer, it is very beneficiary to study and make contributions. The HDFS source code analysis project is my first step in these areas.
</p>
<p align="justify">
Why HDFS? There are great number of open-source techniques online, such as Map Reduce, Spark, Hbase, etc. I choose HDFS not only become it is simpler than other distributed projects, but also the distributed file system will be the foundation. Previously, Map Reduce is the major trend in cloud computing, nowadays, we find that Spark draws great attentions. In the future, new technologies will be proposed that will beat the Spark. However, I believe the distributed file system will be the foundation for all these techniques. Therefore to study and understand it will be very fruitful.
</p>
<p align="justify">
The major objective of the HDFS source code analysis project is to help myself learn and understand the HDFS source code. Finally, I hope I am able to write the distributed file system. In the future, if I have a plan, all these materials will be revised to help other people learn and understand the HDFS source code.
</p>

## Checking out the source
<p align="justify">
Don't waste your time reading latest version of the Hadoop source codes, developers have spent years building this program, current version is too complex for people without any experiences in distributed systems. Let's analyze the source codes from [Hadoop-1.0.0](https://archive.apache.org/dist/hadoop/core/hadoop-1.0.0/).
</p>
<p align="justify">
To check out the source code, use [vim](https://www.vim.org)  (an editor) and [cscope](http://cscope.sourceforge.net) (for code navigation)
</p>

## Source code analysis - Configuration
<p align="justify">
Configuration locates in (/src/core/org/apache/hadoop/conf) is a very important component of the hadoop program, hadoop use the configuration to read data from web/files (XML) in order to extend and configure the program. Let's first study the configuration.java file which defines the configuration class. We don't need to know every details of the class (In the future, we can come back any time and make improvements if you want to).</p>

{% highlight java %}
{% endhighlight %}
## Import source codes in eclipse
Kepler and Java6


## Install Hadoop
Please refer [link](https://isaacchanghau.github.io/post/install_hadoop_mac/)
