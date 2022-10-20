#include <stdio.h>
//1
int prime(long int n);

//11-----------------------
int getReverse(int num);
int getSumOfDigit(int num);
 
void main()
{
    //1-----------------------------------------------
    int n,res=0,i;
    
    printf("\nENTER A NUMBER: ");
    
    scanf("%d",&n);
    
    res=prime(n);
    
    if(res==0)
    printf("\n%d is prime.\n",n);
    else 
    printf("\n%d is not prime.\n",n);
    
    //2-----------------------------------------------
    
    int num=n;

    // true if num is perfectly divisible by 2
    if(num % 2 == 0)
        printf("%d is even.\n", num);
    else
        printf("%d is odd.\n", num);
    
    
    //3----------------------------------------------
    int reversed = 0, remainder, original;
    
    original = n;
    // reversed integer is stored in reversed variable
    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }
    // palindrome if orignal and reversed are equal
    if (original == reversed)
        printf("%d is a palindrome.\n", original);
    else
        printf("%d is not a palindrome.\n", original);

    //4-------------------------------------------------
    int number=original,flag=0;
    for(i = 0; i <= number/2; i++)
    {
        if(number == i*i)
        {
            printf("%d is a perfect square\n", number);
            flag=1;
            break; 
        }
        
    }
    if(flag== 0)
    printf("%d is not a perfect square\n", number);
    
    //5------------------------------------------------
    
    int originalNum, result = 0;
    
    originalNum = number;

    while (originalNum != 0) {
       // remainder contains the last digit
        remainder = originalNum % 10;
        
       result += remainder * remainder * remainder;
        
       // removing last digit from the orignal number
       originalNum /= 10;
    }

    if (result == number)
        printf("%d is an Armstrong number.", num);
    else
        printf("%d is not an Armstrong number.", num);

    printf("\n");
    
    
    //6-----------------------------------------------------
    n=number;
    i=0;
    flag = 0;
    printf("The divisors of %d are: 1",n);
  for (i = 2; i <= n / 2; ++i) {

    // if n is divisible by i, then n is not prime
    // change flag to 1 for non-prime number
    if (n % i == 0) {
      printf(",%d",i);
        flag = 1;
    }
      // flag is 0 for prime numbers
  } 
    printf("\n");
    if (flag == 0)
      printf("%d is a prime number.\n", n);
    
    //7----------------------------------------------------------
    long int decimalNumber=n;
        printf("Equivalent hexadecimal number is: %ld",decimalNumber);
    printf("\n");
    
    //8-----------------------------------------------------------
    
    long int quotient=0;
    decimalNumber=n;
    remainder=0;
        int binaryNumber[100],j;
    i=1;

        quotient = decimalNumber;
        while(quotient!=0) {
                binaryNumber[i++]= quotient % 2;
                quotient = quotient / 2;
        }
        printf("Equivalent binary value of decimal number %ld: ",decimalNumber);
        for (j = i -1 ;j> 0;j--)
                 printf("%d",binaryNumber[j]);
    printf("\n");
    
    //9--------------------------------------------------------------------
    
    printf("Equivalent octal number is: %ld",decimalNumber);
    printf("\n");

    
    //10-----------------------------------------------------------------------
      i=0, flag=0;
      printf(" ");
      // initialize first and second terms
      int t1 = 0, t2 = 1;

      // initialize the next term (3rd term)
      int nextTerm = t1 + t2;

      // print 3rd to nth terms
      for (i = 3; i <= n; ++i) 
      {
        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;
          if(n==nextTerm)
              flag=1;
          if(n<nextTerm)
              break;
      }
    
        if (flag==1)
        printf("%d The no is fibonacci ",n);
        else 
            printf("%d The no is not fibonacci",n);
        printf("\n");
    
    
    //11---------------------------------------------------------------------------
    num=n;
    int digitSum=0, reverse=0;
 
    /* get sum of digits of input number */
    digitSum = getSumOfDigit(num);
    /* reverse the digits of digitSum*/
    reverse = getReverse(digitSum);
 
    if ((digitSum * reverse) == num) {
        printf("%d is a Magic Number\n", num);
    } else {
        printf("%d is not a Magic Number\n", num);
    }
    
    //12--------------------------------------------------------------------
    n=n;
    i=0; 
        int sum = 0; 

        for(i=1;i<=n;i++) 
        { 
                sum = sum + i; 
        } 
        printf("The sum of first %d numbers is %d\n",n,sum); 
    
    //13-------------------------------------------------------------------------
    int rres=0;
    i=0;
    int pi=0;
    int disp=0;
    printf("Enter 1 if you wish to see the list of primes till %d:",n);
    scanf("%d",&disp);
    if(disp==1)
    {
        if(n>2)
        {
        printf("2");
        pi=1;
        }
        if(n>3)
        {
        printf(",3");
            pi=2;
        }
        if(n>5)
        {
        printf(",5");
            pi=3;
        }
    }
    for(i=2;i<=n;i++)
    {
        if((i%2!=0)&&(i%3!=0)&&(i%5!=0))
        {
            //printf("[RES pre= %d ]",rres);
            rres= prime(i);
             //printf("| %d, res=%d  |\n", i,rres);
            if(rres == 0)
            {
                pi=pi+1;
                if(disp==1)
                    printf(",%d",i);
            }
            rres=0;
            
        }
    }
    printf(".\n");
    printf("Total no primes =%d \n", (pi));
       
    
    //14---------------------------------------------
    int m;    
       n=n;
    sum=0;
    while(n>0)    
    {    
    m=n%10;    
    sum=sum+m;    
    n=n/10;    
    } 
    n=number;
    printf("Sum of the digits of %d is = %d \n",n,sum);  
    
    //15---------------------------------------------------------------------------
     number=n, i=0, sum=0;
         for(i=0;i < number; i++)
         {
          sum = sum+i;

          if(sum == number)
          {
           printf("%d is TRIANGULAR NUMBER.\n", number);
           break;
          }
         }

         if(number == i)
         {
          printf("%d is NOT TRIANGULAR NUMBER.\n", number);
         }
}
int prime(long int n)
{
    long int i=0;
    for(i=5;i<n/2;i++)
    {
       
        if(n%i==0)
            return 1;
        else
            continue;
    }
    return 0;
}

/* Function to reverse an integer  */
int getReverse(int num) 
{
    int r = 0;
    while (num > 0) {
        r = (r * 10) + (num % 10);
        num = num / 10;
    }
    return r;
  }
   
/* Function to calculate sum of digits of a number*/
int getSumOfDigit(int num){
    int sum = 0;
    while(num != 0){
        /* num%10 gives least significant digit of num */
        sum = sum + num%10;
        num = num/10; 
    }
    return sum;
}
