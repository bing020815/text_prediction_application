# text
Codes for text prediction 


## Model
The N-gram model was built by `bigram`, `trigram`, `fourgram` and `fivegram` models using __chain rule__, __maximum likelihood estimation__ and __backoff approach__.

## Concept
__Note:__ the expression ![W_1^{n-1}](https://render.githubusercontent.com/render/math?math=%24W_1%5E%7Bn-1%7D%24) means the string ![w_1,w_2,...,w_{n-1}](https://render.githubusercontent.com/render/math?math=%24w_1%2Cw_2%2C...%2Cw_%7Bn-1%7D%24)

Applying **chain rule of probability**:  

![P(X_1...X_n) = P(X_1)P(X_2|X_1)P(X_3|X_1^2)...P(X_n|X_1^{n-1})](https://render.githubusercontent.com/render/math?math=%24P(X_1...X_n)%20%3D%20P(X_1)P(X_2%7CX_1)P(X_3%7CX_1%5E2)...P(X_n%7CX_1%5E%7Bn-1%7D)%24)  
![ = \displaystyle\prod_{k=1}^{n} P(X_k|X_1^{k-1})](https://render.githubusercontent.com/render/math?math=%24%20%3D%20%5Cdisplaystyle%5Cprod_%7Bk%3D1%7D%5E%7Bn%7D%20P(X_k%7CX_1%5E%7Bk-1%7D)%24)     
*(equation  1)*  
<p><br></p>

Applying **chain rule** to words:  

![P(w_1^n) = P(w_1)P(w_2|w_1)P(w_3|w_1^2)...P(w_n|w_1^{n-1})](https://render.githubusercontent.com/render/math?math=%24P(w_1%5En)%20%3D%20P(w_1)P(w_2%7Cw_1)P(w_3%7Cw_1%5E2)...P(w_n%7Cw_1%5E%7Bn-1%7D)%24)  
![ = \displaystyle\prod_{k=1}^{n} P(w_k|w_1^{k-1})](https://render.githubusercontent.com/render/math?math=%24%20%3D%20%5Cdisplaystyle%5Cprod_%7Bk%3D1%7D%5E%7Bn%7D%20P(w_k%7Cw_1%5E%7Bk-1%7D)%24)  
*(equation  2)*  
<p><br></p>

The bigram model to predict the condition probability of the next word, use the following approximation:  

![P(w_n|w_1^{n-1})\approx P(w_n|w_{n-1})](https://render.githubusercontent.com/render/math?math=%24P(w_n%7Cw_1%5E%7Bn-1%7D)%5Capprox%20P(w_n%7Cw_%7Bn-1%7D)%24)  
*(equation  3)*  
<p><br></p>

The general equation for n-gram approximation to the conditional probability of the next word in a sequence is:  

![P(w_n|w_1^{n-1})\approx P(w_n|w_{n-N+1}^{n-1})](https://render.githubusercontent.com/render/math?math=%24P(w_n%7Cw_1%5E%7Bn-1%7D)%5Capprox%20P(w_n%7Cw_%7Bn-N%2B1%7D%5E%7Bn-1%7D)%24)   
*(equation  4)*  
<p><br></p>

According to the **equation 4**, the next word in the sentence depends on its immediate past words, known as context words.   
![P(w_{n} | w_{n-N+1}, w_{n-N},..., w_{n-1})$ where $w_{n-N+1}, w_{n-N},..., w_{n-1}](https://render.githubusercontent.com/render/math?math=%24P(w_%7Bn%7D%20%7C%20w_%7Bn-N%2B1%7D%2C%20w_%7Bn-N%7D%2C...%2C%20w_%7Bn-1%7D)%24%20where%20%24w_%7Bn-N%2B1%7D%2C%20w_%7Bn-N%7D%2C...%2C%20w_%7Bn-1%7D%24) is the context words  
<p><br></p>

__Inferred equations for n-grams__:  

* bigram (N=1)  :  ![P(w_{n}| w_{n-1})](https://render.githubusercontent.com/render/math?math=P(w_%7Bn%7D%7C%20w_%7Bn-1%7D))    
* trigram (N=2) :  ![P(w_{n}| w_{n-2}, w_{n-1})](https://render.githubusercontent.com/render/math?math=%24P(w_%7Bn%7D%7C%20w_%7Bn-2%7D%2C%20w_%7Bn-1%7D)%24)    
* 4-gram  (N=3) :  ![P(w_{n}| w_{n-3}, w_{n-2})](https://render.githubusercontent.com/render/math?math=%24P(w_%7Bn%7D%7C%20w_%7Bn-3%7D%2C%20w_%7Bn-2%7D)%24)     
<p><br></p>

To get the n-gram probabilities, use estilmate probabilities, __maximum likelihood estimation__ (__MLE__), and normalize the counts so the probability can lie between 0 and 1. Here is the example for computing a bigram probability:

![P(w_n | w_{n-1}) = \frac{C(w_{n-1}w_n)}{\displaystyle\sum_{w}C(w_{n-1}w)}](https://render.githubusercontent.com/render/math?math=P(w_n%20%7C%20w_%7Bn-1%7D)%20%3D%20%5Cfrac%7BC(w_%7Bn-1%7Dw_n)%7D%7B%5Cdisplaystyle%5Csum_%7Bw%7DC(w_%7Bn-1%7Dw)%7D)  
*(equation  5)*  

<p><br></p>

The equation 5 can be simplified. Since the sum of all bigram counts that start with a given word ![w_{n-1}](https://render.githubusercontent.com/render/math?math=w_%7Bn-1%7D) must be equal to the unigram count for that word ![w_{n-1}](https://render.githubusercontent.com/render/math?math=w_%7Bn-1%7D):

![P(w_n | w_{n-1}) = \frac{C(w_{n-1}w_n)}{C(w_{n-1})}](https://render.githubusercontent.com/render/math?math=P(w_n%20%7C%20w_%7Bn-1%7D)%20%3D%20%5Cfrac%7BC(w_%7Bn-1%7Dw_n)%7D%7BC(w_%7Bn-1%7D)%7D)  
*(equation  6)*   

<p><br></p>

__Generalized equations for n-grams__:  

bigram (N=1)  :  ![P(w_{n}| w_{n-1}) = \frac{C(w_{n-1}w_n)}{C(w_{n-1})}](https://render.githubusercontent.com/render/math?math=P(w_%7Bn%7D%7C%20w_%7Bn-1%7D)%20%3D%20%5Cfrac%7BC(w_%7Bn-1%7Dw_n)%7D%7BC(w_%7Bn-1%7D)%7D)   
trigram (N=2) :  ![P(w_{n}| w_{n-2}, w_{n-1})= \frac{C(w_{n-2}w_{n-1}w_n)}{C(w_{n-2}w_{n-1})}](https://render.githubusercontent.com/render/math?math=P(w_%7Bn%7D%7C%20w_%7Bn-2%7D%2C%20w_%7Bn-1%7D)%3D%20%5Cfrac%7BC(w_%7Bn-2%7Dw_%7Bn-1%7Dw_n)%7D%7BC(w_%7Bn-2%7Dw_%7Bn-1%7D)%7D)   
4-gram  (N=3) :  ![P(w_{n}| w_{n-3}, w_{n-2}, w_{n-1})= \frac{C(w_{n-3}w_{n-2}w_{n-1}w_n)}{C(w_{n-3}w_{n-2}w_{n-1})}](https://render.githubusercontent.com/render/math?math=P(w_%7Bn%7D%7C%20w_%7Bn-3%7D%2C%20w_%7Bn-2%7D%2C%20w_%7Bn-1%7D)%3D%20%5Cfrac%7BC(w_%7Bn-3%7Dw_%7Bn-2%7Dw_%7Bn-1%7Dw_n)%7D%7BC(w_%7Bn-3%7Dw_%7Bn-2%7Dw_%7Bn-1%7D)%7D)    


<p><br></p>
<p><br></p>

Reference:  
[Speech and Language Processing : Chapter 3]  
[latex-markdown](https://alexanderrodin.com/github-latex-markdown/)
