---
title:  "HDFS source code analysis - 1"
categories: Distributed Systems
mathjax: true
---
## Preface
Nowadays, big data and cloud computing are two most important high-tech tends. As data storage and computation power requirements increase every year, the vertical scaling techniques will be the most effective solution. Fortunately, it is still an ative area far from mature, which gives us great opportutnities in both research and industry. As a young researcher and engineer, it is very benificiary to study and make contributions. The HDFS source code analysis project is my first step in these areas. 

Why HDFS? There are great number of open-source techniques online, such as Map Reduce, Spark, Hbase, etc. I choose HDFS not only become it is simpler than other distrituted projects, but also the ditributed file system will be the foundation. Previously, Map Reduce is the major trend in cloud computing, nowadays, we find that Spark draws great attentions. In the future, new technologies will be proposed that will beat the Spark. However, I believe the distributed fille system will be the foundation for all these techniques. Therefore to study and understand it will be very fruitful.

The major objective of the HDFS source code analysis project is to help myself learn and understand the HDFS source code. Finally, I hope I am able to write the distributed file system. In the future, if I have a plan, all these materials will be revised to help other people learn and understand the HDFS source code.

##










Embed code by putting `{{ "{% highlight language " }}%}` `{{ "{% endhighlight " }}%}` blocks around it.

{% highlight c %}

static void asyncEnabled(Dict* args, void* vAdmin, String* txid, struct Allocator* requestAlloc)
{
    struct Admin* admin = Identity_check((struct Admin*) vAdmin);
    int64_t enabled = admin->asyncEnabled;
    Dict d = Dict_CONST(String_CONST("asyncEnabled"), Int_OBJ(enabled), NULL);
    Admin_sendMessage(&d, txid, admin);
}

{% endhighlight %}


## MathJax

You can enable MathJax by setting `mathjax: true` on a page or globally in the `_config.yml`. Some examples:

[Euler's formula](https://en.wikipedia.org/wiki/Euler%27s_formula) relates the  complex exponential function to the trigonometric functions.

$$ e^{ix}=cos(x)+isin(x) $$

The [Euler-Lagrange](https://en.wikipedia.org/wiki/Lagrangian_mechanics) differential equation is the fundamental equation of calculus of variations.

$$ \frac{\mathrm{d}}{\mathrm{d}t} \left ( \frac{\partial L}{\partial \dot{q}} \right ) = \frac{\partial L}{\partial q} $$

The [Schrödinger equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation) describes how the quantum state of a quantum system changes with time.

$$ i\hbar\frac{\partial}{\partial t} \Psi(\mathbf{r},t) = \left [ \frac{-\hbar^2}{2\mu}\nabla^2 + V(\mathbf{r},t)\right ] \Psi(\mathbf{r},t) $$

## Images

Upload an image to the *assets* folder and embed it with `![title](/assets/name.jpg))`. Keep in mind that the path needs to be adjusted if Jekyll is run inside a subfolder.

[![Flower](../assets/flower.jpg)](../assets/flower.jpg)

[Flower](https://unsplash.com/photos/iGrsa9rL11o) by Tj Holowaychuk

## Embedded Content

You can also embed a lot of stuff, for example from YouTube. To scale the video to full width use the `<div class="embed"></div>` wrapper around the iframe.

<div class="embed"><iframe src="https://www.youtube.com/embed/_C0A5zX-iqM" frameborder="0" allowfullscreen></iframe></div>

## Large Content

You can use a `.large` wrapper to increase the width of an image or iframe:

<a class="large" href="../assets/swiss-alps.jpg">![Swiss Alps](../assets/swiss-alps.jpg)</a>

[Swiss Alps](https://unsplash.com/photos/u0DmxB76uF4) by René Reichelt
