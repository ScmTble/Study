```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char a[100];
    char c;
    int d,b;
    gets(a);
    sscanf(a,"%d %c %d",&b,&c,&d);  //去掉多余空白字符
    printf("%d %c %d",b,c,d);
    system("pause");
    return 0;
}
```

# assert()

```c
//assert()断言函数，用于在调试过程中捕捉程序错误
#include <stdio.h>
#include <assert.h>
int main(){
    int m, n, result;
    scanf("%d %d", &m, &n);
    assert(n != 0);  //写作 assert(n) 更加简洁
    result = m / n;
    printf("result = %d\n", result);
    return 0;
}
/*
本例用来计算两个数相除的结果，由于被除数不能为 0，所以我们加入了 assert() 来检测错误。

如果输入100 20，那么 n 的值为 20，n != 0这个条件成立，assert() 不进行任何操作，最终的输出结果为：
100 20↙
result = 5

如果输入100 0，那么 n 的值为 0，n != 0这个条件不成立，assert() 就会报告错误，并终止程序执行，最终的结果如下所示：
100 0↙
Assertion failed: n != 0,  file E:\\CDemo\main.c, line 6
*/
```



