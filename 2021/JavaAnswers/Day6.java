import java.io.*;
import java.util.*;
import java.util.stream.LongStream;

public class Advent {
    public static void main(String[] args) throws FileNotFoundException {
        var inputFile = new File("Advent2021/src/day6.txt");
        var scan = new Scanner(inputFile);
        var txt = scan.next();
        var input = LongStream.range(0, 10).map(x -> txt.length() - txt.replace(""+x, "").length()).toArray();
        scan.close();
        System.out.println(solution(input));
    }
    public static long solution(long[] fish) {
        for (int day = 0; day < 256; day++) {
            var first = fish[0];
            for (int i = 0; i < 9; i++) {
                fish[i] = fish[i+1] + ((i == 8 || i == 6)? first : 0L);
            }
        }
        return Arrays.stream(fish).sum();
    }
}
