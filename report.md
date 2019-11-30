# Project 1 Report: Monte Carlo Deencrypting

## Introduction

The purpose of this project was to do a small experiment with a Monte Carlo process as a means of breaking through small encryptions. Monte Carlo methods are a form of "random walk" estimation for complex calculations, i.e. an estimation function is given a large number of random inputs and the convergence of the outputs estimates the true output.

To that end, we wanted to attempt to "estimate" an encryption key using a Monte Carlo method as the breaking software. Since encryptions in general are made of randomly generated cipher values, the purpose of the alorigthm we developed is to estimate towards the random value within a certain degree of error.

## Methods



## Results



## Conclusions

Overall, we found that the Monte Carlo estimation method is interesting for deencrypting, but likely not applicable in a larger sense because it is computationally very heavy. With out best method, we found a reasonably successful error rate of XXXXXXXXX for 3-bit encryptions, but the success quickly drops off for higher level encryption. This means that standard 8-bit encryptions the method will only function as well as a random guess.
