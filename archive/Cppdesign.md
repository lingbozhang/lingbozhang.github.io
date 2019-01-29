---
title: "Archive"
---
# C++ design patterns
## Resource acquisition is initialization (RAII)
[Reference](https://www.tomdalling.com/blog/software-design/resource-acquisition-is-initialisation-raii-explained/)
{% highlight C++ %}
class A {
public:
    A(T resource):_resource(resource){}
    ~A(){delete _resource};
private:
    _resource;
};
{% endhighlight %}

