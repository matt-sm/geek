// strcmp

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
            Console.WriteLine(string.Compare("Helz", "Hela"));
            Console.WriteLine(strcmp("Helz", "Hela"));
            Console.WriteLine("---");
            
            Console.WriteLine(string.Compare("", "ABCD"));
            Console.WriteLine(strcmp("", "ABCD"));
            Console.WriteLine("---");

            Console.WriteLine(string.Compare("aa", "a"));
            Console.WriteLine(strcmp("aa", "a"));
            Console.WriteLine("---");

            Console.WriteLine(string.Compare("Hello", "World"));
            Console.WriteLine(strcmp("Hello", "World"));
            Console.WriteLine("---");

            Console.WriteLine(string.Compare("ABCD", "abcdEghe"));
            Console.WriteLine(strcmp("ABCD", "Hela"));
            Console.WriteLine("---");

            Console.WriteLine(string.Compare("GeeksForGeeks", "gEEksFORGeEKs"));
            Console.WriteLine(strcmp("GeeksForGeeks", "gEEksFORGeEKs"));
            Console.WriteLine("---");
        }
        
        static int strcmp(string s1, string s2)
        {
            int i;
            
            var c1 = s1.ToCharArray();
            var c2 = s2.ToCharArray();
            
            for (i = 0; i < c1.Length && i < c2.Length; i++)
            {
                if (char.ToLower(c1[i]) == char.ToLower(c2[i]))
                {
                    continue;
                }
                else
                {
                    break;
                }
            }
            
            var ch1 = (c1.Length == i ? char.MinValue : c1[i]);
            var ch2 = (c2.Length == i ? char.MinValue : c2[i]);

            if (ch1 == ch2)
            {
                 return 0;
            }
            
            if (ch1 < ch2)
            {
                 return -1;
            }
            
            return 1;
        }
    }
}
