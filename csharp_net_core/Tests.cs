using Xunit;

namespace MyApp {
    public class MyTestClass {
        [Fact]
        public void DoesPrimeTestWork() {
            Assert.True(Program.is_prime(2), "2 should be prime");
            Assert.True(Program.is_prime(3), "3 should be prime");
            Assert.False(Program.is_prime(4), "4 should not be prime");
            Assert.False(Program.is_prime(16), "16 should not be prime");
        }
    }
}
