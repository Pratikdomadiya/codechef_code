import java.io.*;
class Codechef {
    public static void main(String[] args) throws Exception{
        InputStream is = System.in;
        OutputStream os = System.out;
        ScanReader in = new ScanReader(is);
        PrintWriter out = new PrintWriter(os);
        
        int t = in.scanInt();
        int[] primeNumber = new int[1000003];
        getprime(1000002, primeNumber);
        while(t-- > 0){
            int x = in.scanInt();
            int y = in.scanInt();
        
                int n = primeNumber[x];
                if(n<=y)
                    out.println("Chef");
                else
                    out.println("Divyam");
            
        }
        
        out.close();
    }
    static void getprime(int n, int[] primeNumber)
    {
        boolean prime_num[] = new boolean[n + 1];
        for (int i = 0; i <= n; i++)
            prime_num[i] = true;

        for (int p = 2; p * p <= n; p++) 
        {
            if (prime_num[p] == true) 
            {
                for (int i = p * p; i <= n; i += p)
                    prime_num[i] = false;
            }
        }
        int check = 0;
        for (int i = 2; i <= n; i++)
        {
            if (prime_num[i] == true)
                check += 1;
            primeNumber[i] = check;
        }
    }

    static class ScanReader {
        private byte[] buf = new byte[5 * 1024];
        private int index;
        private BufferedInputStream in;
        private int total;
 
        public ScanReader(InputStream inputStream) {
            in = new BufferedInputStream(inputStream);
        }
 
        private int scan() {
            if (index >= total) {
                index = 0;
                try {
                    total = in.read(buf);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                if (total <= 0) return -1;
            }
            return buf[index++];
        }
 
        public int scanInt() {
            int integer = 0;
            int n = scan();
            while (isWhiteSpace(n)) n = scan();
            int neg = 1;
            if (n == '-') {
                neg = -1;
                n = scan();
            }
            while (!isWhiteSpace(n)) {
                if (n >= '0' && n <= '9') {
                    integer *= 10;
                    integer += n - '0';
                    n = scan();
                }
            }
            return neg * integer;
        }
 
        private boolean isWhiteSpace(int n) {
            if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
            else return false;
        }
 
    }
}
