// Euler Problem 1 - Multiples of 3 and 5
//Rextester.Program.Main is the entry point for your code. Don't change it.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Your code goes here
            Console.WriteLine(SumMultiples(1000));
        }
        
        static int SumMultiples(int max)
        {
           var sum = 0;
            
           for (int i = 1; i * 3 < max; i++)
           {
               if ((i * 3) % 5 != 0)
               {
                 sum += (i * 3);
               }
               
               if (i * 5 < 1000)
               {
                  sum += (i * 5);   
               }               
           }
            
           return sum;
        }
    }
}
