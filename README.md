# HackerrankCodingInterviewQuestions
Questions for computer science interviews

There are several coding interview questions on hackerrank.  I solved all of them passing 100% of test cases except for "M-th to last" problem where i got 83.33% of test cases- i don't have access to the test cases that failed, and i cannot find any input that fails on my own.

1. M-th to last:
For this question, you will write a program that, given a positive integer M and a list of integers L, outputs the list element M links away from the end of the list. For this program, we will use 1-indexing. That means mth_to_last(1) is the "1st-to-last" element, or simply the last element in the list.

2. Fibonacci Lite:
For this question, you will write a program that generates values from the Fibonacci sequence. The Fibonnaci sequence is recursively defined by:
Fn = Fn - 1 + Fn - 2
Using the following seed values:
F0 = 0, F1 = 1
Given a number n, print the nth value of the Fibonacci sequence.

3. Fibonacci Returns
This question expands on our earlier Fibonacci Lite challenge. While the goal of Fibonacci Lite was to understand recursion, this challenge is about solving problems efficiently with dynamic programming.
The difference in this challenge is that each test case will consist of many inputs instead of just one. Furthermore, we're allowing larger values of n. You'll need to use dynamic programming to solve all the inputs without running out of time.
So, given many numbers n, print the nth value of the Fibonacci sequence for each of them, in order, on their own line.
Here are the definitions of the sequence again:
Fn = Fn - 1 + Fn - 2
Using the following seed values:
F0 = 0, F1 = 1

4. Find the uncoupled integer
Write a program that, given a list of integers as an argument to STDIN
n1, n2, n3, ..
Prints out the only uncoupled (unpaired) integer in the list to STDOUT.

5. Balanced Delimiters
For this question, you will parse a string to determine if it contains only "balanced delimiters."
A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

6. FizzBuzz Classic
Write a program that, given a number n from STDIN, prints out all numbers from 1 to n (inclusive) to STDOUT, each on their own line. But there's a catch:
For numbers divisible by 3, instead of n, print Fizz
For numbers divisible by 5, instead of n, print Buzz
For numbers divisible by 3 and 5, just print FizzBuzz

7.  Factorial of N
Write a program that, given a number n from STDIN, prints out the factorial of n to STDOUT:
If n is 0, n factorial is 1
n! is not defined for negative numbers.

8. The Coin Change Problem
You have m types of coins available in infinite quantities where the value of each coin is given in the array C=[c0,c1,...,Cm-1]. Can you determine the number of ways of making change for n units using the given types of coins? For example, if m=4, and C=[8,3,1,2], we can make change for n=3 units in three ways: {1,1,1}, {1,2}, and {3}.
Given n, m, and C, print the number of ways to make change for n units using any number of coins having the values given in C.

