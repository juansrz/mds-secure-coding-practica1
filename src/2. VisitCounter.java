package es.urjc.etsii.grafo.CPIF;

import java.io.*;
import java.util.concurrent.*;

public class VisitCounter {
    private static final String FILE_NAME = "visit_count.txt";
    private static int count = 10;
    public static void old_counter() throws IOException {
        count+=1;
        BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME)); //Bug here
        writer.write(String.valueOf(count));
        writer.close();
    };
    // Simulate visit by incrementing the count
    public static void incrementVisitCount() {
        try {
            // Read the current count from the file
            BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME));
            int currentCount = Integer.parseInt(reader.readLine());
            reader.close();

            // Increment the count
            currentCount++;

            // Write the updated count back to the file
            BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME));
            writer.write(String.valueOf(currentCount));
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws InterruptedException, IOException {
        // Set the initial visit count to 0
        BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME));
        writer.write("0");
        writer.close();

        ExecutorService executor = Executors.newFixedThreadPool(10);
        for (int i = 0; i < 1000; i++) {
            executor.submit(VisitCounter::incrementVisitCount);
        }

        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);
    }
}

