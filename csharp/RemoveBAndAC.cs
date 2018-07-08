// Remove “b” and “ac” from a given string
// http://www.geeksforgeeks.org/remove-a-and-bc-from-a-given-string/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        const int One = 1;
        const int Two = 2;
        
        public static void Main(string[] args)
        {
            //Your code goes here
            StringFilter("ab");
            StringFilter("ad");
            StringFilter("");
            StringFilter("acbac");
            StringFilter("aaac");
            StringFilter("react");
            StringFilter("aa");
            StringFilter("ababaac");
        }
        
        static void StringFilter(string s)
        {
            int j = 0, state = One;
            
            var c = s.ToCharArray();
            
            for (int i = 0; i < c.Length; i++)
            {
               if (c[i] != 'b' && c[i] != 'c')
               {
                  c[j++] = c[i];
                  state = One;
               }
                
               else if (c[i] == 'c' && state == Two)
               {
                  j--;   
               }
                
               if (c[i] == 'a' && state == One)
               {
                  state = Two;   
               }
            }
            
            s = new string(c);
            
            if (j < s.Length)
            {
               s = s.Remove(j);   
            }
            
            Console.WriteLine(s);   
        }
    }
}
