// IsPalindrome - tests if a string is an anagram of a palindrome

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
            Console.WriteLine(IsPalindrome("ssdddd"));
            Console.WriteLine(IsPalindrome("anav"));
            Console.WriteLine(IsPalindrome("A new order began a more Roman age bred Rowena"));
            Console.WriteLine(IsPalindrome("Aerate pet area"));
            Console.WriteLine(IsPalindrome("Anne I vote more cars race Rome to Vienna"));
            Console.WriteLine(IsPalindrome(null));
            Console.WriteLine(IsPalindrome("aaxxccjjjhhh"));
            Console.WriteLine(IsPalindrome("alula"));
            Console.WriteLine(IsPalindrome("A tin mug for a jar of gum Nita"));
        }
        
        static bool IsPalindrome(string s)
        {
            if (s == null || s.Length == 0) return false;
            
            var d = new Dictionary<char, int>();
            for (int i = 0; i < s.Length; i++)
            {
               // ignore case 
               var ch = char.ToLower(s[i]);
               
                // ignore spaces
               if (ch == ' ') continue;
                
               // count occurances of each char 
               if (d.ContainsKey(ch))
               {
                  d[ch] = ++d[ch];   
               }
               else
               {
                   d.Add(ch, 1);
               }
            }
            
            int oddCounter = 0;
            foreach (var c in d.Values)
            {
              if (c % 2 != 0)
              {
                if (oddCounter == 0)
                {
                   oddCounter++;   
                }
                else
                {
                   return false;  
                }
              }
            }
            
            return true;
        }
    }
}
