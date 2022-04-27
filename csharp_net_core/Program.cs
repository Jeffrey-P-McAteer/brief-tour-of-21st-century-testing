
using System;

namespace MyApp {
    public class Program {

        public static void Main(string[] args) {
            if (args.Length < 1) {
                var running_binary = System.Diagnostics.Process.GetCurrentProcess()?.MainModule?.FileName ?? "csharp_net_core";
                Console.WriteLine("Usage: "+running_binary+" number [number2, number3, ...]");
                Console.WriteLine("Prints primality test for each integer given.");
            }
            else {
                for (int i=0; i<args.Length; i+=1) {
                    int num = int.Parse(args[i]);
                    bool p = is_prime(num);
                    if (p) {
                      Console.WriteLine(num+" is Prime");
                    }
                    else {
                      Console.WriteLine(num+" is not Prime");
                    }
                }
            }
        }

        // Stolen from https://en.wikipedia.org/wiki/Primality_test
        public static bool is_prime(int n) {
            if (n == 2 || n == 3) {
                return true;
            }

            if (n <= 1 || n % 2 == 0 || n % 3 == 0) {
                return false;
            }

            for (int i = 5; i * i <= n; i += 6) {
                if (n % i == 0 || n % (i + 2) == 0) {
                    return false;
                }
            }

            return true;
        }

    }
}
