import java.io.BufferedReader;
import java.io.FileReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) {
        String filePath = "./glava_7.txt";
        String word = "Пьер";
        int count = 0;

        try {
            BufferedReader reader = new BufferedReader(new FileReader(filePath));
            String line;
            while ((line = reader.readLine()) != null) {
                StringTokenizer tokenizer = new StringTokenizer(line);
                while (tokenizer.hasMoreTokens()) {
                    if (tokenizer.nextToken().equals(word)) {
                        count++;
                    }
                }
            }
            reader.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
        
        System.out.println("Слово \"" + word + "\" встречается " + count + " раз(а)");
    }
}

