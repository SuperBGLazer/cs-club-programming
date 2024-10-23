// Go to https://aka.ms/new-console-template 

using System;
namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
           

            bool firstNumberFound = false;
            bool secondNumberFound = false;
            string response = "";

            double a = 0;
            double b = 0;
        


            while (!firstNumberFound) {
                response = "";

                Console.WriteLine("Is " + String.Format("{0:0.0}", a) + " your first number? (y/n): ");
                response = Console.ReadLine();
                
                if (response == "y") {
                    firstNumberFound = true;
                    Console.WriteLine("Finally!");
                }

                else {
                    Console.WriteLine("Aw man");
                }



                a += 0.1;
            }

          
             while (!secondNumberFound) {
                    response = "";
                
                    Console.WriteLine("Is " + String.Format("{0:0.0}", b) + " your second number? (y/n): ");
                    response = Console.ReadLine();
                
                if (response == "y") {
                    secondNumberFound = true;
                    Console.WriteLine("Finally!");
                }

                else {
                    Console.WriteLine("Aw man");
                }



                  
                b += 0.1;
                }


        Console.WriteLine("The sum is probably around like " + Math.Round( a + b - 0.2, 1));
        }
    }
}
