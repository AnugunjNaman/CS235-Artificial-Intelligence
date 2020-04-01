import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.Random;

public class AI2AI{

    static char start;
    static int choose;

    public static void main(String[] args){
        FastScanner fs = new FastScanner();
        System.out.println("Game Begins");
        System.out.print("Enter the no. of sticks: ");
        int n = fs.nextInt();
        Random rand = new Random();
        int turn = rand.nextInt(2);
        if(turn == 1){
        System.out.println("Player A's Turn First");
        System.out.println("Player " + evaluate(n, 'A') + " wins");
        }
        if(turn == 0){
        System.out.println("Player B's Turn");
        System.out.println("Player " + evaluate(n, 'B') + " wins");
        }
    }

    static void sort(int[] a){
        ArrayList<Integer>l = new ArrayList<>();
        for(int i: a)
            l.add(i);
        Collections.sort(l);
        for(int i = 0; i < a.length; i++)
            a[i] = l.get(i);
    }

    static class FastScanner{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");
        String next(){
            while(!st.hasMoreTokens())
                try{
                    st = new StringTokenizer(br.readLine());
                } catch(IOException e){
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt(){
            return Integer.parseInt(next());
        }
        int[] readArray(int n){
            int[] a = new int[n];
            for(int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }
        long nextLong(){
            return Long.parseLong(next());
        }
    }

    static int utility(int m, int sticks_choose, int alpha, int beta, char turn){
        if(m <= 0 && turn == 'A'){
            if(start == 'A'){
            choose = sticks_choose;
            }
            return 10;
        }

        if(m <= 0 && turn == 'B'){
            if(start == 'B'){
            choose = sticks_choose;
            }
        return -10;
        }

        if(turn =='A'){
            int value = -100;
            int eval;
            for(int i=1;i<=3;i++){
                eval = utility(m-i, sticks_choose, alpha, beta, 'B');
                value = Math.max(value, eval);
                alpha = Math.max(alpha, eval);
                    if(beta <= alpha)
                        break;
            }
            return value;
        }

        else{
            int value1 = 100;
            int eval1;
            for(int j=1;j<=3;j++){
                eval1 = utility(m-j, sticks_choose, alpha, beta, 'A');
                value1 = Math.min(value1, eval1);
                beta = Math.min(beta, eval1);
                if(beta <=  alpha)
                    break;
            }
            return value1;
        }
    }

    static char evaluate(int n, char first_turn){
        int value = 0;
        int x = 0;
        char curr_turn = first_turn;
        System.out.println("Sticks Left: " + n);
        while(n > 0){
            if(curr_turn == 'A'){
                value = -100;
                for(int i=1;i<=3;i++){
                    if(n == 1){
                        choose = 1;
                        break;
                    }
                    start = 'A';
                    x = utility(n-i, i, -100, 100, 'B');
                    if(x > value){
                    value = x;
                    }
                }
                n = n-choose;
                System.out.println("Player A chooses: " + choose + "\n");
                System.out.println("(Remaining sticks: " + n + ")");
                curr_turn = 'B';
            }
            else{
                value = 100;
                for(int i=1;i<=3;i++){
                    if(n == 1){
                        choose = 1;
                        break;
                    }
                    start = 'B';
                    x = utility(n-i, i, -100, 100, 'A');
                    if(x < value){
                        value = x;
                    }
                }
                n = n-choose;
                System.out.println("Player B chooses: " + choose + "\n");
                System.out.println("(Remaining sticks: " + n + ")");
                curr_turn = 'A';
            }
        choose = 0;
        }
        return curr_turn;
    }
} 

