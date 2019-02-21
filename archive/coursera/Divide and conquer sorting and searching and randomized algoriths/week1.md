---
title:  "Notes"
categories: coursera
mathjax: true
---
# Week 1
Integer multiplication: 
Karatsuba multiplication
Gauss algorithm

# Week 2
The master method:
T(n)=aT(n/b)+O(n^d)

\begin{align}
\begin{aligned}
T(n)&=O(n^dlogn) \quad\text{if}\quad a=b^d\\
    &=O(n^d)     \quad\text{if}\quad a<b^d\\
    &=O(n^{log_b a}) \quad\text{if}\quad a>b^d
\end{aligned}
\end{align}